from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_install_state import DeviceInstallState
    from .entity import Entity

from .entity import Entity

@dataclass
class UserInstallStateSummary(Entity):
    """
    Contains properties for the installation state summary for a user.
    """
    # The install state of the eBook.
    device_states: Optional[List[DeviceInstallState]] = None
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
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserInstallStateSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserInstallStateSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_install_state import DeviceInstallState
        from .entity import Entity

        from .device_install_state import DeviceInstallState
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "device_states": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(DeviceInstallState)),
            "failed_device_count": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "installed_device_count": lambda n : setattr(self, 'installed_device_count', n.get_int_value()),
            "not_installed_device_count": lambda n : setattr(self, 'not_installed_device_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("device_states", self.device_states)
        writer.write_int_value("failed_device_count", self.failed_device_count)
        writer.write_int_value("installed_device_count", self.installed_device_count)
        writer.write_int_value("not_installed_device_count", self.not_installed_device_count)
        writer.write_str_value("user_name", self.user_name)
    

