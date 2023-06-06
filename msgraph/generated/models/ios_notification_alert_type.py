from enum import Enum

class IosNotificationAlertType(str, Enum):
    # Device default value, no intent.
    DeviceDefault = "deviceDefault",
    # Banner.
    Banner = "banner",
    # Modal.
    Modal = "modal",
    # None.
    None_ = "none",

