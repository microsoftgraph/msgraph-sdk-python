from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CopyToSectionGroupPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the copyToSectionGroup method.
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
        Instantiates a new copyToSectionGroupPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The groupId property
        self._group_id: Optional[str] = None
        # The id property
        self._id: Optional[str] = None
        # The renameAs property
        self._rename_as: Optional[str] = None
        # The siteCollectionId property
        self._site_collection_id: Optional[str] = None
        # The siteId property
        self._site_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CopyToSectionGroupPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CopyToSectionGroupPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CopyToSectionGroupPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group_id": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "rename_as": lambda n : setattr(self, 'rename_as', n.get_str_value()),
            "site_collection_id": lambda n : setattr(self, 'site_collection_id', n.get_str_value()),
            "site_id": lambda n : setattr(self, 'site_id', n.get_str_value()),
        }
        return fields
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The groupId property
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The groupId property
        Args:
            value: Value to set for the groupId property.
        """
        self._group_id = value
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The id property
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def rename_as(self,) -> Optional[str]:
        """
        Gets the renameAs property value. The renameAs property
        Returns: Optional[str]
        """
        return self._rename_as
    
    @rename_as.setter
    def rename_as(self,value: Optional[str] = None) -> None:
        """
        Sets the renameAs property value. The renameAs property
        Args:
            value: Value to set for the renameAs property.
        """
        self._rename_as = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("id", self.id)
        writer.write_str_value("renameAs", self.rename_as)
        writer.write_str_value("siteCollectionId", self.site_collection_id)
        writer.write_str_value("siteId", self.site_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def site_collection_id(self,) -> Optional[str]:
        """
        Gets the siteCollectionId property value. The siteCollectionId property
        Returns: Optional[str]
        """
        return self._site_collection_id
    
    @site_collection_id.setter
    def site_collection_id(self,value: Optional[str] = None) -> None:
        """
        Sets the siteCollectionId property value. The siteCollectionId property
        Args:
            value: Value to set for the siteCollectionId property.
        """
        self._site_collection_id = value
    
    @property
    def site_id(self,) -> Optional[str]:
        """
        Gets the siteId property value. The siteId property
        Returns: Optional[str]
        """
        return self._site_id
    
    @site_id.setter
    def site_id(self,value: Optional[str] = None) -> None:
        """
        Sets the siteId property value. The siteId property
        Args:
            value: Value to set for the siteId property.
        """
        self._site_id = value
    

