from enum import Enum

class LifecycleEventType(Enum):
    Missed = "missed",
    SubscriptionRemoved = "subscriptionRemoved",
    ReauthorizationRequired = "reauthorizationRequired",

