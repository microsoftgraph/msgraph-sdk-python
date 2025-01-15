from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
    from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
    from .multi_tenant_organization_member_transition_details import MultiTenantOrganizationMemberTransitionDetails

from .directory_object import DirectoryObject

@dataclass
class MultiTenantOrganizationMember(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.multiTenantOrganizationMember"
    # Tenant ID of the tenant that added the tenant to the multitenant organization. Read-only.
    added_by_tenant_id: Optional[UUID] = None
    # Date and time when the tenant was added to the multitenant organization. Read-only.
    added_date_time: Optional[datetime.datetime] = None
    # Display name of the tenant added to the multitenant organization.
    display_name: Optional[str] = None
    # Date and time when the tenant joined the multitenant organization. Read-only.
    joined_date_time: Optional[datetime.datetime] = None
    # Role of the tenant in the multitenant organization. The possible values are: owner, member (default), unknownFutureValue. Tenants with the owner role can manage the multitenant organization but tenants with the member role can only participate in a multitenant organization. There can be multiple tenants with the owner role in a multitenant organization.
    role: Optional[MultiTenantOrganizationMemberRole] = None
    # State of the tenant in the multitenant organization. The possible values are: pending, active, removed, unknownFutureValue. Tenants in the pending state must join the multitenant organization to participate in the multitenant organization. Tenants in the active state can participate in the multitenant organization. Tenants in the removed state are in the process of being removed from the multitenant organization. Read-only.
    state: Optional[MultiTenantOrganizationMemberState] = None
    # Tenant ID of the Microsoft Entra tenant added to the multitenant organization. Set at the time tenant is added.Supports $filter. Key.
    tenant_id: Optional[str] = None
    # Details of the processing status for a tenant in a multitenant organization. Read-only. Nullable.
    transition_details: Optional[MultiTenantOrganizationMemberTransitionDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MultiTenantOrganizationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiTenantOrganizationMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MultiTenantOrganizationMember()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
        from .multi_tenant_organization_member_transition_details import MultiTenantOrganizationMemberTransitionDetails

        from .directory_object import DirectoryObject
        from .multi_tenant_organization_member_role import MultiTenantOrganizationMemberRole
        from .multi_tenant_organization_member_state import MultiTenantOrganizationMemberState
        from .multi_tenant_organization_member_transition_details import MultiTenantOrganizationMemberTransitionDetails

        fields: dict[str, Callable[[Any], None]] = {
            "addedByTenantId": lambda n : setattr(self, 'added_by_tenant_id', n.get_uuid_value()),
            "addedDateTime": lambda n : setattr(self, 'added_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "joinedDateTime": lambda n : setattr(self, 'joined_date_time', n.get_datetime_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(MultiTenantOrganizationMemberRole)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(MultiTenantOrganizationMemberState)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "transitionDetails": lambda n : setattr(self, 'transition_details', n.get_object_value(MultiTenantOrganizationMemberTransitionDetails)),
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
        writer.write_uuid_value("addedByTenantId", self.added_by_tenant_id)
        writer.write_datetime_value("addedDateTime", self.added_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("joinedDateTime", self.joined_date_time)
        writer.write_enum_value("role", self.role)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("transitionDetails", self.transition_details)
    

