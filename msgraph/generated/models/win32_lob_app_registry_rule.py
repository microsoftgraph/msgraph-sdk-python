from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .win32_lob_app_registry_rule_operation_type import Win32LobAppRegistryRuleOperationType
    from .win32_lob_app_rule import Win32LobAppRule
    from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

from .win32_lob_app_rule import Win32LobAppRule

@dataclass
class Win32LobAppRegistryRule(Win32LobAppRule, Parsable):
    """
    A complex type to store registry rule data for a Win32 LOB app.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppRegistryRule"
    # A value indicating whether to search the 32-bit registry on 64-bit systems.
    check32_bit_on64_system: Optional[bool] = None
    # The registry comparison value.
    comparison_value: Optional[str] = None
    # The full path of the registry entry containing the value to detect.
    key_path: Optional[str] = None
    # A list of possible operations for rules used to make determinations about an application based on registry keys or values. Unless noted, the values can be used with either detection or requirement rules.
    operation_type: Optional[Win32LobAppRegistryRuleOperationType] = None
    # Contains properties for detection operator.
    operator: Optional[Win32LobAppRuleOperator] = None
    # The name of the registry value to detect.
    value_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppRegistryRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppRegistryRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppRegistryRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .win32_lob_app_registry_rule_operation_type import Win32LobAppRegistryRuleOperationType
        from .win32_lob_app_rule import Win32LobAppRule
        from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

        from .win32_lob_app_registry_rule_operation_type import Win32LobAppRegistryRuleOperationType
        from .win32_lob_app_rule import Win32LobAppRule
        from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

        fields: dict[str, Callable[[Any], None]] = {
            "check32BitOn64System": lambda n : setattr(self, 'check32_bit_on64_system', n.get_bool_value()),
            "comparisonValue": lambda n : setattr(self, 'comparison_value', n.get_str_value()),
            "keyPath": lambda n : setattr(self, 'key_path', n.get_str_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(Win32LobAppRegistryRuleOperationType)),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(Win32LobAppRuleOperator)),
            "valueName": lambda n : setattr(self, 'value_name', n.get_str_value()),
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
        writer.write_str_value("keyPath", self.key_path)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_str_value("valueName", self.value_name)
    

