from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.message import Message

@dataclass
class CreateReplyAllPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The Comment property
    comment: Optional[str] = None
    # The Message property
    message: Optional[Message] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateReplyAllPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateReplyAllPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateReplyAllPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.message import Message

        from ......models.message import Message

        fields: Dict[str, Callable[[Any], None]] = {
            "Comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "Message": lambda n : setattr(self, 'message', n.get_object_value(Message)),
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
        from ......models.message import Message

        writer.write_str_value("Comment", self.comment)
        writer.write_object_value("Message", self.message)
        writer.write_additional_data_value(self.additional_data)
    

