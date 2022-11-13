from enum import Enum

class AndroidWorkProfileDefaultAppPermissionPolicyType(Enum):
    # Device default value, no intent.
    DeviceDefault = "deviceDefault",
    # Prompt.
    Prompt = "prompt",
    # Auto grant.
    AutoGrant = "autoGrant",
    # Auto deny.
    AutoDeny = "autoDeny",

