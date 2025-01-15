from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PrinterLocation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The altitude, in meters, that the printer is located at.
    altitude_in_meters: Optional[int] = None
    # The building that the printer is located in.
    building: Optional[str] = None
    # The city that the printer is located in.
    city: Optional[str] = None
    # The country or region that the printer is located in.
    country_or_region: Optional[str] = None
    # The floor that the printer is located on. Only numerical values are supported right now.
    floor: Optional[str] = None
    # The description of the floor that the printer is located on.
    floor_description: Optional[str] = None
    # The latitude that the printer is located at.
    latitude: Optional[float] = None
    # The longitude that the printer is located at.
    longitude: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organizational hierarchy that the printer belongs to. The elements should be in hierarchical order.
    organization: Optional[list[str]] = None
    # The postal code that the printer is located in.
    postal_code: Optional[str] = None
    # The description of the room that the printer is located in.
    room_description: Optional[str] = None
    # The room that the printer is located in. Only numerical values are supported right now.
    room_name: Optional[str] = None
    # The site that the printer is located in.
    site: Optional[str] = None
    # The state or province that the printer is located in.
    state_or_province: Optional[str] = None
    # The street address where the printer is located.
    street_address: Optional[str] = None
    # The subdivision that the printer is located in. The elements should be in hierarchical order.
    subdivision: Optional[list[str]] = None
    # The subunit property
    subunit: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrinterLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrinterLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrinterLocation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "altitudeInMeters": lambda n : setattr(self, 'altitude_in_meters', n.get_int_value()),
            "building": lambda n : setattr(self, 'building', n.get_str_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "countryOrRegion": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "floor": lambda n : setattr(self, 'floor', n.get_str_value()),
            "floorDescription": lambda n : setattr(self, 'floor_description', n.get_str_value()),
            "latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_collection_of_primitive_values(str)),
            "postalCode": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "roomDescription": lambda n : setattr(self, 'room_description', n.get_str_value()),
            "roomName": lambda n : setattr(self, 'room_name', n.get_str_value()),
            "site": lambda n : setattr(self, 'site', n.get_str_value()),
            "stateOrProvince": lambda n : setattr(self, 'state_or_province', n.get_str_value()),
            "streetAddress": lambda n : setattr(self, 'street_address', n.get_str_value()),
            "subdivision": lambda n : setattr(self, 'subdivision', n.get_collection_of_primitive_values(str)),
            "subunit": lambda n : setattr(self, 'subunit', n.get_collection_of_primitive_values(str)),
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
        writer.write_int_value("altitudeInMeters", self.altitude_in_meters)
        writer.write_str_value("building", self.building)
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryOrRegion", self.country_or_region)
        writer.write_str_value("floor", self.floor)
        writer.write_str_value("floorDescription", self.floor_description)
        writer.write_float_value("latitude", self.latitude)
        writer.write_float_value("longitude", self.longitude)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("organization", self.organization)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("roomDescription", self.room_description)
        writer.write_str_value("roomName", self.room_name)
        writer.write_str_value("site", self.site)
        writer.write_str_value("stateOrProvince", self.state_or_province)
        writer.write_str_value("streetAddress", self.street_address)
        writer.write_collection_of_primitive_values("subdivision", self.subdivision)
        writer.write_collection_of_primitive_values("subunit", self.subunit)
        writer.write_additional_data_value(self.additional_data)
    

