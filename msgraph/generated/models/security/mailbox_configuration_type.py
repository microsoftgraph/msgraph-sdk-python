from enum import Enum

class MailboxConfigurationType(str, Enum):
    MailForwardingRule = "mailForwardingRule",
    OwaSettings = "owaSettings",
    EwsSettings = "ewsSettings",
    MailDelegation = "mailDelegation",
    UserInboxRule = "userInboxRule",
    UnknownFutureValue = "unknownFutureValue",

