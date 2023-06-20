from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_lob_app, ios_lob_app, mac_o_s_lob_app, mobile_app, mobile_app_content, win32_lob_app, windows_app_x, windows_mobile_m_s_i, windows_universal_app_x

from . import mobile_app

@dataclass
class MobileLobApp(mobile_app.MobileApp):
    odata_type = "#microsoft.graph.mobileLobApp"
    # The internal committed content version.
    committed_content_version: Optional[str] = None
    # The list of content versions for this app.
    content_versions: Optional[List[mobile_app_content.MobileAppContent]] = None
    # The name of the main Lob application file.
    file_name: Optional[str] = None
    # The total size, including all uploaded files.
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileLobApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidLobApp".casefold():
            from . import android_lob_app

            return android_lob_app.AndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobApp".casefold():
            from . import ios_lob_app

            return ios_lob_app.IosLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSLobApp".casefold():
            from . import mac_o_s_lob_app

            return mac_o_s_lob_app.MacOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobApp".casefold():
            from . import win32_lob_app

            return win32_lob_app.Win32LobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAppX".casefold():
            from . import windows_app_x

            return windows_app_x.WindowsAppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMobileMSI".casefold():
            from . import windows_mobile_m_s_i

            return windows_mobile_m_s_i.WindowsMobileMSI()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUniversalAppX".casefold():
            from . import windows_universal_app_x

            return windows_universal_app_x.WindowsUniversalAppX()
        return MobileLobApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_lob_app, ios_lob_app, mac_o_s_lob_app, mobile_app, mobile_app_content, win32_lob_app, windows_app_x, windows_mobile_m_s_i, windows_universal_app_x

        from . import android_lob_app, ios_lob_app, mac_o_s_lob_app, mobile_app, mobile_app_content, win32_lob_app, windows_app_x, windows_mobile_m_s_i, windows_universal_app_x

        fields: Dict[str, Callable[[Any], None]] = {
            "committedContentVersion": lambda n : setattr(self, 'committed_content_version', n.get_str_value()),
            "contentVersions": lambda n : setattr(self, 'content_versions', n.get_collection_of_object_values(mobile_app_content.MobileAppContent)),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_str_value("committedContentVersion", self.committed_content_version)
        writer.write_collection_of_object_values("contentVersions", self.content_versions)
        writer.write_str_value("fileName", self.file_name)
        writer.write_int_value("size", self.size)
    

