from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_map_feature import BaseMapFeature
    from .footprint_map import FootprintMap
    from .level_map import LevelMap

from .base_map_feature import BaseMapFeature

@dataclass
class BuildingMap(BaseMapFeature, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.buildingMap"
    # Represents the approximate physical extent of a referenced building. It corresponds to footprint.geojson in IMDF format.
    footprints: Optional[list[FootprintMap]] = None
    # Represents a physical floor structure within a building. It corresponds to level.geojson in IMDF format.
    levels: Optional[list[LevelMap]] = None
    # Identifier for the building to which this buildingMap belongs.
    place_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BuildingMap:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BuildingMap
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BuildingMap()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_map_feature import BaseMapFeature
        from .footprint_map import FootprintMap
        from .level_map import LevelMap

        from .base_map_feature import BaseMapFeature
        from .footprint_map import FootprintMap
        from .level_map import LevelMap

        fields: dict[str, Callable[[Any], None]] = {
            "footprints": lambda n : setattr(self, 'footprints', n.get_collection_of_object_values(FootprintMap)),
            "levels": lambda n : setattr(self, 'levels', n.get_collection_of_object_values(LevelMap)),
            "placeId": lambda n : setattr(self, 'place_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("footprints", self.footprints)
        writer.write_collection_of_object_values("levels", self.levels)
        writer.write_str_value("placeId", self.place_id)
    

