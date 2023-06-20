from enum import Enum

class SubjectRightsRequestType(str, Enum):
    Export = "export",
    Delete = "delete",
    Access = "access",
    TagForAction = "tagForAction",
    UnknownFutureValue = "unknownFutureValue",

