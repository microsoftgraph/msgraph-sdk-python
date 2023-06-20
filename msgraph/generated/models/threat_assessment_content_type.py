from enum import Enum

class ThreatAssessmentContentType(str, Enum):
    Mail = "mail",
    Url = "url",
    File = "file",

