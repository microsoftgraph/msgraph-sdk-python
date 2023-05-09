from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class UrlMatchInfo(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new urlMatchInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A list of the URL prefixes that must match URLs to be processed by this URL-to-item-resolver.
        self._base_urls: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A regular expression that will be matched towards the URL that is processed by this URL-to-item-resolver. The ECMAScript specification for regular expressions (ECMA-262) is used for the evaluation. The named groups defined by the regular expression will be used later to extract values from the URL.
        self._url_pattern: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def base_urls(self,) -> Optional[List[str]]:
        """
        Gets the baseUrls property value. A list of the URL prefixes that must match URLs to be processed by this URL-to-item-resolver.
        Returns: Optional[List[str]]
        """
        return self._base_urls
    
    @base_urls.setter
    def base_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the baseUrls property value. A list of the URL prefixes that must match URLs to be processed by this URL-to-item-resolver.
        Args:
            value: Value to set for the base_urls property.
        """
        self._base_urls = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UrlMatchInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UrlMatchInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UrlMatchInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "baseUrls": lambda n : setattr(self, 'base_urls', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "urlPattern": lambda n : setattr(self, 'url_pattern', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("baseUrls", self.base_urls)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("urlPattern", self.url_pattern)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def url_pattern(self,) -> Optional[str]:
        """
        Gets the urlPattern property value. A regular expression that will be matched towards the URL that is processed by this URL-to-item-resolver. The ECMAScript specification for regular expressions (ECMA-262) is used for the evaluation. The named groups defined by the regular expression will be used later to extract values from the URL.
        Returns: Optional[str]
        """
        return self._url_pattern
    
    @url_pattern.setter
    def url_pattern(self,value: Optional[str] = None) -> None:
        """
        Sets the urlPattern property value. A regular expression that will be matched towards the URL that is processed by this URL-to-item-resolver. The ECMAScript specification for regular expressions (ECMA-262) is used for the evaluation. The named groups defined by the regular expression will be used later to extract values from the URL.
        Args:
            value: Value to set for the url_pattern property.
        """
        self._url_pattern = value
    

