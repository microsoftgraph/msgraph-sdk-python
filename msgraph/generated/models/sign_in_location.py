from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .geo_coordinates import GeoCoordinates

@dataclass
class SignInLocation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Provides the city where the sign-in originated and is determined using latitude/longitude information from the sign-in activity.
    city: Optional[str] = None
    # Provides the country code info (two letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.
    country_or_region: Optional[str] = None
    # Provides the latitude, longitude and altitude where the sign-in originated.
    geo_coordinates: Optional[GeoCoordinates] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignInLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignInLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SignInLocation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .geo_coordinates import GeoCoordinates

        from .geo_coordinates import GeoCoordinates

        fields: dict[str, Callable[[Any], None]] = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "countryOrRegion": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "geoCoordinates": lambda n : setattr(self, 'geo_coordinates', n.get_object_value(GeoCoordinates)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryOrRegion", self.country_or_region)
        writer.write_object_value("geoCoordinates", self.geo_coordinates)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

