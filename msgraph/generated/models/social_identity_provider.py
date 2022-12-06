from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_provider_base = lazy_import('msgraph.generated.models.identity_provider_base')

class SocialIdentityProvider(identity_provider_base.IdentityProviderBase):
    @property
    def client_id(self,) -> Optional[str]:
        """
        Gets the clientId property value. The identifier for the client application obtained when registering the application with the identity provider. Required.
        Returns: Optional[str]
        """
        return self._client_id
    
    @client_id.setter
    def client_id(self,value: Optional[str] = None) -> None:
        """
        Sets the clientId property value. The identifier for the client application obtained when registering the application with the identity provider. Required.
        Args:
            value: Value to set for the clientId property.
        """
        self._client_id = value
    
    @property
    def client_secret(self,) -> Optional[str]:
        """
        Gets the clientSecret property value. The client secret for the application that is obtained when the application is registered with the identity provider. This is write-only. A read operation returns ****. Required.
        Returns: Optional[str]
        """
        return self._client_secret
    
    @client_secret.setter
    def client_secret(self,value: Optional[str] = None) -> None:
        """
        Sets the clientSecret property value. The client secret for the application that is obtained when the application is registered with the identity provider. This is write-only. A read operation returns ****. Required.
        Args:
            value: Value to set for the clientSecret property.
        """
        self._client_secret = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new SocialIdentityProvider and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.socialIdentityProvider"
        # The identifier for the client application obtained when registering the application with the identity provider. Required.
        self._client_id: Optional[str] = None
        # The client secret for the application that is obtained when the application is registered with the identity provider. This is write-only. A read operation returns ****. Required.
        self._client_secret: Optional[str] = None
        # For a B2B scenario, possible values: Google, Facebook. For a B2C scenario, possible values: Microsoft, Google, Amazon, LinkedIn, Facebook, GitHub, Twitter, Weibo, QQ, WeChat. Required.
        self._identity_provider_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SocialIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SocialIdentityProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SocialIdentityProvider()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "client_id": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "client_secret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "identity_provider_type": lambda n : setattr(self, 'identity_provider_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_provider_type(self,) -> Optional[str]:
        """
        Gets the identityProviderType property value. For a B2B scenario, possible values: Google, Facebook. For a B2C scenario, possible values: Microsoft, Google, Amazon, LinkedIn, Facebook, GitHub, Twitter, Weibo, QQ, WeChat. Required.
        Returns: Optional[str]
        """
        return self._identity_provider_type
    
    @identity_provider_type.setter
    def identity_provider_type(self,value: Optional[str] = None) -> None:
        """
        Sets the identityProviderType property value. For a B2B scenario, possible values: Google, Facebook. For a B2C scenario, possible values: Microsoft, Google, Amazon, LinkedIn, Facebook, GitHub, Twitter, Weibo, QQ, WeChat. Required.
        Args:
            value: Value to set for the identityProviderType property.
        """
        self._identity_provider_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("clientSecret", self.client_secret)
        writer.write_str_value("identityProviderType", self.identity_provider_type)
    

