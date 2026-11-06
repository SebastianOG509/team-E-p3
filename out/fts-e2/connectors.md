# Connectors of FTS

| ID | Source → Target | Nature | Coupling | Information carried | Boundary |
|----|-----------------|--------|----------|---------------------|----------|
| SoS_K4a | Road Gateway → Fluvial Gateway | Dependency | Blocking | Solicitud de capacidad y turno de transferencia camión-barcaza | Yes |
| SoS_K4b | Fluvial Gateway → Road Gateway | Data flow | Blocking | Confirmación de muelle fluvial y horario, o rechazo | Yes |
| SoS_K10a | Fluvial Gateway → Caribbean Port Gateway | Dependency | Blocking | Arribo de barcaza y solicitud de muelle de transferencia | Yes |
| SoS_K10b | Caribbean Port Gateway → Fluvial Gateway | Data flow | Blocking | Asignación de muelle de transferencia y ventana, o rechazo | Yes |
| SoS_K15 | Fluvial Gateway → National Coordination Gateway | Event notification | Sink | Custodia recibida por el operador fluvial | Yes |
| SoS_K16 | Fluvial Gateway → National Coordination Gateway | Event notification | Supply | Posición de barcaza o remolcador y estado de navegación | Yes |
| SoS_K19a | Fluvial Gateway → National Coordination Gateway | Dependency | Blocking | Consulta de estado consolidado de la carga en la que participa el operador fluvial | Yes |
| SoS_K19b | National Coordination Gateway → Fluvial Gateway | Data flow | Blocking | Estado consolidado limitado a su carga; v3: posición y ETA estimadas | Yes |
| SoS_K28a | Fluvial Gateway → Road Gateway | Dependency | Blocking | Solicitud de camiones para retirar unidades en puerto fluvial | Yes |
| SoS_K28b | Road Gateway → Fluvial Gateway | Data flow | Blocking | Vehículos asignados y cita de retiro, o rechazo | Yes |
| SoS_K31a | Caribbean Port Gateway → Fluvial Gateway | Dependency | Blocking | Unidades liberadas para transferencia patio-barcaza y solicitud de capacidad | Yes |
| SoS_K31b | Fluvial Gateway → Caribbean Port Gateway | Data flow | Blocking | Barcazas asignadas, muelle y ventana de cargue, o rechazo | Yes |
| SoS_K35 | National Coordination Gateway → Fluvial Gateway | Event notification | Sink | Estado de servicio de un constituyente: degradado o restablecido | Yes |
| SoS_K5 | Road Gateway → National Coordination Gateway | Event notification | Sink | Custodia recibida por el transportador; v3: ETA al despachar | Yes |
| SoS_K32 | National Coordination Gateway → Caribbean Port Gateway | Event notification | Sink | Cambio de levante en puertos del Caribe; v3: estado de servicio | Yes |
| E_K1 | Fluvial Gateway → Traductor de Modelo Canónico | Dependency | Blocking | Solicitud de turno de transferencia en formato canónico (llega por SoS-K4a). | No |
| E_K2 | Traductor de Modelo Canónico → Servicio de Turnos de Transferencia | Dependency | Blocking | Solicitud de turno en modelo interno. | No |
| E_K3 | Servicio de Turnos de Transferencia → Base de Operaciones Fluvial | Dependency | Blocking | Consulta de disponibilidad de muelle y barcaza. | No |
| E_K4 | Base de Operaciones Fluvial → Servicio de Turnos de Transferencia | Data flow | Blocking | Disponibilidad y programación vigente. | No |
| E_K5 | Servicio de Turnos de Transferencia → Base de Operaciones Fluvial | Data flow | Sink | Registro del turno asignado. | No |
| E_K6 | Servicio de Turnos de Transferencia → Traductor de Modelo Canónico | Data flow | Blocking | Muelle y horario asignados. | No |
| E_K7 | Traductor de Modelo Canónico → Fluvial Gateway | Data flow | Blocking | Confirmación de turno en formato canónico (sale por SoS-K4b). | No |
| E_K8 | Servicio de Programación de Viajes → Traductor de Modelo Canónico | Dependency | Blocking | Arribo estimado y solicitud de atraque. | No |
| E_K9 | Traductor de Modelo Canónico → Fluvial Gateway | Dependency | Blocking | Solicitud de atraque en formato canónico (sale por SoS-K10a). | No |
| E_K10 | Fluvial Gateway → Traductor de Modelo Canónico | Data flow | Blocking | Asignación de muelle y ventana operativa (llega por SoS-K10b). | No |
| E_K11 | Traductor de Modelo Canónico → Servicio de Programación de Viajes | Data flow | Blocking | Asignación de muelle y ventana en modelo interno. | No |
| E_K12 | Servicio de Programación de Viajes → Base de Operaciones Fluvial | Data flow | Sink | Registro del viaje con muelle y ventana asignados. | No |
| E_K13 | Panel del Operador Fluvial → Servicio de Programación de Viajes | Dependency | Blocking | Creación o cambio de viajes y asignación de barcazas. | No |
| E_K14 | Servicio de Programación de Viajes → Panel del Operador Fluvial | Data flow | Blocking | Itinerario y estado de los viajes. | No |
| E_K15 | Servicio de Programación de Viajes → App del Capitán | Data flow | Supply | Itinerario y ventana de atraque. | No |
| E_K16 | Servicio de Turnos de Transferencia → Terminal de Operación de Muelle | Data flow | Supply | Turnos de transferencia programados. | No |
| E_K17 | Grúa del Terminal Fluvial → Gateway IoT de Campo | Data flow | Sink | Movimientos de carga ejecutados. | No |
| E_K18 | Sensor de Carga y Sello → Gateway IoT de Campo | Data flow | Supply | Estado del sello y lecturas de carga. | No |
| E_K19 | Terminal de Operación de Muelle → Servicio de Custodia | Event notification | Sink | Traspaso de carga registrado (emisor, receptor, estado del sello declarado por el operador de muelle). Entrega 2: lleva credenciales y datos para validar el origen del traspaso (E-QS4). | No |
| E_K20 | Servicio de Custodia → Base de Operaciones Fluvial | Data flow | Sink | Registro de custodia. | No |
| E_K21 | Servicio de Custodia → Broker Interno de Eventos | Event notification | Sink | Traspaso de custodia confirmado. | No |
| E_K22 | Unidad a Bordo GPS/AIS → Gateway IoT de Campo | Data flow | Supply | Posición, rumbo y velocidad. Enlace intermitente río–tierra (celular o satelital); la Unidad a Bordo no almacena lecturas. Entrega 2: lleva además un latido cada 10 s y la identidad y secuencia de cada posición (E-QS2, E-QS6). | No |
| E_K23 | Gateway IoT de Campo → Servicio de Seguimiento de Flota | Data flow | Supply | Telemetría normalizada (posiciones, estado del sello, movimientos de grúa). Entrega 2: lleva latidos, identidad y secuencia (E-QS2, E-QS6). | No |
| E_K24 | Servicio de Seguimiento de Flota → Almacén de Telemetría | Data flow | Sink | Histórico de posiciones y lecturas. Entrega 2: registra por identidad y secuencia, sin duplicados (E-QS2). | No |
| E_K25 | Servicio de Seguimiento de Flota → Broker Interno de Eventos | Event notification | Sink | Posición, estado de navegación y novedades reportadas. Entrega 2: incluye el estado de vigencia («vigente» o «sin telemetría vigente, causa no confirmada») (E-QS6). | No |
| E_K26 | Broker Interno de Eventos → Traductor de Modelo Canónico | Event notification | Sink | Eventos de custodia y de navegación. Entrega 2: entrega desde la Cola Persistente, con prioridad (E-QS1). | No |
| E_K27 | Traductor de Modelo Canónico → Fluvial Gateway | Event notification | Sink | Traspaso de custodia en formato canónico (sale por SoS-K15). | No |
| E_K28 | Traductor de Modelo Canónico → Fluvial Gateway | Event notification | Supply | Posición y estado de navegación en formato canónico (sale por SoS-K16). | No |
| E_K29 | Broker Interno de Eventos → Panel del Operador Fluvial | Event notification | Sink | Alertas y eventos para el operador. Entrega 2: además lleva el aviso de estado de servicio, alertas de ataque y vigencia. | No |
| E_K30 | Panel del Operador Fluvial → Servicio de Consulta de Estado | Dependency | Blocking | Consulta de estado consolidado de la carga. | No |
| E_K31 | Servicio de Consulta de Estado → Traductor de Modelo Canónico | Dependency | Blocking | Consulta de estado consolidado en modelo interno. | No |
| E_K32 | Traductor de Modelo Canónico → Fluvial Gateway | Dependency | Blocking | Consulta de estado consolidado en formato canónico (sale por SoS-K19a). | No |
| E_K33 | Fluvial Gateway → Traductor de Modelo Canónico | Data flow | Blocking | Estado consolidado de la carga consultada (llega por SoS-K19b). Entrega 2: el estado consolidado puede traer ETA estimadas (P4). | No |
| E_K34 | Traductor de Modelo Canónico → Servicio de Consulta de Estado | Data flow | Blocking | Estado consolidado en modelo interno. Entrega 2: igual que E-K33. | No |
| E_K35 | Servicio de Consulta de Estado → Panel del Operador Fluvial | Data flow | Blocking | Estado consolidado para mostrar al operador. Entrega 2: muestra además si el dato es estimado o real y la fecha del último reporte real. | No |
| E_K36 | Remolcador → Unidad a Bordo GPS/AIS | Data flow | Supply | Rumbo, velocidad y estado de navegación del remolcador. | No |
| E_K37 | Barcaza → Unidad a Bordo GPS/AIS | Data flow | Supply | Estado y calado de la barcaza. | No |
| E_K38 | App del Capitán → Servicio de Seguimiento de Flota | Event notification | Sink | Novedades reportadas por el capitán (incidentes, retrasos, condiciones del río). | No |
| E_K39 | Servicio de Turnos de Transferencia → Traductor de Modelo Canónico | Dependency | Blocking | Solicitud de capacidad de camiones para retirar carga descargada de barcazas (puerto, unidades, ventana de retiro), en modelo interno. | No |
| E_K40 | Traductor de Modelo Canónico → Fluvial Gateway | Dependency | Blocking | Solicitud de retiro en formato canónico (sale por SoS-K28a). | No |
| E_K41 | Fluvial Gateway → Traductor de Modelo Canónico | Data flow | Blocking | Confirmación de vehículos asignados y cita de retiro, o rechazo (llega por SoS-K28b). | No |
| E_K42 | Traductor de Modelo Canónico → Servicio de Turnos de Transferencia | Data flow | Blocking | Confirmación de vehículos y cita de retiro, o rechazo, en modelo interno. | No |
| E_K43 | Fluvial Gateway → Traductor de Modelo Canónico | Dependency | Blocking | Solicitud de capacidad de convoy fluvial para unidades liberadas en el puerto (llega por SoS-K31a). | No |
| E_K44 | Traductor de Modelo Canónico → Servicio de Programación de Viajes | Dependency | Blocking | Solicitud de capacidad de convoy fluvial en modelo interno. | No |
| E_K45 | Servicio de Programación de Viajes → Traductor de Modelo Canónico | Data flow | Blocking | Barcazas asignadas, muelle y ventana de cargue, o rechazo, en modelo interno. | No |
| E_K46 | Traductor de Modelo Canónico → Fluvial Gateway | Data flow | Blocking | Confirmación de barcazas, muelle y ventana de cargue, o rechazo, en formato canónico (sale por SoS-K31b). | No |
| E_K47 | Fluvial Gateway → Traductor de Modelo Canónico | Event notification | Sink | aviso de estado de servicio en formato canónico (llega por SoS-K35). | No |
| E_K48 | Traductor de Modelo Canónico → Broker Interno de Eventos | Event notification | Sink | aviso de estado de servicio en modelo interno. | No |
| E_K49 | Broker Interno de Eventos → Servicio de Turnos de Transferencia | Event notification | Sink | estado de servicio; planificar con ETA estimada y holgura ≥ 30 min, o reanudar. | No |
| E_K50 | Broker Interno de Eventos → Servicio de Programación de Viajes | Event notification | Sink | estado de servicio; despachar a su hora con composición parcial (P5), o reanudar. | No |
| E_K51 | Broker Interno de Eventos → Servicio de Consulta de Estado | Event notification | Sink | estado de servicio; limitar SoS- K19a a ≤ 2 intentos/s o iniciar la reconciliación. | No |
| E_K52 | Servicio de Consulta de Estado → Servicio de Turnos de Transferencia | Data flow | Supply | posiciones y ETA estimadas de camiones hacia el terminal, con incertidumbre y fecha del último reporte real. | No |
| E_K53 | Servicio de Consulta de Estado → Servicio de Custodia | Data flow | Supply | estado consolidado para reconciliar custodia tras el restablecimiento. | No |
| E_K54 | Servicio de Consulta de Estado → Servicio de Programación de Viajes | Data flow | Supply | estado consolidado y ETA estimadas para planificar y reconciliar viajes. | No |
| E_K55 | Broker Interno de Eventos → Cola Persistente de Eventos | Data flow | Sink | evento de custodia o navegación a persistir, con su prioridad. | No |
| E_K56 | Cola Persistente de Eventos → Broker Interno de Eventos | Data flow | Sink | eventos pendientes de entrega, en orden de prioridad. | No |
| E_K57 | Unidad a Bordo GPS/AIS → Búfer No Volátil de Posiciones | Data flow | Sink | posición con identidad, secuencia y hora original, guardada antes de enviarla. | No |
| E_K58 | Búfer No Volátil de Posiciones → Gateway IoT de Campo | Data flow | Sink | rezago de posiciones retenidas, hasta 10/s por convoy al reconectar. | No |
| E_K59 | Servicio de Seguimiento de Flota → Gateway IoT de Campo | Data flow | Sink | acuse duradero de las posiciones persistidas (identidad y secuencia). | No |
| E_K60 | Gateway IoT de Campo → Búfer No Volátil de Posiciones | Data flow | Sink | acuse que autoriza liberar las posiciones retenidas. | No |
| E_K61 | Traductor de Modelo Canónico → Traductor de Modelo Canónico (standby) | Data flow | Supply | réplica del estado de las transacciones en curso. | No |
| E_K62 | Fluvial Gateway → Traductor de Modelo Canónico | Dependency | Blocking | sondeo de salud de la instancia primaria (cada 2 s). | No |
| E_K63 | Traductor de Modelo Canónico → Fluvial Gateway | Data flow | Blocking | estado de salud de la instancia primaria. | No |
| E_K64 | Fluvial Gateway → Traductor de Modelo Canónico (standby) | Dependency | Blocking | sondeo de salud del standby y tráfico redirigido tras la conmutación. | No |
| E_K65 | Traductor de Modelo Canónico (standby) → Fluvial Gateway | Data flow | Blocking | estado de salud y respuestas del standby. | No |
| E_K66 | Fluvial Gateway → Registro de Auditoría | Event notification | Sink | evidencia de cada decisión de verificación (origen, motivo, correlación). | No |
| E_K67 | Servicio de Custodia → Registro de Auditoría | Event notification | Sink | evidencia de la validación de origen de cada traspaso (E-K19). | No |
| E_K68 | Servicio de Turnos de Transferencia → Registro de Auditoría | Event notification | Sink | evidencia de la correlación entre SoS-K28b y la solicitud SoS-K28a pendiente. | No |
| E_K69 | Fluvial Gateway → Broker Interno de Eventos | Event notification | Sink | alerta agrupada de ataque (≤ 30 s desde el primer rechazo). | No |
