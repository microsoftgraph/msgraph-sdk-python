from enum import Enum

class SharingDomainRestrictionMode(str, Enum):
    None_ = "none",
    AllowList = "allowList",
    BlockList = "blockList",
    UnknownFutureValue = "unknownFutureValue",

