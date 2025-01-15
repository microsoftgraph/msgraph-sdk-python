from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

@dataclass
class UnifiedRoleManagementPolicyExpirationRule(UnifiedRoleManagementPolicyRule, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule"
    # Indicates whether expiration is required or if it's a permanently active assignment or eligibility.
    is_expiration_required: Optional[bool] = None
    # The maximum duration allowed for eligibility or assignment that isn't permanent. Required when isExpirationRequired is true.
    maximum_duration: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleManagementPolicyExpirationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyExpirationRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementPolicyExpirationRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

        fields: dict[str, Callable[[Any], None]] = {
            "isExpirationRequired": lambda n : setattr(self, 'is_expiration_required', n.get_bool_value()),
            "maximumDuration": lambda n : setattr(self, 'maximum_duration', n.get_timedelta_value()),
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
        writer.write_bool_value("isExpirationRequired", self.is_expiration_required)
        writer.write_timedelta_value("maximumDuration", self.maximum_duration)
    

