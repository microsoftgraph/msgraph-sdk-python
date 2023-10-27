from enum import Enum

class AttackSimulationOperationType(str, Enum):
    CreateSimualation = "createSimualation",
    UpdateSimulation = "updateSimulation",
    UnknownFutureValue = "unknownFutureValue",

