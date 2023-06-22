from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import run_as_account_type, win32_lob_app_restart_behavior

@dataclass
class Win32LobAppInstallExperience(AdditionalDataHolder, Parsable):
    """
    Contains installation experience properties for a Win32 App
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Indicates the type of restart action.
    device_restart_behavior: Optional[win32_lob_app_restart_behavior.Win32LobAppRestartBehavior] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of execution context the app runs in.
    run_as_account: Optional[run_as_account_type.RunAsAccountType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppInstallExperience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppInstallExperience
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppInstallExperience()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import run_as_account_type, win32_lob_app_restart_behavior

        from . import run_as_account_type, win32_lob_app_restart_behavior

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceRestartBehavior": lambda n : setattr(self, 'device_restart_behavior', n.get_enum_value(win32_lob_app_restart_behavior.Win32LobAppRestartBehavior)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "runAsAccount": lambda n : setattr(self, 'run_as_account', n.get_enum_value(run_as_account_type.RunAsAccountType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("deviceRestartBehavior", self.device_restart_behavior)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_additional_data_value(self.additional_data)
    

