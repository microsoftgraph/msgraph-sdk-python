from enum import Enum

class LocationType(str, Enum):
    Default = "default",
    ConferenceRoom = "conferenceRoom",
    HomeAddress = "homeAddress",
    BusinessAddress = "businessAddress",
    GeoCoordinates = "geoCoordinates",
    StreetAddress = "streetAddress",
    Hotel = "hotel",
    Restaurant = "restaurant",
    LocalBusiness = "localBusiness",
    PostalAddress = "postalAddress",

