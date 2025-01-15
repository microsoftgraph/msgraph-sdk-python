from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase
    from .pkcs12_certificate_information import Pkcs12CertificateInformation

from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase

@dataclass
class ClientCertificateAuthentication(ApiAuthenticationConfigurationBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.clientCertificateAuthentication"
    # The list of certificates uploaded for this API connector.
    certificate_list: Optional[list[Pkcs12CertificateInformation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClientCertificateAuthentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClientCertificateAuthentication
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClientCertificateAuthentication()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase
        from .pkcs12_certificate_information import Pkcs12CertificateInformation

        from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase
        from .pkcs12_certificate_information import Pkcs12CertificateInformation

        fields: dict[str, Callable[[Any], None]] = {
            "certificateList": lambda n : setattr(self, 'certificate_list', n.get_collection_of_object_values(Pkcs12CertificateInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("certificateList", self.certificate_list)
    

