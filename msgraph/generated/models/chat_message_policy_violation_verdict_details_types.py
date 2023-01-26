from enum import Enum

class ChatMessagePolicyViolationVerdictDetailsTypes(Enum):
    None_ = "none",
    AllowFalsePositiveOverride = "allowFalsePositiveOverride",
    AllowOverrideWithoutJustification = "allowOverrideWithoutJustification",
    AllowOverrideWithJustification = "allowOverrideWithJustification",

