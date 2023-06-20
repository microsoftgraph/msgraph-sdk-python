from enum import Enum

class TeamworkApplicationIdentityType(str, Enum):
    AadApplication = "aadApplication",
    Bot = "bot",
    TenantBot = "tenantBot",
    Office365Connector = "office365Connector",
    OutgoingWebhook = "outgoingWebhook",
    UnknownFutureValue = "unknownFutureValue",

