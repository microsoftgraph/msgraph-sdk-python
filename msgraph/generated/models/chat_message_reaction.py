from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import chat_message_reaction_identity_set

@dataclass
class ChatMessageReaction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported values are like, angry, sad, laugh, heart, surprised.
    reaction_type: Optional[str] = None
    # The user property
    user: Optional[chat_message_reaction_identity_set.ChatMessageReactionIdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessageReaction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageReaction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessageReaction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import chat_message_reaction_identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reactionType": lambda n : setattr(self, 'reaction_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(chat_message_reaction_identity_set.ChatMessageReactionIdentitySet)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("reactionType", self.reaction_type)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

