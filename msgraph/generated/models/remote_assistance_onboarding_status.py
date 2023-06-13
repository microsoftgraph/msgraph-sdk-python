from enum import Enum

class RemoteAssistanceOnboardingStatus(str, Enum):
    # The status reported when there is no active TeamViewer connector configured or active
    NotOnboarded = "notOnboarded",
    # The status reported when the system has initiated a TeamViewer connection, but the service has not yet completed the confirmation of a connector
    Onboarding = "onboarding",
    # The status reported when the system has successfully exchanged account information with TeamViewer and can now initiate remote assistance sessions with clients
    Onboarded = "onboarded",

