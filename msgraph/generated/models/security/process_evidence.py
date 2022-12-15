from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')
detection_status = lazy_import('msgraph.generated.models.security.detection_status')
file_details = lazy_import('msgraph.generated.models.security.file_details')
user_account = lazy_import('msgraph.generated.models.security.user_account')

class ProcessEvidence(alert_evidence.AlertEvidence):
    def __init__(self,) -> None:
        """
        Instantiates a new ProcessEvidence and sets the default values.
        """
        super().__init__()
        # The status of the detection.The possible values are: detected, blocked, prevented, unknownFutureValue.
        self._detection_status: Optional[detection_status.DetectionStatus] = None
        # Image file details.
        self._image_file: Optional[file_details.FileDetails] = None
        # A unique identifier assigned to a device by Microsoft Defender for Endpoint.
        self._mde_device_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Date and time when the parent of the process was created.
        self._parent_process_creation_date_time: Optional[datetime] = None
        # Process ID (PID) of the parent process that spawned the process.
        self._parent_process_id: Optional[int] = None
        # Parent process image file details.
        self._parent_process_image_file: Optional[file_details.FileDetails] = None
        # Command line used to create the new process.
        self._process_command_line: Optional[str] = None
        # Date and time the process was created.
        self._process_creation_date_time: Optional[datetime] = None
        # Process ID (PID) of the newly created process.
        self._process_id: Optional[int] = None
        # User details of the user that ran the process.
        self._user_account: Optional[user_account.UserAccount] = None
    
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
    
    @property
    def detection_status(self,) -> Optional[detection_status.DetectionStatus]:
        """
        Gets the detectionStatus property value. The status of the detection.The possible values are: detected, blocked, prevented, unknownFutureValue.
        Returns: Optional[detection_status.DetectionStatus]
        """
        return self._detection_status
    
    @detection_status.setter
    def detection_status(self,value: Optional[detection_status.DetectionStatus] = None) -> None:
        """
        Sets the detectionStatus property value. The status of the detection.The possible values are: detected, blocked, prevented, unknownFutureValue.
        Args:
            value: Value to set for the detectionStatus property.
        """
        self._detection_status = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "detection_status": lambda n : setattr(self, 'detection_status', n.get_enum_value(detection_status.DetectionStatus)),
            "image_file": lambda n : setattr(self, 'image_file', n.get_object_value(file_details.FileDetails)),
            "mde_device_id": lambda n : setattr(self, 'mde_device_id', n.get_str_value()),
            "parent_process_creation_date_time": lambda n : setattr(self, 'parent_process_creation_date_time', n.get_datetime_value()),
            "parent_process_id": lambda n : setattr(self, 'parent_process_id', n.get_int_value()),
            "parent_process_image_file": lambda n : setattr(self, 'parent_process_image_file', n.get_object_value(file_details.FileDetails)),
            "process_command_line": lambda n : setattr(self, 'process_command_line', n.get_str_value()),
            "process_creation_date_time": lambda n : setattr(self, 'process_creation_date_time', n.get_datetime_value()),
            "process_id": lambda n : setattr(self, 'process_id', n.get_int_value()),
            "user_account": lambda n : setattr(self, 'user_account', n.get_object_value(user_account.UserAccount)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def image_file(self,) -> Optional[file_details.FileDetails]:
        """
        Gets the imageFile property value. Image file details.
        Returns: Optional[file_details.FileDetails]
        """
        return self._image_file
    
    @image_file.setter
    def image_file(self,value: Optional[file_details.FileDetails] = None) -> None:
        """
        Sets the imageFile property value. Image file details.
        Args:
            value: Value to set for the imageFile property.
        """
        self._image_file = value
    
    @property
    def mde_device_id(self,) -> Optional[str]:
        """
        Gets the mdeDeviceId property value. A unique identifier assigned to a device by Microsoft Defender for Endpoint.
        Returns: Optional[str]
        """
        return self._mde_device_id
    
    @mde_device_id.setter
    def mde_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the mdeDeviceId property value. A unique identifier assigned to a device by Microsoft Defender for Endpoint.
        Args:
            value: Value to set for the mdeDeviceId property.
        """
        self._mde_device_id = value
    
    @property
    def parent_process_creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the parentProcessCreationDateTime property value. Date and time when the parent of the process was created.
        Returns: Optional[datetime]
        """
        return self._parent_process_creation_date_time
    
    @parent_process_creation_date_time.setter
    def parent_process_creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the parentProcessCreationDateTime property value. Date and time when the parent of the process was created.
        Args:
            value: Value to set for the parentProcessCreationDateTime property.
        """
        self._parent_process_creation_date_time = value
    
    @property
    def parent_process_id(self,) -> Optional[int]:
        """
        Gets the parentProcessId property value. Process ID (PID) of the parent process that spawned the process.
        Returns: Optional[int]
        """
        return self._parent_process_id
    
    @parent_process_id.setter
    def parent_process_id(self,value: Optional[int] = None) -> None:
        """
        Sets the parentProcessId property value. Process ID (PID) of the parent process that spawned the process.
        Args:
            value: Value to set for the parentProcessId property.
        """
        self._parent_process_id = value
    
    @property
    def parent_process_image_file(self,) -> Optional[file_details.FileDetails]:
        """
        Gets the parentProcessImageFile property value. Parent process image file details.
        Returns: Optional[file_details.FileDetails]
        """
        return self._parent_process_image_file
    
    @parent_process_image_file.setter
    def parent_process_image_file(self,value: Optional[file_details.FileDetails] = None) -> None:
        """
        Sets the parentProcessImageFile property value. Parent process image file details.
        Args:
            value: Value to set for the parentProcessImageFile property.
        """
        self._parent_process_image_file = value
    
    @property
    def process_command_line(self,) -> Optional[str]:
        """
        Gets the processCommandLine property value. Command line used to create the new process.
        Returns: Optional[str]
        """
        return self._process_command_line
    
    @process_command_line.setter
    def process_command_line(self,value: Optional[str] = None) -> None:
        """
        Sets the processCommandLine property value. Command line used to create the new process.
        Args:
            value: Value to set for the processCommandLine property.
        """
        self._process_command_line = value
    
    @property
    def process_creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the processCreationDateTime property value. Date and time the process was created.
        Returns: Optional[datetime]
        """
        return self._process_creation_date_time
    
    @process_creation_date_time.setter
    def process_creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the processCreationDateTime property value. Date and time the process was created.
        Args:
            value: Value to set for the processCreationDateTime property.
        """
        self._process_creation_date_time = value
    
    @property
    def process_id(self,) -> Optional[int]:
        """
        Gets the processId property value. Process ID (PID) of the newly created process.
        Returns: Optional[int]
        """
        return self._process_id
    
    @process_id.setter
    def process_id(self,value: Optional[int] = None) -> None:
        """
        Sets the processId property value. Process ID (PID) of the newly created process.
        Args:
            value: Value to set for the processId property.
        """
        self._process_id = value
    
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
    
    @property
    def user_account(self,) -> Optional[user_account.UserAccount]:
        """
        Gets the userAccount property value. User details of the user that ran the process.
        Returns: Optional[user_account.UserAccount]
        """
        return self._user_account
    
    @user_account.setter
    def user_account(self,value: Optional[user_account.UserAccount] = None) -> None:
        """
        Sets the userAccount property value. User details of the user that ran the process.
        Args:
            value: Value to set for the userAccount property.
        """
        self._user_account = value
    

