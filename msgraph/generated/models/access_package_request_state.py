from enum import Enum

class AccessPackageRequestState(str, Enum):
    Submitted = "submitted",
    PendingApproval = "pendingApproval",
    Delivering = "delivering",
    Delivered = "delivered",
    DeliveryFailed = "deliveryFailed",
    Denied = "denied",
    Scheduled = "scheduled",
    Canceled = "canceled",
    PartiallyDelivered = "partiallyDelivered",
    UnknownFutureValue = "unknownFutureValue",

