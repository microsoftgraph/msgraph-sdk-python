from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import managed_android_lob_app, managed_android_store_app, managed_app_availability, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_lob_app, mobile_app

from . import mobile_app

@dataclass
class ManagedApp(mobile_app.MobileApp):
    odata_type = "#microsoft.graph.managedApp"
    # A managed (MAM) application's availability.
    app_availability: Optional[managed_app_availability.ManagedAppAvailability] = None
    # The Application's version.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidLobApp".casefold():
            from . import managed_android_lob_app

            return managed_android_lob_app.ManagedAndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidStoreApp".casefold():
            from . import managed_android_store_app

            return managed_android_store_app.ManagedAndroidStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSLobApp".casefold():
            from . import managed_i_o_s_lob_app

            return managed_i_o_s_lob_app.ManagedIOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSStoreApp".casefold():
            from . import managed_i_o_s_store_app

            return managed_i_o_s_store_app.ManagedIOSStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedMobileLobApp".casefold():
            from . import managed_mobile_lob_app

            return managed_mobile_lob_app.ManagedMobileLobApp()
        return ManagedApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import managed_android_lob_app, managed_android_store_app, managed_app_availability, managed_i_o_s_lob_app, managed_i_o_s_store_app, managed_mobile_lob_app, mobile_app

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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("appAvailability", self.app_availability)
        writer.write_str_value("version", self.version)
    

