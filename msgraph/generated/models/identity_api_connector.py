from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

api_authentication_configuration_base = lazy_import('msgraph.generated.models.api_authentication_configuration_base')
entity = lazy_import('msgraph.generated.models.entity')

class IdentityApiConnector(entity.Entity):
    @property
    def authentication_configuration(self,) -> Optional[api_authentication_configuration_base.ApiAuthenticationConfigurationBase]:
        """
        Gets the authenticationConfiguration property value. The object which describes the authentication configuration details for calling the API. Basic and PKCS 12 client certificate are supported.
        Returns: Optional[api_authentication_configuration_base.ApiAuthenticationConfigurationBase]
        """
        return self._authentication_configuration
    
    @authentication_configuration.setter
    def authentication_configuration(self,value: Optional[api_authentication_configuration_base.ApiAuthenticationConfigurationBase] = None) -> None:
        """
        Sets the authenticationConfiguration property value. The object which describes the authentication configuration details for calling the API. Basic and PKCS 12 client certificate are supported.
        Args:
            value: Value to set for the authenticationConfiguration property.
        """
        self._authentication_configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IdentityApiConnector and sets the default values.
        """
        super().__init__()
        # The object which describes the authentication configuration details for calling the API. Basic and PKCS 12 client certificate are supported.
        self._authentication_configuration: Optional[api_authentication_configuration_base.ApiAuthenticationConfigurationBase] = None
        # The name of the API connector.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The URL of the API endpoint to call.
        self._target_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityApiConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityApiConnector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdentityApiConnector()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the API connector.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the API connector.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_configuration": lambda n : setattr(self, 'authentication_configuration', n.get_object_value(api_authentication_configuration_base.ApiAuthenticationConfigurationBase)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "target_url": lambda n : setattr(self, 'target_url', n.get_str_value()),
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
        writer.write_object_value("authenticationConfiguration", self.authentication_configuration)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("targetUrl", self.target_url)
    
    @property
    def target_url(self,) -> Optional[str]:
        """
        Gets the targetUrl property value. The URL of the API endpoint to call.
        Returns: Optional[str]
        """
        return self._target_url
    
    @target_url.setter
    def target_url(self,value: Optional[str] = None) -> None:
        """
        Sets the targetUrl property value. The URL of the API endpoint to call.
        Args:
            value: Value to set for the targetUrl property.
        """
        self._target_url = value
    

