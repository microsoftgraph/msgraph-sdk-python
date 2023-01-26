from enum import Enum

class ChatMessagePolicyViolationDlpActionTypes(Enum):
    None_ = "none",
    NotifySender = "notifySender",
    BlockAccess = "blockAccess",
    BlockAccessExternal = "blockAccessExternal",

