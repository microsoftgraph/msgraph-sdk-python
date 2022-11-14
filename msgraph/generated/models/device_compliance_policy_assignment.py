from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import device_and_app_management_assignment_target, entity

class DeviceCompliancePolicyAssignment(entity.Entity):
    """
    Device compliance policy assignment.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceCompliancePolicyAssignment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceCompliancePolicyAssignment"
        # Target for the compliance policy assignment.
        self._target: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicyAssignment
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicyAssignment()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "target": lambda n : setattr(self, 'target', n.get_object_value(device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("target", self.target)

    @property
    def target(self,) -> Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]:
        """
        Gets the target property value. Target for the compliance policy assignment.
        Returns: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]
        """
        return self._target

    @target.setter
    def target(self,value: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None) -> None:
        """
        Sets the target property value. Target for the compliance policy assignment.
        Args:
            value: Value to set for the target property.
        """
        self._target = value


