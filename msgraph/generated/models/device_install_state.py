from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .install_state import InstallState

from .entity import Entity

@dataclass
class DeviceInstallState(Entity):
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceInstallState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceInstallState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceInstallState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .install_state import InstallState

        from .entity import Entity
        from .install_state import InstallState

        fields: Dict[str, Callable[[Any], None]] = {
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "install_state": lambda n : setattr(self, 'install_state', n.get_enum_value(InstallState)),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "os_description": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("device_id", self.device_id)
        writer.write_str_value("device_name", self.device_name)
        writer.write_str_value("error_code", self.error_code)
        writer.write_enum_value("install_state", self.install_state)
        writer.write_datetime_value("last_sync_date_time", self.last_sync_date_time)
        writer.write_str_value("os_description", self.os_description)
        writer.write_str_value("os_version", self.os_version)
        writer.write_str_value("user_name", self.user_name)
    

