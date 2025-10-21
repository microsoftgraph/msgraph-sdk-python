from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_lob_app import AndroidLobApp
    from .ios_lob_app import IosLobApp
    from .mac_o_s_dmg_app import MacOSDmgApp
    from .mac_o_s_lob_app import MacOSLobApp
    from .mobile_app import MobileApp
    from .mobile_app_content import MobileAppContent
    from .win32_lob_app import Win32LobApp
    from .windows_app_x import WindowsAppX
    from .windows_mobile_m_s_i import WindowsMobileMSI
    from .windows_universal_app_x import WindowsUniversalAppX

from .mobile_app import MobileApp

@dataclass
class MobileLobApp(MobileApp, Parsable):
    """
    An abstract base class containing properties for all mobile line-of-business apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mobileLobApp"
    # The internal committed content version.
    committed_content_version: Optional[str] = None
    # The list of content versions for this app. This property is read-only.
    content_versions: Optional[list[MobileAppContent]] = None
    # The name of the main Lob application file.
    file_name: Optional[str] = None
    # The total size, including all uploaded files. This property is read-only.
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileLobApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidLobApp".casefold():
            from .android_lob_app import AndroidLobApp

            return AndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobApp".casefold():
            from .ios_lob_app import IosLobApp

            return IosLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDmgApp".casefold():
            from .mac_o_s_dmg_app import MacOSDmgApp

            return MacOSDmgApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSLobApp".casefold():
            from .mac_o_s_lob_app import MacOSLobApp

            return MacOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobApp".casefold():
            from .win32_lob_app import Win32LobApp

            return Win32LobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAppX".casefold():
            from .windows_app_x import WindowsAppX

            return WindowsAppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMobileMSI".casefold():
            from .windows_mobile_m_s_i import WindowsMobileMSI

            return WindowsMobileMSI()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUniversalAppX".casefold():
            from .windows_universal_app_x import WindowsUniversalAppX

            return WindowsUniversalAppX()
        return MobileLobApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_lob_app import AndroidLobApp
        from .ios_lob_app import IosLobApp
        from .mac_o_s_dmg_app import MacOSDmgApp
        from .mac_o_s_lob_app import MacOSLobApp
        from .mobile_app import MobileApp
        from .mobile_app_content import MobileAppContent
        from .win32_lob_app import Win32LobApp
        from .windows_app_x import WindowsAppX
        from .windows_mobile_m_s_i import WindowsMobileMSI
        from .windows_universal_app_x import WindowsUniversalAppX

        from .android_lob_app import AndroidLobApp
        from .ios_lob_app import IosLobApp
        from .mac_o_s_dmg_app import MacOSDmgApp
        from .mac_o_s_lob_app import MacOSLobApp
        from .mobile_app import MobileApp
        from .mobile_app_content import MobileAppContent
        from .win32_lob_app import Win32LobApp
        from .windows_app_x import WindowsAppX
        from .windows_mobile_m_s_i import WindowsMobileMSI
        from .windows_universal_app_x import WindowsUniversalAppX

        fields: dict[str, Callable[[Any], None]] = {
            "committedContentVersion": lambda n : setattr(self, 'committed_content_version', n.get_str_value()),
            "contentVersions": lambda n : setattr(self, 'content_versions', n.get_collection_of_object_values(MobileAppContent)),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_str_value("committedContentVersion", self.committed_content_version)
        writer.write_collection_of_object_values("contentVersions", self.content_versions)
        writer.write_str_value("fileName", self.file_name)
    

