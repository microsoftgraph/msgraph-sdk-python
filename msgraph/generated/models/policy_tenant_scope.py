from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_binding import PolicyBinding
    from .policy_scope_base import PolicyScopeBase

from .policy_scope_base import PolicyScopeBase

@dataclass
class PolicyTenantScope(PolicyScopeBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.policyTenantScope"
    # Specifies the users and groups included in or excluded from this tenant-level policy scope.
    policy_scope: Optional[PolicyBinding] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyTenantScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyTenantScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyTenantScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_binding import PolicyBinding
        from .policy_scope_base import PolicyScopeBase

        from .policy_binding import PolicyBinding
        from .policy_scope_base import PolicyScopeBase

        fields: dict[str, Callable[[Any], None]] = {
            "policyScope": lambda n : setattr(self, 'policy_scope', n.get_object_value(PolicyBinding)),
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
        writer.write_object_value("policyScope", self.policy_scope)
    

