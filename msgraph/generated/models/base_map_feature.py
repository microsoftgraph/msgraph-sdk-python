from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .building_map import BuildingMap
    from .entity import Entity
    from .fixture_map import FixtureMap
    from .footprint_map import FootprintMap
    from .level_map import LevelMap
    from .section_map import SectionMap
    from .unit_map import UnitMap

from .entity import Entity

@dataclass
class BaseMapFeature(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Concatenated key-value pair of all properties of a GeoJSON file for this baseMapFeature.
    properties: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BaseMapFeature:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseMapFeature
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.buildingMap".casefold():
            from .building_map import BuildingMap

            return BuildingMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fixtureMap".casefold():
            from .fixture_map import FixtureMap

            return FixtureMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.footprintMap".casefold():
            from .footprint_map import FootprintMap

            return FootprintMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.levelMap".casefold():
            from .level_map import LevelMap

            return LevelMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sectionMap".casefold():
            from .section_map import SectionMap

            return SectionMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unitMap".casefold():
            from .unit_map import UnitMap

            return UnitMap()
        return BaseMapFeature()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .building_map import BuildingMap
        from .entity import Entity
        from .fixture_map import FixtureMap
        from .footprint_map import FootprintMap
        from .level_map import LevelMap
        from .section_map import SectionMap
        from .unit_map import UnitMap

        from .building_map import BuildingMap
        from .entity import Entity
        from .fixture_map import FixtureMap
        from .footprint_map import FootprintMap
        from .level_map import LevelMap
        from .section_map import SectionMap
        from .unit_map import UnitMap

        fields: dict[str, Callable[[Any], None]] = {
            "properties": lambda n : setattr(self, 'properties', n.get_str_value()),
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
        writer.write_str_value("properties", self.properties)
    

