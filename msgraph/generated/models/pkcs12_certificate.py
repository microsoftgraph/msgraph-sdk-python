from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

api_authentication_configuration_base = lazy_import('msgraph.generated.models.api_authentication_configuration_base')

class Pkcs12Certificate(api_authentication_configuration_base.ApiAuthenticationConfigurationBase):
    def __init__(self,) -> None:
        """
        Instantiates a new Pkcs12Certificate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.pkcs12Certificate"
        # The password for the pfx file. Required. If no password is used, you must still provide a value of ''.
        self._password: Optional[str] = None
        # Represents the pfx content that is sent. The value should be a base-64 encoded version of the actual certificate content. Required.
        self._pkcs12_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Pkcs12Certificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Pkcs12Certificate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Pkcs12Certificate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "pkcs12_value": lambda n : setattr(self, 'pkcs12_value', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def password(self,) -> Optional[str]:
        """
        Gets the password property value. The password for the pfx file. Required. If no password is used, you must still provide a value of ''.
        Returns: Optional[str]
        """
        return self._password
    
    @password.setter
    def password(self,value: Optional[str] = None) -> None:
        """
        Sets the password property value. The password for the pfx file. Required. If no password is used, you must still provide a value of ''.
        Args:
            value: Value to set for the password property.
        """
        self._password = value
    
    @property
    def pkcs12_value(self,) -> Optional[str]:
        """
        Gets the pkcs12Value property value. Represents the pfx content that is sent. The value should be a base-64 encoded version of the actual certificate content. Required.
        Returns: Optional[str]
        """
        return self._pkcs12_value
    
    @pkcs12_value.setter
    def pkcs12_value(self,value: Optional[str] = None) -> None:
        """
        Sets the pkcs12Value property value. Represents the pfx content that is sent. The value should be a base-64 encoded version of the actual certificate content. Required.
        Args:
            value: Value to set for the pkcs12Value property.
        """
        self._pkcs12_value = value
    
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
        writer.write_str_value("pkcs12Value", self.pkcs12_value)
    

