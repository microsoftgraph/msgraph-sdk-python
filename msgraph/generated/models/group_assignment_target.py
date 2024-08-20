from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
    from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget

from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget

@dataclass
class GroupAssignmentTarget(DeviceAndAppManagementAssignmentTarget):
    """
    Represents an assignment to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupAssignmentTarget"
    # The group Id that is the target of the assignment.
    group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupAssignmentTarget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exclusionGroupAssignmentTarget".casefold():
            from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget

            return ExclusionGroupAssignmentTarget()
        return GroupAssignmentTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget

        from .device_and_app_management_assignment_target import DeviceAndAppManagementAssignmentTarget
        from .exclusion_group_assignment_target import ExclusionGroupAssignmentTarget

        fields: Dict[str, Callable[[Any], None]] = {
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
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
        writer.write_str_value("groupId", self.group_id)
    

