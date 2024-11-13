from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget

from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget

@dataclass
class CloudPcManagementGroupAssignmentTarget(CloudPcManagementAssignmentTarget, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudPcManagementGroupAssignmentTarget"
    # The ID of the target group for the assignment.
    group_id: Optional[str] = None
    # The unique identifier for the service plan that indicates which size of the Cloud PC to provision for the user. Use a null value, when the provisioningType is dedicated.
    service_plan_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcManagementGroupAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcManagementGroupAssignmentTarget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcManagementGroupAssignmentTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget

        from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget

        fields: Dict[str, Callable[[Any], None]] = {
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "servicePlanId": lambda n : setattr(self, 'service_plan_id', n.get_str_value()),
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
        from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget

        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("servicePlanId", self.service_plan_id)
    

