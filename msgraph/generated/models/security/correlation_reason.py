from enum import Enum

class CorrelationReason(str, Enum):
    RepeatedAlertOccurrence = "repeatedAlertOccurrence",
    SameGeography = "sameGeography",
    SimilarArtifacts = "similarArtifacts",
    SameTargetedAsset = "sameTargetedAsset",
    SameNetworkSegment = "sameNetworkSegment",
    EventSequence = "eventSequence",
    TimeFrame = "timeFrame",
    SameThreatSource = "sameThreatSource",
    SimilarTTPsOrBehavior = "similarTTPsOrBehavior",
    SameActor = "sameActor",
    SameCampaign = "sameCampaign",
    SharedIndicators = "sharedIndicators",
    SameAsset = "sameAsset",
    NetworkProximity = "networkProximity",
    EventCasualSequence = "eventCasualSequence",
    TemporalProximity = "temporalProximity",
    LateralMovementPath = "lateralMovementPath",
    UnknownFutureValue = "unknownFutureValue",

