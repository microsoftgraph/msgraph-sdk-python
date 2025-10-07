from enum import Enum

class EngagementConversationMessageReactionType(str, Enum):
    # Like reaction, represented as a thumbs-up hand. A positive sentiment.
    Like = "like",
    # Love reaction, represented as a solid heart shape. A very positive sentiment.
    Love = "love",
    # Celebrate reaction, represented as a party hat. A positive sentiment.
    Celebrate = "celebrate",
    # Thank reaction, represented as applauding hands. A positive sentiment.
    Thank = "thank",
    # Laugh reaction, represented as a grinning face. A positive sentiment.
    Laugh = "laugh",
    # Sad reaction, represented as a frowning face. A sympathetic sentiment.
    Sad = "sad",
    # Happy reaction, represented as an open mouth smile face. A very positive sentiment.
    Happy = "happy",
    # Excited reaction, represented as a face with closed eyes and a big smile. A very positive sentiment.
    Excited = "excited",
    # Smiling reaction, represented as a face with a small smile. A positive sentiment.
    Smile = "smile",
    # Silly reaction, represented as an upside down smiling face. A positive sentiment.
    Silly = "silly",
    # Intense laughter reaction, represented as a crying laughing face. A very positive sentiment.
    IntenseLaugh = "intenseLaugh",
    # Star struck reaction, represented as a face with stars for eyes. A very positive sentiment.
    StarStruck = "starStruck",
    # Goofy reaction, represented as a face with tongue sticking out of mouth. A positive sentiment.
    Goofy = "goofy",
    # Thinking reaction, represented as a face with a hand on the chin. A neutral sentiment.
    Thinking = "thinking",
    # Surprised reaction, represented as a face with its mouth open. A neutral sentiment.
    Surprised = "surprised",
    # Mind blown reaction, represented as a face with its head covered in an exploding cloud. A positive sentiment.
    MindBlown = "mindBlown",
    # Scared reaction, represented as a face with fearful look. A negative sentiment.
    Scared = "scared",
    # Crying reaction, represented as a face with tears streaming down. A negative sentiment.
    Crying = "crying",
    # Shocked reaction, represented as a face with two hands against cheeks and mouth open. A negative sentiment.
    Shocked = "shocked",
    # Angry reaction, represented as a face with furrowed eyebrows and sad mouth. A very negative sentiment.
    Angry = "angry",
    # Agree reaction, represented as a hand pointing upward. A positive sentiment.
    Agree = "agree",
    # Praise reaction, represented as two hands facing outward. A positive sentiment.
    Praise = "praise",
    # Taking notes reaction, represented as a hand holding a pen. A neutral sentiment.
    TakingNotes = "takingNotes",
    # Heart broken reaction, represented as a broken heart. A negative sentiment.
    HeartBroken = "heartBroken",
    # Support reaction, represented as red numbers showing 100. A positive sentiment.
    Support = "support",
    # Confirmed reaction, represented as a green check mark. A neutral sentiment.
    Confirmed = "confirmed",
    # Watching reaction, represented as two eyeballs. A neutral sentiment.
    Watching = "watching",
    # Brain reaction, represented as a brain. A neutral sentiment.
    Brain = "brain",
    # Medal reaction, represented as a medal hanging from a sash. A positive sentiment.
    Medal = "medal",
    # Bullseye reaction, represented as a target with an arrow in the middle. A positive sentiment.
    Bullseye = "bullseye",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

