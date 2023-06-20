from enum import Enum

class ChatMessagePolicyViolationUserActionTypes(str, Enum):
    None_ = "none",
    Override = "override",
    ReportFalsePositive = "reportFalsePositive",

