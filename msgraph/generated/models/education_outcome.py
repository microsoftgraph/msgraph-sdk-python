from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_feedback_outcome import EducationFeedbackOutcome
    from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
    from .education_points_outcome import EducationPointsOutcome
    from .education_rubric_outcome import EducationRubricOutcome
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class EducationOutcome(Entity):
    # The individual who updated the resource.
    last_modified_by: Optional[IdentitySet] = None
    # The moment in time when the resource was last modified. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2021 is 2021-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationOutcome
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFeedbackOutcome".casefold():
            from .education_feedback_outcome import EducationFeedbackOutcome

            return EducationFeedbackOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFeedbackResourceOutcome".casefold():
            from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome

            return EducationFeedbackResourceOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationPointsOutcome".casefold():
            from .education_points_outcome import EducationPointsOutcome

            return EducationPointsOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationRubricOutcome".casefold():
            from .education_rubric_outcome import EducationRubricOutcome

            return EducationRubricOutcome()
        return EducationOutcome()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_feedback_outcome import EducationFeedbackOutcome
        from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
        from .education_points_outcome import EducationPointsOutcome
        from .education_rubric_outcome import EducationRubricOutcome
        from .entity import Entity
        from .identity_set import IdentitySet

        from .education_feedback_outcome import EducationFeedbackOutcome
        from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
        from .education_points_outcome import EducationPointsOutcome
        from .education_rubric_outcome import EducationRubricOutcome
        from .entity import Entity
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

