from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence

from .alert_evidence import AlertEvidence

@dataclass
class ActiveDirectoryDomainEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.activeDirectoryDomainEvidence"
    # The activeDirectoryDomainName property
    active_directory_domain_name: Optional[str] = None
    # The trustedDomains property
    trusted_domains: Optional[list[ActiveDirectoryDomainEvidence]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActiveDirectoryDomainEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActiveDirectoryDomainEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActiveDirectoryDomainEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence

        from .alert_evidence import AlertEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "activeDirectoryDomainName": lambda n : setattr(self, 'active_directory_domain_name', n.get_str_value()),
            "trustedDomains": lambda n : setattr(self, 'trusted_domains', n.get_collection_of_object_values(ActiveDirectoryDomainEvidence)),
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
        writer.write_str_value("activeDirectoryDomainName", self.active_directory_domain_name)
        writer.write_collection_of_object_values("trustedDomains", self.trusted_domains)
    

