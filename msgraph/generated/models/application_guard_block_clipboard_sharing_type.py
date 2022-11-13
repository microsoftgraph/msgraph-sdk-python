from enum import Enum

class ApplicationGuardBlockClipboardSharingType(Enum):
    # Not Configured
    NotConfigured = "notConfigured",
    # Block clipboard to share data both from Host to Container and from Container to Host
    BlockBoth = "blockBoth",
    # Block clipboard to share data from Host to Container
    BlockHostToContainer = "blockHostToContainer",
    # Block clipboard to share data from Container to Host
    BlockContainerToHost = "blockContainerToHost",
    # Block clipboard to share data neither from Host to Container nor from Container to Host
    BlockNone = "blockNone",

