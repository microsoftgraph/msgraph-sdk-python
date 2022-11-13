from enum import Enum

class MicrosoftEdgeChannel(Enum):
    # The Dev Channel is intended to help you plan and develop with the latest capabilities of Microsoft Edge.
    Dev = "dev",
    # The Beta Channel is intended for production deployment to a representative sample set of users. New features ship about every 4 weeks. Security and quality updates ship as needed.
    Beta = "beta",
    # The Stable Channel is intended for broad deployment within organizations, and it's the channel that most users should be on. New features ship about every 4 weeks. Security and quality updates ship as needed.
    Stable = "stable",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

