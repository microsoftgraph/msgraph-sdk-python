from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_type import AttributeType

@dataclass
class AttributeMappingParameterSchema(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The given parameter can be provided multiple times (for example, multiple input strings in the Concatenate(string,string,...) function).
    allow_multiple_occurrences: Optional[bool] = None
    # Parameter name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # true if the parameter is required; otherwise false.
    required: Optional[bool] = None
    # The type property
    type: Optional[AttributeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttributeMappingParameterSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttributeMappingParameterSchema
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttributeMappingParameterSchema()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_type import AttributeType

        from .attribute_type import AttributeType

        fields: Dict[str, Callable[[Any], None]] = {
            "allowMultipleOccurrences": lambda n : setattr(self, 'allow_multiple_occurrences', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(AttributeType)),
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
        writer.write_bool_value("allowMultipleOccurrences", self.allow_multiple_occurrences)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("required", self.required)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

