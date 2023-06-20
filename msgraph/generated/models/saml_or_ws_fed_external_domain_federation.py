from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import external_domain_name, saml_or_ws_fed_provider

from . import saml_or_ws_fed_provider

@dataclass
class SamlOrWsFedExternalDomainFederation(saml_or_ws_fed_provider.SamlOrWsFedProvider):
    odata_type = "#microsoft.graph.samlOrWsFedExternalDomainFederation"
    # Collection of domain names of the external organizations that the tenant is federating with. Supports $filter (eq).
    domains: Optional[List[external_domain_name.ExternalDomainName]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SamlOrWsFedExternalDomainFederation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SamlOrWsFedExternalDomainFederation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SamlOrWsFedExternalDomainFederation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import external_domain_name, saml_or_ws_fed_provider

        from . import external_domain_name, saml_or_ws_fed_provider

        fields: Dict[str, Callable[[Any], None]] = {
            "domains": lambda n : setattr(self, 'domains', n.get_collection_of_object_values(external_domain_name.ExternalDomainName)),
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
        writer.write_collection_of_object_values("domains", self.domains)
    

