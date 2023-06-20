from enum import Enum

class ChatMessagePolicyViolationVerdictDetailsTypes(str, Enum):
    None_ = "none",
    AllowFalsePositiveOverride = "allowFalsePositiveOverride",
    AllowOverrideWithoutJustification = "allowOverrideWithoutJustification",
    AllowOverrideWithJustification = "allowOverrideWithJustification",

