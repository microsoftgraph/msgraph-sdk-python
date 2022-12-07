from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_instance_decision_item = lazy_import('msgraph.generated.models.access_review_instance_decision_item')
access_review_reviewer = lazy_import('msgraph.generated.models.access_review_reviewer')
access_review_reviewer_scope = lazy_import('msgraph.generated.models.access_review_reviewer_scope')
access_review_scope = lazy_import('msgraph.generated.models.access_review_scope')
access_review_stage = lazy_import('msgraph.generated.models.access_review_stage')
entity = lazy_import('msgraph.generated.models.entity')

class AccessReviewInstance(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewInstance and sets the default values.
        """
        super().__init__()
        # Returns the collection of reviewers who were contacted to complete this review. While the reviewers and fallbackReviewers properties of the accessReviewScheduleDefinition might specify group owners or managers as reviewers, contactedReviewers returns their individual identities. Supports $select. Read-only.
        self._contacted_reviewers: Optional[List[access_review_reviewer.AccessReviewReviewer]] = None
        # Each user reviewed in an accessReviewInstance has a decision item representing if they were approved, denied, or not yet reviewed.
        self._decisions: Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]] = None
        # DateTime when review instance is scheduled to end.The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only.
        self._end_date_time: Optional[datetime] = None
        # This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. Supports $select.
        self._fallback_reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # This collection of access review scopes is used to define who the reviewers are. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.
        self._reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
        # Created based on scope and instanceEnumerationScope at the accessReviewScheduleDefinition level. Defines the scope of users reviewed in a group. Supports $select and $filter (contains only). Read-only.
        self._scope: Optional[access_review_scope.AccessReviewScope] = None
        # If the instance has multiple stages, this returns the collection of stages. A new stage will only be created when the previous stage ends. The existence, number, and settings of stages on a review instance are created based on the accessReviewStageSettings on the parent accessReviewScheduleDefinition.
        self._stages: Optional[List[access_review_stage.AccessReviewStage]] = None
        # DateTime when review instance is scheduled to start. May be in the future. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only.
        self._start_date_time: Optional[datetime] = None
        # Specifies the status of an accessReview. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $select, $orderby, and $filter (eq only). Read-only.
        self._status: Optional[str] = None
    
    @property
    def contacted_reviewers(self,) -> Optional[List[access_review_reviewer.AccessReviewReviewer]]:
        """
        Gets the contactedReviewers property value. Returns the collection of reviewers who were contacted to complete this review. While the reviewers and fallbackReviewers properties of the accessReviewScheduleDefinition might specify group owners or managers as reviewers, contactedReviewers returns their individual identities. Supports $select. Read-only.
        Returns: Optional[List[access_review_reviewer.AccessReviewReviewer]]
        """
        return self._contacted_reviewers
    
    @contacted_reviewers.setter
    def contacted_reviewers(self,value: Optional[List[access_review_reviewer.AccessReviewReviewer]] = None) -> None:
        """
        Sets the contactedReviewers property value. Returns the collection of reviewers who were contacted to complete this review. While the reviewers and fallbackReviewers properties of the accessReviewScheduleDefinition might specify group owners or managers as reviewers, contactedReviewers returns their individual identities. Supports $select. Read-only.
        Args:
            value: Value to set for the contactedReviewers property.
        """
        self._contacted_reviewers = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewInstance()
    
    @property
    def decisions(self,) -> Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]]:
        """
        Gets the decisions property value. Each user reviewed in an accessReviewInstance has a decision item representing if they were approved, denied, or not yet reviewed.
        Returns: Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]]
        """
        return self._decisions
    
    @decisions.setter
    def decisions(self,value: Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]] = None) -> None:
        """
        Sets the decisions property value. Each user reviewed in an accessReviewInstance has a decision item representing if they were approved, denied, or not yet reviewed.
        Args:
            value: Value to set for the decisions property.
        """
        self._decisions = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. DateTime when review instance is scheduled to end.The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. DateTime when review instance is scheduled to end.The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    @property
    def fallback_reviewers(self,) -> Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]:
        """
        Gets the fallbackReviewers property value. This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. Supports $select.
        Returns: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]
        """
        return self._fallback_reviewers
    
    @fallback_reviewers.setter
    def fallback_reviewers(self,value: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None) -> None:
        """
        Sets the fallbackReviewers property value. This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. Supports $select.
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
            "contacted_reviewers": lambda n : setattr(self, 'contacted_reviewers', n.get_collection_of_object_values(access_review_reviewer.AccessReviewReviewer)),
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_object_values(access_review_instance_decision_item.AccessReviewInstanceDecisionItem)),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "fallback_reviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(access_review_scope.AccessReviewScope)),
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(access_review_stage.AccessReviewStage)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def reviewers(self,) -> Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]:
        """
        Gets the reviewers property value. This collection of access review scopes is used to define who the reviewers are. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.
        Returns: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]
        """
        return self._reviewers
    
    @reviewers.setter
    def reviewers(self,value: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None) -> None:
        """
        Sets the reviewers property value. This collection of access review scopes is used to define who the reviewers are. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.
        Args:
            value: Value to set for the reviewers property.
        """
        self._reviewers = value
    
    @property
    def scope(self,) -> Optional[access_review_scope.AccessReviewScope]:
        """
        Gets the scope property value. Created based on scope and instanceEnumerationScope at the accessReviewScheduleDefinition level. Defines the scope of users reviewed in a group. Supports $select and $filter (contains only). Read-only.
        Returns: Optional[access_review_scope.AccessReviewScope]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[access_review_scope.AccessReviewScope] = None) -> None:
        """
        Sets the scope property value. Created based on scope and instanceEnumerationScope at the accessReviewScheduleDefinition level. Defines the scope of users reviewed in a group. Supports $select and $filter (contains only). Read-only.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("contactedReviewers", self.contacted_reviewers)
        writer.write_collection_of_object_values("decisions", self.decisions)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_object_value("scope", self.scope)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
    
    @property
    def stages(self,) -> Optional[List[access_review_stage.AccessReviewStage]]:
        """
        Gets the stages property value. If the instance has multiple stages, this returns the collection of stages. A new stage will only be created when the previous stage ends. The existence, number, and settings of stages on a review instance are created based on the accessReviewStageSettings on the parent accessReviewScheduleDefinition.
        Returns: Optional[List[access_review_stage.AccessReviewStage]]
        """
        return self._stages
    
    @stages.setter
    def stages(self,value: Optional[List[access_review_stage.AccessReviewStage]] = None) -> None:
        """
        Sets the stages property value. If the instance has multiple stages, this returns the collection of stages. A new stage will only be created when the previous stage ends. The existence, number, and settings of stages on a review instance are created based on the accessReviewStageSettings on the parent accessReviewScheduleDefinition.
        Args:
            value: Value to set for the stages property.
        """
        self._stages = value
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. DateTime when review instance is scheduled to start. May be in the future. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. DateTime when review instance is scheduled to start. May be in the future. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. Specifies the status of an accessReview. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $select, $orderby, and $filter (eq only). Read-only.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. Specifies the status of an accessReview. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $select, $orderby, and $filter (eq only). Read-only.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

