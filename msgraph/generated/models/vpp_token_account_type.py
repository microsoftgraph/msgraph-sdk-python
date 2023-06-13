from enum import Enum

class VppTokenAccountType(str, Enum):
    # Apple Volume Purchase Program token associated with an business program.
    Business = "business",
    # Apple Volume Purchase Program token associated with an education program.
    Education = "education",

