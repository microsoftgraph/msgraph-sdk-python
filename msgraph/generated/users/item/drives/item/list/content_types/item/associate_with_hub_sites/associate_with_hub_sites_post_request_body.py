from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AssociateWithHubSitesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the associateWithHubSites method.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new associateWithHubSitesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The hubSiteUrls property
        self._hub_site_urls: Optional[List[str]] = None
        # The propagateToExistingLists property
        self._propagate_to_existing_lists: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssociateWithHubSitesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssociateWithHubSitesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssociateWithHubSitesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "hub_site_urls": lambda n : setattr(self, 'hub_site_urls', n.get_collection_of_primitive_values(str)),
            "propagate_to_existing_lists": lambda n : setattr(self, 'propagate_to_existing_lists', n.get_bool_value()),
        }
        return fields
    
    @property
    def hub_site_urls(self,) -> Optional[List[str]]:
        """
        Gets the hubSiteUrls property value. The hubSiteUrls property
        Returns: Optional[List[str]]
        """
        return self._hub_site_urls
    
    @hub_site_urls.setter
    def hub_site_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the hubSiteUrls property value. The hubSiteUrls property
        Args:
            value: Value to set for the hubSiteUrls property.
        """
        self._hub_site_urls = value
    
    @property
    def propagate_to_existing_lists(self,) -> Optional[bool]:
        """
        Gets the propagateToExistingLists property value. The propagateToExistingLists property
        Returns: Optional[bool]
        """
        return self._propagate_to_existing_lists
    
    @propagate_to_existing_lists.setter
    def propagate_to_existing_lists(self,value: Optional[bool] = None) -> None:
        """
        Sets the propagateToExistingLists property value. The propagateToExistingLists property
        Args:
            value: Value to set for the propagateToExistingLists property.
        """
        self._propagate_to_existing_lists = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("hubSiteUrls", self.hub_site_urls)
        writer.write_bool_value("propagateToExistingLists", self.propagate_to_existing_lists)
        writer.write_additional_data_value(self.additional_data)
    

