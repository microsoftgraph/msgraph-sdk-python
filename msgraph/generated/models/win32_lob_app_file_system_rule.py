from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_file_system_operation_type import Win32LobAppFileSystemOperationType
    from .win32_lob_app_rule import Win32LobAppRule
    from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

from .win32_lob_app_rule import Win32LobAppRule

@dataclass
class Win32LobAppFileSystemRule(Win32LobAppRule, Parsable):
    """
    A complex type to store file or folder rule data for a Win32 LOB app.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppFileSystemRule"
    # A value indicating whether to expand environment variables in the 32-bit context on 64-bit systems.
    check32_bit_on64_system: Optional[bool] = None
    # The file or folder comparison value.
    comparison_value: Optional[str] = None
    # The file or folder name to look up.
    file_or_folder_name: Optional[str] = None
    # A list of possible operations for rules used to make determinations about an application based on files or folders. Unless noted, can be used with either detection or requirement rules.
    operation_type: Optional[Win32LobAppFileSystemOperationType] = None
    # Contains properties for detection operator.
    operator: Optional[Win32LobAppRuleOperator] = None
    # The file or folder path to look up.
    path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppFileSystemRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppFileSystemRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppFileSystemRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_file_system_operation_type import Win32LobAppFileSystemOperationType
        from .win32_lob_app_rule import Win32LobAppRule
        from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

        from .win32_lob_app_file_system_operation_type import Win32LobAppFileSystemOperationType
        from .win32_lob_app_rule import Win32LobAppRule
        from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

        fields: dict[str, Callable[[Any], None]] = {
            "check32BitOn64System": lambda n : setattr(self, 'check32_bit_on64_system', n.get_bool_value()),
            "comparisonValue": lambda n : setattr(self, 'comparison_value', n.get_str_value()),
            "fileOrFolderName": lambda n : setattr(self, 'file_or_folder_name', n.get_str_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(Win32LobAppFileSystemOperationType)),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(Win32LobAppRuleOperator)),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
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
        writer.write_bool_value("check32BitOn64System", self.check32_bit_on64_system)
        writer.write_str_value("comparisonValue", self.comparison_value)
        writer.write_str_value("fileOrFolderName", self.file_or_folder_name)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("path", self.path)
    

