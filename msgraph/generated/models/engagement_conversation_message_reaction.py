from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .engagement_conversation_message_reaction_type import EngagementConversationMessageReactionType
    from .engagement_identity_set import EngagementIdentitySet
    from .entity import Entity

from .entity import Entity

@dataclass
class EngagementConversationMessageReaction(Entity, Parsable):
    """
    A reaction to a conversation message.
    """
    # Date and time when the reaction was added. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reactionBy property
    reaction_by: Optional[EngagementIdentitySet] = None
    # Types of reactions to conversation messages.
    reaction_type: Optional[EngagementConversationMessageReactionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EngagementConversationMessageReaction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EngagementConversationMessageReaction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EngagementConversationMessageReaction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .engagement_conversation_message_reaction_type import EngagementConversationMessageReactionType
        from .engagement_identity_set import EngagementIdentitySet
        from .entity import Entity

        from .engagement_conversation_message_reaction_type import EngagementConversationMessageReactionType
        from .engagement_identity_set import EngagementIdentitySet
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "reactionBy": lambda n : setattr(self, 'reaction_by', n.get_object_value(EngagementIdentitySet)),
            "reactionType": lambda n : setattr(self, 'reaction_type', n.get_enum_value(EngagementConversationMessageReactionType)),
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
        writer.write_object_value("reactionBy", self.reaction_by)
        writer.write_enum_value("reactionType", self.reaction_type)
    

