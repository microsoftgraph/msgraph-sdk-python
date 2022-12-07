from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SharepointIds(AdditionalDataHolder, Parsable):
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
        Instantiates a new sharepointIds and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The unique identifier (guid) for the item's list in SharePoint.
        self._list_id: Optional[str] = None
        # An integer identifier for the item within the containing list.
        self._list_item_id: Optional[str] = None
        # The unique identifier (guid) for the item within OneDrive for Business or a SharePoint site.
        self._list_item_unique_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The unique identifier (guid) for the item's site collection (SPSite).
        self._site_id: Optional[str] = None
        # The SharePoint URL for the site that contains the item.
        self._site_url: Optional[str] = None
        # The unique identifier (guid) for the tenancy.
        self._tenant_id: Optional[str] = None
        # The unique identifier (guid) for the item's site (SPWeb).
        self._web_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharepointIds:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharepointIds
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharepointIds()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "list_id": lambda n : setattr(self, 'list_id', n.get_str_value()),
            "list_item_id": lambda n : setattr(self, 'list_item_id', n.get_str_value()),
            "list_item_unique_id": lambda n : setattr(self, 'list_item_unique_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "site_id": lambda n : setattr(self, 'site_id', n.get_str_value()),
            "site_url": lambda n : setattr(self, 'site_url', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "web_id": lambda n : setattr(self, 'web_id', n.get_str_value()),
        }
        return fields
    
    @property
    def list_id(self,) -> Optional[str]:
        """
        Gets the listId property value. The unique identifier (guid) for the item's list in SharePoint.
        Returns: Optional[str]
        """
        return self._list_id
    
    @list_id.setter
    def list_id(self,value: Optional[str] = None) -> None:
        """
        Sets the listId property value. The unique identifier (guid) for the item's list in SharePoint.
        Args:
            value: Value to set for the listId property.
        """
        self._list_id = value
    
    @property
    def list_item_id(self,) -> Optional[str]:
        """
        Gets the listItemId property value. An integer identifier for the item within the containing list.
        Returns: Optional[str]
        """
        return self._list_item_id
    
    @list_item_id.setter
    def list_item_id(self,value: Optional[str] = None) -> None:
        """
        Sets the listItemId property value. An integer identifier for the item within the containing list.
        Args:
            value: Value to set for the listItemId property.
        """
        self._list_item_id = value
    
    @property
    def list_item_unique_id(self,) -> Optional[str]:
        """
        Gets the listItemUniqueId property value. The unique identifier (guid) for the item within OneDrive for Business or a SharePoint site.
        Returns: Optional[str]
        """
        return self._list_item_unique_id
    
    @list_item_unique_id.setter
    def list_item_unique_id(self,value: Optional[str] = None) -> None:
        """
        Sets the listItemUniqueId property value. The unique identifier (guid) for the item within OneDrive for Business or a SharePoint site.
        Args:
            value: Value to set for the listItemUniqueId property.
        """
        self._list_item_unique_id = value
    
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
            value: Value to set for the OdataType property.
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
        writer.write_str_value("listId", self.list_id)
        writer.write_str_value("listItemId", self.list_item_id)
        writer.write_str_value("listItemUniqueId", self.list_item_unique_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("siteId", self.site_id)
        writer.write_str_value("siteUrl", self.site_url)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("webId", self.web_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def site_id(self,) -> Optional[str]:
        """
        Gets the siteId property value. The unique identifier (guid) for the item's site collection (SPSite).
        Returns: Optional[str]
        """
        return self._site_id
    
    @site_id.setter
    def site_id(self,value: Optional[str] = None) -> None:
        """
        Sets the siteId property value. The unique identifier (guid) for the item's site collection (SPSite).
        Args:
            value: Value to set for the siteId property.
        """
        self._site_id = value
    
    @property
    def site_url(self,) -> Optional[str]:
        """
        Gets the siteUrl property value. The SharePoint URL for the site that contains the item.
        Returns: Optional[str]
        """
        return self._site_url
    
    @site_url.setter
    def site_url(self,value: Optional[str] = None) -> None:
        """
        Sets the siteUrl property value. The SharePoint URL for the site that contains the item.
        Args:
            value: Value to set for the siteUrl property.
        """
        self._site_url = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The unique identifier (guid) for the tenancy.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The unique identifier (guid) for the tenancy.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def web_id(self,) -> Optional[str]:
        """
        Gets the webId property value. The unique identifier (guid) for the item's site (SPWeb).
        Returns: Optional[str]
        """
        return self._web_id
    
    @web_id.setter
    def web_id(self,value: Optional[str] = None) -> None:
        """
        Sets the webId property value. The unique identifier (guid) for the item's site (SPWeb).
        Args:
            value: Value to set for the webId property.
        """
        self._web_id = value
    

