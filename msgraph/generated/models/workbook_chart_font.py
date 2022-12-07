from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class WorkbookChartFont(entity.Entity):
    @property
    def bold(self,) -> Optional[bool]:
        """
        Gets the bold property value. Represents the bold status of font.
        Returns: Optional[bool]
        """
        return self._bold
    
    @bold.setter
    def bold(self,value: Optional[bool] = None) -> None:
        """
        Sets the bold property value. Represents the bold status of font.
        Args:
            value: Value to set for the bold property.
        """
        self._bold = value
    
    @property
    def color(self,) -> Optional[str]:
        """
        Gets the color property value. HTML color code representation of the text color. E.g. #FF0000 represents Red.
        Returns: Optional[str]
        """
        return self._color
    
    @color.setter
    def color(self,value: Optional[str] = None) -> None:
        """
        Sets the color property value. HTML color code representation of the text color. E.g. #FF0000 represents Red.
        Args:
            value: Value to set for the color property.
        """
        self._color = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChartFont and sets the default values.
        """
        super().__init__()
        # Represents the bold status of font.
        self._bold: Optional[bool] = None
        # HTML color code representation of the text color. E.g. #FF0000 represents Red.
        self._color: Optional[str] = None
        # Represents the italic status of the font.
        self._italic: Optional[bool] = None
        # Font name (e.g. 'Calibri')
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Size of the font (e.g. 11)
        self._size: Optional[float] = None
        # Type of underline applied to the font. The possible values are: None, Single.
        self._underline: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartFont:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartFont
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartFont()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bold": lambda n : setattr(self, 'bold', n.get_bool_value()),
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "italic": lambda n : setattr(self, 'italic', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_float_value()),
            "underline": lambda n : setattr(self, 'underline', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def italic(self,) -> Optional[bool]:
        """
        Gets the italic property value. Represents the italic status of the font.
        Returns: Optional[bool]
        """
        return self._italic
    
    @italic.setter
    def italic(self,value: Optional[bool] = None) -> None:
        """
        Sets the italic property value. Represents the italic status of the font.
        Args:
            value: Value to set for the italic property.
        """
        self._italic = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Font name (e.g. 'Calibri')
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Font name (e.g. 'Calibri')
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("bold", self.bold)
        writer.write_str_value("color", self.color)
        writer.write_bool_value("italic", self.italic)
        writer.write_str_value("name", self.name)
        writer.write_float_value("size", self.size)
        writer.write_str_value("underline", self.underline)
    
    @property
    def size(self,) -> Optional[float]:
        """
        Gets the size property value. Size of the font (e.g. 11)
        Returns: Optional[float]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[float] = None) -> None:
        """
        Sets the size property value. Size of the font (e.g. 11)
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
    @property
    def underline(self,) -> Optional[str]:
        """
        Gets the underline property value. Type of underline applied to the font. The possible values are: None, Single.
        Returns: Optional[str]
        """
        return self._underline
    
    @underline.setter
    def underline(self,value: Optional[str] = None) -> None:
        """
        Sets the underline property value. Type of underline applied to the font. The possible values are: None, Single.
        Args:
            value: Value to set for the underline property.
        """
        self._underline = value
    

