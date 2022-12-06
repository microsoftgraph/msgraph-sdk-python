from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_configuration_setting_item = lazy_import('msgraph.generated.models.app_configuration_setting_item')
managed_device_mobile_app_configuration = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration')

class IosMobileAppConfiguration(managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new IosMobileAppConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosMobileAppConfiguration"
        # mdm app configuration Base64 binary.
        self._encoded_setting_xml: Optional[bytes] = None
        # app configuration setting items.
        self._settings: Optional[List[app_configuration_setting_item.AppConfigurationSettingItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosMobileAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosMobileAppConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosMobileAppConfiguration()
    
    @property
    def encoded_setting_xml(self,) -> Optional[bytes]:
        """
        Gets the encodedSettingXml property value. mdm app configuration Base64 binary.
        Returns: Optional[bytes]
        """
        return self._encoded_setting_xml
    
    @encoded_setting_xml.setter
    def encoded_setting_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the encodedSettingXml property value. mdm app configuration Base64 binary.
        Args:
            value: Value to set for the encodedSettingXml property.
        """
        self._encoded_setting_xml = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "encoded_setting_xml": lambda n : setattr(self, 'encoded_setting_xml', n.get_bytes_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_collection_of_object_values(app_configuration_setting_item.AppConfigurationSettingItem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("encodedSettingXml", self.encoded_setting_xml)
        writer.write_collection_of_object_values("settings", self.settings)
    
    @property
    def settings(self,) -> Optional[List[app_configuration_setting_item.AppConfigurationSettingItem]]:
        """
        Gets the settings property value. app configuration setting items.
        Returns: Optional[List[app_configuration_setting_item.AppConfigurationSettingItem]]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[List[app_configuration_setting_item.AppConfigurationSettingItem]] = None) -> None:
        """
        Sets the settings property value. app configuration setting items.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

