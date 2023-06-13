from enum import Enum

class DelegateMeetingMessageDeliveryOptions(str, Enum):
    SendToDelegateAndInformationToPrincipal = "sendToDelegateAndInformationToPrincipal",
    SendToDelegateAndPrincipal = "sendToDelegateAndPrincipal",
    SendToDelegateOnly = "sendToDelegateOnly",

