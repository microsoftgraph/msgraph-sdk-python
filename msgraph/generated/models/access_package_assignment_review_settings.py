from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_expiration_behavior, entitlement_management_schedule, subject_set

@dataclass
class AccessPackageAssignmentReviewSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The default decision to apply if the access is not reviewed. The possible values are: keepAccess, removeAccess, acceptAccessRecommendation, unknownFutureValue.
    expiration_behavior: Optional[access_review_expiration_behavior.AccessReviewExpirationBehavior] = None
    # This collection specifies the users who will be the fallback reviewers when the primary reviewers don't respond.
    fallback_reviewers: Optional[List[subject_set.SubjectSet]] = None
    # If true, access reviews are required for assignments through this policy.
    is_enabled: Optional[bool] = None
    # Specifies whether to display recommendations to the reviewer. The default value is true.
    is_recommendation_enabled: Optional[bool] = None
    # Specifies whether the reviewer must provide justification for the approval. The default value is true.
    is_reviewer_justification_required: Optional[bool] = None
    # Specifies whether the principals can review their own assignments.
    is_self_review: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This collection specifies the users or group of users who will review the access package assignments.
    primary_reviewers: Optional[List[subject_set.SubjectSet]] = None
    # When the first review should start and how often it should recur.
    schedule: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentReviewSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentReviewSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentReviewSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_expiration_behavior, entitlement_management_schedule, subject_set

        from . import access_review_expiration_behavior, entitlement_management_schedule, subject_set

        fields: Dict[str, Callable[[Any], None]] = {
            "expirationBehavior": lambda n : setattr(self, 'expiration_behavior', n.get_enum_value(access_review_expiration_behavior.AccessReviewExpirationBehavior)),
            "fallbackReviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(subject_set.SubjectSet)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "isRecommendationEnabled": lambda n : setattr(self, 'is_recommendation_enabled', n.get_bool_value()),
            "isReviewerJustificationRequired": lambda n : setattr(self, 'is_reviewer_justification_required', n.get_bool_value()),
            "isSelfReview": lambda n : setattr(self, 'is_self_review', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primaryReviewers": lambda n : setattr(self, 'primary_reviewers', n.get_collection_of_object_values(subject_set.SubjectSet)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(entitlement_management_schedule.EntitlementManagementSchedule)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("expirationBehavior", self.expiration_behavior)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isRecommendationEnabled", self.is_recommendation_enabled)
        writer.write_bool_value("isReviewerJustificationRequired", self.is_reviewer_justification_required)
        writer.write_bool_value("isSelfReview", self.is_self_review)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("primaryReviewers", self.primary_reviewers)
        writer.write_object_value("schedule", self.schedule)
        writer.write_additional_data_value(self.additional_data)
    

