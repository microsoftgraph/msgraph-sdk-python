from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TextColumn(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Whether to allow multiple lines of text.
    allow_multiple_lines: Optional[bool] = None
    # Whether updates to this column should replace existing text, or append to it.
    append_changes_to_existing_text: Optional[bool] = None
    # The size of the text box.
    lines_for_editing: Optional[int] = None
    # The maximum number of characters for the value.
    max_length: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of text being stored. Must be one of plain or richText
    text_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TextColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TextColumn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TextColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allowMultipleLines": lambda n : setattr(self, 'allow_multiple_lines', n.get_bool_value()),
            "appendChangesToExistingText": lambda n : setattr(self, 'append_changes_to_existing_text', n.get_bool_value()),
            "linesForEditing": lambda n : setattr(self, 'lines_for_editing', n.get_int_value()),
            "maxLength": lambda n : setattr(self, 'max_length', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "textType": lambda n : setattr(self, 'text_type', n.get_str_value()),
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
        writer.write_bool_value("allowMultipleLines", self.allow_multiple_lines)
        writer.write_bool_value("appendChangesToExistingText", self.append_changes_to_existing_text)
        writer.write_int_value("linesForEditing", self.lines_for_editing)
        writer.write_int_value("maxLength", self.max_length)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("textType", self.text_type)
        writer.write_additional_data_value(self.additional_data)
    

