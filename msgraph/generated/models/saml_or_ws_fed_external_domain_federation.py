from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .external_domain_name import ExternalDomainName
    from .saml_or_ws_fed_provider import SamlOrWsFedProvider

from .saml_or_ws_fed_provider import SamlOrWsFedProvider

@dataclass
class SamlOrWsFedExternalDomainFederation(SamlOrWsFedProvider):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.samlOrWsFedExternalDomainFederation"
    # Collection of domain names of the external organizations that the tenant is federating with. Supports $filter (eq).
    domains: Optional[List[ExternalDomainName]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SamlOrWsFedExternalDomainFederation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SamlOrWsFedExternalDomainFederation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SamlOrWsFedExternalDomainFederation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .external_domain_name import ExternalDomainName
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider

        from .external_domain_name import ExternalDomainName
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider

        fields: Dict[str, Callable[[Any], None]] = {
            "domains": lambda n : setattr(self, 'domains', n.get_collection_of_object_values(ExternalDomainName)),
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
        writer.write_collection_of_object_values("domains", self.domains)
    

