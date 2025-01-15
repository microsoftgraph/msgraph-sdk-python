from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_local_credential import DeviceLocalCredential
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceLocalCredentialInfo(Entity, Parsable):
    # The credentials of the device's local administrator account backed up to Azure Active Directory.
    credentials: Optional[list[DeviceLocalCredential]] = None
    # Display name of the device that the local credentials are associated with.
    device_name: Optional[str] = None
    # When the local administrator account credential was backed up to Azure Active Directory.
    last_backup_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When the local administrator account credential will be refreshed and backed up to Azure Active Directory.
    refresh_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceLocalCredentialInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceLocalCredentialInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceLocalCredentialInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_local_credential import DeviceLocalCredential
        from .entity import Entity

        from .device_local_credential import DeviceLocalCredential
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "credentials": lambda n : setattr(self, 'credentials', n.get_collection_of_object_values(DeviceLocalCredential)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "lastBackupDateTime": lambda n : setattr(self, 'last_backup_date_time', n.get_datetime_value()),
            "refreshDateTime": lambda n : setattr(self, 'refresh_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("credentials", self.credentials)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_datetime_value("lastBackupDateTime", self.last_backup_date_time)
        writer.write_datetime_value("refreshDateTime", self.refresh_date_time)
    

