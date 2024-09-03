from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ChoiceColumn(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # If true, allows custom values that aren't in the configured choices.
    allow_text_entry: Optional[bool] = None
    # The list of values available for this column.
    choices: Optional[List[str]] = None
    # How the choices are to be presented in the UX. Must be one of checkBoxes, dropDownMenu, or radioButtons
    display_as: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChoiceColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChoiceColumn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChoiceColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allowTextEntry": lambda n : setattr(self, 'allow_text_entry', n.get_bool_value()),
            "choices": lambda n : setattr(self, 'choices', n.get_collection_of_primitive_values(str)),
            "displayAs": lambda n : setattr(self, 'display_as', n.get_str_value()),
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
        writer.write_bool_value("allowTextEntry", self.allow_text_entry)
        writer.write_collection_of_primitive_values("choices", self.choices)
        writer.write_str_value("displayAs", self.display_as)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

