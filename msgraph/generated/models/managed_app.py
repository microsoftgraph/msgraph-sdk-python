from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import managed_android_lob_app, managed_android_store_app, managed_app_availability, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_lob_app, mobile_app

from . import mobile_app

class ManagedApp(mobile_app.MobileApp):
    def __init__(self,) -> None:
        """
        Instantiates a new ManagedApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.managedApp"
        # A managed (MAM) application's availability.
        self._app_availability: Optional[managed_app_availability.ManagedAppAvailability] = None
        # The Application's version.
        self._version: Optional[str] = None
    
    @property
    def app_availability(self,) -> Optional[managed_app_availability.ManagedAppAvailability]:
        """
        Gets the appAvailability property value. A managed (MAM) application's availability.
        Returns: Optional[managed_app_availability.ManagedAppAvailability]
        """
        return self._app_availability
    
    @app_availability.setter
    def app_availability(self,value: Optional[managed_app_availability.ManagedAppAvailability] = None) -> None:
        """
        Sets the appAvailability property value. A managed (MAM) application's availability.
        Args:
            value: Value to set for the app_availability property.
        """
        self._app_availability = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.managedAndroidLobApp":
                from . import managed_android_lob_app

                return managed_android_lob_app.ManagedAndroidLobApp()
            if mapping_value == "#microsoft.graph.managedAndroidStoreApp":
                from . import managed_android_store_app

                return managed_android_store_app.ManagedAndroidStoreApp()
            if mapping_value == "#microsoft.graph.managedIOSLobApp":
                from . import managed_i_o_s_lob_app

                return managed_i_o_s_lob_app.ManagedIOSLobApp()
            if mapping_value == "#microsoft.graph.managedIOSStoreApp":
                from . import managed_i_o_s_store_app

                return managed_i_o_s_store_app.ManagedIOSStoreApp()
            if mapping_value == "#microsoft.graph.managedMobileLobApp":
                from . import managed_mobile_lob_app

                return managed_mobile_lob_app.ManagedMobileLobApp()
        return ManagedApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import managed_android_lob_app, managed_android_store_app, managed_app_availability, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_lob_app, mobile_app

        fields: Dict[str, Callable[[Any], None]] = {
            "appAvailability": lambda n : setattr(self, 'app_availability', n.get_enum_value(managed_app_availability.ManagedAppAvailability)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_enum_value("appAvailability", self.app_availability)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The Application's version.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The Application's version.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

