from enum import Enum

class SharingDomainRestrictionMode(Enum):
    None_ = "none",
    AllowList = "allowList",
    BlockList = "blockList",
    UnknownFutureValue = "unknownFutureValue",

