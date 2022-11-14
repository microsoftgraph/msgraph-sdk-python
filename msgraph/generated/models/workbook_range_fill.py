from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import entity

class WorkbookRangeFill(entity.Entity):
    @property
    def color(self,) -> Optional[str]:
        """
        Gets the color property value. HTML color code representing the color of the border line, of the form #RRGGBB (e.g. 'FFA500') or as a named HTML color (e.g. 'orange')
        Returns: Optional[str]
        """
        return self._color

    @color.setter
    def color(self,value: Optional[str] = None) -> None:
        """
        Sets the color property value. HTML color code representing the color of the border line, of the form #RRGGBB (e.g. 'FFA500') or as a named HTML color (e.g. 'orange')
        Args:
            value: Value to set for the color property.
        """
        self._color = value

    def __init__(self,) -> None:
        """
        Instantiates a new workbookRangeFill and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.workbookRangeFill"
        # HTML color code representing the color of the border line, of the form #RRGGBB (e.g. 'FFA500') or as a named HTML color (e.g. 'orange')
        self._color: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookRangeFill:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookRangeFill
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return WorkbookRangeFill()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
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
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("color", self.color)


