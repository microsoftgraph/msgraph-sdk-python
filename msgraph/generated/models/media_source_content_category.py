from enum import Enum

class MediaSourceContentCategory(str, Enum):
    Meeting = "meeting",
    LiveStream = "liveStream",
    Presentation = "presentation",
    ScreenRecording = "screenRecording",
    Story = "story",
    Profile = "profile",
    Chat = "chat",
    Note = "note",
    Comment = "comment",
    UnknownFutureValue = "unknownFutureValue",

