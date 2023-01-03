from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class LinkedResource(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def application_name(self,) -> Optional[str]:
        """
        Gets the applicationName property value. Field indicating the app name of the source that is sending the linkedResource.
        Returns: Optional[str]
        """
        return self._application_name
    
    @application_name.setter
    def application_name(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationName property value. Field indicating the app name of the source that is sending the linkedResource.
        Args:
            value: Value to set for the applicationName property.
        """
        self._application_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new linkedResource and sets the default values.
        """
        super().__init__()
        # Field indicating the app name of the source that is sending the linkedResource.
        self._application_name: Optional[str] = None
        # Field indicating the title of the linkedResource.
        self._display_name: Optional[str] = None
        # Id of the object that is associated with this task on the third-party/partner system.
        self._external_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Deep link to the linkedResource.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LinkedResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LinkedResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LinkedResource()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Field indicating the title of the linkedResource.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Field indicating the title of the linkedResource.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. Id of the object that is associated with this task on the third-party/partner system.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. Id of the object that is associated with this task on the third-party/partner system.
        Args:
            value: Value to set for the externalId property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_name": lambda n : setattr(self, 'application_name', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "external_id": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("applicationName", self.application_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. Deep link to the linkedResource.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. Deep link to the linkedResource.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

