from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_expiration_behavior import AccessReviewExpirationBehavior
    from .entitlement_management_schedule import EntitlementManagementSchedule
    from .subject_set import SubjectSet

@dataclass
class AccessPackageAssignmentReviewSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The default decision to apply if the access is not reviewed. The possible values are: keepAccess, removeAccess, acceptAccessRecommendation, unknownFutureValue.
    expiration_behavior: Optional[AccessReviewExpirationBehavior] = None
    # This collection specifies the users who will be the fallback reviewers when the primary reviewers don't respond.
    fallback_reviewers: Optional[list[SubjectSet]] = None
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
    primary_reviewers: Optional[list[SubjectSet]] = None
    # When the first review should start and how often it should recur.
    schedule: Optional[EntitlementManagementSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignmentReviewSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentReviewSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentReviewSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_expiration_behavior import AccessReviewExpirationBehavior
        from .entitlement_management_schedule import EntitlementManagementSchedule
        from .subject_set import SubjectSet

        from .access_review_expiration_behavior import AccessReviewExpirationBehavior
        from .entitlement_management_schedule import EntitlementManagementSchedule
        from .subject_set import SubjectSet

        fields: dict[str, Callable[[Any], None]] = {
            "expirationBehavior": lambda n : setattr(self, 'expiration_behavior', n.get_enum_value(AccessReviewExpirationBehavior)),
            "fallbackReviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(SubjectSet)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "isRecommendationEnabled": lambda n : setattr(self, 'is_recommendation_enabled', n.get_bool_value()),
            "isReviewerJustificationRequired": lambda n : setattr(self, 'is_reviewer_justification_required', n.get_bool_value()),
            "isSelfReview": lambda n : setattr(self, 'is_self_review', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primaryReviewers": lambda n : setattr(self, 'primary_reviewers', n.get_collection_of_object_values(SubjectSet)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(EntitlementManagementSchedule)),
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
    

