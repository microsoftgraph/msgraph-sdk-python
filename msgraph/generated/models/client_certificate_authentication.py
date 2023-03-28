from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import api_authentication_configuration_base, pkcs12_certificate_information

from . import api_authentication_configuration_base

class ClientCertificateAuthentication(api_authentication_configuration_base.ApiAuthenticationConfigurationBase):
    def __init__(self,) -> None:
        """
        Instantiates a new ClientCertificateAuthentication and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.clientCertificateAuthentication"
        # The list of certificates uploaded for this API connector.
        self._certificate_list: Optional[List[pkcs12_certificate_information.Pkcs12CertificateInformation]] = None
    
    @property
    def certificate_list(self,) -> Optional[List[pkcs12_certificate_information.Pkcs12CertificateInformation]]:
        """
        Gets the certificateList property value. The list of certificates uploaded for this API connector.
        Returns: Optional[List[pkcs12_certificate_information.Pkcs12CertificateInformation]]
        """
        return self._certificate_list
    
    @certificate_list.setter
    def certificate_list(self,value: Optional[List[pkcs12_certificate_information.Pkcs12CertificateInformation]] = None) -> None:
        """
        Sets the certificateList property value. The list of certificates uploaded for this API connector.
        Args:
            value: Value to set for the certificate_list property.
        """
        self._certificate_list = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClientCertificateAuthentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ClientCertificateAuthentication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ClientCertificateAuthentication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import api_authentication_configuration_base, pkcs12_certificate_information

        fields: Dict[str, Callable[[Any], None]] = {
            "certificateList": lambda n : setattr(self, 'certificate_list', n.get_collection_of_object_values(pkcs12_certificate_information.Pkcs12CertificateInformation)),
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
        writer.write_collection_of_object_values("certificateList", self.certificate_list)
    

