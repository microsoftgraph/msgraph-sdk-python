from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_instance_decision_item = lazy_import('msgraph.generated.models.access_review_instance_decision_item')
access_review_reviewer_scope = lazy_import('msgraph.generated.models.access_review_reviewer_scope')
entity = lazy_import('msgraph.generated.models.entity')

class AccessReviewStage(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewStage and sets the default values.
        """
        super().__init__()
        # Each user reviewed in an accessReviewStage has a decision item representing if they were approved, denied, or not yet reviewed.
        self._decisions: Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]] = None
        # The date and time in ISO 8601 format and UTC time when the review stage is scheduled to end. This property is the cumulative total of the durationInDays for all stages. Read-only.
        self._end_date_time: Optional[datetime] = None
        # This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist.
        self._fallback_reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # This collection of access review scopes is used to define who the reviewers are. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.
        self._reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
        # The date and time in ISO 8601 format and UTC time when the review stage is scheduled to start. Read-only.
        self._start_date_time: Optional[datetime] = None
        # Specifies the status of an accessReviewStage. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $orderby, and $filter (eq only). Read-only.
        self._status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewStage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewStage()
    
    @property
    def decisions(self,) -> Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]]:
        """
        Gets the decisions property value. Each user reviewed in an accessReviewStage has a decision item representing if they were approved, denied, or not yet reviewed.
        Returns: Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]]
        """
        return self._decisions
    
    @decisions.setter
    def decisions(self,value: Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]] = None) -> None:
        """
        Sets the decisions property value. Each user reviewed in an accessReviewStage has a decision item representing if they were approved, denied, or not yet reviewed.
        Args:
            value: Value to set for the decisions property.
        """
        self._decisions = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The date and time in ISO 8601 format and UTC time when the review stage is scheduled to end. This property is the cumulative total of the durationInDays for all stages. Read-only.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The date and time in ISO 8601 format and UTC time when the review stage is scheduled to end. This property is the cumulative total of the durationInDays for all stages. Read-only.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    @property
    def fallback_reviewers(self,) -> Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]:
        """
        Gets the fallbackReviewers property value. This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist.
        Returns: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]
        """
        return self._fallback_reviewers
    
    @fallback_reviewers.setter
    def fallback_reviewers(self,value: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None) -> None:
        """
        Sets the fallbackReviewers property value. This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist.
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
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_object_values(access_review_instance_decision_item.AccessReviewInstanceDecisionItem)),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "fallback_reviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def reviewers(self,) -> Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]:
        """
        Gets the reviewers property value. This collection of access review scopes is used to define who the reviewers are. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.
        Returns: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]
        """
        return self._reviewers
    
    @reviewers.setter
    def reviewers(self,value: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None) -> None:
        """
        Sets the reviewers property value. This collection of access review scopes is used to define who the reviewers are. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.
        Args:
            value: Value to set for the reviewers property.
        """
        self._reviewers = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("decisions", self.decisions)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The date and time in ISO 8601 format and UTC time when the review stage is scheduled to start. Read-only.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The date and time in ISO 8601 format and UTC time when the review stage is scheduled to start. Read-only.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. Specifies the status of an accessReviewStage. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $orderby, and $filter (eq only). Read-only.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. Specifies the status of an accessReviewStage. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $orderby, and $filter (eq only). Read-only.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

