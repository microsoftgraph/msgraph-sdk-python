from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import win32_lob_app_file_system_rule, win32_lob_app_power_shell_script_rule, win32_lob_app_product_code_rule, win32_lob_app_registry_rule, win32_lob_app_rule_type

@dataclass
class Win32LobAppRule(AdditionalDataHolder, Parsable):
    """
    A base complex type to store the detection or requirement rule data for a Win32 LOB app.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Contains rule types for Win32 LOB apps.
    rule_type: Optional[win32_lob_app_rule_type.Win32LobAppRuleType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.win32LobAppFileSystemRule":
                from . import win32_lob_app_file_system_rule

                return win32_lob_app_file_system_rule.Win32LobAppFileSystemRule()
            if mapping_value == "#microsoft.graph.win32LobAppPowerShellScriptRule":
                from . import win32_lob_app_power_shell_script_rule

                return win32_lob_app_power_shell_script_rule.Win32LobAppPowerShellScriptRule()
            if mapping_value == "#microsoft.graph.win32LobAppProductCodeRule":
                from . import win32_lob_app_product_code_rule

                return win32_lob_app_product_code_rule.Win32LobAppProductCodeRule()
            if mapping_value == "#microsoft.graph.win32LobAppRegistryRule":
                from . import win32_lob_app_registry_rule

                return win32_lob_app_registry_rule.Win32LobAppRegistryRule()
        return Win32LobAppRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import win32_lob_app_file_system_rule, win32_lob_app_power_shell_script_rule, win32_lob_app_product_code_rule, win32_lob_app_registry_rule, win32_lob_app_rule_type

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleType": lambda n : setattr(self, 'rule_type', n.get_enum_value(win32_lob_app_rule_type.Win32LobAppRuleType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ruleType", self.rule_type)
        writer.write_additional_data_value(self.additional_data)
    

