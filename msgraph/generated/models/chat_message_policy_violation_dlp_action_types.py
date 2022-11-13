from enum import Enum

class ChatMessagePolicyViolationDlpActionTypes(Enum):
    None_escaped = "none",
    NotifySender = "notifySender",
    BlockAccess = "blockAccess",
    BlockAccessExternal = "blockAccessExternal",

