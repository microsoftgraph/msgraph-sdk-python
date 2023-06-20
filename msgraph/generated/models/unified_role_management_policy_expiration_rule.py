from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_policy_rule

from . import unified_role_management_policy_rule

@dataclass
class UnifiedRoleManagementPolicyExpirationRule(unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule):
    odata_type = "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule"
    # Indicates whether expiration is required or if it's a permanently active assignment or eligibility.
    is_expiration_required: Optional[bool] = None
    # The maximum duration allowed for eligibility or assignment which is not permanent. Required when isExpirationRequired is true.
    maximum_duration: Optional[timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyExpirationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyExpirationRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementPolicyExpirationRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_policy_rule

        from . import unified_role_management_policy_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "isExpirationRequired": lambda n : setattr(self, 'is_expiration_required', n.get_bool_value()),
            "maximumDuration": lambda n : setattr(self, 'maximum_duration', n.get_timedelta_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("isExpirationRequired", self.is_expiration_required)
        writer.write_timedelta_value("maximumDuration", self.maximum_duration)
    

