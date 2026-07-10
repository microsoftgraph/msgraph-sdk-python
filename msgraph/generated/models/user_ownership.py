from enum import Enum

class UserOwnership(str, Enum):
    None_ = "none",
    LawfulBasisForProcessing = "lawfulBasisForProcessing",
    RightToAccess = "rightToAccess",
    RightToBeInformed = "rightToBeInformed",
    RightToDataPortability = "rightToDataPortability",
    RightToObject = "rightToObject",
    RightToRectification = "rightToRectification",
    RightToRestrictionOfProcessing = "rightToRestrictionOfProcessing",
    RightsRelatedToAutomatedDecisionMaking = "rightsRelatedToAutomatedDecisionMaking",
    UnknownFutureValue = "unknownFutureValue",

