from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import url_to_item_resolver_base

class ActivitySettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new activitySettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies configurations to identify an externalItem based on a shared URL.
        self._url_to_item_resolvers: Optional[List[url_to_item_resolver_base.UrlToItemResolverBase]] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ActivitySettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ActivitySettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ActivitySettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import url_to_item_resolver_base

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "urlToItemResolvers": lambda n : setattr(self, 'url_to_item_resolvers', n.get_collection_of_object_values(url_to_item_resolver_base.UrlToItemResolverBase)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("urlToItemResolvers", self.url_to_item_resolvers)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def url_to_item_resolvers(self,) -> Optional[List[url_to_item_resolver_base.UrlToItemResolverBase]]:
        """
        Gets the urlToItemResolvers property value. Specifies configurations to identify an externalItem based on a shared URL.
        Returns: Optional[List[url_to_item_resolver_base.UrlToItemResolverBase]]
        """
        return self._url_to_item_resolvers
    
    @url_to_item_resolvers.setter
    def url_to_item_resolvers(self,value: Optional[List[url_to_item_resolver_base.UrlToItemResolverBase]] = None) -> None:
        """
        Sets the urlToItemResolvers property value. Specifies configurations to identify an externalItem based on a shared URL.
        Args:
            value: Value to set for the url_to_item_resolvers property.
        """
        self._url_to_item_resolvers = value
    

