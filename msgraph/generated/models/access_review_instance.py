from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
    from .access_review_reviewer import AccessReviewReviewer
    from .access_review_reviewer_scope import AccessReviewReviewerScope
    from .access_review_scope import AccessReviewScope
    from .access_review_stage import AccessReviewStage
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessReviewInstance(Entity, Parsable):
    # Returns the collection of reviewers who were contacted to complete this review. While the reviewers and fallbackReviewers properties of the accessReviewScheduleDefinition might specify group owners or managers as reviewers, contactedReviewers returns their individual identities. Supports $select. Read-only.
    contacted_reviewers: Optional[List[AccessReviewReviewer]] = None
    # Each user reviewed in an accessReviewInstance has a decision item representing if they were approved, denied, or not yet reviewed.
    decisions: Optional[List[AccessReviewInstanceDecisionItem]] = None
    # DateTime when review instance is scheduled to end.The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only.
    end_date_time: Optional[datetime.datetime] = None
    # This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. Supports $select.
    fallback_reviewers: Optional[List[AccessReviewReviewerScope]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This collection of access review scopes is used to define who the reviewers are. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.
    reviewers: Optional[List[AccessReviewReviewerScope]] = None
    # Created based on scope and instanceEnumerationScope at the accessReviewScheduleDefinition level. Defines the scope of users reviewed in a group. Supports $select and $filter (contains only). Read-only.
    scope: Optional[AccessReviewScope] = None
    # If the instance has multiple stages, this returns the collection of stages. A new stage will only be created when the previous stage ends. The existence, number, and settings of stages on a review instance are created based on the accessReviewStageSettings on the parent accessReviewScheduleDefinition.
    stages: Optional[List[AccessReviewStage]] = None
    # DateTime when review instance is scheduled to start. May be in the future. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only.
    start_date_time: Optional[datetime.datetime] = None
    # Specifies the status of an accessReview. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $select, $orderby, and $filter (eq only). Read-only.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_reviewer import AccessReviewReviewer
        from .access_review_reviewer_scope import AccessReviewReviewerScope
        from .access_review_scope import AccessReviewScope
        from .access_review_stage import AccessReviewStage
        from .entity import Entity

        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_reviewer import AccessReviewReviewer
        from .access_review_reviewer_scope import AccessReviewReviewerScope
        from .access_review_scope import AccessReviewScope
        from .access_review_stage import AccessReviewStage
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "contactedReviewers": lambda n : setattr(self, 'contacted_reviewers', n.get_collection_of_object_values(AccessReviewReviewer)),
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_object_values(AccessReviewInstanceDecisionItem)),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "fallbackReviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(AccessReviewReviewerScope)),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(AccessReviewReviewerScope)),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(AccessReviewScope)),
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(AccessReviewStage)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_reviewer import AccessReviewReviewer
        from .access_review_reviewer_scope import AccessReviewReviewerScope
        from .access_review_scope import AccessReviewScope
        from .access_review_stage import AccessReviewStage
        from .entity import Entity

        writer.write_collection_of_object_values("contactedReviewers", self.contacted_reviewers)
        writer.write_collection_of_object_values("decisions", self.decisions)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_object_value("scope", self.scope)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
    

