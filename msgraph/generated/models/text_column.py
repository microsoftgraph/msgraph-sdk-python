from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TextColumn(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def allow_multiple_lines(self,) -> Optional[bool]:
        """
        Gets the allowMultipleLines property value. Whether to allow multiple lines of text.
        Returns: Optional[bool]
        """
        return self._allow_multiple_lines
    
    @allow_multiple_lines.setter
    def allow_multiple_lines(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowMultipleLines property value. Whether to allow multiple lines of text.
        Args:
            value: Value to set for the allowMultipleLines property.
        """
        self._allow_multiple_lines = value
    
    @property
    def append_changes_to_existing_text(self,) -> Optional[bool]:
        """
        Gets the appendChangesToExistingText property value. Whether updates to this column should replace existing text, or append to it.
        Returns: Optional[bool]
        """
        return self._append_changes_to_existing_text
    
    @append_changes_to_existing_text.setter
    def append_changes_to_existing_text(self,value: Optional[bool] = None) -> None:
        """
        Sets the appendChangesToExistingText property value. Whether updates to this column should replace existing text, or append to it.
        Args:
            value: Value to set for the appendChangesToExistingText property.
        """
        self._append_changes_to_existing_text = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new textColumn and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Whether to allow multiple lines of text.
        self._allow_multiple_lines: Optional[bool] = None
        # Whether updates to this column should replace existing text, or append to it.
        self._append_changes_to_existing_text: Optional[bool] = None
        # The size of the text box.
        self._lines_for_editing: Optional[int] = None
        # The maximum number of characters for the value.
        self._max_length: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The type of text being stored. Must be one of plain or richText
        self._text_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TextColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TextColumn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TextColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_multiple_lines": lambda n : setattr(self, 'allow_multiple_lines', n.get_bool_value()),
            "append_changes_to_existing_text": lambda n : setattr(self, 'append_changes_to_existing_text', n.get_bool_value()),
            "lines_for_editing": lambda n : setattr(self, 'lines_for_editing', n.get_int_value()),
            "max_length": lambda n : setattr(self, 'max_length', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "text_type": lambda n : setattr(self, 'text_type', n.get_str_value()),
        }
        return fields
    
    @property
    def lines_for_editing(self,) -> Optional[int]:
        """
        Gets the linesForEditing property value. The size of the text box.
        Returns: Optional[int]
        """
        return self._lines_for_editing
    
    @lines_for_editing.setter
    def lines_for_editing(self,value: Optional[int] = None) -> None:
        """
        Sets the linesForEditing property value. The size of the text box.
        Args:
            value: Value to set for the linesForEditing property.
        """
        self._lines_for_editing = value
    
    @property
    def max_length(self,) -> Optional[int]:
        """
        Gets the maxLength property value. The maximum number of characters for the value.
        Returns: Optional[int]
        """
        return self._max_length
    
    @max_length.setter
    def max_length(self,value: Optional[int] = None) -> None:
        """
        Sets the maxLength property value. The maximum number of characters for the value.
        Args:
            value: Value to set for the maxLength property.
        """
        self._max_length = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowMultipleLines", self.allow_multiple_lines)
        writer.write_bool_value("appendChangesToExistingText", self.append_changes_to_existing_text)
        writer.write_int_value("linesForEditing", self.lines_for_editing)
        writer.write_int_value("maxLength", self.max_length)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("textType", self.text_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def text_type(self,) -> Optional[str]:
        """
        Gets the textType property value. The type of text being stored. Must be one of plain or richText
        Returns: Optional[str]
        """
        return self._text_type
    
    @text_type.setter
    def text_type(self,value: Optional[str] = None) -> None:
        """
        Sets the textType property value. The type of text being stored. Must be one of plain or richText
        Args:
            value: Value to set for the textType property.
        """
        self._text_type = value
    

