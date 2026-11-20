from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_content_script import MobileAppContentScript
    from .win32_lob_app_install_power_shell_script import Win32LobAppInstallPowerShellScript
    from .win32_lob_app_uninstall_power_shell_script import Win32LobAppUninstallPowerShellScript

from .mobile_app_content_script import MobileAppContentScript

@dataclass
class Win32LobAppScript(MobileAppContentScript, Parsable):
    """
    A representation of a script that can be run on an end-user device managed by Intune in relation to a Win32 app.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppScript"
    # Indicates whether or not to enforce a signature check when running the script. When TRUE, the script cannot be run without enforcing a signature check. When FALSE, no signature check will be enforced when running the script. Default value is FALSE.
    enforce_signature_check: Optional[bool] = None
    # Indicates whether the script will run as 32-bit or 64-bit. When TRUE, the script will run as 32-bit. When FALSE, the script will run as 64-bit. Default value is FALSE.
    run_as32_bit: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppScript:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppScript
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if not mapping_value:
            return Win32LobAppScript()
        if mapping_value.casefold() == "#microsoft.graph.win32LobAppInstallPowerShellScript".casefold():
            from .win32_lob_app_install_power_shell_script import Win32LobAppInstallPowerShellScript

            return Win32LobAppInstallPowerShellScript()
        if mapping_value.casefold() == "#microsoft.graph.win32LobAppUninstallPowerShellScript".casefold():
            from .win32_lob_app_uninstall_power_shell_script import Win32LobAppUninstallPowerShellScript

            return Win32LobAppUninstallPowerShellScript()
        return Win32LobAppScript()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_content_script import MobileAppContentScript
        from .win32_lob_app_install_power_shell_script import Win32LobAppInstallPowerShellScript
        from .win32_lob_app_uninstall_power_shell_script import Win32LobAppUninstallPowerShellScript

        from .mobile_app_content_script import MobileAppContentScript
        from .win32_lob_app_install_power_shell_script import Win32LobAppInstallPowerShellScript
        from .win32_lob_app_uninstall_power_shell_script import Win32LobAppUninstallPowerShellScript

        fields: dict[str, Callable[[Any], None]] = {
            "enforceSignatureCheck": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "runAs32Bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
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
        writer.write_bool_value("enforceSignatureCheck", self.enforce_signature_check)
        writer.write_bool_value("runAs32Bit", self.run_as32_bit)
    

