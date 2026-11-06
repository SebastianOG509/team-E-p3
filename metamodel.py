import os
from textx import metamodel_from_file, get_location, TextXSemanticError


def _error(message, obj):
    raise TextXSemanticError(message, **get_location(obj))


def _crosses(link):
    return len({c.system.name for c in link.path}) > 1


def _boundary(connector):
    """A connector is a boundary connector when one of its links joins two constituents."""
    return any(_crosses(link) for link in connector.links)


def _singles(factor):
    return factor.members if factor.__class__.__name__ == 'Group' else [factor]


def check_model(model):
    components = [e for e in model.elements if e.__class__.__name__ == 'Component']
    connectors = [e for e in model.elements if e.__class__.__name__ == 'Connector']

    for k in connectors:
        # C1. Every link joins at least two components.
        for link in k.links:
            if len(link.path) < 2:
                _error(f'{k.name}: a link must join at least two components', k)
        # C2. A control command has a single source with authority over its targets.
        if 'control_command' in k.natures:
            sources = {link.path[0].name for link in k.links}
            if len(sources) > 1:
                _error(f'{k.name}: control command with several sources {sorted(sources)}', k)
        # C3. Every boundary connector is governed by an agreement among owners.
        if _boundary(k) and not k.agreement:
            _error(f'{k.name}: boundary connector without agreement', k)
        for link in k.links:
            for a, b in zip(link.path, link.path[1:]):
                # C6 [E]. Event-driven style (FTS, Delivery 1, section 5.2): a service of T3
                # publishes events only to a broker or to a data store (T4), so producers
                # do not know their consumers.
                if ('event_notification' in k.natures and a.tier == 'T3'
                        and b.role != 'broker' and b.tier != 'T4'):
                    _error(f'{k.name}: {a.name} (T3) publishes an event directly to {b.name} ({b.tier}), '
                           f'which is neither a broker nor a data store', k)
                # C7 [E]. Client-server style (FTS, Delivery 1, section 5.3): a client of T1
                # requests only from services of T3.
                if 'dependency' in k.natures and a.tier == 'T1' and b.tier != 'T3':
                    _error(f'{k.name}: client {a.name} (T1) requests from {b.name} ({b.tier}), '
                           f'which is not a T3 service', k)

    # C4. A data store (T4) is accessed by dependency from a single component (Laboratory 4).
    for c in components:
        if c.tier == 'T4':
            users = {link.path[-2].name
                     for k in connectors if 'dependency' in k.natures
                     for link in k.links if link.path[-1] is c}
            if len(users) > 1:
                _error(f'{c.name}: data store shared by {sorted(users)}', c)

    # C5 [E, extended]. Every factor of an analysis carries the property its metric needs
    # (an optional number that is not written takes the value 0).
    for a in model.analyses:
        for f in a.factors:
            for s in _singles(f):
                r = s.ref
                if a.metric in ('availability', 'latency') and not getattr(r, a.metric):
                    _error(f'{a.name}: {r.name} has no {a.metric} property', a)
        if a.metric == 'detection':
            first = a.factors[0]
            if first.__class__.__name__ != 'Single' or first.ref.__class__.__name__ != 'Component' \
                    or not first.ref.period:
                _error(f'{a.name}: the first factor of a detection analysis needs a period', a)
            if not a.misses:
                _error(f'{a.name}: a detection analysis needs the number of missed heartbeats (misses)', a)
            for f in a.factors[1:]:
                for s in _singles(f):
                    if not s.ref.latency:
                        _error(f'{a.name}: {s.ref.name} has no latency property', a)


def create_metamodel():
    grammar = os.path.join(os.path.dirname(__file__), 'arch.tx')
    mm = metamodel_from_file(grammar)
    mm.register_model_processor(lambda model, metamodel: check_model(model))
    return mm
