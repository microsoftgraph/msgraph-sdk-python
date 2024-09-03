from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
    from .multi_tenant_organization_member import MultiTenantOrganizationMember
    from .multi_tenant_organization_state import MultiTenantOrganizationState

from .entity import Entity

@dataclass
class MultiTenantOrganization(Entity):
    # Date when multitenant organization was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the multitenant organization.
    description: Optional[str] = None
    # Display name of the multitenant organization.
    display_name: Optional[str] = None
    # Defines the status of a tenant joining a multitenant organization.
    join_request: Optional[MultiTenantOrganizationJoinRequestRecord] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # State of the multitenant organization. The possible values are: active, inactive, unknownFutureValue. active indicates the multitenant organization is created. inactive indicates the multitenant organization isn't created. Read-only.
    state: Optional[MultiTenantOrganizationState] = None
    # Defines tenants added to a multitenant organization.
    tenants: Optional[List[MultiTenantOrganizationMember]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MultiTenantOrganization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiTenantOrganization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MultiTenantOrganization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
        from .multi_tenant_organization_member import MultiTenantOrganizationMember
        from .multi_tenant_organization_state import MultiTenantOrganizationState

        from .entity import Entity
        from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
        from .multi_tenant_organization_member import MultiTenantOrganizationMember
        from .multi_tenant_organization_state import MultiTenantOrganizationState

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "joinRequest": lambda n : setattr(self, 'join_request', n.get_object_value(MultiTenantOrganizationJoinRequestRecord)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(MultiTenantOrganizationState)),
            "tenants": lambda n : setattr(self, 'tenants', n.get_collection_of_object_values(MultiTenantOrganizationMember)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("joinRequest", self.join_request)
        writer.write_enum_value("state", self.state)
        writer.write_collection_of_object_values("tenants", self.tenants)
    

