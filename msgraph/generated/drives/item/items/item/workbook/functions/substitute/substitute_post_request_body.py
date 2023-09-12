from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class SubstitutePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The instanceNum property
    instance_num: Optional[Json] = None
    # The newText property
    new_text: Optional[Json] = None
    # The oldText property
    old_text: Optional[Json] = None
    # The text property
    text: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubstitutePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubstitutePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SubstitutePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "instanceNum": lambda n : setattr(self, 'instance_num', n.get_object_value(Json)),
            "newText": lambda n : setattr(self, 'new_text', n.get_object_value(Json)),
            "oldText": lambda n : setattr(self, 'old_text', n.get_object_value(Json)),
            "text": lambda n : setattr(self, 'text', n.get_object_value(Json)),
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
        writer.write_object_value("instanceNum", self.instance_num)
        writer.write_object_value("newText", self.new_text)
        writer.write_object_value("oldText", self.old_text)
        writer.write_object_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

