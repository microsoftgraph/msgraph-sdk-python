from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_provider_base = lazy_import('msgraph.generated.models.identity_provider_base')

class AppleManagedIdentityProvider(identity_provider_base.IdentityProviderBase):
    @property
    def certificate_data(self,) -> Optional[str]:
        """
        Gets the certificateData property value. The certificate data, which is a long string of text from the certificate. Can be null.
        Returns: Optional[str]
        """
        return self._certificate_data
    
    @certificate_data.setter
    def certificate_data(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateData property value. The certificate data, which is a long string of text from the certificate. Can be null.
        Args:
            value: Value to set for the certificateData property.
        """
        self._certificate_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AppleManagedIdentityProvider and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.appleManagedIdentityProvider"
        # The certificate data, which is a long string of text from the certificate. Can be null.
        self._certificate_data: Optional[str] = None
        # The Apple developer identifier. Required.
        self._developer_id: Optional[str] = None
        # The Apple key identifier. Required.
        self._key_id: Optional[str] = None
        # The Apple service identifier. Required.
        self._service_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleManagedIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppleManagedIdentityProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppleManagedIdentityProvider()
    
    @property
    def developer_id(self,) -> Optional[str]:
        """
        Gets the developerId property value. The Apple developer identifier. Required.
        Returns: Optional[str]
        """
        return self._developer_id
    
    @developer_id.setter
    def developer_id(self,value: Optional[str] = None) -> None:
        """
        Sets the developerId property value. The Apple developer identifier. Required.
        Args:
            value: Value to set for the developerId property.
        """
        self._developer_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate_data": lambda n : setattr(self, 'certificate_data', n.get_str_value()),
            "developer_id": lambda n : setattr(self, 'developer_id', n.get_str_value()),
            "key_id": lambda n : setattr(self, 'key_id', n.get_str_value()),
            "service_id": lambda n : setattr(self, 'service_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def key_id(self,) -> Optional[str]:
        """
        Gets the keyId property value. The Apple key identifier. Required.
        Returns: Optional[str]
        """
        return self._key_id
    
    @key_id.setter
    def key_id(self,value: Optional[str] = None) -> None:
        """
        Sets the keyId property value. The Apple key identifier. Required.
        Args:
            value: Value to set for the keyId property.
        """
        self._key_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("certificateData", self.certificate_data)
        writer.write_str_value("developerId", self.developer_id)
        writer.write_str_value("keyId", self.key_id)
        writer.write_str_value("serviceId", self.service_id)
    
    @property
    def service_id(self,) -> Optional[str]:
        """
        Gets the serviceId property value. The Apple service identifier. Required.
        Returns: Optional[str]
        """
        return self._service_id
    
    @service_id.setter
    def service_id(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceId property value. The Apple service identifier. Required.
        Args:
            value: Value to set for the serviceId property.
        """
        self._service_id = value
    

