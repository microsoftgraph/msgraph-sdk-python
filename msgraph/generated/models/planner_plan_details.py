from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, planner_category_descriptions, planner_user_ids

from . import entity

@dataclass
class PlannerPlanDetails(entity.Entity):
    # An object that specifies the descriptions of the 25 categories that can be associated with tasks in the plan.
    category_descriptions: Optional[planner_category_descriptions.PlannerCategoryDescriptions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Set of user IDs that this plan is shared with. If you are leveraging Microsoft 365 groups, use the Groups API to manage group membership to share the group's plan. You can also add existing members of the group to this collection, although it is not required for them to access the plan owned by the group.
    shared_with: Optional[planner_user_ids.PlannerUserIds] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerPlanDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PlannerPlanDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, planner_category_descriptions, planner_user_ids

        from . import entity, planner_category_descriptions, planner_user_ids

        fields: Dict[str, Callable[[Any], None]] = {
            "categoryDescriptions": lambda n : setattr(self, 'category_descriptions', n.get_object_value(planner_category_descriptions.PlannerCategoryDescriptions)),
            "sharedWith": lambda n : setattr(self, 'shared_with', n.get_object_value(planner_user_ids.PlannerUserIds)),
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
        writer.write_object_value("categoryDescriptions", self.category_descriptions)
        writer.write_object_value("sharedWith", self.shared_with)
    

