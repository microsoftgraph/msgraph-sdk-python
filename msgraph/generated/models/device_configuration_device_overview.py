from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class DeviceConfigurationDeviceOverview(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new deviceConfigurationDeviceOverview and sets the default values.
        """
        super().__init__()
        # Version of the policy for that overview
        self._configuration_version: Optional[int] = None
        # Number of error devices
        self._error_count: Optional[int] = None
        # Number of failed devices
        self._failed_count: Optional[int] = None
        # Last update time
        self._last_update_date_time: Optional[datetime] = None
        # Number of not applicable devices
        self._not_applicable_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Number of pending devices
        self._pending_count: Optional[int] = None
        # Number of succeeded devices
        self._success_count: Optional[int] = None
    
    @property
    def configuration_version(self,) -> Optional[int]:
        """
        Gets the configurationVersion property value. Version of the policy for that overview
        Returns: Optional[int]
        """
        return self._configuration_version
    
    @configuration_version.setter
    def configuration_version(self,value: Optional[int] = None) -> None:
        """
        Sets the configurationVersion property value. Version of the policy for that overview
        Args:
            value: Value to set for the configuration_version property.
        """
        self._configuration_version = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceConfigurationDeviceOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfigurationDeviceOverview
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceConfigurationDeviceOverview()
    
    @property
    def error_count(self,) -> Optional[int]:
        """
        Gets the errorCount property value. Number of error devices
        Returns: Optional[int]
        """
        return self._error_count
    
    @error_count.setter
    def error_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCount property value. Number of error devices
        Args:
            value: Value to set for the error_count property.
        """
        self._error_count = value
    
    @property
    def failed_count(self,) -> Optional[int]:
        """
        Gets the failedCount property value. Number of failed devices
        Returns: Optional[int]
        """
        return self._failed_count
    
    @failed_count.setter
    def failed_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedCount property value. Number of failed devices
        Args:
            value: Value to set for the failed_count property.
        """
        self._failed_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "configurationVersion": lambda n : setattr(self, 'configuration_version', n.get_int_value()),
            "errorCount": lambda n : setattr(self, 'error_count', n.get_int_value()),
            "failedCount": lambda n : setattr(self, 'failed_count', n.get_int_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "notApplicableCount": lambda n : setattr(self, 'not_applicable_count', n.get_int_value()),
            "pendingCount": lambda n : setattr(self, 'pending_count', n.get_int_value()),
            "successCount": lambda n : setattr(self, 'success_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdateDateTime property value. Last update time
        Returns: Optional[datetime]
        """
        return self._last_update_date_time
    
    @last_update_date_time.setter
    def last_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdateDateTime property value. Last update time
        Args:
            value: Value to set for the last_update_date_time property.
        """
        self._last_update_date_time = value
    
    @property
    def not_applicable_count(self,) -> Optional[int]:
        """
        Gets the notApplicableCount property value. Number of not applicable devices
        Returns: Optional[int]
        """
        return self._not_applicable_count
    
    @not_applicable_count.setter
    def not_applicable_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notApplicableCount property value. Number of not applicable devices
        Args:
            value: Value to set for the not_applicable_count property.
        """
        self._not_applicable_count = value
    
    @property
    def pending_count(self,) -> Optional[int]:
        """
        Gets the pendingCount property value. Number of pending devices
        Returns: Optional[int]
        """
        return self._pending_count
    
    @pending_count.setter
    def pending_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingCount property value. Number of pending devices
        Args:
            value: Value to set for the pending_count property.
        """
        self._pending_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("configurationVersion", self.configuration_version)
        writer.write_int_value("errorCount", self.error_count)
        writer.write_int_value("failedCount", self.failed_count)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_int_value("notApplicableCount", self.not_applicable_count)
        writer.write_int_value("pendingCount", self.pending_count)
        writer.write_int_value("successCount", self.success_count)
    
    @property
    def success_count(self,) -> Optional[int]:
        """
        Gets the successCount property value. Number of succeeded devices
        Returns: Optional[int]
        """
        return self._success_count
    
    @success_count.setter
    def success_count(self,value: Optional[int] = None) -> None:
        """
        Sets the successCount property value. Number of succeeded devices
        Args:
            value: Value to set for the success_count property.
        """
        self._success_count = value
    

