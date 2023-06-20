from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_history_decision_filter, access_review_history_instance, access_review_history_schedule_settings, access_review_history_status, access_review_scope, entity, user_identity

from . import entity

@dataclass
class AccessReviewHistoryDefinition(entity.Entity):
    # The createdBy property
    created_by: Optional[user_identity.UserIdentity] = None
    # Timestamp when the access review definition was created.
    created_date_time: Optional[datetime] = None
    # Determines which review decisions will be included in the fetched review history data if specified. Optional on create. All decisions will be included by default if no decisions are provided on create. Possible values are: approve, deny, dontKnow, notReviewed, and notNotified.
    decisions: Optional[List[access_review_history_decision_filter.AccessReviewHistoryDecisionFilter]] = None
    # Name for the access review history data collection. Required.
    display_name: Optional[str] = None
    # If the accessReviewHistoryDefinition is a recurring definition, instances represent each recurrence. A definition that does not recur will have exactly one instance.
    instances: Optional[List[access_review_history_instance.AccessReviewHistoryInstance]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A timestamp. Reviews ending on or before this date will be included in the fetched history data. Only required if scheduleSettings is not defined.
    review_history_period_end_date_time: Optional[datetime] = None
    # A timestamp. Reviews starting on or before this date will be included in the fetched history data. Only required if scheduleSettings is not defined.
    review_history_period_start_date_time: Optional[datetime] = None
    # The settings for a recurring access review history definition series. Only required if reviewHistoryPeriodStartDateTime or reviewHistoryPeriodEndDateTime are not defined. Not supported yet.
    schedule_settings: Optional[access_review_history_schedule_settings.AccessReviewHistoryScheduleSettings] = None
    # Used to scope what reviews are included in the fetched history data. Fetches reviews whose scope matches with this provided scope. Required.
    scopes: Optional[List[access_review_scope.AccessReviewScope]] = None
    # Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue.
    status: Optional[access_review_history_status.AccessReviewHistoryStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewHistoryDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewHistoryDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewHistoryDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_history_decision_filter, access_review_history_instance, access_review_history_schedule_settings, access_review_history_status, access_review_scope, entity, user_identity

        from . import access_review_history_decision_filter, access_review_history_instance, access_review_history_schedule_settings, access_review_history_status, access_review_scope, entity, user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(user_identity.UserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_enum_values(access_review_history_decision_filter.AccessReviewHistoryDecisionFilter)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(access_review_history_instance.AccessReviewHistoryInstance)),
            "reviewHistoryPeriodEndDateTime": lambda n : setattr(self, 'review_history_period_end_date_time', n.get_datetime_value()),
            "reviewHistoryPeriodStartDateTime": lambda n : setattr(self, 'review_history_period_start_date_time', n.get_datetime_value()),
            "scheduleSettings": lambda n : setattr(self, 'schedule_settings', n.get_object_value(access_review_history_schedule_settings.AccessReviewHistoryScheduleSettings)),
            "scopes": lambda n : setattr(self, 'scopes', n.get_collection_of_object_values(access_review_scope.AccessReviewScope)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(access_review_history_status.AccessReviewHistoryStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
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
    

