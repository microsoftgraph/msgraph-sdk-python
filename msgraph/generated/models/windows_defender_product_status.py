from enum import Enum

class WindowsDefenderProductStatus(str, Enum):
    # No status
    NoStatus = "noStatus",
    # Service not running
    ServiceNotRunning = "serviceNotRunning",
    # Service started without any malware protection engine
    ServiceStartedWithoutMalwareProtection = "serviceStartedWithoutMalwareProtection",
    # Pending full scan due to threat action
    PendingFullScanDueToThreatAction = "pendingFullScanDueToThreatAction",
    # Pending reboot due to threat action
    PendingRebootDueToThreatAction = "pendingRebootDueToThreatAction",
    # Pending manual steps due to threat action
    PendingManualStepsDueToThreatAction = "pendingManualStepsDueToThreatAction",
    # Antivirus (AV) signatures out of date
    AvSignaturesOutOfDate = "avSignaturesOutOfDate",
    # Antisypware (AS) signatures out of date
    AsSignaturesOutOfDate = "asSignaturesOutOfDate",
    # No quick scan has happened for a specified period
    NoQuickScanHappenedForSpecifiedPeriod = "noQuickScanHappenedForSpecifiedPeriod",
    # No full scan has happened for a specified period
    NoFullScanHappenedForSpecifiedPeriod = "noFullScanHappenedForSpecifiedPeriod",
    # System initiated scan in progress
    SystemInitiatedScanInProgress = "systemInitiatedScanInProgress",
    # System initiated clean in progress
    SystemInitiatedCleanInProgress = "systemInitiatedCleanInProgress",
    # There are samples pending submission
    SamplesPendingSubmission = "samplesPendingSubmission",
    # Product running in evaluation mode
    ProductRunningInEvaluationMode = "productRunningInEvaluationMode",
    # Product running in non-genuine Windows mode
    ProductRunningInNonGenuineMode = "productRunningInNonGenuineMode",
    # Product expired
    ProductExpired = "productExpired",
    # Off-line scan required
    OfflineScanRequired = "offlineScanRequired",
    # Service is shutting down as part of system shutdown
    ServiceShutdownAsPartOfSystemShutdown = "serviceShutdownAsPartOfSystemShutdown",
    # Threat remediation failed critically
    ThreatRemediationFailedCritically = "threatRemediationFailedCritically",
    # Threat remediation failed non-critically
    ThreatRemediationFailedNonCritically = "threatRemediationFailedNonCritically",
    # No status flags set (well initialized state)
    NoStatusFlagsSet = "noStatusFlagsSet",
    # Platform is out of date
    PlatformOutOfDate = "platformOutOfDate",
    # Platform update is in progress
    PlatformUpdateInProgress = "platformUpdateInProgress",
    # Platform is about to be outdated
    PlatformAboutToBeOutdated = "platformAboutToBeOutdated",
    # Signature or platform end of life is past or is impending
    SignatureOrPlatformEndOfLifeIsPastOrIsImpending = "signatureOrPlatformEndOfLifeIsPastOrIsImpending",
    # Windows SMode signatures still in use on non-Win10S install
    WindowsSModeSignaturesInUseOnNonWin10SInstall = "windowsSModeSignaturesInUseOnNonWin10SInstall",

