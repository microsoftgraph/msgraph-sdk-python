from enum import Enum

class VideoCodec(str, Enum):
    Unknown = "unknown",
    Invalid = "invalid",
    Av1 = "av1",
    H263 = "h263",
    H264 = "h264",
    H264s = "h264s",
    H264uc = "h264uc",
    H265 = "h265",
    Rtvc1 = "rtvc1",
    RtVideo = "rtVideo",
    Xrtvc1 = "xrtvc1",
    UnknownFutureValue = "unknownFutureValue",

