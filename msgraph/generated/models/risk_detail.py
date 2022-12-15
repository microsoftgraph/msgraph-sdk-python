from enum import Enum

class RiskDetail(Enum):
    None_escaped = "none",
    AdminGeneratedTemporaryPassword = "adminGeneratedTemporaryPassword",
    UserPerformedSecuredPasswordChange = "userPerformedSecuredPasswordChange",
    UserPerformedSecuredPasswordReset = "userPerformedSecuredPasswordReset",
    AdminConfirmedSigninSafe = "adminConfirmedSigninSafe",
    AiConfirmedSigninSafe = "aiConfirmedSigninSafe",
    UserPassedMFADrivenByRiskBasedPolicy = "userPassedMFADrivenByRiskBasedPolicy",
    AdminDismissedAllRiskForUser = "adminDismissedAllRiskForUser",
    AdminConfirmedSigninCompromised = "adminConfirmedSigninCompromised",
    Hidden = "hidden",
    AdminConfirmedUserCompromised = "adminConfirmedUserCompromised",
    UnknownFutureValue = "unknownFutureValue",
    AdminConfirmedServicePrincipalCompromised = "adminConfirmedServicePrincipalCompromised",
    AdminDismissedAllRiskForServicePrincipal = "adminDismissedAllRiskForServicePrincipal",
    M365DAdminDismissedDetection = "m365DAdminDismissedDetection",

