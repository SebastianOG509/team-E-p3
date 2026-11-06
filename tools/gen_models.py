"""Writes the two models of the Fluvial Transportation System (FTS) from the tables of
Delivery 2 (tools/fts_data.json) and from the joint model models/sos.arch.

  python3 tools/gen_models.py     ->  models/fts-e1.arch  (starting structure, Delivery 1)
                                      models/fts-e2.arch  (resulting structure, Delivery 2)
The boundary components and the global connectors are copied verbatim from sos.arch.
"""
import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), '..')
data = json.load(open(os.path.join(ROOT, 'tools', 'fts_data.json'), encoding='utf-8'))
sos = open(os.path.join(ROOT, 'models', 'sos.arch'), encoding='utf-8').read().split('\n')

# ── pieces copied from sos.arch ──────────────────────────────────────────────
constituents = [l for l in sos if l.startswith('constituent ')]
boundary = {re.match(r'component (\w+)', l).group(1): l for l in sos
            if l.startswith('component ') and ' tier T2 ' in l}
blocks, cur = {}, None
for l in sos:
    m = re.match(r'connector (\w+)', l)
    if m:
        cur = m.group(1); blocks[cur] = [l]
    elif cur and l.startswith('  '):
        blocks[cur].append(l)
    else:
        cur = None

FTS_GLOBAL = ['SoS_K4a', 'SoS_K4b', 'SoS_K10a', 'SoS_K10b', 'SoS_K15', 'SoS_K16',
              'SoS_K19a', 'SoS_K19b', 'SoS_K28a', 'SoS_K28b', 'SoS_K31a', 'SoS_K31b', 'SoS_K35']
M4_ONLY = ['SoS_K5', 'SoS_K32']          # to compose the budgets of SoS-QS1 (M4) as in sos.arch

# ── properties that the analyses need (ms; availability in %) ────────────────
COMP = {
    'e1': {'TRA': {'availability': 99.5}, 'CON': {'latency': 30000}, 'BRO': {'role': 'broker'}},
    'e2': {'TRA': {'availability': 99.5}, 'TRS': {'availability': 99.5}, 'CON': {'latency': 30000},
           'BRO': {'role': 'broker'}, 'UAB': {'period': 10000}},
}
CONN = {   # latency (ms) of the stages of each analysis
    'e1': {'E-K19': 10, 'E-K20': 10, 'E-K21': 10, 'E-K26': 1660, 'E-K27': 10,     # E-QS1: 4 x 10 + 1 660 (FIFO queue)
           'E-K32': 40000, 'E-K33': 5200},                                          # SoS-QS1, FTS stage: 40 s + 5.2 s
    'e2': {'E-K19': 30, 'E-K20': 30, 'E-K21': 30, 'E-K26': 30, 'E-K27': 30,        # E-QS1: 5 x 30
           'E-K32': 40000, 'E-K33': 2000,                                           # SoS-QS1, FTS stage: 40 s + 2 s
           'E-K22': 10000, 'E-K58': 18000, 'E-K59': 2000,                           # E-QS2: 10 + 18 + 2 s
           'E-K25': 5000},                                                          # E-QS6: propagation
}
ANALYSES = {
    'e1': '''// E-QS3: availability of the translation (Delivery 2, 8.1.3): 99.5 %
analysis EQS3 scenario "E-QS3 (disponibilidad del Traductor)" availability target 99.9 :
  TRA
// E-QS1: custody chain E-K19, E-K20, E-K21, E-K26, E-K27 (Delivery 2, 8.1.1)
analysis EQS1 scenario "E-QS1 (custodia oportuna)" latency target 30000 :
  E_K19, E_K20, E_K21, E_K26, E_K27
// SoS-QS1 (M4): local stage of the FTS, queries + last answer + applying results (Delivery 2, 8.1.1)
analysis FTSQS1 scenario "SoS-QS1 (M4, tramo del FTS)" latency target 300000 :
  E_K32, E_K33, CON
// SoS-QS1 (M4): composition of the joint budgets, as in sos.arch
analysis SoSQS1M4 scenario "SoS-QS1 (M4)" latency target 900000 :
  RGW, SoS_K5, NCG, SoS_K32, CGW
''',
    'e2': '''// E-QS3: availability of the translation with a standby replica and common cause (8.1.3)
analysis EQS3 scenario "E-QS3 (disponibilidad del Traductor)" availability target 99.9 :
  [TRA | TRS] beta 0.10
// E-QS1: custody chain E-K19, E-K20, E-K21, E-K26, E-K27 (8.1.1)
analysis EQS1 scenario "E-QS1 (custodia oportuna)" latency target 30000 :
  E_K19, E_K20, E_K21, E_K26, E_K27
// E-QS2: detection of the reconnection + drain of the backlog + durable ack (8.1.2)
analysis EQS2 scenario "E-QS2 (persistencia de posiciones)" latency target 60000 :
  E_K22, E_K58, E_K59
// E-QS6: three missed heartbeats of 10 s + propagation (8.1.6)
analysis EQS6 scenario "E-QS6 (detección del silencio)" detection misses 3 target 35000 :
  UAB, E_K25
// SoS-QS1 (M4): local stage of the FTS
analysis FTSQS1 scenario "SoS-QS1 (M4, tramo del FTS)" latency target 300000 :
  E_K32, E_K33, CON
// SoS-QS1 (M4): composition of the joint budgets, as in sos.arch
analysis SoSQS1M4 scenario "SoS-QS1 (M4)" latency target 900000 :
  RGW, SoS_K5, NCG, SoS_K32, CGW
''',
}
TITLE = {'e1': 'starting structure of Delivery 1, with the properties of Delivery 2',
         'e2': 'resulting structure of Delivery 2'}


