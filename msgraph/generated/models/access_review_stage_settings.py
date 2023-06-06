from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_reviewer_scope

@dataclass
class AccessReviewStageSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Indicate which decisions will go to the next stage. Can be a sub-set of Approve, Deny, Recommendation, or NotReviewed. If not provided, all decisions will go to the next stage. Optional.
    decisions_that_will_move_to_next_stage: Optional[List[str]] = None
    # Defines the sequential or parallel order of the stages and depends on the stageId. Only sequential stages are currently supported. For example, if stageId is 2, then dependsOn must be 1. If stageId is 1, do not specify dependsOn. Required if stageId is not 1.
    depends_on: Optional[List[str]] = None
    # The duration of the stage. Required.  NOTE: The cumulative value of this property across all stages  1. Will override the instanceDurationInDays setting on the accessReviewScheduleDefinition object. 2. Cannot exceed the length of one recurrence. That is, if the review recurs weekly, the cumulative durationInDays cannot exceed 7.
    duration_in_days: Optional[int] = None
    # If provided, the fallback reviewers are asked to complete a review if the primary reviewers do not exist. For example, if managers are selected as reviewers and a principal under review does not have a manager in Azure AD, the fallback reviewers are asked to review that principal. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition object.
    fallback_reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether showing recommendations to reviewers is enabled. Required. NOTE: The value of this property will override override the corresponding setting on the accessReviewScheduleDefinition object.
    recommendations_enabled: Optional[bool] = None
    # Defines who the reviewers are. If none are specified, the review is a self-review (users review their own access).  For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will override the corresponding setting on the accessReviewScheduleDefinition.
    reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
    # Unique identifier of the accessReviewStageSettings object. The stageId will be used by the dependsOn property to indicate the order of the stages. Required.
    stage_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewStageSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewStageSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewStageSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_reviewer_scope

        fields: Dict[str, Callable[[Any], None]] = {
            "decisionsThatWillMoveToNextStage": lambda n : setattr(self, 'decisions_that_will_move_to_next_stage', n.get_collection_of_primitive_values(str)),
            "dependsOn": lambda n : setattr(self, 'depends_on', n.get_collection_of_primitive_values(str)),
            "durationInDays": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
            "fallbackReviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendationsEnabled": lambda n : setattr(self, 'recommendations_enabled', n.get_bool_value()),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "stageId": lambda n : setattr(self, 'stage_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("decisionsThatWillMoveToNextStage", self.decisions_that_will_move_to_next_stage)
        writer.write_collection_of_primitive_values("dependsOn", self.depends_on)
        writer.write_int_value("durationInDays", self.duration_in_days)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("recommendationsEnabled", self.recommendations_enabled)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_str_value("stageId", self.stage_id)
        writer.write_additional_data_value(self.additional_data)
    

