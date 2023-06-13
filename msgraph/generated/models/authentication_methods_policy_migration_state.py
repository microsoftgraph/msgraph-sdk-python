from enum import Enum

class AuthenticationMethodsPolicyMigrationState(str, Enum):
    PreMigration = "preMigration",
    MigrationInProgress = "migrationInProgress",
    MigrationComplete = "migrationComplete",
    UnknownFutureValue = "unknownFutureValue",

