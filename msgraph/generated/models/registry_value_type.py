from enum import Enum

class RegistryValueType(str, Enum):
    Unknown = "unknown",
    Binary = "binary",
    Dword = "dword",
    DwordLittleEndian = "dwordLittleEndian",
    DwordBigEndian = "dwordBigEndian",
    ExpandSz = "expandSz",
    Link = "link",
    MultiSz = "multiSz",
    None_ = "none",
    Qword = "qword",
    QwordlittleEndian = "qwordlittleEndian",
    Sz = "sz",
    UnknownFutureValue = "unknownFutureValue",

