from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class SettingStateDeviceSummary(Entity, Parsable):
    """
    Device Compilance Policy and Configuration for a Setting State summary
    """
    # Device Compliant count for the setting
    compliant_device_count: Optional[int] = None
    # Device conflict error count for the setting
    conflict_device_count: Optional[int] = None
    # Device error count for the setting
    error_device_count: Optional[int] = None
    # Name of the InstancePath for the setting
    instance_path: Optional[str] = None
    # Device NonCompliant count for the setting
    non_compliant_device_count: Optional[int] = None
    # Device Not Applicable count for the setting
    not_applicable_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device Compliant count for the setting
    remediated_device_count: Optional[int] = None
    # Name of the setting
    setting_name: Optional[str] = None
    # Device Unkown count for the setting
    unknown_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SettingStateDeviceSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SettingStateDeviceSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SettingStateDeviceSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "compliantDeviceCount": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "conflictDeviceCount": lambda n : setattr(self, 'conflict_device_count', n.get_int_value()),
            "errorDeviceCount": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "instancePath": lambda n : setattr(self, 'instance_path', n.get_str_value()),
            "nonCompliantDeviceCount": lambda n : setattr(self, 'non_compliant_device_count', n.get_int_value()),
            "notApplicableDeviceCount": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "remediatedDeviceCount": lambda n : setattr(self, 'remediated_device_count', n.get_int_value()),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "unknownDeviceCount": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
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
        writer.write_int_value("compliantDeviceCount", self.compliant_device_count)
        writer.write_int_value("conflictDeviceCount", self.conflict_device_count)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_str_value("instancePath", self.instance_path)
        writer.write_int_value("nonCompliantDeviceCount", self.non_compliant_device_count)
        writer.write_int_value("notApplicableDeviceCount", self.not_applicable_device_count)
        writer.write_int_value("remediatedDeviceCount", self.remediated_device_count)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)
    

