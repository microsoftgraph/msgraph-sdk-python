from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_map_feature import BaseMapFeature
    from .fixture_map import FixtureMap
    from .section_map import SectionMap
    from .unit_map import UnitMap

from .base_map_feature import BaseMapFeature

@dataclass
class LevelMap(BaseMapFeature, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.levelMap"
    # Collection of fixtures (such as furniture or equipment) on this level. Supports upsert.
    fixtures: Optional[list[FixtureMap]] = None
    # Identifier of the floor to which this levelMap belongs.
    place_id: Optional[str] = None
    # Collection of sections (such as zones or partitions) on this level. Supports upsert.
    sections: Optional[list[SectionMap]] = None
    # Collection of units (such as rooms or offices) on this level. Supports upsert.
    units: Optional[list[UnitMap]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LevelMap:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LevelMap
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LevelMap()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_map_feature import BaseMapFeature
        from .fixture_map import FixtureMap
        from .section_map import SectionMap
        from .unit_map import UnitMap

        from .base_map_feature import BaseMapFeature
        from .fixture_map import FixtureMap
        from .section_map import SectionMap
        from .unit_map import UnitMap

        fields: dict[str, Callable[[Any], None]] = {
            "fixtures": lambda n : setattr(self, 'fixtures', n.get_collection_of_object_values(FixtureMap)),
            "placeId": lambda n : setattr(self, 'place_id', n.get_str_value()),
            "sections": lambda n : setattr(self, 'sections', n.get_collection_of_object_values(SectionMap)),
            "units": lambda n : setattr(self, 'units', n.get_collection_of_object_values(UnitMap)),
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
        writer.write_collection_of_object_values("fixtures", self.fixtures)
        writer.write_str_value("placeId", self.place_id)
        writer.write_collection_of_object_values("sections", self.sections)
        writer.write_collection_of_object_values("units", self.units)
    

