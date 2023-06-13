from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_policy_rule

from . import unified_role_management_policy_rule

@dataclass
class UnifiedRoleManagementPolicyAuthenticationContextRule(unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule):
    odata_type = "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule"
    # The value of the authentication context claim.
    claim_value: Optional[str] = None
    # Whether this rule is enabled.
    is_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyAuthenticationContextRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyAuthenticationContextRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementPolicyAuthenticationContextRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_policy_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "claimValue": lambda n : setattr(self, 'claim_value', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
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
        writer.write_str_value("claimValue", self.claim_value)
        writer.write_bool_value("isEnabled", self.is_enabled)
    

