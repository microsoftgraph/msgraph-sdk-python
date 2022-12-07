from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

win32_lob_app_registry_rule_operation_type = lazy_import('msgraph.generated.models.win32_lob_app_registry_rule_operation_type')
win32_lob_app_rule = lazy_import('msgraph.generated.models.win32_lob_app_rule')
win32_lob_app_rule_operator = lazy_import('msgraph.generated.models.win32_lob_app_rule_operator')

class Win32LobAppRegistryRule(win32_lob_app_rule.Win32LobAppRule):
    @property
    def check32_bit_on64_system(self,) -> Optional[bool]:
        """
        Gets the check32BitOn64System property value. A value indicating whether to search the 32-bit registry on 64-bit systems.
        Returns: Optional[bool]
        """
        return self._check32_bit_on64_system
    
    @check32_bit_on64_system.setter
    def check32_bit_on64_system(self,value: Optional[bool] = None) -> None:
        """
        Sets the check32BitOn64System property value. A value indicating whether to search the 32-bit registry on 64-bit systems.
        Args:
            value: Value to set for the check32BitOn64System property.
        """
        self._check32_bit_on64_system = value
    
    @property
    def comparison_value(self,) -> Optional[str]:
        """
        Gets the comparisonValue property value. The registry comparison value.
        Returns: Optional[str]
        """
        return self._comparison_value
    
    @comparison_value.setter
    def comparison_value(self,value: Optional[str] = None) -> None:
        """
        Sets the comparisonValue property value. The registry comparison value.
        Args:
            value: Value to set for the comparisonValue property.
        """
        self._comparison_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Win32LobAppRegistryRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.win32LobAppRegistryRule"
        # A value indicating whether to search the 32-bit registry on 64-bit systems.
        self._check32_bit_on64_system: Optional[bool] = None
        # The registry comparison value.
        self._comparison_value: Optional[str] = None
        # The full path of the registry entry containing the value to detect.
        self._key_path: Optional[str] = None
        # Contains all supported registry data detection type.
        self._operation_type: Optional[win32_lob_app_registry_rule_operation_type.Win32LobAppRegistryRuleOperationType] = None
        # Contains properties for detection operator.
        self._operator: Optional[win32_lob_app_rule_operator.Win32LobAppRuleOperator] = None
        # The name of the registry value to detect.
        self._value_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppRegistryRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppRegistryRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppRegistryRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "check32_bit_on64_system": lambda n : setattr(self, 'check32_bit_on64_system', n.get_bool_value()),
            "comparison_value": lambda n : setattr(self, 'comparison_value', n.get_str_value()),
            "key_path": lambda n : setattr(self, 'key_path', n.get_str_value()),
            "operation_type": lambda n : setattr(self, 'operation_type', n.get_enum_value(win32_lob_app_registry_rule_operation_type.Win32LobAppRegistryRuleOperationType)),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(win32_lob_app_rule_operator.Win32LobAppRuleOperator)),
            "value_name": lambda n : setattr(self, 'value_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def key_path(self,) -> Optional[str]:
        """
        Gets the keyPath property value. The full path of the registry entry containing the value to detect.
        Returns: Optional[str]
        """
        return self._key_path
    
    @key_path.setter
    def key_path(self,value: Optional[str] = None) -> None:
        """
        Sets the keyPath property value. The full path of the registry entry containing the value to detect.
        Args:
            value: Value to set for the keyPath property.
        """
        self._key_path = value
    
    @property
    def operation_type(self,) -> Optional[win32_lob_app_registry_rule_operation_type.Win32LobAppRegistryRuleOperationType]:
        """
        Gets the operationType property value. Contains all supported registry data detection type.
        Returns: Optional[win32_lob_app_registry_rule_operation_type.Win32LobAppRegistryRuleOperationType]
        """
        return self._operation_type
    
    @operation_type.setter
    def operation_type(self,value: Optional[win32_lob_app_registry_rule_operation_type.Win32LobAppRegistryRuleOperationType] = None) -> None:
        """
        Sets the operationType property value. Contains all supported registry data detection type.
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
        writer.write_str_value("keyPath", self.key_path)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("valueName", self.value_name)
    
    @property
    def value_name(self,) -> Optional[str]:
        """
        Gets the valueName property value. The name of the registry value to detect.
        Returns: Optional[str]
        """
        return self._value_name
    
    @value_name.setter
    def value_name(self,value: Optional[str] = None) -> None:
        """
        Sets the valueName property value. The name of the registry value to detect.
        Args:
            value: Value to set for the valueName property.
        """
        self._value_name = value
    

