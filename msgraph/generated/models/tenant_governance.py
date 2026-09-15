from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .governance_invitation import GovernanceInvitation
    from .governance_relationship import GovernanceRelationship
    from .governance_request import GovernanceRequest
    from .related_tenant import RelatedTenant
    from .tenant_governance_policy_template import TenantGovernancePolicyTemplate
    from .tenant_governance_setting import TenantGovernanceSetting

from .entity import Entity

@dataclass
class TenantGovernance(Entity, Parsable):
    # The governanceInvitations property
    governance_invitations: Optional[list[GovernanceInvitation]] = None
    # The governancePolicyTemplates property
    governance_policy_templates: Optional[list[TenantGovernancePolicyTemplate]] = None
    # The governanceRelationships property
    governance_relationships: Optional[list[GovernanceRelationship]] = None
    # The governanceRequests property
    governance_requests: Optional[list[GovernanceRequest]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The relatedTenants property
    related_tenants: Optional[list[RelatedTenant]] = None
    # The settings property
    settings: Optional[TenantGovernanceSetting] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantGovernance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantGovernance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantGovernance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .governance_invitation import GovernanceInvitation
        from .governance_relationship import GovernanceRelationship
        from .governance_request import GovernanceRequest
        from .related_tenant import RelatedTenant
        from .tenant_governance_policy_template import TenantGovernancePolicyTemplate
        from .tenant_governance_setting import TenantGovernanceSetting

        from .entity import Entity
        from .governance_invitation import GovernanceInvitation
        from .governance_relationship import GovernanceRelationship
        from .governance_request import GovernanceRequest
        from .related_tenant import RelatedTenant
        from .tenant_governance_policy_template import TenantGovernancePolicyTemplate
        from .tenant_governance_setting import TenantGovernanceSetting

        fields: dict[str, Callable[[Any], None]] = {
            "governanceInvitations": lambda n : setattr(self, 'governance_invitations', n.get_collection_of_object_values(GovernanceInvitation)),
            "governancePolicyTemplates": lambda n : setattr(self, 'governance_policy_templates', n.get_collection_of_object_values(TenantGovernancePolicyTemplate)),
            "governanceRelationships": lambda n : setattr(self, 'governance_relationships', n.get_collection_of_object_values(GovernanceRelationship)),
            "governanceRequests": lambda n : setattr(self, 'governance_requests', n.get_collection_of_object_values(GovernanceRequest)),
            "relatedTenants": lambda n : setattr(self, 'related_tenants', n.get_collection_of_object_values(RelatedTenant)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(TenantGovernanceSetting)),
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
        writer.write_collection_of_object_values("governanceInvitations", self.governance_invitations)
        writer.write_collection_of_object_values("governancePolicyTemplates", self.governance_policy_templates)
        writer.write_collection_of_object_values("governanceRelationships", self.governance_relationships)
        writer.write_collection_of_object_values("governanceRequests", self.governance_requests)
        writer.write_collection_of_object_values("relatedTenants", self.related_tenants)
        writer.write_object_value("settings", self.settings)
    

