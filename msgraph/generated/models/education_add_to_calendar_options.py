from enum import Enum

class EducationAddToCalendarOptions(str, Enum):
    None_ = "none",
    StudentsAndPublisher = "studentsAndPublisher",
    StudentsAndTeamOwners = "studentsAndTeamOwners",
    UnknownFutureValue = "unknownFutureValue",
    StudentsOnly = "studentsOnly",

