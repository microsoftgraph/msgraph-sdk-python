from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_provider_base

from . import identity_provider_base

@dataclass
class AppleManagedIdentityProvider(identity_provider_base.IdentityProviderBase):
    odata_type = "#microsoft.graph.appleManagedIdentityProvider"
    # The certificate data, which is a long string of text from the certificate. Can be null.
    certificate_data: Optional[str] = None
    # The Apple developer identifier. Required.
    developer_id: Optional[str] = None
    # The Apple key identifier. Required.
    key_id: Optional[str] = None
    # The Apple service identifier. Required.
    service_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleManagedIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppleManagedIdentityProvider
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppleManagedIdentityProvider()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_provider_base

        from . import identity_provider_base

        fields: Dict[str, Callable[[Any], None]] = {
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
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("certificateData", self.certificate_data)
        writer.write_str_value("developerId", self.developer_id)
        writer.write_str_value("keyId", self.key_id)
        writer.write_str_value("serviceId", self.service_id)
    

