from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .location_constraint_item import LocationConstraintItem
    from .location_type import LocationType
    from .location_unique_id_type import LocationUniqueIdType
    from .outlook_geo_coordinates import OutlookGeoCoordinates
    from .physical_address import PhysicalAddress

@dataclass
class Location(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The street address of the location.
    address: Optional[PhysicalAddress] = None
    # The geographic coordinates and elevation of the location.
    coordinates: Optional[OutlookGeoCoordinates] = None
    # The name associated with the location.
    display_name: Optional[str] = None
    # Optional email address of the location.
    location_email_address: Optional[str] = None
    # The type of location. The possible values are: default, conferenceRoom, homeAddress, businessAddress,geoCoordinates, streetAddress, hotel, restaurant, localBusiness, postalAddress. Read-only.
    location_type: Optional[LocationType] = None
    # Optional URI representing the location.
    location_uri: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # For internal use only.
    unique_id: Optional[str] = None
    # For internal use only.
    unique_id_type: Optional[LocationUniqueIdType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Location:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Location
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.locationConstraintItem".casefold():
            from .location_constraint_item import LocationConstraintItem

            return LocationConstraintItem()
        return Location()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .location_constraint_item import LocationConstraintItem
        from .location_type import LocationType
        from .location_unique_id_type import LocationUniqueIdType
        from .outlook_geo_coordinates import OutlookGeoCoordinates
        from .physical_address import PhysicalAddress

        from .location_constraint_item import LocationConstraintItem
        from .location_type import LocationType
        from .location_unique_id_type import LocationUniqueIdType
        from .outlook_geo_coordinates import OutlookGeoCoordinates
        from .physical_address import PhysicalAddress

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PhysicalAddress)),
            "coordinates": lambda n : setattr(self, 'coordinates', n.get_object_value(OutlookGeoCoordinates)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "locationEmailAddress": lambda n : setattr(self, 'location_email_address', n.get_str_value()),
            "locationType": lambda n : setattr(self, 'location_type', n.get_enum_value(LocationType)),
            "locationUri": lambda n : setattr(self, 'location_uri', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "uniqueId": lambda n : setattr(self, 'unique_id', n.get_str_value()),
            "uniqueIdType": lambda n : setattr(self, 'unique_id_type', n.get_enum_value(LocationUniqueIdType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("address", self.address)
        writer.write_object_value("coordinates", self.coordinates)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("locationEmailAddress", self.location_email_address)
        writer.write_enum_value("locationType", self.location_type)
        writer.write_str_value("locationUri", self.location_uri)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("uniqueId", self.unique_id)
        writer.write_enum_value("uniqueIdType", self.unique_id_type)
        writer.write_additional_data_value(self.additional_data)
    

