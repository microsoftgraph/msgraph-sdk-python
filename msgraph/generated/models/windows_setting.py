from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_setting_instance import WindowsSettingInstance
    from .windows_setting_type import WindowsSettingType

from .entity import Entity

@dataclass
class WindowsSetting(Entity, Parsable):
    # A collection of setting values for a given windowsSetting.
    instances: Optional[list[WindowsSettingInstance]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of setting payloads contained in the instances navigation property.
    payload_type: Optional[str] = None
    # The settingType property
    setting_type: Optional[WindowsSettingType] = None
    # A unique identifier for the device the setting might belong to if it is of the settingType backup.
    windows_device_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_setting_instance import WindowsSettingInstance
        from .windows_setting_type import WindowsSettingType

        from .entity import Entity
        from .windows_setting_instance import WindowsSettingInstance
        from .windows_setting_type import WindowsSettingType

        fields: dict[str, Callable[[Any], None]] = {
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(WindowsSettingInstance)),
            "payloadType": lambda n : setattr(self, 'payload_type', n.get_str_value()),
            "settingType": lambda n : setattr(self, 'setting_type', n.get_enum_value(WindowsSettingType)),
            "windowsDeviceId": lambda n : setattr(self, 'windows_device_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("instances", self.instances)
        writer.write_str_value("payloadType", self.payload_type)
        writer.write_enum_value("settingType", self.setting_type)
        writer.write_str_value("windowsDeviceId", self.windows_device_id)
    

