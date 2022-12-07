from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

win32_lob_app_file_system_operation_type = lazy_import('msgraph.generated.models.win32_lob_app_file_system_operation_type')
win32_lob_app_rule = lazy_import('msgraph.generated.models.win32_lob_app_rule')
win32_lob_app_rule_operator = lazy_import('msgraph.generated.models.win32_lob_app_rule_operator')

class Win32LobAppFileSystemRule(win32_lob_app_rule.Win32LobAppRule):
    @property
    def check32_bit_on64_system(self,) -> Optional[bool]:
        """
        Gets the check32BitOn64System property value. A value indicating whether to expand environment variables in the 32-bit context on 64-bit systems.
        Returns: Optional[bool]
        """
        return self._check32_bit_on64_system
    
    @check32_bit_on64_system.setter
    def check32_bit_on64_system(self,value: Optional[bool] = None) -> None:
        """
        Sets the check32BitOn64System property value. A value indicating whether to expand environment variables in the 32-bit context on 64-bit systems.
        Args:
            value: Value to set for the check32BitOn64System property.
        """
        self._check32_bit_on64_system = value
    
    @property
    def comparison_value(self,) -> Optional[str]:
        """
        Gets the comparisonValue property value. The file or folder comparison value.
        Returns: Optional[str]
        """
        return self._comparison_value
    
    @comparison_value.setter
    def comparison_value(self,value: Optional[str] = None) -> None:
        """
        Sets the comparisonValue property value. The file or folder comparison value.
        Args:
            value: Value to set for the comparisonValue property.
        """
        self._comparison_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Win32LobAppFileSystemRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.win32LobAppFileSystemRule"
        # A value indicating whether to expand environment variables in the 32-bit context on 64-bit systems.
        self._check32_bit_on64_system: Optional[bool] = None
        # The file or folder comparison value.
        self._comparison_value: Optional[str] = None
        # The file or folder name to look up.
        self._file_or_folder_name: Optional[str] = None
        # Contains all supported file system detection type.
        self._operation_type: Optional[win32_lob_app_file_system_operation_type.Win32LobAppFileSystemOperationType] = None
        # Contains properties for detection operator.
        self._operator: Optional[win32_lob_app_rule_operator.Win32LobAppRuleOperator] = None
        # The file or folder path to look up.
        self._path: Optional[str] = None
    
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
    
    @property
    def file_or_folder_name(self,) -> Optional[str]:
        """
        Gets the fileOrFolderName property value. The file or folder name to look up.
        Returns: Optional[str]
        """
        return self._file_or_folder_name
    
    @file_or_folder_name.setter
    def file_or_folder_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileOrFolderName property value. The file or folder name to look up.
        Args:
            value: Value to set for the fileOrFolderName property.
        """
        self._file_or_folder_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "check32_bit_on64_system": lambda n : setattr(self, 'check32_bit_on64_system', n.get_bool_value()),
            "comparison_value": lambda n : setattr(self, 'comparison_value', n.get_str_value()),
            "file_or_folder_name": lambda n : setattr(self, 'file_or_folder_name', n.get_str_value()),
            "operation_type": lambda n : setattr(self, 'operation_type', n.get_enum_value(win32_lob_app_file_system_operation_type.Win32LobAppFileSystemOperationType)),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(win32_lob_app_rule_operator.Win32LobAppRuleOperator)),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def operation_type(self,) -> Optional[win32_lob_app_file_system_operation_type.Win32LobAppFileSystemOperationType]:
        """
        Gets the operationType property value. Contains all supported file system detection type.
        Returns: Optional[win32_lob_app_file_system_operation_type.Win32LobAppFileSystemOperationType]
        """
        return self._operation_type
    
    @operation_type.setter
    def operation_type(self,value: Optional[win32_lob_app_file_system_operation_type.Win32LobAppFileSystemOperationType] = None) -> None:
        """
        Sets the operationType property value. Contains all supported file system detection type.
        Args:
            value: Value to set for the operationType property.
        """
        self._operation_type = value
    
    @property
    def operator(self,) -> Optional[win32_lob_app_rule_operator.Win32LobAppRuleOperator]:
        """
        Gets the operator property value. Contains properties for detection operator.
        Returns: Optional[win32_lob_app_rule_operator.Win32LobAppRuleOperator]
        """
        return self._operator
    
    @operator.setter
    def operator(self,value: Optional[win32_lob_app_rule_operator.Win32LobAppRuleOperator] = None) -> None:
        """
        Sets the operator property value. Contains properties for detection operator.
        Args:
            value: Value to set for the operator property.
        """
        self._operator = value
    
    @property
    def path(self,) -> Optional[str]:
        """
        Gets the path property value. The file or folder path to look up.
        Returns: Optional[str]
        """
        return self._path
    
    @path.setter
    def path(self,value: Optional[str] = None) -> None:
        """
        Sets the path property value. The file or folder path to look up.
        Args:
            value: Value to set for the path property.
        """
        self._path = value
    
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
    

