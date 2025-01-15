from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .permission_grant_condition_set import PermissionGrantConditionSet
    from .policy_base import PolicyBase

from .policy_base import PolicyBase

@dataclass
class PermissionGrantPolicy(PolicyBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.permissionGrantPolicy"
    # Condition sets that are excluded in this permission grant policy. Automatically expanded on GET.
    excludes: Optional[list[PermissionGrantConditionSet]] = None
    # Condition sets that are included in this permission grant policy. Automatically expanded on GET.
    includes: Optional[list[PermissionGrantConditionSet]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PermissionGrantPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionGrantPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PermissionGrantPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .permission_grant_condition_set import PermissionGrantConditionSet
        from .policy_base import PolicyBase

        from .permission_grant_condition_set import PermissionGrantConditionSet
        from .policy_base import PolicyBase

        fields: dict[str, Callable[[Any], None]] = {
            "excludes": lambda n : setattr(self, 'excludes', n.get_collection_of_object_values(PermissionGrantConditionSet)),
            "includes": lambda n : setattr(self, 'includes', n.get_collection_of_object_values(PermissionGrantConditionSet)),
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
        writer.write_collection_of_object_values("excludes", self.excludes)
        writer.write_collection_of_object_values("includes", self.includes)
    

