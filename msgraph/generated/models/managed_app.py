from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .managed_android_lob_app import ManagedAndroidLobApp
    from .managed_android_store_app import ManagedAndroidStoreApp
    from .managed_app_availability import ManagedAppAvailability
    from .managed_i_o_s_lob_app import ManagedIOSLobApp
    from .managed_i_o_s_store_app import ManagedIOSStoreApp
    from .managed_mobile_lob_app import ManagedMobileLobApp
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class ManagedApp(MobileApp):
    """
    Abstract class that contains properties and inherited properties for apps that you can manage with an Intune app protection policy.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.managedApp"
    # A managed (MAM) application's availability.
    app_availability: Optional[ManagedAppAvailability] = None
    # The Application's version.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidLobApp".casefold():
            from .managed_android_lob_app import ManagedAndroidLobApp

            return ManagedAndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidStoreApp".casefold():
            from .managed_android_store_app import ManagedAndroidStoreApp

            return ManagedAndroidStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSLobApp".casefold():
            from .managed_i_o_s_lob_app import ManagedIOSLobApp

            return ManagedIOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSStoreApp".casefold():
            from .managed_i_o_s_store_app import ManagedIOSStoreApp

            return ManagedIOSStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedMobileLobApp".casefold():
            from .managed_mobile_lob_app import ManagedMobileLobApp

            return ManagedMobileLobApp()
        return ManagedApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .managed_android_lob_app import ManagedAndroidLobApp
        from .managed_android_store_app import ManagedAndroidStoreApp
        from .managed_app_availability import ManagedAppAvailability
        from .managed_i_o_s_lob_app import ManagedIOSLobApp
        from .managed_i_o_s_store_app import ManagedIOSStoreApp
        from .managed_mobile_lob_app import ManagedMobileLobApp
        from .mobile_app import MobileApp

        from .managed_android_lob_app import ManagedAndroidLobApp
        from .managed_android_store_app import ManagedAndroidStoreApp
        from .managed_app_availability import ManagedAppAvailability
        from .managed_i_o_s_lob_app import ManagedIOSLobApp
        from .managed_i_o_s_store_app import ManagedIOSStoreApp
        from .managed_mobile_lob_app import ManagedMobileLobApp
        from .mobile_app import MobileApp

        fields: Dict[str, Callable[[Any], None]] = {
            "appAvailability": lambda n : setattr(self, 'app_availability', n.get_enum_value(ManagedAppAvailability)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_enum_value("appAvailability", self.app_availability)
        writer.write_str_value("version", self.version)
    

