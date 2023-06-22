from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_feedback_outcome, education_feedback_resource_outcome, education_points_outcome, education_rubric_outcome, entity, identity_set

from . import entity

@dataclass
class EducationOutcome(entity.Entity):
    # The individual who updated the resource.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The moment in time when the resource was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2021 is 2021-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationOutcome
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFeedbackOutcome".casefold():
            from . import education_feedback_outcome

            return education_feedback_outcome.EducationFeedbackOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFeedbackResourceOutcome".casefold():
            from . import education_feedback_resource_outcome

            return education_feedback_resource_outcome.EducationFeedbackResourceOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationPointsOutcome".casefold():
            from . import education_points_outcome

            return education_points_outcome.EducationPointsOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationRubricOutcome".casefold():
            from . import education_rubric_outcome

            return education_rubric_outcome.EducationRubricOutcome()
        return EducationOutcome()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_feedback_outcome, education_feedback_resource_outcome, education_points_outcome, education_rubric_outcome, entity, identity_set

        from . import education_feedback_outcome, education_feedback_resource_outcome, education_points_outcome, education_rubric_outcome, entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

