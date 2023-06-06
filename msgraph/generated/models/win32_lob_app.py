from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_lob_app, win32_lob_app_install_experience, win32_lob_app_msi_information, win32_lob_app_return_code, win32_lob_app_rule, windows_architecture

from . import mobile_lob_app

@dataclass
class Win32LobApp(mobile_lob_app.MobileLobApp):
    odata_type = "#microsoft.graph.win32LobApp"
    # Contains properties for Windows architecture.
    applicable_architectures: Optional[windows_architecture.WindowsArchitecture] = None
    # The command line to install this app
    install_command_line: Optional[str] = None
    # The install experience for this app.
    install_experience: Optional[win32_lob_app_install_experience.Win32LobAppInstallExperience] = None
    # The value for the minimum CPU speed which is required to install this app.
    minimum_cpu_speed_in_m_hz: Optional[int] = None
    # The value for the minimum free disk space which is required to install this app.
    minimum_free_disk_space_in_m_b: Optional[int] = None
    # The value for the minimum physical memory which is required to install this app.
    minimum_memory_in_m_b: Optional[int] = None
    # The value for the minimum number of processors which is required to install this app.
    minimum_number_of_processors: Optional[int] = None
    # The value for the minimum supported windows release.
    minimum_supported_windows_release: Optional[str] = None
    # The MSI details if this Win32 app is an MSI app.
    msi_information: Optional[win32_lob_app_msi_information.Win32LobAppMsiInformation] = None
    # The return codes for post installation behavior.
    return_codes: Optional[List[win32_lob_app_return_code.Win32LobAppReturnCode]] = None
    # The detection and requirement rules for this app.
    rules: Optional[List[win32_lob_app_rule.Win32LobAppRule]] = None
    # The relative path of the setup file in the encrypted Win32LobApp package.
    setup_file_path: Optional[str] = None
    # The command line to uninstall this app
    uninstall_command_line: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_lob_app, win32_lob_app_install_experience, win32_lob_app_msi_information, win32_lob_app_return_code, win32_lob_app_rule, windows_architecture

        fields: Dict[str, Callable[[Any], None]] = {
            "applicableArchitectures": lambda n : setattr(self, 'applicable_architectures', n.get_enum_value(windows_architecture.WindowsArchitecture)),
            "installCommandLine": lambda n : setattr(self, 'install_command_line', n.get_str_value()),
            "installExperience": lambda n : setattr(self, 'install_experience', n.get_object_value(win32_lob_app_install_experience.Win32LobAppInstallExperience)),
            "minimumCpuSpeedInMHz": lambda n : setattr(self, 'minimum_cpu_speed_in_m_hz', n.get_int_value()),
            "minimumFreeDiskSpaceInMB": lambda n : setattr(self, 'minimum_free_disk_space_in_m_b', n.get_int_value()),
            "minimumMemoryInMB": lambda n : setattr(self, 'minimum_memory_in_m_b', n.get_int_value()),
            "minimumNumberOfProcessors": lambda n : setattr(self, 'minimum_number_of_processors', n.get_int_value()),
            "minimumSupportedWindowsRelease": lambda n : setattr(self, 'minimum_supported_windows_release', n.get_str_value()),
            "msiInformation": lambda n : setattr(self, 'msi_information', n.get_object_value(win32_lob_app_msi_information.Win32LobAppMsiInformation)),
            "returnCodes": lambda n : setattr(self, 'return_codes', n.get_collection_of_object_values(win32_lob_app_return_code.Win32LobAppReturnCode)),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(win32_lob_app_rule.Win32LobAppRule)),
            "setupFilePath": lambda n : setattr(self, 'setup_file_path', n.get_str_value()),
            "uninstallCommandLine": lambda n : setattr(self, 'uninstall_command_line', n.get_str_value()),
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
    

