from enum import Enum

class ChatMessagePolicyViolationDlpActionTypes(str, Enum):
    None_ = "none",
    NotifySender = "notifySender",
    BlockAccess = "blockAccess",
    BlockAccessExternal = "blockAccessExternal",

