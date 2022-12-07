from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_history_decision_filter = lazy_import('msgraph.generated.models.access_review_history_decision_filter')
access_review_history_instance = lazy_import('msgraph.generated.models.access_review_history_instance')
access_review_history_schedule_settings = lazy_import('msgraph.generated.models.access_review_history_schedule_settings')
access_review_history_status = lazy_import('msgraph.generated.models.access_review_history_status')
access_review_scope = lazy_import('msgraph.generated.models.access_review_scope')
entity = lazy_import('msgraph.generated.models.entity')
user_identity = lazy_import('msgraph.generated.models.user_identity')

class AccessReviewHistoryDefinition(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewHistoryDefinition and sets the default values.
        """
        super().__init__()
        # The createdBy property
        self._created_by: Optional[user_identity.UserIdentity] = None
        # Timestamp when the access review definition was created.
        self._created_date_time: Optional[datetime] = None
        # Determines which review decisions will be included in the fetched review history data if specified. Optional on create. All decisions will be included by default if no decisions are provided on create. Possible values are: approve, deny, dontKnow, notReviewed, and notNotified.
        self._decisions: Optional[List[access_review_history_decision_filter.AccessReviewHistoryDecisionFilter]] = None
        # Name for the access review history data collection. Required.
        self._display_name: Optional[str] = None
        # If the accessReviewHistoryDefinition is a recurring definition, instances represent each recurrence. A definition that does not recur will have exactly one instance.
        self._instances: Optional[List[access_review_history_instance.AccessReviewHistoryInstance]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A timestamp. Reviews ending on or before this date will be included in the fetched history data. Only required if scheduleSettings is not defined.
        self._review_history_period_end_date_time: Optional[datetime] = None
        # A timestamp. Reviews starting on or before this date will be included in the fetched history data. Only required if scheduleSettings is not defined.
        self._review_history_period_start_date_time: Optional[datetime] = None
        # The settings for a recurring access review history definition series. Only required if reviewHistoryPeriodStartDateTime or reviewHistoryPeriodEndDateTime are not defined. Not supported yet.
        self._schedule_settings: Optional[access_review_history_schedule_settings.AccessReviewHistoryScheduleSettings] = None
        # Used to scope what reviews are included in the fetched history data. Fetches reviews whose scope matches with this provided scope. Required.
        self._scopes: Optional[List[access_review_scope.AccessReviewScope]] = None
        # Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue.
        self._status: Optional[access_review_history_status.AccessReviewHistoryStatus] = None
    
    @property
    def created_by(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Timestamp when the access review definition was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Timestamp when the access review definition was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewHistoryDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewHistoryDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewHistoryDefinition()
    
    @property
    def decisions(self,) -> Optional[List[access_review_history_decision_filter.AccessReviewHistoryDecisionFilter]]:
        """
        Gets the decisions property value. Determines which review decisions will be included in the fetched review history data if specified. Optional on create. All decisions will be included by default if no decisions are provided on create. Possible values are: approve, deny, dontKnow, notReviewed, and notNotified.
        Returns: Optional[List[access_review_history_decision_filter.AccessReviewHistoryDecisionFilter]]
        """
        return self._decisions
    
    @decisions.setter
    def decisions(self,value: Optional[List[access_review_history_decision_filter.AccessReviewHistoryDecisionFilter]] = None) -> None:
        """
        Sets the decisions property value. Determines which review decisions will be included in the fetched review history data if specified. Optional on create. All decisions will be included by default if no decisions are provided on create. Possible values are: approve, deny, dontKnow, notReviewed, and notNotified.
        Args:
            value: Value to set for the decisions property.
        """
        self._decisions = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name for the access review history data collection. Required.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name for the access review history data collection. Required.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(user_identity.UserIdentity)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_enum_values(access_review_history_decision_filter.AccessReviewHistoryDecisionFilter)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(access_review_history_instance.AccessReviewHistoryInstance)),
            "review_history_period_end_date_time": lambda n : setattr(self, 'review_history_period_end_date_time', n.get_datetime_value()),
            "review_history_period_start_date_time": lambda n : setattr(self, 'review_history_period_start_date_time', n.get_datetime_value()),
            "schedule_settings": lambda n : setattr(self, 'schedule_settings', n.get_object_value(access_review_history_schedule_settings.AccessReviewHistoryScheduleSettings)),
            "scopes": lambda n : setattr(self, 'scopes', n.get_collection_of_object_values(access_review_scope.AccessReviewScope)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(access_review_history_status.AccessReviewHistoryStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def instances(self,) -> Optional[List[access_review_history_instance.AccessReviewHistoryInstance]]:
        """
        Gets the instances property value. If the accessReviewHistoryDefinition is a recurring definition, instances represent each recurrence. A definition that does not recur will have exactly one instance.
        Returns: Optional[List[access_review_history_instance.AccessReviewHistoryInstance]]
        """
        return self._instances
    
    @instances.setter
    def instances(self,value: Optional[List[access_review_history_instance.AccessReviewHistoryInstance]] = None) -> None:
        """
        Sets the instances property value. If the accessReviewHistoryDefinition is a recurring definition, instances represent each recurrence. A definition that does not recur will have exactly one instance.
        Args:
            value: Value to set for the instances property.
        """
        self._instances = value
    
    @property
    def review_history_period_end_date_time(self,) -> Optional[datetime]:
        """
        Gets the reviewHistoryPeriodEndDateTime property value. A timestamp. Reviews ending on or before this date will be included in the fetched history data. Only required if scheduleSettings is not defined.
        Returns: Optional[datetime]
        """
        return self._review_history_period_end_date_time
    
    @review_history_period_end_date_time.setter
    def review_history_period_end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reviewHistoryPeriodEndDateTime property value. A timestamp. Reviews ending on or before this date will be included in the fetched history data. Only required if scheduleSettings is not defined.
        Args:
            value: Value to set for the reviewHistoryPeriodEndDateTime property.
        """
        self._review_history_period_end_date_time = value
    
    @property
    def review_history_period_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the reviewHistoryPeriodStartDateTime property value. A timestamp. Reviews starting on or before this date will be included in the fetched history data. Only required if scheduleSettings is not defined.
        Returns: Optional[datetime]
        """
        return self._review_history_period_start_date_time
    
    @review_history_period_start_date_time.setter
    def review_history_period_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reviewHistoryPeriodStartDateTime property value. A timestamp. Reviews starting on or before this date will be included in the fetched history data. Only required if scheduleSettings is not defined.
        Args:
            value: Value to set for the reviewHistoryPeriodStartDateTime property.
        """
        self._review_history_period_start_date_time = value
    
    @property
    def schedule_settings(self,) -> Optional[access_review_history_schedule_settings.AccessReviewHistoryScheduleSettings]:
        """
        Gets the scheduleSettings property value. The settings for a recurring access review history definition series. Only required if reviewHistoryPeriodStartDateTime or reviewHistoryPeriodEndDateTime are not defined. Not supported yet.
        Returns: Optional[access_review_history_schedule_settings.AccessReviewHistoryScheduleSettings]
        """
        return self._schedule_settings
    
    @schedule_settings.setter
    def schedule_settings(self,value: Optional[access_review_history_schedule_settings.AccessReviewHistoryScheduleSettings] = None) -> None:
        """
        Sets the scheduleSettings property value. The settings for a recurring access review history definition series. Only required if reviewHistoryPeriodStartDateTime or reviewHistoryPeriodEndDateTime are not defined. Not supported yet.
        Args:
            value: Value to set for the scheduleSettings property.
        """
        self._schedule_settings = value
    
    @property
    def scopes(self,) -> Optional[List[access_review_scope.AccessReviewScope]]:
        """
        Gets the scopes property value. Used to scope what reviews are included in the fetched history data. Fetches reviews whose scope matches with this provided scope. Required.
        Returns: Optional[List[access_review_scope.AccessReviewScope]]
        """
        return self._scopes
    
    @scopes.setter
    def scopes(self,value: Optional[List[access_review_scope.AccessReviewScope]] = None) -> None:
        """
        Sets the scopes property value. Used to scope what reviews are included in the fetched history data. Fetches reviews whose scope matches with this provided scope. Required.
        Args:
            value: Value to set for the scopes property.
        """
        self._scopes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("decisions", self.decisions)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("instances", self.instances)
        writer.write_datetime_value("reviewHistoryPeriodEndDateTime", self.review_history_period_end_date_time)
        writer.write_datetime_value("reviewHistoryPeriodStartDateTime", self.review_history_period_start_date_time)
        writer.write_object_value("scheduleSettings", self.schedule_settings)
        writer.write_collection_of_object_values("scopes", self.scopes)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[access_review_history_status.AccessReviewHistoryStatus]:
        """
        Gets the status property value. Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue.
        Returns: Optional[access_review_history_status.AccessReviewHistoryStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[access_review_history_status.AccessReviewHistoryStatus] = None) -> None:
        """
        Sets the status property value. Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

