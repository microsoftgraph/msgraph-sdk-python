from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .install_state import InstallState

from .entity import Entity

@dataclass
class DeviceInstallState(Entity, Parsable):
    """
    Contains properties for the installation state for a device.
    """
    # Device Id.
    device_id: Optional[str] = None
    # Device name.
    device_name: Optional[str] = None
    # The error code for install failures.
    error_code: Optional[str] = None
    # Possible values for install state.
    install_state: Optional[InstallState] = None
    # Last sync date and time.
    last_sync_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # OS Description.
    os_description: Optional[str] = None
    # OS Version.
    os_version: Optional[str] = None
    # Device User Name.
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceInstallState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceInstallState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceInstallState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .install_state import InstallState

        from .entity import Entity
        from .install_state import InstallState

        fields: dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "installState": lambda n : setattr(self, 'install_state', n.get_enum_value(InstallState)),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "osDescription": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_enum_value("installState", self.install_state)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("userName", self.user_name)
    

