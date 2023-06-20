from enum import Enum

class ClonableTeamParts(str, Enum):
    Apps = "apps",
    Tabs = "tabs",
    Settings = "settings",
    Channels = "channels",
    Members = "members",

