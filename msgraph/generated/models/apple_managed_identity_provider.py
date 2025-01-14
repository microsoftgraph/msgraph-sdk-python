from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_provider_base import IdentityProviderBase

from .identity_provider_base import IdentityProviderBase

@dataclass
class AppleManagedIdentityProvider(IdentityProviderBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.appleManagedIdentityProvider"
    # The certificate data, which is a long string of text from the certificate. Can be null.
    certificate_data: Optional[str] = None
    # The Apple developer identifier. Required.
    developer_id: Optional[str] = None
    # The Apple key identifier. Required.
    key_id: Optional[str] = None
    # The Apple service identifier. Required.
    service_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppleManagedIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppleManagedIdentityProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppleManagedIdentityProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_provider_base import IdentityProviderBase

        from .identity_provider_base import IdentityProviderBase

        fields: dict[str, Callable[[Any], None]] = {
            "certificateData": lambda n : setattr(self, 'certificate_data', n.get_str_value()),
            "developerId": lambda n : setattr(self, 'developer_id', n.get_str_value()),
            "keyId": lambda n : setattr(self, 'key_id', n.get_str_value()),
            "serviceId": lambda n : setattr(self, 'service_id', n.get_str_value()),
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
        writer.write_str_value("certificateData", self.certificate_data)
        writer.write_str_value("developerId", self.developer_id)
        writer.write_str_value("keyId", self.key_id)
        writer.write_str_value("serviceId", self.service_id)
    

