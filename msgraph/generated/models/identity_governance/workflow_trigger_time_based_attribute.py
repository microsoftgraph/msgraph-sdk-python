from enum import Enum

class WorkflowTriggerTimeBasedAttribute(str, Enum):
    EmployeeHireDate = "employeeHireDate",
    EmployeeLeaveDateTime = "employeeLeaveDateTime",
    UnknownFutureValue = "unknownFutureValue",
    CreatedDateTime = "createdDateTime",

