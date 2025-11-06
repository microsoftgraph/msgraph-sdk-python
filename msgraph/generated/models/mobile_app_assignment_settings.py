from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_lob_app_assignment_settings import IosLobAppAssignmentSettings
    from .ios_store_app_assignment_settings import IosStoreAppAssignmentSettings
    from .ios_vpp_app_assignment_settings import IosVppAppAssignmentSettings
    from .mac_os_lob_app_assignment_settings import MacOsLobAppAssignmentSettings
    from .microsoft_store_for_business_app_assignment_settings import MicrosoftStoreForBusinessAppAssignmentSettings
    from .win32_lob_app_assignment_settings import Win32LobAppAssignmentSettings
    from .windows_app_x_app_assignment_settings import WindowsAppXAppAssignmentSettings
    from .windows_universal_app_x_app_assignment_settings import WindowsUniversalAppXAppAssignmentSettings

@dataclass
class MobileAppAssignmentSettings(AdditionalDataHolder, BackedModel, Parsable):
    """
    Abstract class to contain properties used to assign a mobile app to a group.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobAppAssignmentSettings".casefold():
            from .ios_lob_app_assignment_settings import IosLobAppAssignmentSettings

            return IosLobAppAssignmentSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosStoreAppAssignmentSettings".casefold():
            from .ios_store_app_assignment_settings import IosStoreAppAssignmentSettings

            return IosStoreAppAssignmentSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppAppAssignmentSettings".casefold():
            from .ios_vpp_app_assignment_settings import IosVppAppAssignmentSettings

            return IosVppAppAssignmentSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOsLobAppAssignmentSettings".casefold():
            from .mac_os_lob_app_assignment_settings import MacOsLobAppAssignmentSettings

            return MacOsLobAppAssignmentSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftStoreForBusinessAppAssignmentSettings".casefold():
            from .microsoft_store_for_business_app_assignment_settings import MicrosoftStoreForBusinessAppAssignmentSettings

            return MicrosoftStoreForBusinessAppAssignmentSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobAppAssignmentSettings".casefold():
            from .win32_lob_app_assignment_settings import Win32LobAppAssignmentSettings

            return Win32LobAppAssignmentSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAppXAppAssignmentSettings".casefold():
            from .windows_app_x_app_assignment_settings import WindowsAppXAppAssignmentSettings

            return WindowsAppXAppAssignmentSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUniversalAppXAppAssignmentSettings".casefold():
            from .windows_universal_app_x_app_assignment_settings import WindowsUniversalAppXAppAssignmentSettings

            return WindowsUniversalAppXAppAssignmentSettings()
        return MobileAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ios_lob_app_assignment_settings import IosLobAppAssignmentSettings
        from .ios_store_app_assignment_settings import IosStoreAppAssignmentSettings
        from .ios_vpp_app_assignment_settings import IosVppAppAssignmentSettings
        from .mac_os_lob_app_assignment_settings import MacOsLobAppAssignmentSettings
        from .microsoft_store_for_business_app_assignment_settings import MicrosoftStoreForBusinessAppAssignmentSettings
        from .win32_lob_app_assignment_settings import Win32LobAppAssignmentSettings
        from .windows_app_x_app_assignment_settings import WindowsAppXAppAssignmentSettings
        from .windows_universal_app_x_app_assignment_settings import WindowsUniversalAppXAppAssignmentSettings

        from .ios_lob_app_assignment_settings import IosLobAppAssignmentSettings
        from .ios_store_app_assignment_settings import IosStoreAppAssignmentSettings
        from .ios_vpp_app_assignment_settings import IosVppAppAssignmentSettings
        from .mac_os_lob_app_assignment_settings import MacOsLobAppAssignmentSettings
        from .microsoft_store_for_business_app_assignment_settings import MicrosoftStoreForBusinessAppAssignmentSettings
        from .win32_lob_app_assignment_settings import Win32LobAppAssignmentSettings
        from .windows_app_x_app_assignment_settings import WindowsAppXAppAssignmentSettings
        from .windows_universal_app_x_app_assignment_settings import WindowsUniversalAppXAppAssignmentSettings

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

