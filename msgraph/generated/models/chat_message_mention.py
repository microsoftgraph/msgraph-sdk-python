from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet

@dataclass
class ChatMessageMention(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Index of an entity being mentioned in the specified chatMessage. Matches the {index} value in the corresponding <at id='{index}'> tag in the message body.
    id: Optional[int] = None
    # String used to represent the mention. For example, a user's display name, a team name.
    mention_text: Optional[str] = None
    # The entity (user, application, team, or channel) that was @mentioned.
    mentioned: Optional[ChatMessageMentionedIdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChatMessageMention:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageMention
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChatMessageMention()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet

        from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "mentionText": lambda n : setattr(self, 'mention_text', n.get_str_value()),
            "mentioned": lambda n : setattr(self, 'mentioned', n.get_object_value(ChatMessageMentionedIdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("id", self.id)
        writer.write_str_value("mentionText", self.mention_text)
        writer.write_object_value("mentioned", self.mentioned)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

