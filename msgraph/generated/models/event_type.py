from enum import Enum

class EventType(str, Enum):
    SingleInstance = "singleInstance",
    Occurrence = "occurrence",
    Exception = "exception",
    SeriesMaster = "seriesMaster",

