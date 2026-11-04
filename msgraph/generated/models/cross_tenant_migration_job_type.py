from enum import Enum

class CrossTenantMigrationJobType(str, Enum):
    Validate = "validate",
    Migrate = "migrate",
    UnknownFutureValue = "unknownFutureValue",

