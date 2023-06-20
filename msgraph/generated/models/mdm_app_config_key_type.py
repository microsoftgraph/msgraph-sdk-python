from enum import Enum

class MdmAppConfigKeyType(str, Enum):
    StringType = "stringType",
    IntegerType = "integerType",
    RealType = "realType",
    BooleanType = "booleanType",
    TokenType = "tokenType",

