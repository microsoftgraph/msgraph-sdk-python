from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

run_as_account_type = lazy_import('msgraph.generated.models.run_as_account_type')
win32_lob_app_power_shell_script_rule_operation_type = lazy_import('msgraph.generated.models.win32_lob_app_power_shell_script_rule_operation_type')
win32_lob_app_rule = lazy_import('msgraph.generated.models.win32_lob_app_rule')
win32_lob_app_rule_operator = lazy_import('msgraph.generated.models.win32_lob_app_rule_operator')

class Win32LobAppPowerShellScriptRule(win32_lob_app_rule.Win32LobAppRule):
    @property
    def comparison_value(self,) -> Optional[str]:
        """
        Gets the comparisonValue property value. The script output comparison value. Do not specify a value if the rule is used for detection.
        Returns: Optional[str]
        """
        return self._comparison_value
    
    @comparison_value.setter
    def comparison_value(self,value: Optional[str] = None) -> None:
        """
        Sets the comparisonValue property value. The script output comparison value. Do not specify a value if the rule is used for detection.
        Args:
            value: Value to set for the comparisonValue property.
        """
        self._comparison_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Win32LobAppPowerShellScriptRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.win32LobAppPowerShellScriptRule"
        # The script output comparison value. Do not specify a value if the rule is used for detection.
        self._comparison_value: Optional[str] = None
        # The display name for the rule. Do not specify this value if the rule is used for detection.
        self._display_name: Optional[str] = None
        # A value indicating whether a signature check is enforced.
        self._enforce_signature_check: Optional[bool] = None
        # Contains all supported Powershell Script output detection type.
        self._operation_type: Optional[win32_lob_app_power_shell_script_rule_operation_type.Win32LobAppPowerShellScriptRuleOperationType] = None
        # Contains properties for detection operator.
        self._operator: Optional[win32_lob_app_rule_operator.Win32LobAppRuleOperator] = None
        # A value indicating whether the script should run as 32-bit.
        self._run_as32_bit: Optional[bool] = None
        # The execution context of the script. Do not specify this value if the rule is used for detection. Script detection rules will run in the same context as the associated app install context. Possible values are: system, user.
        self._run_as_account: Optional[run_as_account_type.RunAsAccountType] = None
        # The base64-encoded script content.
        self._script_content: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobAppPowerShellScriptRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobAppPowerShellScriptRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobAppPowerShellScriptRule()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the rule. Do not specify this value if the rule is used for detection.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the rule. Do not specify this value if the rule is used for detection.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enforce_signature_check(self,) -> Optional[bool]:
        """
        Gets the enforceSignatureCheck property value. A value indicating whether a signature check is enforced.
        Returns: Optional[bool]
        """
        return self._enforce_signature_check
    
    @enforce_signature_check.setter
    def enforce_signature_check(self,value: Optional[bool] = None) -> None:
        """
        Sets the enforceSignatureCheck property value. A value indicating whether a signature check is enforced.
        Args:
            value: Value to set for the enforceSignatureCheck property.
        """
        self._enforce_signature_check = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "comparison_value": lambda n : setattr(self, 'comparison_value', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforce_signature_check": lambda n : setattr(self, 'enforce_signature_check', n.get_bool_value()),
            "operation_type": lambda n : setattr(self, 'operation_type', n.get_enum_value(win32_lob_app_power_shell_script_rule_operation_type.Win32LobAppPowerShellScriptRuleOperationType)),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(win32_lob_app_rule_operator.Win32LobAppRuleOperator)),
            "run_as32_bit": lambda n : setattr(self, 'run_as32_bit', n.get_bool_value()),
            "run_as_account": lambda n : setattr(self, 'run_as_account', n.get_enum_value(run_as_account_type.RunAsAccountType)),
            "script_content": lambda n : setattr(self, 'script_content', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def operation_type(self,) -> Optional[win32_lob_app_power_shell_script_rule_operation_type.Win32LobAppPowerShellScriptRuleOperationType]:
        """
        Gets the operationType property value. Contains all supported Powershell Script output detection type.
        Returns: Optional[win32_lob_app_power_shell_script_rule_operation_type.Win32LobAppPowerShellScriptRuleOperationType]
        """
        return self._operation_type
    
    @operation_type.setter
    def operation_type(self,value: Optional[win32_lob_app_power_shell_script_rule_operation_type.Win32LobAppPowerShellScriptRuleOperationType] = None) -> None:
        """
        Sets the operationType property value. Contains all supported Powershell Script output detection type.
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
    def run_as32_bit(self,) -> Optional[bool]:
        """
        Gets the runAs32Bit property value. A value indicating whether the script should run as 32-bit.
        Returns: Optional[bool]
        """
        return self._run_as32_bit
    
    @run_as32_bit.setter
    def run_as32_bit(self,value: Optional[bool] = None) -> None:
        """
        Sets the runAs32Bit property value. A value indicating whether the script should run as 32-bit.
        Args:
            value: Value to set for the runAs32Bit property.
        """
        self._run_as32_bit = value
    
    @property
    def run_as_account(self,) -> Optional[run_as_account_type.RunAsAccountType]:
        """
        Gets the runAsAccount property value. The execution context of the script. Do not specify this value if the rule is used for detection. Script detection rules will run in the same context as the associated app install context. Possible values are: system, user.
        Returns: Optional[run_as_account_type.RunAsAccountType]
        """
        return self._run_as_account
    
    @run_as_account.setter
    def run_as_account(self,value: Optional[run_as_account_type.RunAsAccountType] = None) -> None:
        """
        Sets the runAsAccount property value. The execution context of the script. Do not specify this value if the rule is used for detection. Script detection rules will run in the same context as the associated app install context. Possible values are: system, user.
        Args:
            value: Value to set for the runAsAccount property.
        """
        self._run_as_account = value
    
    @property
    def script_content(self,) -> Optional[str]:
        """
        Gets the scriptContent property value. The base64-encoded script content.
        Returns: Optional[str]
        """
        return self._script_content
    
    @script_content.setter
    def script_content(self,value: Optional[str] = None) -> None:
        """
        Sets the scriptContent property value. The base64-encoded script content.
        Args:
            value: Value to set for the scriptContent property.
        """
        self._script_content = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("comparisonValue", self.comparison_value)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enforceSignatureCheck", self.enforce_signature_check)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_bool_value("runAs32Bit", self.run_as32_bit)
        writer.write_enum_value("runAsAccount", self.run_as_account)
        writer.write_str_value("scriptContent", self.script_content)
    

