from enum import Enum

class EdgeSearchEngineType(Enum):
    # Uses factory settings of Edge to assign the default search engine as per the user market
    Default = "default",
    # Sets Bing as the default search engine
    Bing = "bing",

