from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')
detection_status = lazy_import('msgraph.generated.models.security.detection_status')
file_details = lazy_import('msgraph.generated.models.security.file_details')

class FileEvidence(alert_evidence.AlertEvidence):
    def __init__(self,) -> None:
        """
        Instantiates a new FileEvidence and sets the default values.
        """
        super().__init__()
        # The status of the detection.The possible values are: detected, blocked, prevented, unknownFutureValue.
        self._detection_status: Optional[detection_status.DetectionStatus] = None
        # The file details.
        self._file_details: Optional[file_details.FileDetails] = None
        # A unique identifier assigned to a device by Microsoft Defender for Endpoint.
        self._mde_device_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FileEvidence()
    
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
    
    @property
    def file_details(self,) -> Optional[file_details.FileDetails]:
        """
        Gets the fileDetails property value. The file details.
        Returns: Optional[file_details.FileDetails]
        """
        return self._file_details
    
    @file_details.setter
    def file_details(self,value: Optional[file_details.FileDetails] = None) -> None:
        """
        Sets the fileDetails property value. The file details.
        Args:
            value: Value to set for the fileDetails property.
        """
        self._file_details = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "detection_status": lambda n : setattr(self, 'detection_status', n.get_enum_value(detection_status.DetectionStatus)),
            "file_details": lambda n : setattr(self, 'file_details', n.get_object_value(file_details.FileDetails)),
            "mde_device_id": lambda n : setattr(self, 'mde_device_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
        writer.write_object_value("fileDetails", self.file_details)
        writer.write_str_value("mdeDeviceId", self.mde_device_id)
    

