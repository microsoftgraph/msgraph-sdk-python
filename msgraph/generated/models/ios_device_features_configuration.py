from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
    from .ios_home_screen_item import IosHomeScreenItem
    from .ios_home_screen_page import IosHomeScreenPage
    from .ios_notification_settings import IosNotificationSettings

from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase

@dataclass
class IosDeviceFeaturesConfiguration(AppleDeviceFeaturesConfigurationBase, Parsable):
    """
    iOS Device Features Configuration Profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosDeviceFeaturesConfiguration"
    # Asset tag information for the device, displayed on the login window and lock screen.
    asset_tag_template: Optional[str] = None
    # A list of app and folders to appear on the Home Screen Dock. This collection can contain a maximum of 500 elements.
    home_screen_dock_icons: Optional[list[IosHomeScreenItem]] = None
    # A list of pages on the Home Screen. This collection can contain a maximum of 500 elements.
    home_screen_pages: Optional[list[IosHomeScreenPage]] = None
    # A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.
    lock_screen_footnote: Optional[str] = None
    # Notification settings for each bundle id. Applicable to devices in supervised mode only (iOS 9.3 and later). This collection can contain a maximum of 500 elements.
    notification_settings: Optional[list[IosNotificationSettings]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosDeviceFeaturesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosDeviceFeaturesConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosDeviceFeaturesConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .ios_home_screen_item import IosHomeScreenItem
        from .ios_home_screen_page import IosHomeScreenPage
        from .ios_notification_settings import IosNotificationSettings

        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .ios_home_screen_item import IosHomeScreenItem
        from .ios_home_screen_page import IosHomeScreenPage
        from .ios_notification_settings import IosNotificationSettings

        fields: dict[str, Callable[[Any], None]] = {
            "assetTagTemplate": lambda n : setattr(self, 'asset_tag_template', n.get_str_value()),
            "homeScreenDockIcons": lambda n : setattr(self, 'home_screen_dock_icons', n.get_collection_of_object_values(IosHomeScreenItem)),
            "homeScreenPages": lambda n : setattr(self, 'home_screen_pages', n.get_collection_of_object_values(IosHomeScreenPage)),
            "lockScreenFootnote": lambda n : setattr(self, 'lock_screen_footnote', n.get_str_value()),
            "notificationSettings": lambda n : setattr(self, 'notification_settings', n.get_collection_of_object_values(IosNotificationSettings)),
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
        writer.write_str_value("assetTagTemplate", self.asset_tag_template)
        writer.write_collection_of_object_values("homeScreenDockIcons", self.home_screen_dock_icons)
        writer.write_collection_of_object_values("homeScreenPages", self.home_screen_pages)
        writer.write_str_value("lockScreenFootnote", self.lock_screen_footnote)
        writer.write_collection_of_object_values("notificationSettings", self.notification_settings)
    

