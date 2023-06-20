from enum import Enum

class ExchangeIdFormat(str, Enum):
    EntryId = "entryId",
    EwsId = "ewsId",
    ImmutableEntryId = "immutableEntryId",
    RestId = "restId",
    RestImmutableEntryId = "restImmutableEntryId",

