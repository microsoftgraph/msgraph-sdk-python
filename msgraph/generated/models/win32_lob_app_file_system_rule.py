from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import win32_lob_app_file_system_operation_type, win32_lob_app_rule, win32_lob_app_rule_operator

from . import win32_lob_app_rule

@dataclass
class Win32LobAppFileSystemRule(win32_lob_app_rule.Win32LobAppRule):
    odata_type = "#microsoft.graph.win32LobAppFileSystemRule"
    # A value indicating whether to expand environment variables in the 32-bit context on 64-bit systems.
    check32_bit_on64_system: Optional[bool] = None
    # The file or folder comparison value.
    comparison_value: Optional[str] = None
    # The file or folder name to look up.
    file_or_folder_name: Optional[str] = None
    # Contains all supported file system detection type.
    operation_type: Optional[win32_lob_app_file_system_operation_type.Win32LobAppFileSystemOperationType] = None
    # Contains properties for detection operator.
    operator: Optional[win32_lob_app_rule_operator.Win32LobAppRuleOperator] = None
    # The file or folder path to look up.
    path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppFileSystemRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppFileSystemRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppFileSystemRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import win32_lob_app_file_system_operation_type, win32_lob_app_rule, win32_lob_app_rule_operator

        fields: Dict[str, Callable[[Any], None]] = {
            "check32BitOn64System": lambda n : setattr(self, 'check32_bit_on64_system', n.get_bool_value()),
            "comparisonValue": lambda n : setattr(self, 'comparison_value', n.get_str_value()),
            "fileOrFolderName": lambda n : setattr(self, 'file_or_folder_name', n.get_str_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(win32_lob_app_file_system_operation_type.Win32LobAppFileSystemOperationType)),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(win32_lob_app_rule_operator.Win32LobAppRuleOperator)),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
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
        writer.write_bool_value("check32BitOn64System", self.check32_bit_on64_system)
        writer.write_str_value("comparisonValue", self.comparison_value)
        writer.write_str_value("fileOrFolderName", self.file_or_folder_name)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("path", self.path)
    

