from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

category_color = lazy_import('msgraph.generated.models.category_color')
entity = lazy_import('msgraph.generated.models.entity')

class OutlookCategory(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def color(self,) -> Optional[category_color.CategoryColor]:
        """
        Gets the color property value. A pre-set color constant that characterizes a category, and that is mapped to one of 25 predefined colors. See the note below.
        Returns: Optional[category_color.CategoryColor]
        """
        return self._color
    
    @color.setter
    def color(self,value: Optional[category_color.CategoryColor] = None) -> None:
        """
        Sets the color property value. A pre-set color constant that characterizes a category, and that is mapped to one of 25 predefined colors. See the note below.
        Args:
            value: Value to set for the color property.
        """
        self._color = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new outlookCategory and sets the default values.
        """
        super().__init__()
        # A pre-set color constant that characterizes a category, and that is mapped to one of 25 predefined colors. See the note below.
        self._color: Optional[category_color.CategoryColor] = None
        # A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutlookCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OutlookCategory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OutlookCategory()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. A unique name that identifies a category in the user's mailbox. After a category is created, the name cannot be changed. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "color": lambda n : setattr(self, 'color', n.get_enum_value(category_color.CategoryColor)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("color", self.color)
        writer.write_str_value("displayName", self.display_name)
    

