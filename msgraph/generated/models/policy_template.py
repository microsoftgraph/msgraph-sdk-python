from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
    from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate

from .entity import Entity

@dataclass
class PolicyTemplate(Entity, Parsable):
    # Defines an optional cross-tenant access policy template with user synchronization settings for a multitenant organization.
    multi_tenant_organization_identity_synchronization: Optional[MultiTenantOrganizationIdentitySyncPolicyTemplate] = None
    # Defines an optional cross-tenant access policy template with inbound and outbound partner configuration settings for a multitenant organization.
    multi_tenant_organization_partner_configuration: Optional[MultiTenantOrganizationPartnerConfigurationTemplate] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
        from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate

        from .entity import Entity
        from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
        from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "multiTenantOrganizationIdentitySynchronization": lambda n : setattr(self, 'multi_tenant_organization_identity_synchronization', n.get_object_value(MultiTenantOrganizationIdentitySyncPolicyTemplate)),
            "multiTenantOrganizationPartnerConfiguration": lambda n : setattr(self, 'multi_tenant_organization_partner_configuration', n.get_object_value(MultiTenantOrganizationPartnerConfigurationTemplate)),
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
        writer.write_object_value("multiTenantOrganizationIdentitySynchronization", self.multi_tenant_organization_identity_synchronization)
        writer.write_object_value("multiTenantOrganizationPartnerConfiguration", self.multi_tenant_organization_partner_configuration)
    

