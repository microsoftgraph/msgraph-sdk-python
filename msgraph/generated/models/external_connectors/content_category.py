from enum import Enum

class ContentCategory(str, Enum):
    Uncategorized = "uncategorized",
    KnowledgeBase = "knowledgeBase",
    Wikis = "wikis",
    FileRepository = "fileRepository",
    Qna = "qna",
    Crm = "crm",
    Dashboard = "dashboard",
    People = "people",
    Media = "media",
    Email = "email",
    Messaging = "messaging",
    MeetingTranscripts = "meetingTranscripts",
    TaskManagement = "taskManagement",
    LearningManagement = "learningManagement",
    UnknownFutureValue = "unknownFutureValue",

