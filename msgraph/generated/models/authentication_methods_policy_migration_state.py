from enum import Enum

class AuthenticationMethodsPolicyMigrationState(Enum):
    PreMigration = "preMigration",
    MigrationInProgress = "migrationInProgress",
    MigrationComplete = "migrationComplete",
    UnknownFutureValue = "unknownFutureValue",

