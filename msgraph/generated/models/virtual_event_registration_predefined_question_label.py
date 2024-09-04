from enum import Enum

class VirtualEventRegistrationPredefinedQuestionLabel(str, Enum):
    Street = "street",
    City = "city",
    State = "state",
    PostalCode = "postalCode",
    CountryOrRegion = "countryOrRegion",
    Industry = "industry",
    JobTitle = "jobTitle",
    Organization = "organization",
    UnknownFutureValue = "unknownFutureValue",

