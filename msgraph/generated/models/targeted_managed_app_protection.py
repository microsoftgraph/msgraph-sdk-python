from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_app_protection import AndroidManagedAppProtection
    from .ios_managed_app_protection import IosManagedAppProtection
    from .managed_app_protection import ManagedAppProtection
    from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

from .managed_app_protection import ManagedAppProtection

@dataclass
class TargetedManagedAppProtection(ManagedAppProtection, Parsable):
    """
    Policy used to configure detailed management settings targeted to specific security groups
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.targetedManagedAppProtection"
    # Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
    assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = None
    # Indicates if the policy is deployed to any inclusion groups or not.
    is_assigned: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TargetedManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TargetedManagedAppProtection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppProtection".casefold():
            from .android_managed_app_protection import AndroidManagedAppProtection

            return AndroidManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppProtection".casefold():
            from .ios_managed_app_protection import IosManagedAppProtection

            return IosManagedAppProtection()
        return TargetedManagedAppProtection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_app_protection import AndroidManagedAppProtection
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_protection import ManagedAppProtection
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

        from .android_managed_app_protection import AndroidManagedAppProtection
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_protection import ManagedAppProtection
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(TargetedManagedAppPolicyAssignment)),
            "isAssigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_bool_value("isAssigned", self.is_assigned)
    

