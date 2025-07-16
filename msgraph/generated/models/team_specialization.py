from enum import Enum

class TeamSpecialization(str, Enum):
    None_ = "none",
    EducationStandard = "educationStandard",
    EducationClass = "educationClass",
    EducationProfessionalLearningCommunity = "educationProfessionalLearningCommunity",
    EducationStaff = "educationStaff",
    HealthcareStandard = "healthcareStandard",
    HealthcareCareCoordination = "healthcareCareCoordination",
    UnknownFutureValue = "unknownFutureValue",

