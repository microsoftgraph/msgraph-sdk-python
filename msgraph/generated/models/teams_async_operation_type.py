from enum import Enum

class TeamsAsyncOperationType(str, Enum):
    Invalid = "invalid",
    CloneTeam = "cloneTeam",
    ArchiveTeam = "archiveTeam",
    UnarchiveTeam = "unarchiveTeam",
    CreateTeam = "createTeam",
    UnknownFutureValue = "unknownFutureValue",
    TeamifyGroup = "teamifyGroup",
    CreateChannel = "createChannel",
    ArchiveChannel = "archiveChannel",
    UnarchiveChannel = "unarchiveChannel",

