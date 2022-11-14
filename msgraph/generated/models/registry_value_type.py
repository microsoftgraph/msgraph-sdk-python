from enum import Enum

class RegistryValueType(Enum):
    Unknown = "unknown",
    Binary = "binary",
    Dword = "dword",
    DwordLittleEndian = "dwordLittleEndian",
    DwordBigEndian = "dwordBigEndian",
    ExpandSz = "expandSz",
    Link = "link",
    MultiSz = "multiSz",
    None_escaped = "none",
    Qword = "qword",
    QwordlittleEndian = "qwordlittleEndian",
    Sz = "sz",
    UnknownFutureValue = "unknownFutureValue",

