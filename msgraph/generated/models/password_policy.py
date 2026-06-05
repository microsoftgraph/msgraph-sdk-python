from enum import Enum

class PasswordPolicy(str, Enum):
    None_ = "none",
    ChangePasswordPeriod = "changePasswordPeriod",
    CharactersCombination = "charactersCombination",
    PasswordHistoryAndReuse = "passwordHistoryAndReuse",
    PasswordLengthLimit = "passwordLengthLimit",
    PersonalInformationUse = "personalInformationUse",
    UnknownFutureValue = "unknownFutureValue",

