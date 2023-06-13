from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_evidence, detection_status, file_details, user_account

from . import alert_evidence

@dataclass
class ProcessEvidence(alert_evidence.AlertEvidence):
    # The status of the detection.The possible values are: detected, blocked, prevented, unknownFutureValue.
    detection_status: Optional[detection_status.DetectionStatus] = None
    # Image file details.
    image_file: Optional[file_details.FileDetails] = None
    # A unique identifier assigned to a device by Microsoft Defender for Endpoint.
    mde_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Date and time when the parent of the process was created.
    parent_process_creation_date_time: Optional[datetime] = None
    # Process ID (PID) of the parent process that spawned the process.
    parent_process_id: Optional[int] = None
    # Parent process image file details.
    parent_process_image_file: Optional[file_details.FileDetails] = None
    # Command line used to create the new process.
    process_command_line: Optional[str] = None
    # Date and time the process was created.
    process_creation_date_time: Optional[datetime] = None
    # Process ID (PID) of the newly created process.
    process_id: Optional[int] = None
    # User details of the user that ran the process.
    user_account: Optional[user_account.UserAccount] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProcessEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProcessEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProcessEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_evidence, detection_status, file_details, user_account

        fields: Dict[str, Callable[[Any], None]] = {
            "detectionStatus": lambda n : setattr(self, 'detection_status', n.get_enum_value(detection_status.DetectionStatus)),
            "imageFile": lambda n : setattr(self, 'image_file', n.get_object_value(file_details.FileDetails)),
            "mdeDeviceId": lambda n : setattr(self, 'mde_device_id', n.get_str_value()),
            "parentProcessCreationDateTime": lambda n : setattr(self, 'parent_process_creation_date_time', n.get_datetime_value()),
            "parentProcessId": lambda n : setattr(self, 'parent_process_id', n.get_int_value()),
            "parentProcessImageFile": lambda n : setattr(self, 'parent_process_image_file', n.get_object_value(file_details.FileDetails)),
            "processCommandLine": lambda n : setattr(self, 'process_command_line', n.get_str_value()),
            "processCreationDateTime": lambda n : setattr(self, 'process_creation_date_time', n.get_datetime_value()),
            "processId": lambda n : setattr(self, 'process_id', n.get_int_value()),
            "userAccount": lambda n : setattr(self, 'user_account', n.get_object_value(user_account.UserAccount)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("detectionStatus", self.detection_status)
        writer.write_object_value("imageFile", self.image_file)
        writer.write_str_value("mdeDeviceId", self.mde_device_id)
        writer.write_datetime_value("parentProcessCreationDateTime", self.parent_process_creation_date_time)
        writer.write_int_value("parentProcessId", self.parent_process_id)
        writer.write_object_value("parentProcessImageFile", self.parent_process_image_file)
        writer.write_str_value("processCommandLine", self.process_command_line)
        writer.write_datetime_value("processCreationDateTime", self.process_creation_date_time)
        writer.write_int_value("processId", self.process_id)
        writer.write_object_value("userAccount", self.user_account)
    

