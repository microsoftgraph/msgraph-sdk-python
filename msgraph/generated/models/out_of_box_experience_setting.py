from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_device_usage_type import WindowsDeviceUsageType
    from .windows_user_type import WindowsUserType

@dataclass
class OutOfBoxExperienceSetting(AdditionalDataHolder, BackedModel, Parsable):
    """
    The Windows Autopilot Deployment Profile settings used by the device for the out-of-box experience. Supports: $select, $top, $skip. $Search, $orderBy and $filter are not supported.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The deviceUsageType property
    device_usage_type: Optional[WindowsDeviceUsageType] = None
    # When TRUE, the link that allows user to start over with a different account on company sign-in is hidden. When false, the link that allows user to start over with a different account on company sign-in is available. Default value is FALSE.
    escape_link_hidden: Optional[bool] = None
    # When TRUE, EULA is hidden to the end user during OOBE. When FALSE, EULA is shown to the end user during OOBE. Default value is FALSE.
    eula_hidden: Optional[bool] = None
    # When TRUE, the keyboard selection page is hidden to the end user during OOBE if Language and Region are set. When FALSE, the keyboard selection page is skipped during OOBE.
    keyboard_selection_page_skipped: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When TRUE, privacy settings is hidden to the end user during OOBE. When FALSE, privacy settings is shown to the end user during OOBE. Default value is FALSE.
    privacy_settings_hidden: Optional[bool] = None
    # The userType property
    user_type: Optional[WindowsUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutOfBoxExperienceSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutOfBoxExperienceSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutOfBoxExperienceSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_device_usage_type import WindowsDeviceUsageType
        from .windows_user_type import WindowsUserType

        from .windows_device_usage_type import WindowsDeviceUsageType
        from .windows_user_type import WindowsUserType

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceUsageType": lambda n : setattr(self, 'device_usage_type', n.get_enum_value(WindowsDeviceUsageType)),
            "escapeLinkHidden": lambda n : setattr(self, 'escape_link_hidden', n.get_bool_value()),
            "eulaHidden": lambda n : setattr(self, 'eula_hidden', n.get_bool_value()),
            "keyboardSelectionPageSkipped": lambda n : setattr(self, 'keyboard_selection_page_skipped', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "privacySettingsHidden": lambda n : setattr(self, 'privacy_settings_hidden', n.get_bool_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(WindowsUserType)),
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
        writer.write_enum_value("deviceUsageType", self.device_usage_type)
        writer.write_bool_value("escapeLinkHidden", self.escape_link_hidden)
        writer.write_bool_value("eulaHidden", self.eula_hidden)
        writer.write_bool_value("keyboardSelectionPageSkipped", self.keyboard_selection_page_skipped)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("privacySettingsHidden", self.privacy_settings_hidden)
        writer.write_enum_value("userType", self.user_type)
        writer.write_additional_data_value(self.additional_data)
    

