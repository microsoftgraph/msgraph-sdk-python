from enum import Enum

class WebsiteType(str, Enum):
    Other = "other",
    Home = "home",
    Work = "work",
    Blog = "blog",
    Profile = "profile",

