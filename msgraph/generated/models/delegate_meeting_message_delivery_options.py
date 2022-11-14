from enum import Enum

class DelegateMeetingMessageDeliveryOptions(Enum):
    SendToDelegateAndInformationToPrincipal = "sendToDelegateAndInformationToPrincipal",
    SendToDelegateAndPrincipal = "sendToDelegateAndPrincipal",
    SendToDelegateOnly = "sendToDelegateOnly",

