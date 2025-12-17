from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_history_decision_filter import AccessReviewHistoryDecisionFilter
    from .access_review_history_instance import AccessReviewHistoryInstance
    from .access_review_history_schedule_settings import AccessReviewHistoryScheduleSettings
    from .access_review_history_status import AccessReviewHistoryStatus
    from .access_review_scope import AccessReviewScope
    from .entity import Entity
    from .user_identity import UserIdentity

from .entity import Entity

@dataclass
class AccessReviewHistoryDefinition(Entity, Parsable):
    # The createdBy property
    created_by: Optional[UserIdentity] = None
    # Timestamp when the access review definition was created.
    created_date_time: Optional[datetime.datetime] = None
    # Determines which review decisions will be included in the fetched review history data if specified. Optional on create. All decisions are included by default if no decisions are provided on create. The possible values are: approve, deny, dontKnow, notReviewed, and notNotified.
    decisions: Optional[list[AccessReviewHistoryDecisionFilter]] = None
    # Name for the access review history data collection. Required.
    display_name: Optional[str] = None
    # If the accessReviewHistoryDefinition is a recurring definition, instances represent each recurrence. A definition that doesn't recur will have exactly one instance.
    instances: Optional[list[AccessReviewHistoryInstance]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A timestamp. Reviews ending on or before this date will be included in the fetched history data. Only required if scheduleSettings isn't defined.
    review_history_period_end_date_time: Optional[datetime.datetime] = None
    # A timestamp. Reviews starting on or before this date will be included in the fetched history data. Only required if scheduleSettings isn't defined.
    review_history_period_start_date_time: Optional[datetime.datetime] = None
    # The settings for a recurring access review history definition series. Only required if reviewHistoryPeriodStartDateTime or reviewHistoryPeriodEndDateTime aren't defined. Not supported yet.
    schedule_settings: Optional[AccessReviewHistoryScheduleSettings] = None
    # Used to scope what reviews are included in the fetched history data. Fetches reviews whose scope matches with this provided scope. Required.
    scopes: Optional[list[AccessReviewScope]] = None
    # Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue.
    status: Optional[AccessReviewHistoryStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewHistoryDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewHistoryDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewHistoryDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_history_decision_filter import AccessReviewHistoryDecisionFilter
        from .access_review_history_instance import AccessReviewHistoryInstance
        from .access_review_history_schedule_settings import AccessReviewHistoryScheduleSettings
        from .access_review_history_status import AccessReviewHistoryStatus
        from .access_review_scope import AccessReviewScope
        from .entity import Entity
        from .user_identity import UserIdentity

        from .access_review_history_decision_filter import AccessReviewHistoryDecisionFilter
        from .access_review_history_instance import AccessReviewHistoryInstance
        from .access_review_history_schedule_settings import AccessReviewHistoryScheduleSettings
        from .access_review_history_status import AccessReviewHistoryStatus
        from .access_review_scope import AccessReviewScope
        from .entity import Entity
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(UserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_enum_values(AccessReviewHistoryDecisionFilter)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(AccessReviewHistoryInstance)),
            "reviewHistoryPeriodEndDateTime": lambda n : setattr(self, 'review_history_period_end_date_time', n.get_datetime_value()),
            "reviewHistoryPeriodStartDateTime": lambda n : setattr(self, 'review_history_period_start_date_time', n.get_datetime_value()),
            "scheduleSettings": lambda n : setattr(self, 'schedule_settings', n.get_object_value(AccessReviewHistoryScheduleSettings)),
            "scopes": lambda n : setattr(self, 'scopes', n.get_collection_of_object_values(AccessReviewScope)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AccessReviewHistoryStatus)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_enum_values("decisions", self.decisions)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("instances", self.instances)
        writer.write_datetime_value("reviewHistoryPeriodEndDateTime", self.review_history_period_end_date_time)
        writer.write_datetime_value("reviewHistoryPeriodStartDateTime", self.review_history_period_start_date_time)
        writer.write_object_value("scheduleSettings", self.schedule_settings)
        writer.write_collection_of_object_values("scopes", self.scopes)
        writer.write_enum_value("status", self.status)
    

