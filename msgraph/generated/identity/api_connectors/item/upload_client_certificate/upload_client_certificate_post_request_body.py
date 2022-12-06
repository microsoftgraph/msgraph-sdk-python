from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UploadClientCertificatePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the uploadClientCertificate method.
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
        Instantiates a new uploadClientCertificatePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The password property
        self._password: Optional[str] = None
        # The pkcs12Value property
        self._pkcs12_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UploadClientCertificatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UploadClientCertificatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UploadClientCertificatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "pkcs12_value": lambda n : setattr(self, 'pkcs12_value', n.get_str_value()),
        }
        return fields
    
    @property
    def password(self,) -> Optional[str]:
        """
        Gets the password property value. The password property
        Returns: Optional[str]
        """
        return self._password
    
    @password.setter
    def password(self,value: Optional[str] = None) -> None:
        """
        Sets the password property value. The password property
        Args:
            value: Value to set for the password property.
        """
        self._password = value
    
    @property
    def pkcs12_value(self,) -> Optional[str]:
        """
        Gets the pkcs12Value property value. The pkcs12Value property
        Returns: Optional[str]
        """
        return self._pkcs12_value
    
    @pkcs12_value.setter
    def pkcs12_value(self,value: Optional[str] = None) -> None:
        """
        Sets the pkcs12Value property value. The pkcs12Value property
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
        writer.write_str_value("password", self.password)
        writer.write_str_value("pkcs12Value", self.pkcs12_value)
        writer.write_additional_data_value(self.additional_data)
    

