from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .engagement_conversation import EngagementConversation
    from .engagement_conversation_moderation_state import EngagementConversationModerationState
    from .engagement_identity_set import EngagementIdentitySet
    from .online_meeting import OnlineMeeting

from .engagement_conversation import EngagementConversation

@dataclass
class OnlineMeetingEngagementConversation(EngagementConversation, Parsable):
    """
    A conversation for Teams QA online meeting.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onlineMeetingEngagementConversation"
    # Represents the moderation state of an Engage conversation message.
    moderation_state: Optional[EngagementConversationModerationState] = None
    # The onlineMeeting property
    online_meeting: Optional[OnlineMeeting] = None
    # The unique identifier of the online meeting associated with this conversation. The online meeting ID links the conversation to a specific meeting instance.
    online_meeting_id: Optional[str] = None
    # The organizer property
    organizer: Optional[EngagementIdentitySet] = None
    # The number of upvotes the conversation received.
    upvote_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnlineMeetingEngagementConversation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeetingEngagementConversation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnlineMeetingEngagementConversation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .engagement_conversation import EngagementConversation
        from .engagement_conversation_moderation_state import EngagementConversationModerationState
        from .engagement_identity_set import EngagementIdentitySet
        from .online_meeting import OnlineMeeting

        from .engagement_conversation import EngagementConversation
        from .engagement_conversation_moderation_state import EngagementConversationModerationState
        from .engagement_identity_set import EngagementIdentitySet
        from .online_meeting import OnlineMeeting

        fields: dict[str, Callable[[Any], None]] = {
            "moderationState": lambda n : setattr(self, 'moderation_state', n.get_enum_value(EngagementConversationModerationState)),
            "onlineMeeting": lambda n : setattr(self, 'online_meeting', n.get_object_value(OnlineMeeting)),
            "onlineMeetingId": lambda n : setattr(self, 'online_meeting_id', n.get_str_value()),
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(EngagementIdentitySet)),
            "upvoteCount": lambda n : setattr(self, 'upvote_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("moderationState", self.moderation_state)
        writer.write_object_value("onlineMeeting", self.online_meeting)
        writer.write_str_value("onlineMeetingId", self.online_meeting_id)
        writer.write_object_value("organizer", self.organizer)
    

