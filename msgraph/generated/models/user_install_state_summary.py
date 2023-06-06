from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_install_state, entity

from . import entity

@dataclass
class UserInstallStateSummary(entity.Entity):
    """
    Contains properties for the installation state summary for a user.
    """
    # The install state of the eBook.
    device_states: Optional[List[device_install_state.DeviceInstallState]] = None
    # Failed Device Count.
    failed_device_count: Optional[int] = None
    # Installed Device Count.
    installed_device_count: Optional[int] = None
    # Not installed device count.
    not_installed_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # User name.
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserInstallStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserInstallStateSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserInstallStateSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_install_state, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceStates": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(device_install_state.DeviceInstallState)),
            "failedDeviceCount": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "installedDeviceCount": lambda n : setattr(self, 'installed_device_count', n.get_int_value()),
            "notInstalledDeviceCount": lambda n : setattr(self, 'not_installed_device_count', n.get_int_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("deviceStates", self.device_states)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_int_value("installedDeviceCount", self.installed_device_count)
        writer.write_int_value("notInstalledDeviceCount", self.not_installed_device_count)
        writer.write_str_value("userName", self.user_name)
    

