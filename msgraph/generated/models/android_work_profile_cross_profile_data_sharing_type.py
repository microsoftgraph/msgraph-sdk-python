from enum import Enum

class AndroidWorkProfileCrossProfileDataSharingType(str, Enum):
    # Device default value, no intent.
    DeviceDefault = "deviceDefault",
    # Prevent any sharing.
    PreventAny = "preventAny",
    # Allow data sharing request from personal profile to work profile.
    AllowPersonalToWork = "allowPersonalToWork",
    # No restrictions on sharing.
    NoRestrictions = "noRestrictions",

