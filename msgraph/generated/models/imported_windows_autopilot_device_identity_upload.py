from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, imported_windows_autopilot_device_identity, imported_windows_autopilot_device_identity_upload_status

from . import entity

class ImportedWindowsAutopilotDeviceIdentityUpload(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ImportedWindowsAutopilotDeviceIdentityUpload and sets the default values.
        """
        super().__init__()
        # DateTime when the entity is created.
        self._created_date_time_utc: Optional[datetime] = None
        # Collection of all Autopilot devices as a part of this upload.
        self._device_identities: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[imported_windows_autopilot_device_identity_upload_status.ImportedWindowsAutopilotDeviceIdentityUploadStatus] = None
    
    @property
    def created_date_time_utc(self,) -> Optional[datetime]:
        """
        Gets the createdDateTimeUtc property value. DateTime when the entity is created.
        Returns: Optional[datetime]
        """
        return self._created_date_time_utc
    
    @created_date_time_utc.setter
    def created_date_time_utc(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTimeUtc property value. DateTime when the entity is created.
        Args:
            value: Value to set for the created_date_time_utc property.
        """
        self._created_date_time_utc = value
    
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
    
    @property
    def device_identities(self,) -> Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]]:
        """
        Gets the deviceIdentities property value. Collection of all Autopilot devices as a part of this upload.
        Returns: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]]
        """
        return self._device_identities
    
    @device_identities.setter
    def device_identities(self,value: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]] = None) -> None:
        """
        Sets the deviceIdentities property value. Collection of all Autopilot devices as a part of this upload.
        Args:
            value: Value to set for the device_identities property.
        """
        self._device_identities = value
    
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
    
    @property
    def status(self,) -> Optional[imported_windows_autopilot_device_identity_upload_status.ImportedWindowsAutopilotDeviceIdentityUploadStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[imported_windows_autopilot_device_identity_upload_status.ImportedWindowsAutopilotDeviceIdentityUploadStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[imported_windows_autopilot_device_identity_upload_status.ImportedWindowsAutopilotDeviceIdentityUploadStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

