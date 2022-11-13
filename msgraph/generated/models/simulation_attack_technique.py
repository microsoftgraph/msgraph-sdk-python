from enum import Enum

class SimulationAttackTechnique(Enum):
    Unknown = "unknown",
    CredentialHarvesting = "credentialHarvesting",
    AttachmentMalware = "attachmentMalware",
    DriveByUrl = "driveByUrl",
    LinkInAttachment = "linkInAttachment",
    LinkToMalwareFile = "linkToMalwareFile",
    UnknownFutureValue = "unknownFutureValue",

