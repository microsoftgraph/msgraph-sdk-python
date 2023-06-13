from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_feedback_resource_outcome_status, education_outcome, education_resource

from . import education_outcome

@dataclass
class EducationFeedbackResourceOutcome(education_outcome.EducationOutcome):
    odata_type = "#microsoft.graph.educationFeedbackResourceOutcome"
    # The actual feedback resource.
    feedback_resource: Optional[education_resource.EducationResource] = None
    # The status of the feedback resource. The possible values are: notPublished, pendingPublish, published, failedPublish, unknownFutureValue.
    resource_status: Optional[education_feedback_resource_outcome_status.EducationFeedbackResourceOutcomeStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationFeedbackResourceOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationFeedbackResourceOutcome
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationFeedbackResourceOutcome()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_feedback_resource_outcome_status, education_outcome, education_resource

        fields: Dict[str, Callable[[Any], None]] = {
            "feedbackResource": lambda n : setattr(self, 'feedback_resource', n.get_object_value(education_resource.EducationResource)),
            "resourceStatus": lambda n : setattr(self, 'resource_status', n.get_enum_value(education_feedback_resource_outcome_status.EducationFeedbackResourceOutcomeStatus)),
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
        writer.write_object_value("feedbackResource", self.feedback_resource)
        writer.write_enum_value("resourceStatus", self.resource_status)
    

