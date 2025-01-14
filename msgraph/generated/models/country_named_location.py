from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .country_lookup_method_type import CountryLookupMethodType
    from .named_location import NamedLocation

from .named_location import NamedLocation

@dataclass
class CountryNamedLocation(NamedLocation, Parsable):
    # List of countries and/or regions in two-letter format specified by ISO 3166-2. Required.
    countries_and_regions: Optional[list[str]] = None
    # Determines what method is used to decide which country the user is located in. Possible values are clientIpAddress(default) and authenticatorAppGps. Note: authenticatorAppGps is not yet supported in the Microsoft Cloud for US Government.
    country_lookup_method: Optional[CountryLookupMethodType] = None
    # true if IP addresses that don't map to a country or region should be included in the named location. Optional. Default value is false.
    include_unknown_countries_and_regions: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CountryNamedLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CountryNamedLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CountryNamedLocation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .country_lookup_method_type import CountryLookupMethodType
        from .named_location import NamedLocation

        from .country_lookup_method_type import CountryLookupMethodType
        from .named_location import NamedLocation

        fields: dict[str, Callable[[Any], None]] = {
            "countriesAndRegions": lambda n : setattr(self, 'countries_and_regions', n.get_collection_of_primitive_values(str)),
            "countryLookupMethod": lambda n : setattr(self, 'country_lookup_method', n.get_enum_value(CountryLookupMethodType)),
            "includeUnknownCountriesAndRegions": lambda n : setattr(self, 'include_unknown_countries_and_regions', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("countriesAndRegions", self.countries_and_regions)
        writer.write_enum_value("countryLookupMethod", self.country_lookup_method)
        writer.write_bool_value("includeUnknownCountriesAndRegions", self.include_unknown_countries_and_regions)
    

