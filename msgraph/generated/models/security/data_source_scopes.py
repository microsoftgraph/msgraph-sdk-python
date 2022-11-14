from enum import Enum

class DataSourceScopes(Enum):
    None_escaped = "none",
    AllTenantMailboxes = "allTenantMailboxes",
    AllTenantSites = "allTenantSites",
    AllCaseCustodians = "allCaseCustodians",
    AllCaseNoncustodialDataSources = "allCaseNoncustodialDataSources",
    UnknownFutureValue = "unknownFutureValue",

