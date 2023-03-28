from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

api_authentication_configuration_base = lazy_import('msgraph.generated.models.api_authentication_configuration_base')

class BasicAuthentication(api_authentication_configuration_base.ApiAuthenticationConfigurationBase):
    def __init__(self,) -> None:
        """
        Instantiates a new BasicAuthentication and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.basicAuthentication"
        # The password. It is not returned in the responses.
        self._password: Optional[str] = None
        # The username.
        self._username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BasicAuthentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BasicAuthentication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BasicAuthentication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "username": lambda n : setattr(self, 'username', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def password(self,) -> Optional[str]:
        """
        Gets the password property value. The password. It is not returned in the responses.
        Returns: Optional[str]
        """
        return self._password
    
    @password.setter
    def password(self,value: Optional[str] = None) -> None:
        """
        Sets the password property value. The password. It is not returned in the responses.
        Args:
            value: Value to set for the password property.
        """
        self._password = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("password", self.password)
        writer.write_str_value("username", self.username)
    
    @property
    def username(self,) -> Optional[str]:
        """
        Gets the username property value. The username.
        Returns: Optional[str]
        """
        return self._username
    
    @username.setter
    def username(self,value: Optional[str] = None) -> None:
        """
        Sets the username property value. The username.
        Args:
            value: Value to set for the username property.
        """
        self._username = value
    

