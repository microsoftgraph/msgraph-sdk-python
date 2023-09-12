from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class ReplacePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The newText property
    new_text: Optional[Json] = None
    # The numChars property
    num_chars: Optional[Json] = None
    # The oldText property
    old_text: Optional[Json] = None
    # The startNum property
    start_num: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReplacePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReplacePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ReplacePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "newText": lambda n : setattr(self, 'new_text', n.get_object_value(Json)),
            "numChars": lambda n : setattr(self, 'num_chars', n.get_object_value(Json)),
            "oldText": lambda n : setattr(self, 'old_text', n.get_object_value(Json)),
            "startNum": lambda n : setattr(self, 'start_num', n.get_object_value(Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("newText", self.new_text)
        writer.write_object_value("numChars", self.num_chars)
        writer.write_object_value("oldText", self.old_text)
        writer.write_object_value("startNum", self.start_num)
        writer.write_additional_data_value(self.additional_data)
    

