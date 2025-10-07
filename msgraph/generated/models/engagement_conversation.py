from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .engagement_conversation_message import EngagementConversationMessage
    from .engagement_creation_mode import EngagementCreationMode
    from .entity import Entity
    from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation

from .entity import Entity

@dataclass
class EngagementConversation(Entity, Parsable):
    """
    Represents a conversation in Viva Engage.
    """
    # Indicates that the resource is in migration state and is currently being used for migration purposes.
    creation_mode: Optional[EngagementCreationMode] = None
    # The messages in a Viva Engage conversation.
    messages: Optional[list[EngagementConversationMessage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The starter property
    starter: Optional[EngagementConversationMessage] = None
    # The unique ID of the first message in a Viva Engage conversation.
    starter_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EngagementConversation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EngagementConversation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onlineMeetingEngagementConversation".casefold():
            from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation

            return OnlineMeetingEngagementConversation()
        return EngagementConversation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .engagement_conversation_message import EngagementConversationMessage
        from .engagement_creation_mode import EngagementCreationMode
        from .entity import Entity
        from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation

        from .engagement_conversation_message import EngagementConversationMessage
        from .engagement_creation_mode import EngagementCreationMode
        from .entity import Entity
        from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation

        fields: dict[str, Callable[[Any], None]] = {
            "creationMode": lambda n : setattr(self, 'creation_mode', n.get_enum_value(EngagementCreationMode)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(EngagementConversationMessage)),
            "starter": lambda n : setattr(self, 'starter', n.get_object_value(EngagementConversationMessage)),
            "starterId": lambda n : setattr(self, 'starter_id', n.get_str_value()),
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
        writer.write_enum_value("creationMode", self.creation_mode)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_object_value("starter", self.starter)
        writer.write_str_value("starterId", self.starter_id)
    

