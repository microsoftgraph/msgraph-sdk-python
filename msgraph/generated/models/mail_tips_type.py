from enum import Enum

class MailTipsType(Enum):
    AutomaticReplies = "automaticReplies",
    MailboxFullStatus = "mailboxFullStatus",
    CustomMailTip = "customMailTip",
    ExternalMemberCount = "externalMemberCount",
    TotalMemberCount = "totalMemberCount",
    MaxMessageSize = "maxMessageSize",
    DeliveryRestriction = "deliveryRestriction",
    ModerationStatus = "moderationStatus",
    RecipientScope = "recipientScope",
    RecipientSuggestions = "recipientSuggestions",

