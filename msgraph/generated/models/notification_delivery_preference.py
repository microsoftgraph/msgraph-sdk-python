from enum import Enum

class NotificationDeliveryPreference(str, Enum):
    Unknown = "unknown",
    DeliverImmedietly = "deliverImmedietly",
    DeliverAfterCampaignEnd = "deliverAfterCampaignEnd",
    UnknownFutureValue = "unknownFutureValue",

