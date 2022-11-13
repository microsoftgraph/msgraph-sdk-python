from enum import Enum

class AccessPackageAssignmentState(Enum):
    Delivering = "delivering",
    PartiallyDelivered = "partiallyDelivered",
    Delivered = "delivered",
    Expired = "expired",
    DeliveryFailed = "deliveryFailed",
    UnknownFutureValue = "unknownFutureValue",

