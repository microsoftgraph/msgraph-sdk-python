from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcUserSettingAssignment(Entity, Parsable):
    # The date and time when this assignment was created. The timestamp type represents the date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The assignment target for the user setting. Currently, the only target supported for this user setting is a user group. For details, see cloudPcManagementGroupAssignmentTarget.
    target: Optional[CloudPcManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcUserSettingAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcUserSettingAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcUserSettingAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget
        from .entity import Entity

        from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
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
        from .cloud_pc_management_assignment_target import CloudPcManagementAssignmentTarget
        from .entity import Entity

        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("target", self.target)
    

