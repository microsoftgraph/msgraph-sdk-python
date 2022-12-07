from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
planner_category_descriptions = lazy_import('msgraph.generated.models.planner_category_descriptions')
planner_user_ids = lazy_import('msgraph.generated.models.planner_user_ids')

class PlannerPlanDetails(entity.Entity):
    @property
    def category_descriptions(self,) -> Optional[planner_category_descriptions.PlannerCategoryDescriptions]:
        """
        Gets the categoryDescriptions property value. An object that specifies the descriptions of the 25 categories that can be associated with tasks in the plan.
        Returns: Optional[planner_category_descriptions.PlannerCategoryDescriptions]
        """
        return self._category_descriptions
    
    @category_descriptions.setter
    def category_descriptions(self,value: Optional[planner_category_descriptions.PlannerCategoryDescriptions] = None) -> None:
        """
        Sets the categoryDescriptions property value. An object that specifies the descriptions of the 25 categories that can be associated with tasks in the plan.
        Args:
            value: Value to set for the categoryDescriptions property.
        """
        self._category_descriptions = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new plannerPlanDetails and sets the default values.
        """
        super().__init__()
        # An object that specifies the descriptions of the 25 categories that can be associated with tasks in the plan.
        self._category_descriptions: Optional[planner_category_descriptions.PlannerCategoryDescriptions] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Set of user IDs that this plan is shared with. If you are leveraging Microsoft 365 groups, use the Groups API to manage group membership to share the group's plan. You can also add existing members of the group to this collection, although it is not required for them to access the plan owned by the group.
        self._shared_with: Optional[planner_user_ids.PlannerUserIds] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerPlanDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerPlanDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "category_descriptions": lambda n : setattr(self, 'category_descriptions', n.get_object_value(planner_category_descriptions.PlannerCategoryDescriptions)),
            "shared_with": lambda n : setattr(self, 'shared_with', n.get_object_value(planner_user_ids.PlannerUserIds)),
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
        writer.write_object_value("categoryDescriptions", self.category_descriptions)
        writer.write_object_value("sharedWith", self.shared_with)
    
    @property
    def shared_with(self,) -> Optional[planner_user_ids.PlannerUserIds]:
        """
        Gets the sharedWith property value. Set of user IDs that this plan is shared with. If you are leveraging Microsoft 365 groups, use the Groups API to manage group membership to share the group's plan. You can also add existing members of the group to this collection, although it is not required for them to access the plan owned by the group.
        Returns: Optional[planner_user_ids.PlannerUserIds]
        """
        return self._shared_with
    
    @shared_with.setter
    def shared_with(self,value: Optional[planner_user_ids.PlannerUserIds] = None) -> None:
        """
        Sets the sharedWith property value. Set of user IDs that this plan is shared with. If you are leveraging Microsoft 365 groups, use the Groups API to manage group membership to share the group's plan. You can also add existing members of the group to this collection, although it is not required for them to access the plan owned by the group.
        Args:
            value: Value to set for the sharedWith property.
        """
        self._shared_with = value
    

