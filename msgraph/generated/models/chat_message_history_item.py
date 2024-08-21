from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message_actions import ChatMessageActions
    from .chat_message_reaction import ChatMessageReaction

@dataclass
class ChatMessageHistoryItem(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The actions property
    actions: Optional[ChatMessageActions] = None
    # The date and time when the message was modified.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reaction in the modified message.
    reaction: Optional[ChatMessageReaction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChatMessageHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageHistoryItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChatMessageHistoryItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message_actions import ChatMessageActions
        from .chat_message_reaction import ChatMessageReaction

        from .chat_message_actions import ChatMessageActions
        from .chat_message_reaction import ChatMessageReaction

        fields: Dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_collection_of_enum_values(ChatMessageActions)),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reaction": lambda n : setattr(self, 'reaction', n.get_object_value(ChatMessageReaction)),
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
        writer.write_enum_value("actions", self.actions)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("reaction", self.reaction)
        writer.write_additional_data_value(self.additional_data)
    

