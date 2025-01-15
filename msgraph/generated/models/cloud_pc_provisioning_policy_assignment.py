from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget
    from .entity import Entity
    from .user import User

from .entity import Entity

@dataclass
class CloudPcProvisioningPolicyAssignment(Entity, Parsable):
    # The assignment targeted users for the provisioning policy. This list of users is computed based on assignments, licenses, group memberships, and policies. Read-only. Supports$expand.
    assigned_users: Optional[list[User]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The assignment target for the provisioning policy. Currently, the only target supported for this policy is a user group. For details, see cloudPcManagementGroupAssignmentTarget.
    target: Optional[CloudPcManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcProvisioningPolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcProvisioningPolicyAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcProvisioningPolicyAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget
        from .entity import Entity
        from .user import User

        from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget
        from .entity import Entity
        from .user import User

        fields: dict[str, Callable[[Any], None]] = {
            "assignedUsers": lambda n : setattr(self, 'assigned_users', n.get_collection_of_object_values(User)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(CloudPcManagementAssignmentTarget)),
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
        writer.write_collection_of_object_values("assignedUsers", self.assigned_users)
        writer.write_object_value("target", self.target)
    

