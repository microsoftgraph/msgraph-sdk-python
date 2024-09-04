from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .detection_status import DetectionStatus
    from .file_details import FileDetails

from .alert_evidence import AlertEvidence

@dataclass
class FileEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.fileEvidence"
    # The status of the detection.The possible values are: detected, blocked, prevented, unknownFutureValue.
    detection_status: Optional[DetectionStatus] = None
    # The file details.
    file_details: Optional[FileDetails] = None
    # A unique identifier assigned to a device by Microsoft Defender for Endpoint.
    mde_device_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .detection_status import DetectionStatus
        from .file_details import FileDetails

        from .alert_evidence import AlertEvidence
        from .detection_status import DetectionStatus
        from .file_details import FileDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "detectionStatus": lambda n : setattr(self, 'detection_status', n.get_enum_value(DetectionStatus)),
            "fileDetails": lambda n : setattr(self, 'file_details', n.get_object_value(FileDetails)),
            "mdeDeviceId": lambda n : setattr(self, 'mde_device_id', n.get_str_value()),
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
        writer.write_enum_value("detectionStatus", self.detection_status)
        writer.write_object_value("fileDetails", self.file_details)
        writer.write_str_value("mdeDeviceId", self.mde_device_id)
    

