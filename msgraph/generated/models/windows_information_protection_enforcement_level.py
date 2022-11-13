from enum import Enum

class WindowsInformationProtectionEnforcementLevel(Enum):
    # No protection enforcement
    NoProtection = "noProtection",
    # Encrypt and Audit only
    EncryptAndAuditOnly = "encryptAndAuditOnly",
    # Encrypt, Audit and Prompt
    EncryptAuditAndPrompt = "encryptAuditAndPrompt",
    # Encrypt, Audit and Block
    EncryptAuditAndBlock = "encryptAuditAndBlock",

