from enum import Enum

class DelegatedAdminRelationshipOperationType(str, Enum):
    DelegatedAdminAccessAssignmentUpdate = "delegatedAdminAccessAssignmentUpdate",
    UnknownFutureValue = "unknownFutureValue",
    DelegatedAdminRelationshipUpdate = "delegatedAdminRelationshipUpdate",

