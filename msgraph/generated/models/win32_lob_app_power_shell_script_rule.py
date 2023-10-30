from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .run_as_account_type import RunAsAccountType
    from .win32_lob_app_power_shell_script_rule_operation_type import Win32LobAppPowerShellScriptRuleOperationType
    from .win32_lob_app_rule import Win32LobAppRule
    from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

from .win32_lob_app_rule import Win32LobAppRule

@dataclass
class Win32LobAppPowerShellScriptRule(Win32LobAppRule):
    """
    A complex type to store the PowerShell script rule data for a Win32 LOB app.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.win32LobAppPowerShellScriptRule"
    # The script output comparison value. Do not specify a value if the rule is used for detection.
    comparison_value: Optional[str] = None
    # The display name for the rule. Do not specify this value if the rule is used for detection.
    display_name: Optional[str] = None
    # A value indicating whether a signature check is enforced.
    enforce_signature_check: Optional[bool] = None
    # Contains all supported Powershell Script output detection type.
    operation_type: Optional[Win32LobAppPowerShellScriptRuleOperationType] = None
    # Contains properties for detection operator.
    operator: Optional[Win32LobAppRuleOperator] = None
    # The execution context of the script. Do not specify this value if the rule is used for detection. Script detection rules will run in the same context as the associated app install context. Possible values are: system, user.
    run_as_account: Optional[RunAsAccountType] = None
    # A value indicating whether the script should run as 32-bit.
    run_as32_bit: Optional[bool] = None
    # The base64-encoded script content.
    script_content: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppPowerShellScriptRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppPowerShellScriptRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppPowerShellScriptRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .run_as_account_type import RunAsAccountType
        from .win32_lob_app_power_shell_script_rule_operation_type import Win32LobAppPowerShellScriptRuleOperationType
        from .win32_lob_app_rule import Win32LobAppRule
        from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

        from .run_as_account_type import RunAsAccountType
        from .win32_lob_app_power_shell_script_rule_operation_type import Win32LobAppPowerShellScriptRuleOperationType
        from .win32_lob_app_rule import Win32LobAppRule
        from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

        fields: Dict[str, Callable[[Any], None]] = {
            "comparison_value": lambda n : setattr(self, 'comparison_value', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforce_signature_check": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "operation_type": lambda n : setattr(self, 'operation_type', n.get_enum_value(Win32LobAppPowerShellScriptRuleOperationType)),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(Win32LobAppRuleOperator)),
            "run_as_account": lambda n : setattr(self, 'run_as_account', n.get_enum_value(RunAsAccountType)),
            "run_as32_bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "script_content": lambda n : setattr(self, 'script_content', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("comparison_value", self.comparison_value)
        writer.write_str_value("display_name", self.display_name)
        writer.write_bool_value("enforce_signature_check", self.enforce_signature_check)
        writer.write_enum_value("operation_type", self.operation_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_enum_value("run_as_account", self.run_as_account)
        writer.write_bool_value("run_as32_bit", self.run_as32_bit)
        writer.write_str_value("script_content", self.script_content)
    

