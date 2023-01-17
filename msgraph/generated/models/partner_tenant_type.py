from enum import Enum

class PartnerTenantType(Enum):
    MicrosoftSupport = "microsoftSupport",
    SyndicatePartner = "syndicatePartner",
    BreadthPartner = "breadthPartner",
    BreadthPartnerDelegatedAdmin = "breadthPartnerDelegatedAdmin",
    ResellerPartnerDelegatedAdmin = "resellerPartnerDelegatedAdmin",
    ValueAddedResellerPartnerDelegatedAdmin = "valueAddedResellerPartnerDelegatedAdmin",
    UnknownFutureValue = "unknownFutureValue",

