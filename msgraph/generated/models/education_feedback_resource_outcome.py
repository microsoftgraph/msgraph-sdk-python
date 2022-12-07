from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_feedback_resource_outcome_status = lazy_import('msgraph.generated.models.education_feedback_resource_outcome_status')
education_outcome = lazy_import('msgraph.generated.models.education_outcome')
education_resource = lazy_import('msgraph.generated.models.education_resource')

class EducationFeedbackResourceOutcome(education_outcome.EducationOutcome):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationFeedbackResourceOutcome and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationFeedbackResourceOutcome"
        # The actual feedback resource.
        self._feedback_resource: Optional[education_resource.EducationResource] = None
        # The status of the feedback resource. The possible values are: notPublished, pendingPublish, published, failedPublish, unknownFutureValue.
        self._resource_status: Optional[education_feedback_resource_outcome_status.EducationFeedbackResourceOutcomeStatus] = None
    
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
    
    @property
    def feedback_resource(self,) -> Optional[education_resource.EducationResource]:
        """
        Gets the feedbackResource property value. The actual feedback resource.
        Returns: Optional[education_resource.EducationResource]
        """
        return self._feedback_resource
    
    @feedback_resource.setter
    def feedback_resource(self,value: Optional[education_resource.EducationResource] = None) -> None:
        """
        Sets the feedbackResource property value. The actual feedback resource.
        Args:
            value: Value to set for the feedbackResource property.
        """
        self._feedback_resource = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "feedback_resource": lambda n : setattr(self, 'feedback_resource', n.get_object_value(education_resource.EducationResource)),
            "resource_status": lambda n : setattr(self, 'resource_status', n.get_enum_value(education_feedback_resource_outcome_status.EducationFeedbackResourceOutcomeStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource_status(self,) -> Optional[education_feedback_resource_outcome_status.EducationFeedbackResourceOutcomeStatus]:
        """
        Gets the resourceStatus property value. The status of the feedback resource. The possible values are: notPublished, pendingPublish, published, failedPublish, unknownFutureValue.
        Returns: Optional[education_feedback_resource_outcome_status.EducationFeedbackResourceOutcomeStatus]
        """
        return self._resource_status
    
    @resource_status.setter
    def resource_status(self,value: Optional[education_feedback_resource_outcome_status.EducationFeedbackResourceOutcomeStatus] = None) -> None:
        """
        Sets the resourceStatus property value. The status of the feedback resource. The possible values are: notPublished, pendingPublish, published, failedPublish, unknownFutureValue.
        Args:
            value: Value to set for the resourceStatus property.
        """
        self._resource_status = value
    
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
    

