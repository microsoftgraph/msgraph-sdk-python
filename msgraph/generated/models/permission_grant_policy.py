from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import permission_grant_condition_set, policy_base

from . import policy_base

@dataclass
class PermissionGrantPolicy(policy_base.PolicyBase):
    odata_type = "#microsoft.graph.permissionGrantPolicy"
    # Condition sets which are excluded in this permission grant policy. Automatically expanded on GET.
    excludes: Optional[List[permission_grant_condition_set.PermissionGrantConditionSet]] = None
    # Condition sets which are included in this permission grant policy. Automatically expanded on GET.
    includes: Optional[List[permission_grant_condition_set.PermissionGrantConditionSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PermissionGrantPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PermissionGrantPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PermissionGrantPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import permission_grant_condition_set, policy_base

        from . import permission_grant_condition_set, policy_base

        fields: Dict[str, Callable[[Any], None]] = {
            "excludes": lambda n : setattr(self, 'excludes', n.get_collection_of_object_values(permission_grant_condition_set.PermissionGrantConditionSet)),
            "includes": lambda n : setattr(self, 'includes', n.get_collection_of_object_values(permission_grant_condition_set.PermissionGrantConditionSet)),
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
        writer.write_collection_of_object_values("excludes", self.excludes)
        writer.write_collection_of_object_values("includes", self.includes)
    

