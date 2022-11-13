from enum import Enum

class DeviceEnrollmentFailureReason(Enum):
    # Default value, failure reason is unknown.
    Unknown = "unknown",
    # Authentication failed
    Authentication = "authentication",
    # Call was authenticated, but not authorized to enroll.
    Authorization = "authorization",
    # Failed to validate the account for enrollment. (Account blocked, enrollment not enabled)
    AccountValidation = "accountValidation",
    # User could not be validated. (User does not exist, missing license)
    UserValidation = "userValidation",
    # Device is not supported for mobile device management.
    DeviceNotSupported = "deviceNotSupported",
    # Account is in maintenance.
    InMaintenance = "inMaintenance",
    # Client sent a request that is not understood/supported by the service.
    BadRequest = "badRequest",
    # Feature(s) used by this enrollment are not supported for this account.
    FeatureNotSupported = "featureNotSupported",
    # Enrollment restrictions configured by admin blocked this enrollment.
    EnrollmentRestrictionsEnforced = "enrollmentRestrictionsEnforced",
    # Client timed out or enrollment was aborted by enduser.
    ClientDisconnected = "clientDisconnected",
    # Enrollment was abandoned by enduser. (Enduser started onboarding but failed to complete it in timely manner)
    UserAbandonment = "userAbandonment",

