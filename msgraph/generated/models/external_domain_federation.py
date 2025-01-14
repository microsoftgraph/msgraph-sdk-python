from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_source import IdentitySource

from .identity_source import IdentitySource

@dataclass
class ExternalDomainFederation(IdentitySource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.externalDomainFederation"
    # The name of the identity source, typically also the domain name. Read only.
    display_name: Optional[str] = None
    # The domain name. Read only.
    domain_name: Optional[str] = None
    # The issuerURI of the incoming federation. Read only.
    issuer_uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalDomainFederation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalDomainFederation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalDomainFederation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_source import IdentitySource

        from .identity_source import IdentitySource

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "issuerUri": lambda n : setattr(self, 'issuer_uri', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("issuerUri", self.issuer_uri)
    

