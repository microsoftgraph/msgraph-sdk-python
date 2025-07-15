from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
    from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

from .entity import Entity

@dataclass
class PrivilegedAccessSchedule(Entity, Parsable):
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedAccessSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentSchedule".casefold():
            from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule

            return PrivilegedAccessGroupAssignmentSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilitySchedule".casefold():
            from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

            return PrivilegedAccessGroupEligibilitySchedule()
        return PrivilegedAccessSchedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

        from .entity import Entity
        from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

        fields: dict[str, Callable[[Any], None]] = {
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
    

