from enum import Enum

class ExchangeIdFormat(Enum):
    EntryId = "entryId",
    EwsId = "ewsId",
    ImmutableEntryId = "immutableEntryId",
    RestId = "restId",
    RestImmutableEntryId = "restImmutableEntryId",

