from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .horizontal_section_column import HorizontalSectionColumn
    from .horizontal_section_layout_type import HorizontalSectionLayoutType
    from .section_emphasis_type import SectionEmphasisType

from .entity import Entity

@dataclass
class HorizontalSection(Entity, Parsable):
    # The set of vertical columns in this section.
    columns: Optional[list[HorizontalSectionColumn]] = None
    # Enumeration value that indicates the emphasis of the section background. The possible values are: none, netural, soft, strong, unknownFutureValue.
    emphasis: Optional[SectionEmphasisType] = None
    # Layout type of the section. The possible values are: none, oneColumn, twoColumns, threeColumns, oneThirdLeftColumn, oneThirdRightColumn, fullWidth, unknownFutureValue.
    layout: Optional[HorizontalSectionLayoutType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HorizontalSection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HorizontalSection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HorizontalSection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .horizontal_section_column import HorizontalSectionColumn
        from .horizontal_section_layout_type import HorizontalSectionLayoutType
        from .section_emphasis_type import SectionEmphasisType

        from .entity import Entity
        from .horizontal_section_column import HorizontalSectionColumn
        from .horizontal_section_layout_type import HorizontalSectionLayoutType
        from .section_emphasis_type import SectionEmphasisType

        fields: dict[str, Callable[[Any], None]] = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(HorizontalSectionColumn)),
            "emphasis": lambda n : setattr(self, 'emphasis', n.get_enum_value(SectionEmphasisType)),
            "layout": lambda n : setattr(self, 'layout', n.get_enum_value(HorizontalSectionLayoutType)),
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
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_enum_value("emphasis", self.emphasis)
        writer.write_enum_value("layout", self.layout)
    

