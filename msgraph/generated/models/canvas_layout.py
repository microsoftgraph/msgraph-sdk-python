from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .horizontal_section import HorizontalSection
    from .vertical_section import VerticalSection

from .entity import Entity

@dataclass
class CanvasLayout(Entity):
    # Collection of horizontal sections on the SharePoint page.
    horizontal_sections: Optional[List[HorizontalSection]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Vertical section on the SharePoint page.
    vertical_section: Optional[VerticalSection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CanvasLayout:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CanvasLayout
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CanvasLayout()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .horizontal_section import HorizontalSection
        from .vertical_section import VerticalSection

        from .entity import Entity
        from .horizontal_section import HorizontalSection
        from .vertical_section import VerticalSection

        fields: Dict[str, Callable[[Any], None]] = {
            "horizontalSections": lambda n : setattr(self, 'horizontal_sections', n.get_collection_of_object_values(HorizontalSection)),
            "verticalSection": lambda n : setattr(self, 'vertical_section', n.get_object_value(VerticalSection)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("horizontalSections", self.horizontal_sections)
        writer.write_object_value("verticalSection", self.vertical_section)
    

