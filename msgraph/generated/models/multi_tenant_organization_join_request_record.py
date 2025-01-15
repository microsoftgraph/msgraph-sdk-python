from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .multi_tenant_organization_join_request_transition_details import MultiTenantOrganizationJoinRequestTransitionDetails
    from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
    from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

from .entity import Entity

@dataclass
class MultiTenantOrganizationJoinRequestRecord(Entity, Parsable):
    # Tenant ID of the Microsoft Entra tenant that added a tenant to the multitenant organization. To reset a failed join request, set addedByTenantId to 00000000-0000-0000-0000-000000000000. Required.
    added_by_tenant_id: Optional[str] = None
    # State of the tenant in the multitenant organization. The possible values are: pending, active, removed, unknownFutureValue. Tenants in the pending state must join the multitenant organization to participate in the multitenant organization. Tenants in the active state can participate in the multitenant organization. Tenants in the removed state are in the process of being removed from the multitenant organization. Read-only.
    member_state: Optional[MultiTenantOrganizationMemberState] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Role of the tenant in the multitenant organization. The possible values are: owner, member (default), unknownFutureValue. Tenants with the owner role can manage the multitenant organization. There can be multiple tenants with the owner role in a multitenant organization. Tenants with the member role can participate in a multitenant organization.
    role: Optional[MultiTenantOrganizationMemberRole] = None
    # Details of the processing status for a tenant joining a multitenant organization. Read-only.
    transition_details: Optional[MultiTenantOrganizationJoinRequestTransitionDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MultiTenantOrganizationJoinRequestRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiTenantOrganizationJoinRequestRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MultiTenantOrganizationJoinRequestRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .multi_tenant_organization_join_request_transition_details import MultiTenantOrganizationJoinRequestTransitionDetails
        from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

        from .entity import Entity
        from .multi_tenant_organization_join_request_transition_details import MultiTenantOrganizationJoinRequestTransitionDetails
        from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState

        fields: dict[str, Callable[[Any], None]] = {
            "addedByTenantId": lambda n : setattr(self, 'added_by_tenant_id', n.get_str_value()),
            "memberState": lambda n : setattr(self, 'member_state', n.get_enum_value(MultiTenantOrganizationMemberState)),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(MultiTenantOrganizationMemberRole)),
            "transitionDetails": lambda n : setattr(self, 'transition_details', n.get_object_value(MultiTenantOrganizationJoinRequestTransitionDetails)),
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
        writer.write_str_value("addedByTenantId", self.added_by_tenant_id)
        writer.write_enum_value("memberState", self.member_state)
        writer.write_enum_value("role", self.role)
        writer.write_object_value("transitionDetails", self.transition_details)
    

