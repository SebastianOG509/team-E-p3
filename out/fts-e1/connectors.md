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
| E_K19 | Terminal de Operación de Muelle → Servicio de Custodia | Event notification | Sink | Traspaso de carga registrado (emisor, receptor, estado del sello declarado por el operador de muelle). | No |
| E_K20 | Servicio de Custodia → Base de Operaciones Fluvial | Data flow | Sink | Registro de custodia. | No |
| E_K21 | Servicio de Custodia → Broker Interno de Eventos | Event notification | Sink | Traspaso de custodia confirmado. | No |
| E_K22 | Unidad a Bordo GPS/AIS → Gateway IoT de Campo | Data flow | Supply | Posición, rumbo y velocidad. Enlace intermitente río–tierra (celular o satelital); la Unidad a Bordo no almacena lecturas. | No |
| E_K23 | Gateway IoT de Campo → Servicio de Seguimiento de Flota | Data flow | Supply | Telemetría normalizada (posiciones, estado del sello, movimientos de grúa). | No |
| E_K24 | Servicio de Seguimiento de Flota → Almacén de Telemetría | Data flow | Sink | Histórico de posiciones y lecturas. | No |
| E_K25 | Servicio de Seguimiento de Flota → Broker Interno de Eventos | Event notification | Sink | Posición, estado de navegación y novedades reportadas. | No |
| E_K26 | Broker Interno de Eventos → Traductor de Modelo Canónico | Event notification | Sink | Eventos de custodia y de navegación. | No |
| E_K27 | Traductor de Modelo Canónico → Fluvial Gateway | Event notification | Sink | Traspaso de custodia en formato canónico (sale por SoS-K15). | No |
| E_K28 | Traductor de Modelo Canónico → Fluvial Gateway | Event notification | Supply | Posición y estado de navegación en formato canónico (sale por SoS-K16). | No |
| E_K29 | Broker Interno de Eventos → Panel del Operador Fluvial | Event notification | Sink | Alertas y eventos para el operador. | No |
| E_K30 | Panel del Operador Fluvial → Servicio de Consulta de Estado | Dependency | Blocking | Consulta de estado consolidado de la carga. | No |
| E_K31 | Servicio de Consulta de Estado → Traductor de Modelo Canónico | Dependency | Blocking | Consulta de estado consolidado en modelo interno. | No |
| E_K32 | Traductor de Modelo Canónico → Fluvial Gateway | Dependency | Blocking | Consulta de estado consolidado en formato canónico (sale por SoS-K19a). | No |
| E_K33 | Fluvial Gateway → Traductor de Modelo Canónico | Data flow | Blocking | Estado consolidado de la carga consultada (llega por SoS-K19b). | No |
| E_K34 | Traductor de Modelo Canónico → Servicio de Consulta de Estado | Data flow | Blocking | Estado consolidado en modelo interno. | No |
| E_K35 | Servicio de Consulta de Estado → Panel del Operador Fluvial | Data flow | Blocking | Estado consolidado para mostrar al operador. | No |
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
