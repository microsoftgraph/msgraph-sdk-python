from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
    from .access_review_reviewer_scope import AccessReviewReviewerScope

@dataclass
class AccessReviewStageSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicate which decisions will go to the next stage. Can be a subset of Approve, Deny, Recommendation, or NotReviewed. If not provided, all decisions will go to the next stage. Optional.
    decisions_that_will_move_to_next_stage: Optional[list[str]] = None
    # Defines the sequential or parallel order of the stages and depends on the stageId. Only sequential stages are currently supported. For example, if stageId is 2, then dependsOn must be 1. If stageId is 1, don't specify dependsOn. Required if stageId isn't 1.
    depends_on: Optional[list[str]] = None
    # The duration of the stage. Required.  NOTE: The cumulative value of this property across all stages  1. Will override the instanceDurationInDays setting on the accessReviewScheduleDefinition object. 2. Can't exceed the length of one recurrence. That is, if the review recurs weekly, the cumulative durationInDays can't exceed 7.
    duration_in_days: Optional[int] = None
    # If provided, the fallback reviewers are asked to complete a review if the primary reviewers don't exist. For example, if managers are selected as reviewers and a principal under review doesn't have a manager in Microsoft Entra ID, the fallback reviewers are asked to review that principal. NOTE: The value of this property overrides the corresponding setting on the accessReviewScheduleDefinition object.
    fallback_reviewers: Optional[list[AccessReviewReviewerScope]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recommendationInsightSettings property
    recommendation_insight_settings: Optional[list[AccessReviewRecommendationInsightSetting]] = None
    # Indicates whether showing recommendations to reviewers is enabled. Required. NOTE: The value of this property overrides override the corresponding setting on the accessReviewScheduleDefinition object.
    recommendations_enabled: Optional[bool] = None
    # Defines who the reviewers are. If none is specified, the review is a self-review (users review their own access).  For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property overrides the corresponding setting on the accessReviewScheduleDefinition.
    reviewers: Optional[list[AccessReviewReviewerScope]] = None
    # Unique identifier of the accessReviewStageSettings object. The stageId is used by the dependsOn property to indicate the order of the stages. Required.
    stage_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewStageSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewStageSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewStageSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
        from .access_review_reviewer_scope import AccessReviewReviewerScope

        from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
        from .access_review_reviewer_scope import AccessReviewReviewerScope

        fields: dict[str, Callable[[Any], None]] = {
            "decisionsThatWillMoveToNextStage": lambda n : setattr(self, 'decisions_that_will_move_to_next_stage', n.get_collection_of_primitive_values(str)),
            "dependsOn": lambda n : setattr(self, 'depends_on', n.get_collection_of_primitive_values(str)),
            "durationInDays": lambda n : setattr(self, 'duration_in_days', n.get_int_value()),
            "fallbackReviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(AccessReviewReviewerScope)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendationInsightSettings": lambda n : setattr(self, 'recommendation_insight_settings', n.get_collection_of_object_values(AccessReviewRecommendationInsightSetting)),
            "recommendationsEnabled": lambda n : setattr(self, 'recommendations_enabled', n.get_bool_value()),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(AccessReviewReviewerScope)),
            "stageId": lambda n : setattr(self, 'stage_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("decisionsThatWillMoveToNextStage", self.decisions_that_will_move_to_next_stage)
        writer.write_collection_of_primitive_values("dependsOn", self.depends_on)
        writer.write_int_value("durationInDays", self.duration_in_days)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("recommendationInsightSettings", self.recommendation_insight_settings)
        writer.write_bool_value("recommendationsEnabled", self.recommendations_enabled)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_str_value("stageId", self.stage_id)
        writer.write_additional_data_value(self.additional_data)
    

