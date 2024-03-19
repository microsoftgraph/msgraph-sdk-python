from enum import Enum

class RiskDetail(str, Enum):
    None_ = "none",
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
    M365DAdminDismissedDetection = "m365DAdminDismissedDetection",
    AdminConfirmedServicePrincipalCompromised = "adminConfirmedServicePrincipalCompromised",
    AdminDismissedAllRiskForServicePrincipal = "adminDismissedAllRiskForServicePrincipal",
    UserChangedPasswordOnPremises = "userChangedPasswordOnPremises",
    AdminDismissedRiskForSignIn = "adminDismissedRiskForSignIn",
    AdminConfirmedAccountSafe = "adminConfirmedAccountSafe",

