from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

external_domain_name = lazy_import('msgraph.generated.models.external_domain_name')
saml_or_ws_fed_provider = lazy_import('msgraph.generated.models.saml_or_ws_fed_provider')

class SamlOrWsFedExternalDomainFederation(saml_or_ws_fed_provider.SamlOrWsFedProvider):
    def __init__(self,) -> None:
        """
        Instantiates a new SamlOrWsFedExternalDomainFederation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.samlOrWsFedExternalDomainFederation"
        # Collection of domain names of the external organizations that the tenant is federating with. Supports $filter (eq).
        self._domains: Optional[List[external_domain_name.ExternalDomainName]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SamlOrWsFedExternalDomainFederation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SamlOrWsFedExternalDomainFederation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SamlOrWsFedExternalDomainFederation()
    
    @property
    def domains(self,) -> Optional[List[external_domain_name.ExternalDomainName]]:
        """
        Gets the domains property value. Collection of domain names of the external organizations that the tenant is federating with. Supports $filter (eq).
        Returns: Optional[List[external_domain_name.ExternalDomainName]]
        """
        return self._domains
    
    @domains.setter
    def domains(self,value: Optional[List[external_domain_name.ExternalDomainName]] = None) -> None:
        """
        Sets the domains property value. Collection of domain names of the external organizations that the tenant is federating with. Supports $filter (eq).
        Args:
            value: Value to set for the domains property.
        """
        self._domains = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("domains", self.domains)
    

