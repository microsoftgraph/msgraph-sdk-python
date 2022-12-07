from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_notification_alert_type = lazy_import('msgraph.generated.models.ios_notification_alert_type')

class IosNotificationSettings(AdditionalDataHolder, Parsable):
    """
    An item describing notification setting.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def alert_type(self,) -> Optional[ios_notification_alert_type.IosNotificationAlertType]:
        """
        Gets the alertType property value. Notification Settings Alert Type.
        Returns: Optional[ios_notification_alert_type.IosNotificationAlertType]
        """
        return self._alert_type
    
    @alert_type.setter
    def alert_type(self,value: Optional[ios_notification_alert_type.IosNotificationAlertType] = None) -> None:
        """
        Sets the alertType property value. Notification Settings Alert Type.
        Args:
            value: Value to set for the alertType property.
        """
        self._alert_type = value
    
    @property
    def app_name(self,) -> Optional[str]:
        """
        Gets the appName property value. Application name to be associated with the bundleID.
        Returns: Optional[str]
        """
        return self._app_name
    
    @app_name.setter
    def app_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appName property value. Application name to be associated with the bundleID.
        Args:
            value: Value to set for the appName property.
        """
        self._app_name = value
    
    @property
    def badges_enabled(self,) -> Optional[bool]:
        """
        Gets the badgesEnabled property value. Indicates whether badges are allowed for this app.
        Returns: Optional[bool]
        """
        return self._badges_enabled
    
    @badges_enabled.setter
    def badges_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the badgesEnabled property value. Indicates whether badges are allowed for this app.
        Args:
            value: Value to set for the badgesEnabled property.
        """
        self._badges_enabled = value
    
    @property
    def bundle_i_d(self,) -> Optional[str]:
        """
        Gets the bundleID property value. Bundle id of app to which to apply these notification settings.
        Returns: Optional[str]
        """
        return self._bundle_i_d
    
    @bundle_i_d.setter
    def bundle_i_d(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleID property value. Bundle id of app to which to apply these notification settings.
        Args:
            value: Value to set for the bundleID property.
        """
        self._bundle_i_d = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new iosNotificationSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Notification Settings Alert Type.
        self._alert_type: Optional[ios_notification_alert_type.IosNotificationAlertType] = None
        # Application name to be associated with the bundleID.
        self._app_name: Optional[str] = None
        # Indicates whether badges are allowed for this app.
        self._badges_enabled: Optional[bool] = None
        # Bundle id of app to which to apply these notification settings.
        self._bundle_i_d: Optional[str] = None
        # Indicates whether notifications are allowed for this app.
        self._enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Publisher to be associated with the bundleID.
        self._publisher: Optional[str] = None
        # Indicates whether notifications can be shown in notification center.
        self._show_in_notification_center: Optional[bool] = None
        # Indicates whether notifications can be shown on the lock screen.
        self._show_on_lock_screen: Optional[bool] = None
        # Indicates whether sounds are allowed for this app.
        self._sounds_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosNotificationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosNotificationSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosNotificationSettings()
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. Indicates whether notifications are allowed for this app.
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. Indicates whether notifications are allowed for this app.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alert_type": lambda n : setattr(self, 'alert_type', n.get_enum_value(ios_notification_alert_type.IosNotificationAlertType)),
            "app_name": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "badges_enabled": lambda n : setattr(self, 'badges_enabled', n.get_bool_value()),
            "bundle_i_d": lambda n : setattr(self, 'bundle_i_d', n.get_str_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "show_in_notification_center": lambda n : setattr(self, 'show_in_notification_center', n.get_bool_value()),
            "show_on_lock_screen": lambda n : setattr(self, 'show_on_lock_screen', n.get_bool_value()),
            "sounds_enabled": lambda n : setattr(self, 'sounds_enabled', n.get_bool_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. Publisher to be associated with the bundleID.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. Publisher to be associated with the bundleID.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def show_in_notification_center(self,) -> Optional[bool]:
        """
        Gets the showInNotificationCenter property value. Indicates whether notifications can be shown in notification center.
        Returns: Optional[bool]
        """
        return self._show_in_notification_center
    
    @show_in_notification_center.setter
    def show_in_notification_center(self,value: Optional[bool] = None) -> None:
        """
        Sets the showInNotificationCenter property value. Indicates whether notifications can be shown in notification center.
        Args:
            value: Value to set for the showInNotificationCenter property.
        """
        self._show_in_notification_center = value
    
    @property
    def show_on_lock_screen(self,) -> Optional[bool]:
        """
        Gets the showOnLockScreen property value. Indicates whether notifications can be shown on the lock screen.
        Returns: Optional[bool]
        """
        return self._show_on_lock_screen
    
    @show_on_lock_screen.setter
    def show_on_lock_screen(self,value: Optional[bool] = None) -> None:
        """
        Sets the showOnLockScreen property value. Indicates whether notifications can be shown on the lock screen.
        Args:
            value: Value to set for the showOnLockScreen property.
        """
        self._show_on_lock_screen = value
    
    @property
    def sounds_enabled(self,) -> Optional[bool]:
        """
        Gets the soundsEnabled property value. Indicates whether sounds are allowed for this app.
        Returns: Optional[bool]
        """
        return self._sounds_enabled
    
    @sounds_enabled.setter
    def sounds_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the soundsEnabled property value. Indicates whether sounds are allowed for this app.
        Args:
            value: Value to set for the soundsEnabled property.
        """
        self._sounds_enabled = value
    

