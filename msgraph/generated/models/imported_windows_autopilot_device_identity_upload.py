from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
    from .imported_windows_autopilot_device_identity_upload_status import ImportedWindowsAutopilotDeviceIdentityUploadStatus

from .entity import Entity

@dataclass
class ImportedWindowsAutopilotDeviceIdentityUpload(Entity):
    """
    Import windows autopilot devices using upload.
    """
    # DateTime when the entity is created.
    created_date_time_utc: Optional[datetime.datetime] = None
    # Collection of all Autopilot devices as a part of this upload.
    device_identities: Optional[List[ImportedWindowsAutopilotDeviceIdentity]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[ImportedWindowsAutopilotDeviceIdentityUploadStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImportedWindowsAutopilotDeviceIdentityUpload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImportedWindowsAutopilotDeviceIdentityUpload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImportedWindowsAutopilotDeviceIdentityUpload()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from .imported_windows_autopilot_device_identity_upload_status import ImportedWindowsAutopilotDeviceIdentityUploadStatus

        from .entity import Entity
        from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from .imported_windows_autopilot_device_identity_upload_status import ImportedWindowsAutopilotDeviceIdentityUploadStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTimeUtc": lambda n : setattr(self, 'created_date_time_utc', n.get_datetime_value()),
            "deviceIdentities": lambda n : setattr(self, 'device_identities', n.get_collection_of_object_values(ImportedWindowsAutopilotDeviceIdentity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ImportedWindowsAutopilotDeviceIdentityUploadStatus)),
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
        writer.write_datetime_value("createdDateTimeUtc", self.created_date_time_utc)
        writer.write_collection_of_object_values("deviceIdentities", self.device_identities)
        writer.write_enum_value("status", self.status)
    

