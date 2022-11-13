from enum import Enum

class SubjectRightsRequestType(Enum):
    Export = "export",
    Delete = "delete",
    Access = "access",
    TagForAction = "tagForAction",
    UnknownFutureValue = "unknownFutureValue",

