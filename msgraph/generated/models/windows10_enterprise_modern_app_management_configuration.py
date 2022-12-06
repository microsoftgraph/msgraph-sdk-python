from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class Windows10EnterpriseModernAppManagementConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10EnterpriseModernAppManagementConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration"
        # Indicates whether or not to uninstall a fixed list of built-in Windows apps.
        self._uninstall_built_in_apps: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10EnterpriseModernAppManagementConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EnterpriseModernAppManagementConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10EnterpriseModernAppManagementConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "uninstall_built_in_apps": lambda n : setattr(self, 'uninstall_built_in_apps', n.get_bool_value()),
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
        writer.write_bool_value("uninstallBuiltInApps", self.uninstall_built_in_apps)
    
    @property
    def uninstall_built_in_apps(self,) -> Optional[bool]:
        """
        Gets the uninstallBuiltInApps property value. Indicates whether or not to uninstall a fixed list of built-in Windows apps.
        Returns: Optional[bool]
        """
        return self._uninstall_built_in_apps
    
    @uninstall_built_in_apps.setter
    def uninstall_built_in_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the uninstallBuiltInApps property value. Indicates whether or not to uninstall a fixed list of built-in Windows apps.
        Args:
            value: Value to set for the uninstallBuiltInApps property.
        """
        self._uninstall_built_in_apps = value
    

