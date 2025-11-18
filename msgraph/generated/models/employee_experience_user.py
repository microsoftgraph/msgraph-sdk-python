from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .engagement_role import EngagementRole
    from .entity import Entity
    from .learning_course_activity import LearningCourseActivity

from .entity import Entity

@dataclass
class EmployeeExperienceUser(Entity, Parsable):
    # Represents the collection of Viva Engage roles assigned to a user.
    assigned_roles: Optional[list[EngagementRole]] = None
    # The learningCourseActivities property
    learning_course_activities: Optional[list[LearningCourseActivity]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmployeeExperienceUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmployeeExperienceUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmployeeExperienceUser()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .engagement_role import EngagementRole
        from .entity import Entity
        from .learning_course_activity import LearningCourseActivity

        from .engagement_role import EngagementRole
        from .entity import Entity
        from .learning_course_activity import LearningCourseActivity

        fields: dict[str, Callable[[Any], None]] = {
            "assignedRoles": lambda n : setattr(self, 'assigned_roles', n.get_collection_of_object_values(EngagementRole)),
            "learningCourseActivities": lambda n : setattr(self, 'learning_course_activities', n.get_collection_of_object_values(LearningCourseActivity)),
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
        writer.write_collection_of_object_values("assignedRoles", self.assigned_roles)
        writer.write_collection_of_object_values("learningCourseActivities", self.learning_course_activities)
    

