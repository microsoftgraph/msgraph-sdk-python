from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegated_administration_role_assignment import DelegatedAdministrationRoleAssignment
    from .entity import Entity
    from .multi_tenant_applications_to_provision import MultiTenantApplicationsToProvision

from .entity import Entity

@dataclass
class TenantGovernancePolicyTemplate(Entity, Parsable):
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The delegatedAdministrationRoleAssignments property
    delegated_administration_role_assignments: Optional[list[DelegatedAdministrationRoleAssignment]] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The governedTenantCanTerminate property
    governed_tenant_can_terminate: Optional[bool] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The multiTenantApplicationsToProvision property
    multi_tenant_applications_to_provision: Optional[list[MultiTenantApplicationsToProvision]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantGovernancePolicyTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantGovernancePolicyTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantGovernancePolicyTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .delegated_administration_role_assignment import DelegatedAdministrationRoleAssignment
        from .entity import Entity
        from .multi_tenant_applications_to_provision import MultiTenantApplicationsToProvision

        from .delegated_administration_role_assignment import DelegatedAdministrationRoleAssignment
        from .entity import Entity
        from .multi_tenant_applications_to_provision import MultiTenantApplicationsToProvision

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "delegatedAdministrationRoleAssignments": lambda n : setattr(self, 'delegated_administration_role_assignments', n.get_collection_of_object_values(DelegatedAdministrationRoleAssignment)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "governedTenantCanTerminate": lambda n : setattr(self, 'governed_tenant_can_terminate', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "multiTenantApplicationsToProvision": lambda n : setattr(self, 'multi_tenant_applications_to_provision', n.get_collection_of_object_values(MultiTenantApplicationsToProvision)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_collection_of_object_values("delegatedAdministrationRoleAssignments", self.delegated_administration_role_assignments)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("governedTenantCanTerminate", self.governed_tenant_can_terminate)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("multiTenantApplicationsToProvision", self.multi_tenant_applications_to_provision)
        writer.write_str_value("version", self.version)
    

