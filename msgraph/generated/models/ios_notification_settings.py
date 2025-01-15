from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_notification_alert_type import IosNotificationAlertType

@dataclass
class IosNotificationSettings(AdditionalDataHolder, BackedModel, Parsable):
    """
    An item describing notification setting.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Notification Settings Alert Type.
    alert_type: Optional[IosNotificationAlertType] = None
    # Application name to be associated with the bundleID.
    app_name: Optional[str] = None
    # Indicates whether badges are allowed for this app.
    badges_enabled: Optional[bool] = None
    # Bundle id of app to which to apply these notification settings.
    bundle_i_d: Optional[str] = None
    # Indicates whether notifications are allowed for this app.
    enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Publisher to be associated with the bundleID.
    publisher: Optional[str] = None
    # Indicates whether notifications can be shown in notification center.
    show_in_notification_center: Optional[bool] = None
    # Indicates whether notifications can be shown on the lock screen.
    show_on_lock_screen: Optional[bool] = None
    # Indicates whether sounds are allowed for this app.
    sounds_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosNotificationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosNotificationSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosNotificationSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ios_notification_alert_type import IosNotificationAlertType

        from .ios_notification_alert_type import IosNotificationAlertType

        fields: dict[str, Callable[[Any], None]] = {
            "alertType": lambda n : setattr(self, 'alert_type', n.get_enum_value(IosNotificationAlertType)),
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "badgesEnabled": lambda n : setattr(self, 'badges_enabled', n.get_bool_value()),
            "bundleID": lambda n : setattr(self, 'bundle_i_d', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "showInNotificationCenter": lambda n : setattr(self, 'show_in_notification_center', n.get_bool_value()),
            "showOnLockScreen": lambda n : setattr(self, 'show_on_lock_screen', n.get_bool_value()),
            "soundsEnabled": lambda n : setattr(self, 'sounds_enabled', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("alertType", self.alert_type)
        writer.write_str_value("appName", self.app_name)
        writer.write_bool_value("badgesEnabled", self.badges_enabled)
        writer.write_str_value("bundleID", self.bundle_i_d)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("publisher", self.publisher)
        writer.write_bool_value("showInNotificationCenter", self.show_in_notification_center)
        writer.write_bool_value("showOnLockScreen", self.show_on_lock_screen)
        writer.write_bool_value("soundsEnabled", self.sounds_enabled)
        writer.write_additional_data_value(self.additional_data)
    