def comp_line(c, props):
    extra = ''
    for key in ('availability', 'latency', 'role', 'period'):
        if key in props:
            extra += f' {key} {props[key]}'
    return f'component {c["id"]} "{c["label"]}" in FTS tier {c["tier"]} kind {c["kind"]}{extra}'


def conn_block(k, model, latency):
    info = k['info_e2'] if model == 'e2' and k.get('info_e2') else k['info']
    lines = [f'connector {k["id"].replace("-", "_")} nature {k["nature"]} coupling {k["coupling"]}',
             f'  carries "{info}"']
    if k['id'] in latency:
        lines.append(f'  latency {latency[k["id"]]}')
    lines.append(f'  : {k["src"]} -> {k["dst"]}')
    return lines


def write(model):
    out = [f'// Model (M1) of the Fluvial Transportation System (FTS): {TITLE[model]}',
           '// Generated by tools/gen_models.py from the tables of Delivery 2 and from sos.arch.',
           'system FTS', ''] + constituents + ['']
    props = COMP[model]
    out.append('// Components of the FTS, by tier')
    for tier in ('T1', 'T2', 'T3', 'T4', 'T5'):
        out.append(f'// {tier}')
        if tier == 'T2':
            out.append(boundary['FGW'])
        for c in data['components']:
            if c['tier'] == tier and c['id'] != 'FGW' and (model == 'e2' or not c['e2_only']):
                out.append(comp_line(c, props.get(c['id'], {})))
    out += ['// T2 — boundary components of the other constituents (as in sos.arch)']
    out += [boundary[b] for b in ('CGW', 'PGW', 'RGW', 'LGW', 'NCG')]
    out += ['', '// Global connectors of the FTS (as in sos.arch)']
    for name in FTS_GLOBAL:
        out += blocks[name]
    out += ['// Global connectors outside the FTS, only to compose the budgets of SoS-QS1 (M4) as in sos.arch']
    for name in M4_ONLY:
        out += blocks[name]
    out += ['', '// Internal connectors of the FTS']
    for k in data['connectors']:
        if model == 'e2' or not k['e2_only']:
            out += conn_block(k, model, CONN[model])
    out += ['', '// Analyses'] + ANALYSES[model].rstrip('\n').split('\n')
    path = os.path.join(ROOT, 'models', f'fts-{model}.arch')
    open(path, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(path, '->', sum(1 for l in out if l.startswith('component')), 'components,',
          sum(1 for l in out if l.startswith('connector')), 'connectors')


if __name__ == '__main__':
    for m in ('e1', 'e2'):
        write(m)
