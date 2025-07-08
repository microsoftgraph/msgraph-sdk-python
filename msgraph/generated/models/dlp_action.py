from enum import Enum

class DlpAction(str, Enum):
    NotifyUser = "notifyUser",
    BlockAccess = "blockAccess",
    DeviceRestriction = "deviceRestriction",
    BrowserRestriction = "browserRestriction",
    UnknownFutureValue = "unknownFutureValue",
    RestrictAccess = "restrictAccess",
    GenerateAlert = "generateAlert",
    GenerateIncidentReportAction = "generateIncidentReportAction",
    SPBlockAnonymousAccess = "sPBlockAnonymousAccess",
    SPRuntimeAccessControl = "sPRuntimeAccessControl",
    SPSharingNotifyUser = "sPSharingNotifyUser",
    SPSharingGenerateIncidentReport = "sPSharingGenerateIncidentReport",

