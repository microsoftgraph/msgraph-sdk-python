from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings
    from .mobile_app_install_time_settings import MobileAppInstallTimeSettings
    from .win32_lob_app_auto_update_settings import Win32LobAppAutoUpdateSettings
    from .win32_lob_app_delivery_optimization_priority import Win32LobAppDeliveryOptimizationPriority
    from .win32_lob_app_notification import Win32LobAppNotification
    from .win32_lob_app_restart_settings import Win32LobAppRestartSettings

from .mobile_app_assignment_settings import MobileAppAssignmentSettings

@dataclass
class Win32LobAppAssignmentSettings(MobileAppAssignmentSettings, Parsable):
    """
    Contains properties used to assign an Win32 LOB mobile app to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppAssignmentSettings"
    # The auto-update settings to apply for this app assignment.
    auto_update_settings: Optional[Win32LobAppAutoUpdateSettings] = None
    # Contains value for delivery optimization priority.
    delivery_optimization_priority: Optional[Win32LobAppDeliveryOptimizationPriority] = None
    # The install time settings to apply for this app assignment.
    install_time_settings: Optional[MobileAppInstallTimeSettings] = None
    # Contains value for notification status.
    notifications: Optional[Win32LobAppNotification] = None
    # The reboot settings to apply for this app assignment.
    restart_settings: Optional[Win32LobAppRestartSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings
        from .mobile_app_install_time_settings import MobileAppInstallTimeSettings
        from .win32_lob_app_auto_update_settings import Win32LobAppAutoUpdateSettings
        from .win32_lob_app_delivery_optimization_priority import Win32LobAppDeliveryOptimizationPriority
        from .win32_lob_app_notification import Win32LobAppNotification
        from .win32_lob_app_restart_settings import Win32LobAppRestartSettings

        from .mobile_app_assignment_settings import MobileAppAssignmentSettings
        from .mobile_app_install_time_settings import MobileAppInstallTimeSettings
        from .win32_lob_app_auto_update_settings import Win32LobAppAutoUpdateSettings
        from .win32_lob_app_delivery_optimization_priority import Win32LobAppDeliveryOptimizationPriority
        from .win32_lob_app_notification import Win32LobAppNotification
        from .win32_lob_app_restart_settings import Win32LobAppRestartSettings

        fields: dict[str, Callable[[Any], None]] = {
            "autoUpdateSettings": lambda n : setattr(self, 'auto_update_settings', n.get_object_value(Win32LobAppAutoUpdateSettings)),
            "deliveryOptimizationPriority": lambda n : setattr(self, 'delivery_optimization_priority', n.get_enum_value(Win32LobAppDeliveryOptimizationPriority)),
            "installTimeSettings": lambda n : setattr(self, 'install_time_settings', n.get_object_value(MobileAppInstallTimeSettings)),
            "notifications": lambda n : setattr(self, 'notifications', n.get_enum_value(Win32LobAppNotification)),
            "restartSettings": lambda n : setattr(self, 'restart_settings', n.get_object_value(Win32LobAppRestartSettings)),
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
        writer.write_object_value("autoUpdateSettings", self.auto_update_settings)
        writer.write_enum_value("deliveryOptimizationPriority", self.delivery_optimization_priority)
        writer.write_object_value("installTimeSettings", self.install_time_settings)
        writer.write_enum_value("notifications", self.notifications)
        writer.write_object_value("restartSettings", self.restart_settings)
    

