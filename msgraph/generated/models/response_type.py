from enum import Enum

class ResponseType(Enum):
    None_escaped = "none",
    Organizer = "organizer",
    TentativelyAccepted = "tentativelyAccepted",
    Accepted = "accepted",
    Declined = "declined",
    NotResponded = "notResponded",

