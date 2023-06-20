from enum import Enum

class SimulationAttackTechnique(str, Enum):
    Unknown = "unknown",
    CredentialHarvesting = "credentialHarvesting",
    AttachmentMalware = "attachmentMalware",
    DriveByUrl = "driveByUrl",
    LinkInAttachment = "linkInAttachment",
    LinkToMalwareFile = "linkToMalwareFile",
    UnknownFutureValue = "unknownFutureValue",

