from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_lob_app import MobileLobApp
    from .win32_lob_app_install_experience import Win32LobAppInstallExperience
    from .win32_lob_app_msi_information import Win32LobAppMsiInformation
    from .win32_lob_app_return_code import Win32LobAppReturnCode
    from .win32_lob_app_rule import Win32LobAppRule
    from .windows_architecture import WindowsArchitecture

from .mobile_lob_app import MobileLobApp

@dataclass
class Win32LobApp(MobileLobApp, Parsable):
    """
    Contains properties and inherited properties for Win32 apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobApp"
    # Indicates the Windows architecture(s) this app should be installed on. The app will be treated as not applicable for devices with architectures not matching the selected value. When a non-null value is provided for the allowedArchitectures property, the value of the applicableArchitectures property is set to none. The possible values are: null, x86, x64, arm64. The possible values are: none, x86, x64, arm, neutral.
    allowed_architectures: Optional[WindowsArchitecture] = None
    # Contains properties for Windows architecture.
    applicable_architectures: Optional[WindowsArchitecture] = None
    # Indicates the command line to install this app. Used to install the Win32 app. Example: msiexec /i 'Orca.Msi' /qn.
    install_command_line: Optional[str] = None
    # Indicates the install experience for this app.
    install_experience: Optional[Win32LobAppInstallExperience] = None
    # Indicates the value for the minimum CPU speed which is required to install this app. Allowed range from 0 to clock speed from WMI helper.
    minimum_cpu_speed_in_m_hz: Optional[int] = None
    # Indicates the value for the minimum free disk space which is required to install this app. Allowed range from 0 to driver's maximum available free space.
    minimum_free_disk_space_in_m_b: Optional[int] = None
    # Indicates the value for the minimum physical memory which is required to install this app. Allowed range from 0 to total physical memory from WMI helper.
    minimum_memory_in_m_b: Optional[int] = None
    # Indicates the value for the minimum number of processors which is required to install this app. Minimum value is 0.
    minimum_number_of_processors: Optional[int] = None
    # Indicates the value for the minimum supported windows release. Example: Windows11_23H2.
    minimum_supported_windows_release: Optional[str] = None
    # Indicates the MSI details if this Win32 app is an MSI app.
    msi_information: Optional[Win32LobAppMsiInformation] = None
    # Indicates the return codes for post installation behavior.
    return_codes: Optional[list[Win32LobAppReturnCode]] = None
    # Indicates the detection and requirement rules for this app. The possible values are: Win32LobAppFileSystemRule, Win32LobAppPowerShellScriptRule, Win32LobAppProductCodeRule, Win32LobAppRegistryRule.
    rules: Optional[list[Win32LobAppRule]] = None
    # Indicates the relative path of the setup file in the encrypted Win32LobApp package. Example: Intel-SA-00075 Detection and Mitigation Tool.msi.
    setup_file_path: Optional[str] = None
    # Indicates the command line to uninstall this app. Used to uninstall the app. Example: msiexec /x '{85F4CBCB-9BBC-4B50-A7D8-E1106771498D}' /qn.
    uninstall_command_line: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_lob_app import MobileLobApp
        from .win32_lob_app_install_experience import Win32LobAppInstallExperience
        from .win32_lob_app_msi_information import Win32LobAppMsiInformation
        from .win32_lob_app_return_code import Win32LobAppReturnCode
        from .win32_lob_app_rule import Win32LobAppRule
        from .windows_architecture import WindowsArchitecture

        from .mobile_lob_app import MobileLobApp
        from .win32_lob_app_install_experience import Win32LobAppInstallExperience
        from .win32_lob_app_msi_information import Win32LobAppMsiInformation
        from .win32_lob_app_return_code import Win32LobAppReturnCode
        from .win32_lob_app_rule import Win32LobAppRule
        from .windows_architecture import WindowsArchitecture

        fields: dict[str, Callable[[Any], None]] = {
            "allowedArchitectures": lambda n : setattr(self, 'allowed_architectures', n.get_collection_of_enum_values(WindowsArchitecture)),
            "applicableArchitectures": lambda n : setattr(self, 'applicable_architectures', n.get_collection_of_enum_values(WindowsArchitecture)),
            "installCommandLine": lambda n : setattr(self, 'install_command_line', n.get_str_value()),
            "installExperience": lambda n : setattr(self, 'install_experience', n.get_object_value(Win32LobAppInstallExperience)),
            "minimumCpuSpeedInMHz": lambda n : setattr(self, 'minimum_cpu_speed_in_m_hz', n.get_int_value()),
            "minimumFreeDiskSpaceInMB": lambda n : setattr(self, 'minimum_free_disk_space_in_m_b', n.get_int_value()),
            "minimumMemoryInMB": lambda n : setattr(self, 'minimum_memory_in_m_b', n.get_int_value()),
            "minimumNumberOfProcessors": lambda n : setattr(self, 'minimum_number_of_processors', n.get_int_value()),
            "minimumSupportedWindowsRelease": lambda n : setattr(self, 'minimum_supported_windows_release', n.get_str_value()),
            "msiInformation": lambda n : setattr(self, 'msi_information', n.get_object_value(Win32LobAppMsiInformation)),
            "returnCodes": lambda n : setattr(self, 'return_codes', n.get_collection_of_object_values(Win32LobAppReturnCode)),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(Win32LobAppRule)),
            "setupFilePath": lambda n : setattr(self, 'setup_file_path', n.get_str_value()),
            "uninstallCommandLine": lambda n : setattr(self, 'uninstall_command_line', n.get_str_value()),
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
        writer.write_enum_value("allowedArchitectures", self.allowed_architectures)
        writer.write_enum_value("applicableArchitectures", self.applicable_architectures)
        writer.write_str_value("installCommandLine", self.install_command_line)
        writer.write_object_value("installExperience", self.install_experience)
        writer.write_int_value("minimumCpuSpeedInMHz", self.minimum_cpu_speed_in_m_hz)
        writer.write_int_value("minimumFreeDiskSpaceInMB", self.minimum_free_disk_space_in_m_b)
        writer.write_int_value("minimumMemoryInMB", self.minimum_memory_in_m_b)
        writer.write_int_value("minimumNumberOfProcessors", self.minimum_number_of_processors)
        writer.write_str_value("minimumSupportedWindowsRelease", self.minimum_supported_windows_release)
        writer.write_object_value("msiInformation", self.msi_information)
        writer.write_collection_of_object_values("returnCodes", self.return_codes)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_str_value("setupFilePath", self.setup_file_path)
        writer.write_str_value("uninstallCommandLine", self.uninstall_command_line)
    

