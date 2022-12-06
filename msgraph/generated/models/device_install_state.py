from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
install_state = lazy_import('msgraph.generated.models.install_state')

class DeviceInstallState(entity.Entity):
    """
    Contains properties for the installation state for a device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceInstallState and sets the default values.
        """
        super().__init__()
        # Device Id.
        self._device_id: Optional[str] = None
        # Device name.
        self._device_name: Optional[str] = None
        # The error code for install failures.
        self._error_code: Optional[str] = None
        # Possible values for install state.
        self._install_state: Optional[install_state.InstallState] = None
        # Last sync date and time.
        self._last_sync_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # OS Description.
        self._os_description: Optional[str] = None
        # OS Version.
        self._os_version: Optional[str] = None
        # Device User Name.
        self._user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceInstallState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceInstallState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceInstallState()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Device Id.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Device Id.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Device name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Device name.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def error_code(self,) -> Optional[str]:
        """
        Gets the errorCode property value. The error code for install failures.
        Returns: Optional[str]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[str] = None) -> None:
        """
        Sets the errorCode property value. The error code for install failures.
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "install_state": lambda n : setattr(self, 'install_state', n.get_enum_value(install_state.InstallState)),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "os_description": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def install_state(self,) -> Optional[install_state.InstallState]:
        """
        Gets the installState property value. Possible values for install state.
        Returns: Optional[install_state.InstallState]
        """
        return self._install_state
    
    @install_state.setter
    def install_state(self,value: Optional[install_state.InstallState] = None) -> None:
        """
        Sets the installState property value. Possible values for install state.
        Args:
            value: Value to set for the installState property.
        """
        self._install_state = value
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. Last sync date and time.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. Last sync date and time.
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def os_description(self,) -> Optional[str]:
        """
        Gets the osDescription property value. OS Description.
        Returns: Optional[str]
        """
        return self._os_description
    
    @os_description.setter
    def os_description(self,value: Optional[str] = None) -> None:
        """
        Sets the osDescription property value. OS Description.
        Args:
            value: Value to set for the osDescription property.
        """
        self._os_description = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. OS Version.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. OS Version.
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_enum_value("installState", self.install_state)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("userName", self.user_name)
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. Device User Name.
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. Device User Name.
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    

