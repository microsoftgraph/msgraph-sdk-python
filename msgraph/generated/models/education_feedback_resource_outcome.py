from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_feedback_resource_outcome_status import EducationFeedbackResourceOutcomeStatus
    from .education_outcome import EducationOutcome
    from .education_resource import EducationResource

from .education_outcome import EducationOutcome

@dataclass
class EducationFeedbackResourceOutcome(EducationOutcome, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationFeedbackResourceOutcome"
    # The actual feedback resource.
    feedback_resource: Optional[EducationResource] = None
    # The status of the feedback resource. The possible values are: notPublished, pendingPublish, published, failedPublish, unknownFutureValue.
    resource_status: Optional[EducationFeedbackResourceOutcomeStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationFeedbackResourceOutcome:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationFeedbackResourceOutcome
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationFeedbackResourceOutcome()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_feedback_resource_outcome_status import EducationFeedbackResourceOutcomeStatus
        from .education_outcome import EducationOutcome
        from .education_resource import EducationResource

        from .education_feedback_resource_outcome_status import EducationFeedbackResourceOutcomeStatus
        from .education_outcome import EducationOutcome
        from .education_resource import EducationResource

        fields: Dict[str, Callable[[Any], None]] = {
            "feedbackResource": lambda n : setattr(self, 'feedback_resource', n.get_object_value(EducationResource)),
            "resourceStatus": lambda n : setattr(self, 'resource_status', n.get_enum_value(EducationFeedbackResourceOutcomeStatus)),
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
        from .education_feedback_resource_outcome_status import EducationFeedbackResourceOutcomeStatus
        from .education_outcome import EducationOutcome
        from .education_resource import EducationResource

        writer.write_object_value("feedbackResource", self.feedback_resource)
        writer.write_enum_value("resourceStatus", self.resource_status)
    

