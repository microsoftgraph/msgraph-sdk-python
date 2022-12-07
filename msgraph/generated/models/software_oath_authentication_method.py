from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method = lazy_import('msgraph.generated.models.authentication_method')

class SoftwareOathAuthenticationMethod(authentication_method.AuthenticationMethod):
    def __init__(self,) -> None:
        """
        Instantiates a new SoftwareOathAuthenticationMethod and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.softwareOathAuthenticationMethod"
        # The secret key of the method. Always returns null.
        self._secret_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SoftwareOathAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SoftwareOathAuthenticationMethod
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SoftwareOathAuthenticationMethod()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "secret_key": lambda n : setattr(self, 'secret_key', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def secret_key(self,) -> Optional[str]:
        """
        Gets the secretKey property value. The secret key of the method. Always returns null.
        Returns: Optional[str]
        """
        return self._secret_key
    
    @secret_key.setter
    def secret_key(self,value: Optional[str] = None) -> None:
        """
        Sets the secretKey property value. The secret key of the method. Always returns null.
        Args:
            value: Value to set for the secretKey property.
        """
        self._secret_key = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("secretKey", self.secret_key)
    

