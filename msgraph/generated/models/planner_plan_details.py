from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .planner_category_descriptions import PlannerCategoryDescriptions
    from .planner_user_ids import PlannerUserIds

from .entity import Entity

@dataclass
class PlannerPlanDetails(Entity, Parsable):
    # An object that specifies the descriptions of the 25 categories that can be associated with tasks in the plan.
    category_descriptions: Optional[PlannerCategoryDescriptions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Set of user IDs that this plan is shared with. If you're using Microsoft 365 groups, use the Groups API to manage group membership to share the group's plan. You can also add existing members of the group to this collection, although it isn't required for them to access the plan owned by the group.
    shared_with: Optional[PlannerUserIds] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerPlanDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerPlanDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .planner_category_descriptions import PlannerCategoryDescriptions
        from .planner_user_ids import PlannerUserIds

        from .entity import Entity
        from .planner_category_descriptions import PlannerCategoryDescriptions
        from .planner_user_ids import PlannerUserIds

        fields: dict[str, Callable[[Any], None]] = {
            "categoryDescriptions": lambda n : setattr(self, 'category_descriptions', n.get_object_value(PlannerCategoryDescriptions)),
            "sharedWith": lambda n : setattr(self, 'shared_with', n.get_object_value(PlannerUserIds)),
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
        writer.write_object_value("categoryDescriptions", self.category_descriptions)
        writer.write_object_value("sharedWith", self.shared_with)
    

