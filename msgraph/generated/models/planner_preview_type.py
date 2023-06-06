from enum import Enum

class PlannerPreviewType(str, Enum):
    Automatic = "automatic",
    NoPreview = "noPreview",
    Checklist = "checklist",
    Description = "description",
    Reference = "reference",

