from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegated_admin_relationship import DelegatedAdminRelationship

from .delegated_admin_relationship import DelegatedAdminRelationship

@dataclass
class ResellerDelegatedAdminRelationship(DelegatedAdminRelationship):
    # The tenant ID of the indirect provider partner who created the relationship for the indirect reseller partner.
    indirect_provider_tenant_id: Optional[str] = None
    # Indicates the indirect reseller partner consent status. true indicates that the partner has yet to review the relationship; false indicates that the partner has already provided consent by approving or rejecting the relationship.
    is_partner_consent_pending: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResellerDelegatedAdminRelationship:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResellerDelegatedAdminRelationship
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResellerDelegatedAdminRelationship()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .delegated_admin_relationship import DelegatedAdminRelationship

        from .delegated_admin_relationship import DelegatedAdminRelationship

        fields: Dict[str, Callable[[Any], None]] = {
            "indirectProviderTenantId": lambda n : setattr(self, 'indirect_provider_tenant_id', n.get_str_value()),
            "isPartnerConsentPending": lambda n : setattr(self, 'is_partner_consent_pending', n.get_bool_value()),
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
        writer.write_str_value("indirectProviderTenantId", self.indirect_provider_tenant_id)
        writer.write_bool_value("isPartnerConsentPending", self.is_partner_consent_pending)
    

