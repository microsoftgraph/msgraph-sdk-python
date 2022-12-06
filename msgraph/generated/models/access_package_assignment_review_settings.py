from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_expiration_behavior = lazy_import('msgraph.generated.models.access_review_expiration_behavior')
entitlement_management_schedule = lazy_import('msgraph.generated.models.entitlement_management_schedule')
subject_set = lazy_import('msgraph.generated.models.subject_set')

class AccessPackageAssignmentReviewSettings(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignmentReviewSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The default decision to apply if the access is not reviewed. The possible values are: keepAccess, removeAccess, acceptAccessRecommendation, unknownFutureValue.
        self._expiration_behavior: Optional[access_review_expiration_behavior.AccessReviewExpirationBehavior] = None
        # This collection specifies the users who will be the fallback reviewers when the primary reviewers don't respond.
        self._fallback_reviewers: Optional[List[subject_set.SubjectSet]] = None
        # If true, access reviews are required for assignments through this policy.
        self._is_enabled: Optional[bool] = None
        # Specifies whether to display recommendations to the reviewer. The default value is true.
        self._is_recommendation_enabled: Optional[bool] = None
        # Specifies whether the reviewer must provide justification for the approval. The default value is true.
        self._is_reviewer_justification_required: Optional[bool] = None
        # Specifies whether the principals can review their own assignments.
        self._is_self_review: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # This collection specifies the users or group of users who will review the access package assignments.
        self._primary_reviewers: Optional[List[subject_set.SubjectSet]] = None
        # When the first review should start and how often it should recur.
        self._schedule: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentReviewSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentReviewSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentReviewSettings()
    
    @property
    def expiration_behavior(self,) -> Optional[access_review_expiration_behavior.AccessReviewExpirationBehavior]:
        """
        Gets the expirationBehavior property value. The default decision to apply if the access is not reviewed. The possible values are: keepAccess, removeAccess, acceptAccessRecommendation, unknownFutureValue.
        Returns: Optional[access_review_expiration_behavior.AccessReviewExpirationBehavior]
        """
        return self._expiration_behavior
    
    @expiration_behavior.setter
    def expiration_behavior(self,value: Optional[access_review_expiration_behavior.AccessReviewExpirationBehavior] = None) -> None:
        """
        Sets the expirationBehavior property value. The default decision to apply if the access is not reviewed. The possible values are: keepAccess, removeAccess, acceptAccessRecommendation, unknownFutureValue.
        Args:
            value: Value to set for the expirationBehavior property.
        """
        self._expiration_behavior = value
    
    @property
    def fallback_reviewers(self,) -> Optional[List[subject_set.SubjectSet]]:
        """
        Gets the fallbackReviewers property value. This collection specifies the users who will be the fallback reviewers when the primary reviewers don't respond.
        Returns: Optional[List[subject_set.SubjectSet]]
        """
        return self._fallback_reviewers
    
    @fallback_reviewers.setter
    def fallback_reviewers(self,value: Optional[List[subject_set.SubjectSet]] = None) -> None:
        """
        Sets the fallbackReviewers property value. This collection specifies the users who will be the fallback reviewers when the primary reviewers don't respond.
        Args:
            value: Value to set for the fallbackReviewers property.
        """
        self._fallback_reviewers = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiration_behavior": lambda n : setattr(self, 'expiration_behavior', n.get_enum_value(access_review_expiration_behavior.AccessReviewExpirationBehavior)),
            "fallback_reviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(subject_set.SubjectSet)),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "is_recommendation_enabled": lambda n : setattr(self, 'is_recommendation_enabled', n.get_bool_value()),
            "is_reviewer_justification_required": lambda n : setattr(self, 'is_reviewer_justification_required', n.get_bool_value()),
            "is_self_review": lambda n : setattr(self, 'is_self_review', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primary_reviewers": lambda n : setattr(self, 'primary_reviewers', n.get_collection_of_object_values(subject_set.SubjectSet)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(entitlement_management_schedule.EntitlementManagementSchedule)),
        }
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. If true, access reviews are required for assignments through this policy.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. If true, access reviews are required for assignments through this policy.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def is_recommendation_enabled(self,) -> Optional[bool]:
        """
        Gets the isRecommendationEnabled property value. Specifies whether to display recommendations to the reviewer. The default value is true.
        Returns: Optional[bool]
        """
        return self._is_recommendation_enabled
    
    @is_recommendation_enabled.setter
    def is_recommendation_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRecommendationEnabled property value. Specifies whether to display recommendations to the reviewer. The default value is true.
        Args:
            value: Value to set for the isRecommendationEnabled property.
        """
        self._is_recommendation_enabled = value
    
    @property
    def is_reviewer_justification_required(self,) -> Optional[bool]:
        """
        Gets the isReviewerJustificationRequired property value. Specifies whether the reviewer must provide justification for the approval. The default value is true.
        Returns: Optional[bool]
        """
        return self._is_reviewer_justification_required
    
    @is_reviewer_justification_required.setter
    def is_reviewer_justification_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReviewerJustificationRequired property value. Specifies whether the reviewer must provide justification for the approval. The default value is true.
        Args:
            value: Value to set for the isReviewerJustificationRequired property.
        """
        self._is_reviewer_justification_required = value
    
    @property
    def is_self_review(self,) -> Optional[bool]:
        """
        Gets the isSelfReview property value. Specifies whether the principals can review their own assignments.
        Returns: Optional[bool]
        """
        return self._is_self_review
    
    @is_self_review.setter
    def is_self_review(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSelfReview property value. Specifies whether the principals can review their own assignments.
        Args:
            value: Value to set for the isSelfReview property.
        """
        self._is_self_review = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def primary_reviewers(self,) -> Optional[List[subject_set.SubjectSet]]:
        """
        Gets the primaryReviewers property value. This collection specifies the users or group of users who will review the access package assignments.
        Returns: Optional[List[subject_set.SubjectSet]]
        """
        return self._primary_reviewers
    
    @primary_reviewers.setter
    def primary_reviewers(self,value: Optional[List[subject_set.SubjectSet]] = None) -> None:
        """
        Sets the primaryReviewers property value. This collection specifies the users or group of users who will review the access package assignments.
        Args:
            value: Value to set for the primaryReviewers property.
        """
        self._primary_reviewers = value
    
    @property
    def schedule(self,) -> Optional[entitlement_management_schedule.EntitlementManagementSchedule]:
        """
        Gets the schedule property value. When the first review should start and how often it should recur.
        Returns: Optional[entitlement_management_schedule.EntitlementManagementSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None) -> None:
        """
        Sets the schedule property value. When the first review should start and how often it should recur.
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

