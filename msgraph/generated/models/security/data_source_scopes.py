from enum import Enum

class DataSourceScopes(str, Enum):
    None_ = "none",
    AllTenantMailboxes = "allTenantMailboxes",
    AllTenantSites = "allTenantSites",
    AllCaseCustodians = "allCaseCustodians",
    AllCaseNoncustodialDataSources = "allCaseNoncustodialDataSources",
    UnknownFutureValue = "unknownFutureValue",

