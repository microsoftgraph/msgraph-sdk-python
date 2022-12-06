from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

country_lookup_method_type = lazy_import('msgraph.generated.models.country_lookup_method_type')
named_location = lazy_import('msgraph.generated.models.named_location')

class CountryNamedLocation(named_location.NamedLocation):
    def __init__(self,) -> None:
        """
        Instantiates a new CountryNamedLocation and sets the default values.
        """
        super().__init__()
        # List of countries and/or regions in two-letter format specified by ISO 3166-2. Required.
        self._countries_and_regions: Optional[List[str]] = None
        # Determines what method is used to decide which country the user is located in. Possible values are clientIpAddress(default) and authenticatorAppGps. Note: authenticatorAppGps is not yet supported in the Microsoft Cloud for US Government.
        self._country_lookup_method: Optional[country_lookup_method_type.CountryLookupMethodType] = None
        # true if IP addresses that don't map to a country or region should be included in the named location. Optional. Default value is false.
        self._include_unknown_countries_and_regions: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def countries_and_regions(self,) -> Optional[List[str]]:
        """
        Gets the countriesAndRegions property value. List of countries and/or regions in two-letter format specified by ISO 3166-2. Required.
        Returns: Optional[List[str]]
        """
        return self._countries_and_regions
    
    @countries_and_regions.setter
    def countries_and_regions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the countriesAndRegions property value. List of countries and/or regions in two-letter format specified by ISO 3166-2. Required.
        Args:
            value: Value to set for the countriesAndRegions property.
        """
        self._countries_and_regions = value
    
    @property
    def country_lookup_method(self,) -> Optional[country_lookup_method_type.CountryLookupMethodType]:
        """
        Gets the countryLookupMethod property value. Determines what method is used to decide which country the user is located in. Possible values are clientIpAddress(default) and authenticatorAppGps. Note: authenticatorAppGps is not yet supported in the Microsoft Cloud for US Government.
        Returns: Optional[country_lookup_method_type.CountryLookupMethodType]
        """
        return self._country_lookup_method
    
    @country_lookup_method.setter
    def country_lookup_method(self,value: Optional[country_lookup_method_type.CountryLookupMethodType] = None) -> None:
        """
        Sets the countryLookupMethod property value. Determines what method is used to decide which country the user is located in. Possible values are clientIpAddress(default) and authenticatorAppGps. Note: authenticatorAppGps is not yet supported in the Microsoft Cloud for US Government.
        Args:
            value: Value to set for the countryLookupMethod property.
        """
        self._country_lookup_method = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CountryNamedLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CountryNamedLocation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CountryNamedLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "countries_and_regions": lambda n : setattr(self, 'countries_and_regions', n.get_collection_of_primitive_values(str)),
            "country_lookup_method": lambda n : setattr(self, 'country_lookup_method', n.get_enum_value(country_lookup_method_type.CountryLookupMethodType)),
            "include_unknown_countries_and_regions": lambda n : setattr(self, 'include_unknown_countries_and_regions', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def include_unknown_countries_and_regions(self,) -> Optional[bool]:
        """
        Gets the includeUnknownCountriesAndRegions property value. true if IP addresses that don't map to a country or region should be included in the named location. Optional. Default value is false.
        Returns: Optional[bool]
        """
        return self._include_unknown_countries_and_regions
    
    @include_unknown_countries_and_regions.setter
    def include_unknown_countries_and_regions(self,value: Optional[bool] = None) -> None:
        """
        Sets the includeUnknownCountriesAndRegions property value. true if IP addresses that don't map to a country or region should be included in the named location. Optional. Default value is false.
        Args:
            value: Value to set for the includeUnknownCountriesAndRegions property.
        """
        self._include_unknown_countries_and_regions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("countriesAndRegions", self.countries_and_regions)
        writer.write_enum_value("countryLookupMethod", self.country_lookup_method)
        writer.write_bool_value("includeUnknownCountriesAndRegions", self.include_unknown_countries_and_regions)
    

