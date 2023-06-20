from enum import Enum

class Mutability(str, Enum):
    ReadWrite = "ReadWrite",
    ReadOnly = "ReadOnly",
    Immutable = "Immutable",
    WriteOnly = "WriteOnly",

