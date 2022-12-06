from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamsTabConfiguration(AdditionalDataHolder, Parsable):
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
        Instantiates a new teamsTabConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Url used for rendering tab contents in Teams. Required.
        self._content_url: Optional[str] = None
        # Identifier for the entity hosted by the tab provider.
        self._entity_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Url called by Teams client when a Tab is removed using the Teams Client.
        self._remove_url: Optional[str] = None
        # Url for showing tab contents outside of Teams.
        self._website_url: Optional[str] = None
    
    @property
    def content_url(self,) -> Optional[str]:
        """
        Gets the contentUrl property value. Url used for rendering tab contents in Teams. Required.
        Returns: Optional[str]
        """
        return self._content_url
    
    @content_url.setter
    def content_url(self,value: Optional[str] = None) -> None:
        """
        Sets the contentUrl property value. Url used for rendering tab contents in Teams. Required.
        Args:
            value: Value to set for the contentUrl property.
        """
        self._content_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsTabConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsTabConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsTabConfiguration()
    
    @property
    def entity_id(self,) -> Optional[str]:
        """
        Gets the entityId property value. Identifier for the entity hosted by the tab provider.
        Returns: Optional[str]
        """
        return self._entity_id
    
    @entity_id.setter
    def entity_id(self,value: Optional[str] = None) -> None:
        """
        Sets the entityId property value. Identifier for the entity hosted by the tab provider.
        Args:
            value: Value to set for the entityId property.
        """
        self._entity_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_url": lambda n : setattr(self, 'content_url', n.get_str_value()),
            "entity_id": lambda n : setattr(self, 'entity_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remove_url": lambda n : setattr(self, 'remove_url', n.get_str_value()),
            "website_url": lambda n : setattr(self, 'website_url', n.get_str_value()),
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def remove_url(self,) -> Optional[str]:
        """
        Gets the removeUrl property value. Url called by Teams client when a Tab is removed using the Teams Client.
        Returns: Optional[str]
        """
        return self._remove_url
    
    @remove_url.setter
    def remove_url(self,value: Optional[str] = None) -> None:
        """
        Sets the removeUrl property value. Url called by Teams client when a Tab is removed using the Teams Client.
        Args:
            value: Value to set for the removeUrl property.
        """
        self._remove_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("contentUrl", self.content_url)
        writer.write_str_value("entityId", self.entity_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("removeUrl", self.remove_url)
        writer.write_str_value("websiteUrl", self.website_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def website_url(self,) -> Optional[str]:
        """
        Gets the websiteUrl property value. Url for showing tab contents outside of Teams.
        Returns: Optional[str]
        """
        return self._website_url
    
    @website_url.setter
    def website_url(self,value: Optional[str] = None) -> None:
        """
        Sets the websiteUrl property value. Url for showing tab contents outside of Teams.
        Args:
            value: Value to set for the websiteUrl property.
        """
        self._website_url = value
    

