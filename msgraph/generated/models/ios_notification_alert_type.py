from enum import Enum

class IosNotificationAlertType(Enum):
    # Device default value, no intent.
    DeviceDefault = "deviceDefault",
    # Banner.
    Banner = "banner",
    # Modal.
    Modal = "modal",
    # None.
    None_escaped = "none",

