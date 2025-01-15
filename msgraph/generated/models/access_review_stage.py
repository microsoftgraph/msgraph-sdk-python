from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
    from .access_review_reviewer_scope import AccessReviewReviewerScope
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessReviewStage(Entity, Parsable):
    # Each user reviewed in an accessReviewStage has a decision item representing if they were approved, denied, or not yet reviewed.
    decisions: Optional[list[AccessReviewInstanceDecisionItem]] = None
    # The date and time in ISO 8601 format and UTC time when the review stage is scheduled to end. This property is the cumulative total of the durationInDays for all stages. Read-only.
    end_date_time: Optional[datetime.datetime] = None
    # This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers are notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner doesn't exist, or manager is specified as reviewer but a user's manager doesn't exist.
    fallback_reviewers: Optional[list[AccessReviewReviewerScope]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This collection of access review scopes is used to define who the reviewers are. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.
    reviewers: Optional[list[AccessReviewReviewerScope]] = None
    # The date and time in ISO 8601 format and UTC time when the review stage is scheduled to start. Read-only.
    start_date_time: Optional[datetime.datetime] = None
    # Specifies the status of an accessReviewStage. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $orderby, and $filter (eq only). Read-only.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewStage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewStage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_reviewer_scope import AccessReviewReviewerScope
        from .entity import Entity

        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_reviewer_scope import AccessReviewReviewerScope
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_object_values(AccessReviewInstanceDecisionItem)),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "fallbackReviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(AccessReviewReviewerScope)),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(AccessReviewReviewerScope)),
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
        writer.write_collection_of_object_values("decisions", self.decisions)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
    

