from enum import Enum

class TeamsAsyncOperationType(Enum):
    Invalid = "invalid",
    CloneTeam = "cloneTeam",
    ArchiveTeam = "archiveTeam",
    UnarchiveTeam = "unarchiveTeam",
    CreateTeam = "createTeam",
    UnknownFutureValue = "unknownFutureValue",
    TeamifyGroup = "teamifyGroup",
    CreateChannel = "createChannel",

