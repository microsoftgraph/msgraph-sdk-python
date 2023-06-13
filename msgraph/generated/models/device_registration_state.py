from enum import Enum

class DeviceRegistrationState(str, Enum):
    # The device is not registered.
    NotRegistered = "notRegistered",
    # The device is registered.
    Registered = "registered",
    # The device has been blocked, wiped or retired.
    Revoked = "revoked",
    # The device has a key conflict.
    KeyConflict = "keyConflict",
    # The device is pending approval.
    ApprovalPending = "approvalPending",
    # The device certificate has been reset.
    CertificateReset = "certificateReset",
    # The device is not registered and pending enrollment.
    NotRegisteredPendingEnrollment = "notRegisteredPendingEnrollment",
    # The device registration status is unknown.
    Unknown = "unknown",

