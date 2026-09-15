from enum import Enum

class RelationshipCreationType(str, Enum):
    # Represents a relationship between two tenants that was created by an explicit approval from the governed tenant admin.
    ApprovedByAdmin = "approvedByAdmin",
    # Represents a relationship between the add-on tenant and the tenant from which it was created.
    AddOnTenant = "addOnTenant",
    # This will help in making this enum evolvable and adding more values in the future-
    UnknownFutureValue = "unknownFutureValue",

