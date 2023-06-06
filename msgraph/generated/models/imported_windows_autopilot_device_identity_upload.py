from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, imported_windows_autopilot_device_identity, imported_windows_autopilot_device_identity_upload_status

from . import entity

@dataclass
class ImportedWindowsAutopilotDeviceIdentityUpload(entity.Entity):
    # DateTime when the entity is created.
    created_date_time_utc: Optional[datetime] = None
    # Collection of all Autopilot devices as a part of this upload.
    device_identities: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[imported_windows_autopilot_device_identity_upload_status.ImportedWindowsAutopilotDeviceIdentityUploadStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImportedWindowsAutopilotDeviceIdentityUpload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImportedWindowsAutopilotDeviceIdentityUpload
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImportedWindowsAutopilotDeviceIdentityUpload()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, imported_windows_autopilot_device_identity, imported_windows_autopilot_device_identity_upload_status

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTimeUtc": lambda n : setattr(self, 'created_date_time_utc', n.get_datetime_value()),
            "deviceIdentities": lambda n : setattr(self, 'device_identities', n.get_collection_of_object_values(imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(imported_windows_autopilot_device_identity_upload_status.ImportedWindowsAutopilotDeviceIdentityUploadStatus)),
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
        writer.write_datetime_value("createdDateTimeUtc", self.created_date_time_utc)
        writer.write_collection_of_object_values("deviceIdentities", self.device_identities)
        writer.write_enum_value("status", self.status)
    

