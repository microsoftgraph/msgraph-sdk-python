from enum import Enum

class AuditLogUserType(str, Enum):
    Regular = "Regular",
    Reserved = "Reserved",
    Admin = "Admin",
    DcAdmin = "DcAdmin",
    System = "System",
    Application = "Application",
    ServicePrincipal = "ServicePrincipal",
    CustomPolicy = "CustomPolicy",
    SystemPolicy = "SystemPolicy",
    PartnerTechnician = "PartnerTechnician",
    Guest = "Guest",
    UnknownFutureValue = "unknownFutureValue",

