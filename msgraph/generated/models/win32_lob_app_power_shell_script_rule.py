from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .run_as_account_type import RunAsAccountType
    from .win32_lob_app_power_shell_script_rule_operation_type import Win32LobAppPowerShellScriptRuleOperationType
    from .win32_lob_app_rule import Win32LobAppRule
    from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

from .win32_lob_app_rule import Win32LobAppRule

@dataclass
class Win32LobAppPowerShellScriptRule(Win32LobAppRule, Parsable):
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
    # The execution context of the script. Do not specify this value if the rule is used for detection. Script detection rules will run in the same context as the associated app install context. The possible values are: system, user.
    run_as_account: Optional[RunAsAccountType] = None
    # A value indicating whether the script should run as 32-bit.
    run_as32_bit: Optional[bool] = None
    # The base64-encoded script content.
    script_content: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Win32LobAppPowerShellScriptRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppPowerShellScriptRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Win32LobAppPowerShellScriptRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .run_as_account_type import RunAsAccountType
        from .win32_lob_app_power_shell_script_rule_operation_type import Win32LobAppPowerShellScriptRuleOperationType
        from .win32_lob_app_rule import Win32LobAppRule
        from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

        from .run_as_account_type import RunAsAccountType
        from .win32_lob_app_power_shell_script_rule_operation_type import Win32LobAppPowerShellScriptRuleOperationType
        from .win32_lob_app_rule import Win32LobAppRule
        from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

        fields: dict[str, Callable[[Any], None]] = {
            "comparisonValue": lambda n : setattr(self, 'comparison_value', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforceSignatureCheck": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(Win32LobAppPowerShellScriptRuleOperationType)),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(Win32LobAppRuleOperator)),
            "runAsAccount": lambda n : setattr(self, 'run_as_account', n.get_enum_value(RunAsAccountType)),
            "runAs32Bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "scriptContent": lambda n : setattr(self, 'script_content', n.get_str_value()),
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
        writer.write_str_value("comparisonValue", self.comparison_value)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enforceSignatureCheck", self.enforce_signature_check)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_bool_value("runAs32Bit", self.run_as32_bit)
        writer.write_str_value("scriptContent", self.script_content)
    

