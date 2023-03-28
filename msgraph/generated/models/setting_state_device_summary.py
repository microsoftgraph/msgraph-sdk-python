from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class SettingStateDeviceSummary(entity.Entity):
    """
    Device Compilance Policy and Configuration for a Setting State summary
    """
    def __init__(self,) -> None:
        """
        Instantiates a new settingStateDeviceSummary and sets the default values.
        """
        super().__init__()
        # Device Compliant count for the setting
        self._compliant_device_count: Optional[int] = None
        # Device conflict error count for the setting
        self._conflict_device_count: Optional[int] = None
        # Device error count for the setting
        self._error_device_count: Optional[int] = None
        # Name of the InstancePath for the setting
        self._instance_path: Optional[str] = None
        # Device NonCompliant count for the setting
        self._non_compliant_device_count: Optional[int] = None
        # Device Not Applicable count for the setting
        self._not_applicable_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Device Compliant count for the setting
        self._remediated_device_count: Optional[int] = None
        # Name of the setting
        self._setting_name: Optional[str] = None
        # Device Unkown count for the setting
        self._unknown_device_count: Optional[int] = None
    
    @property
    def compliant_device_count(self,) -> Optional[int]:
        """
        Gets the compliantDeviceCount property value. Device Compliant count for the setting
        Returns: Optional[int]
        """
        return self._compliant_device_count
    
    @compliant_device_count.setter
    def compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliantDeviceCount property value. Device Compliant count for the setting
        Args:
            value: Value to set for the compliant_device_count property.
        """
        self._compliant_device_count = value
    
    @property
    def conflict_device_count(self,) -> Optional[int]:
        """
        Gets the conflictDeviceCount property value. Device conflict error count for the setting
        Returns: Optional[int]
        """
        return self._conflict_device_count
    
    @conflict_device_count.setter
    def conflict_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the conflictDeviceCount property value. Device conflict error count for the setting
        Args:
            value: Value to set for the conflict_device_count property.
        """
        self._conflict_device_count = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SettingStateDeviceSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SettingStateDeviceSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SettingStateDeviceSummary()
    
    @property
    def error_device_count(self,) -> Optional[int]:
        """
        Gets the errorDeviceCount property value. Device error count for the setting
        Returns: Optional[int]
        """
        return self._error_device_count
    
    @error_device_count.setter
    def error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorDeviceCount property value. Device error count for the setting
        Args:
            value: Value to set for the error_device_count property.
        """
        self._error_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
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
    
    @property
    def instance_path(self,) -> Optional[str]:
        """
        Gets the instancePath property value. Name of the InstancePath for the setting
        Returns: Optional[str]
        """
        return self._instance_path
    
    @instance_path.setter
    def instance_path(self,value: Optional[str] = None) -> None:
        """
        Sets the instancePath property value. Name of the InstancePath for the setting
        Args:
            value: Value to set for the instance_path property.
        """
        self._instance_path = value
    
    @property
    def non_compliant_device_count(self,) -> Optional[int]:
        """
        Gets the nonCompliantDeviceCount property value. Device NonCompliant count for the setting
        Returns: Optional[int]
        """
        return self._non_compliant_device_count
    
    @non_compliant_device_count.setter
    def non_compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the nonCompliantDeviceCount property value. Device NonCompliant count for the setting
        Args:
            value: Value to set for the non_compliant_device_count property.
        """
        self._non_compliant_device_count = value
    
    @property
    def not_applicable_device_count(self,) -> Optional[int]:
        """
        Gets the notApplicableDeviceCount property value. Device Not Applicable count for the setting
        Returns: Optional[int]
        """
        return self._not_applicable_device_count
    
    @not_applicable_device_count.setter
    def not_applicable_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notApplicableDeviceCount property value. Device Not Applicable count for the setting
        Args:
            value: Value to set for the not_applicable_device_count property.
        """
        self._not_applicable_device_count = value
    
    @property
    def remediated_device_count(self,) -> Optional[int]:
        """
        Gets the remediatedDeviceCount property value. Device Compliant count for the setting
        Returns: Optional[int]
        """
        return self._remediated_device_count
    
    @remediated_device_count.setter
    def remediated_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remediatedDeviceCount property value. Device Compliant count for the setting
        Args:
            value: Value to set for the remediated_device_count property.
        """
        self._remediated_device_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. Name of the setting
        Returns: Optional[str]
        """
        return self._setting_name
    
    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. Name of the setting
        Args:
            value: Value to set for the setting_name property.
        """
        self._setting_name = value
    
    @property
    def unknown_device_count(self,) -> Optional[int]:
        """
        Gets the unknownDeviceCount property value. Device Unkown count for the setting
        Returns: Optional[int]
        """
        return self._unknown_device_count
    
    @unknown_device_count.setter
    def unknown_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownDeviceCount property value. Device Unkown count for the setting
        Args:
            value: Value to set for the unknown_device_count property.
        """
        self._unknown_device_count = value
    

