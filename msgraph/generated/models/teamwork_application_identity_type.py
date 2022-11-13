from enum import Enum

class TeamworkApplicationIdentityType(Enum):
    AadApplication = "aadApplication",
    Bot = "bot",
    TenantBot = "tenantBot",
    Office365Connector = "office365Connector",
    OutgoingWebhook = "outgoingWebhook",
    UnknownFutureValue = "unknownFutureValue",

