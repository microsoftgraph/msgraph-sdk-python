from enum import Enum

class ChatMessagePolicyViolationVerdictDetailsTypes(Enum):
    None_escaped = "none",
    AllowFalsePositiveOverride = "allowFalsePositiveOverride",
    AllowOverrideWithoutJustification = "allowOverrideWithoutJustification",
    AllowOverrideWithJustification = "allowOverrideWithJustification",

