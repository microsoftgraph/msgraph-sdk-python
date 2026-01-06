from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .building_map import BuildingMap
    from .place import Place
    from .place_feature_enablement import PlaceFeatureEnablement
    from .resource_link import ResourceLink

from .place import Place

@dataclass
class Building(Place, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.building"
    # Map file associated with a building in Places. This object is the IMDF-format representation of building.geojson.
    map: Optional[BuildingMap] = None
    # A set of links to external resources that are associated with the building. Inherited from place.
    resource_links: Optional[list[ResourceLink]] = None
    # The wifiState property
    wifi_state: Optional[PlaceFeatureEnablement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Building:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Building
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Building()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .building_map import BuildingMap
        from .place import Place
        from .place_feature_enablement import PlaceFeatureEnablement
        from .resource_link import ResourceLink

        from .building_map import BuildingMap
        from .place import Place
        from .place_feature_enablement import PlaceFeatureEnablement
        from .resource_link import ResourceLink

        fields: dict[str, Callable[[Any], None]] = {
            "map": lambda n : setattr(self, 'map', n.get_object_value(BuildingMap)),
            "resourceLinks": lambda n : setattr(self, 'resource_links', n.get_collection_of_object_values(ResourceLink)),
            "wifiState": lambda n : setattr(self, 'wifi_state', n.get_enum_value(PlaceFeatureEnablement)),
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
        writer.write_object_value("map", self.map)
        writer.write_collection_of_object_values("resourceLinks", self.resource_links)
        writer.write_enum_value("wifiState", self.wifi_state)
    

