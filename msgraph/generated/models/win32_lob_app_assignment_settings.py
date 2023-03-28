from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app_assignment_settings, mobile_app_install_time_settings, win32_lob_app_delivery_optimization_priority, win32_lob_app_notification, win32_lob_app_restart_settings

from . import mobile_app_assignment_settings

class Win32LobAppAssignmentSettings(mobile_app_assignment_settings.MobileAppAssignmentSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new Win32LobAppAssignmentSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.win32LobAppAssignmentSettings"
        # Contains value for delivery optimization priority.
        self._delivery_optimization_priority: Optional[win32_lob_app_delivery_optimization_priority.Win32LobAppDeliveryOptimizationPriority] = None
        # The install time settings to apply for this app assignment.
        self._install_time_settings: Optional[mobile_app_install_time_settings.MobileAppInstallTimeSettings] = None
        # Contains value for notification status.
        self._notifications: Optional[win32_lob_app_notification.Win32LobAppNotification] = None
        # The reboot settings to apply for this app assignment.
        self._restart_settings: Optional[win32_lob_app_restart_settings.Win32LobAppRestartSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppAssignmentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppAssignmentSettings()
    
    @property
    def delivery_optimization_priority(self,) -> Optional[win32_lob_app_delivery_optimization_priority.Win32LobAppDeliveryOptimizationPriority]:
        """
        Gets the deliveryOptimizationPriority property value. Contains value for delivery optimization priority.
        Returns: Optional[win32_lob_app_delivery_optimization_priority.Win32LobAppDeliveryOptimizationPriority]
        """
        return self._delivery_optimization_priority
    
    @delivery_optimization_priority.setter
    def delivery_optimization_priority(self,value: Optional[win32_lob_app_delivery_optimization_priority.Win32LobAppDeliveryOptimizationPriority] = None) -> None:
        """
        Sets the deliveryOptimizationPriority property value. Contains value for delivery optimization priority.
        Args:
            value: Value to set for the delivery_optimization_priority property.
        """
        self._delivery_optimization_priority = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app_assignment_settings, mobile_app_install_time_settings, win32_lob_app_delivery_optimization_priority, win32_lob_app_notification, win32_lob_app_restart_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "deliveryOptimizationPriority": lambda n : setattr(self, 'delivery_optimization_priority', n.get_enum_value(win32_lob_app_delivery_optimization_priority.Win32LobAppDeliveryOptimizationPriority)),
            "installTimeSettings": lambda n : setattr(self, 'install_time_settings', n.get_object_value(mobile_app_install_time_settings.MobileAppInstallTimeSettings)),
            "notifications": lambda n : setattr(self, 'notifications', n.get_enum_value(win32_lob_app_notification.Win32LobAppNotification)),
            "restartSettings": lambda n : setattr(self, 'restart_settings', n.get_object_value(win32_lob_app_restart_settings.Win32LobAppRestartSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def install_time_settings(self,) -> Optional[mobile_app_install_time_settings.MobileAppInstallTimeSettings]:
        """
        Gets the installTimeSettings property value. The install time settings to apply for this app assignment.
        Returns: Optional[mobile_app_install_time_settings.MobileAppInstallTimeSettings]
        """
        return self._install_time_settings
    
    @install_time_settings.setter
    def install_time_settings(self,value: Optional[mobile_app_install_time_settings.MobileAppInstallTimeSettings] = None) -> None:
        """
        Sets the installTimeSettings property value. The install time settings to apply for this app assignment.
        Args:
            value: Value to set for the install_time_settings property.
        """
        self._install_time_settings = value
    
    @property
    def notifications(self,) -> Optional[win32_lob_app_notification.Win32LobAppNotification]:
        """
        Gets the notifications property value. Contains value for notification status.
        Returns: Optional[win32_lob_app_notification.Win32LobAppNotification]
        """
        return self._notifications
    
    @notifications.setter
    def notifications(self,value: Optional[win32_lob_app_notification.Win32LobAppNotification] = None) -> None:
        """
        Sets the notifications property value. Contains value for notification status.
        Args:
            value: Value to set for the notifications property.
        """
        self._notifications = value
    
    @property
    def restart_settings(self,) -> Optional[win32_lob_app_restart_settings.Win32LobAppRestartSettings]:
        """
        Gets the restartSettings property value. The reboot settings to apply for this app assignment.
        Returns: Optional[win32_lob_app_restart_settings.Win32LobAppRestartSettings]
        """
        return self._restart_settings
    
    @restart_settings.setter
    def restart_settings(self,value: Optional[win32_lob_app_restart_settings.Win32LobAppRestartSettings] = None) -> None:
        """
        Sets the restartSettings property value. The reboot settings to apply for this app assignment.
        Args:
            value: Value to set for the restart_settings property.
        """
        self._restart_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("deliveryOptimizationPriority", self.delivery_optimization_priority)
        writer.write_object_value("installTimeSettings", self.install_time_settings)
        writer.write_enum_value("notifications", self.notifications)
        writer.write_object_value("restartSettings", self.restart_settings)
    

