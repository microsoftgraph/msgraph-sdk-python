from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_policy_rule

from . import unified_role_management_policy_rule

class UnifiedRoleManagementPolicyEnablementRule(unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule):
    def __init__(self,) -> None:
        """
        Instantiates a new UnifiedRoleManagementPolicyEnablementRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule"
        # The collection of rules that are enabled for this policy rule. For example, MultiFactorAuthentication, Ticketing, and Justification.
        self._enabled_rules: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyEnablementRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyEnablementRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementPolicyEnablementRule()
    
    @property
    def enabled_rules(self,) -> Optional[List[str]]:
        """
        Gets the enabledRules property value. The collection of rules that are enabled for this policy rule. For example, MultiFactorAuthentication, Ticketing, and Justification.
        Returns: Optional[List[str]]
        """
        return self._enabled_rules
    
    @enabled_rules.setter
    def enabled_rules(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enabledRules property value. The collection of rules that are enabled for this policy rule. For example, MultiFactorAuthentication, Ticketing, and Justification.
        Args:
            value: Value to set for the enabled_rules property.
        """
        self._enabled_rules = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_policy_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "enabledRules": lambda n : setattr(self, 'enabled_rules', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("enabledRules", self.enabled_rules)
    

