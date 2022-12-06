from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_assignment_settings = lazy_import('msgraph.generated.models.mobile_app_assignment_settings')

class IosLobAppAssignmentSettings(mobile_app_assignment_settings.MobileAppAssignmentSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new IosLobAppAssignmentSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosLobAppAssignmentSettings"
        # When TRUE, indicates that the app can be uninstalled by the user. When FALSE, indicates that the app cannot be uninstalled by the user. By default, this property is set to null which internally is treated as TRUE.
        self._is_removable: Optional[bool] = None
        # When TRUE, indicates that the app should be uninstalled when the device is removed from Intune. When FALSE, indicates that the app will not be uninstalled when the device is removed from Intune. By default, property is set to null which internally is treated as TRUE.
        self._uninstall_on_device_removal: Optional[bool] = None
        # This is the unique identifier (Id) of the VPN Configuration to apply to the app.
        self._vpn_configuration_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosLobAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosLobAppAssignmentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosLobAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_removable": lambda n : setattr(self, 'is_removable', n.get_bool_value()),
            "uninstall_on_device_removal": lambda n : setattr(self, 'uninstall_on_device_removal', n.get_bool_value()),
            "vpn_configuration_id": lambda n : setattr(self, 'vpn_configuration_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_removable(self,) -> Optional[bool]:
        """
        Gets the isRemovable property value. When TRUE, indicates that the app can be uninstalled by the user. When FALSE, indicates that the app cannot be uninstalled by the user. By default, this property is set to null which internally is treated as TRUE.
        Returns: Optional[bool]
        """
        return self._is_removable
    
    @is_removable.setter
    def is_removable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRemovable property value. When TRUE, indicates that the app can be uninstalled by the user. When FALSE, indicates that the app cannot be uninstalled by the user. By default, this property is set to null which internally is treated as TRUE.
        Args:
            value: Value to set for the isRemovable property.
        """
        self._is_removable = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isRemovable", self.is_removable)
        writer.write_bool_value("uninstallOnDeviceRemoval", self.uninstall_on_device_removal)
        writer.write_str_value("vpnConfigurationId", self.vpn_configuration_id)
    
    @property
    def uninstall_on_device_removal(self,) -> Optional[bool]:
        """
        Gets the uninstallOnDeviceRemoval property value. When TRUE, indicates that the app should be uninstalled when the device is removed from Intune. When FALSE, indicates that the app will not be uninstalled when the device is removed from Intune. By default, property is set to null which internally is treated as TRUE.
        Returns: Optional[bool]
        """
        return self._uninstall_on_device_removal
    
    @uninstall_on_device_removal.setter
    def uninstall_on_device_removal(self,value: Optional[bool] = None) -> None:
        """
        Sets the uninstallOnDeviceRemoval property value. When TRUE, indicates that the app should be uninstalled when the device is removed from Intune. When FALSE, indicates that the app will not be uninstalled when the device is removed from Intune. By default, property is set to null which internally is treated as TRUE.
        Args:
            value: Value to set for the uninstallOnDeviceRemoval property.
        """
        self._uninstall_on_device_removal = value
    
    @property
    def vpn_configuration_id(self,) -> Optional[str]:
        """
        Gets the vpnConfigurationId property value. This is the unique identifier (Id) of the VPN Configuration to apply to the app.
        Returns: Optional[str]
        """
        return self._vpn_configuration_id
    
    @vpn_configuration_id.setter
    def vpn_configuration_id(self,value: Optional[str] = None) -> None:
        """
        Sets the vpnConfigurationId property value. This is the unique identifier (Id) of the VPN Configuration to apply to the app.
        Args:
            value: Value to set for the vpnConfigurationId property.
        """
        self._vpn_configuration_id = value
    

