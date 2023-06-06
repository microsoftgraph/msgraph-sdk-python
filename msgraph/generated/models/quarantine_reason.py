from enum import Enum

class QuarantineReason(str, Enum):
    EncounteredBaseEscrowThreshold = "EncounteredBaseEscrowThreshold",
    EncounteredTotalEscrowThreshold = "EncounteredTotalEscrowThreshold",
    EncounteredEscrowProportionThreshold = "EncounteredEscrowProportionThreshold",
    EncounteredQuarantineException = "EncounteredQuarantineException",
    Unknown = "Unknown",
    QuarantinedOnDemand = "QuarantinedOnDemand",
    TooManyDeletes = "TooManyDeletes",
    IngestionInterrupted = "IngestionInterrupted",

