from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..identity_set import IdentitySet
    from .event_propagation_result import EventPropagationResult
    from .event_query import EventQuery
    from .retention_event_status import RetentionEventStatus
    from .retention_event_type import RetentionEventType

from ..entity import Entity

@dataclass
class RetentionEvent(Entity):
    # The user who created the retentionEvent.
    created_by: Optional[IdentitySet] = None
    # The date time when the retentionEvent was created.
    created_date_time: Optional[datetime.datetime] = None
    # Optional information about the event.
    description: Optional[str] = None
    # Name of the event.
    display_name: Optional[str] = None
    # Represents the success status of a created event and additional information.
    event_propagation_results: Optional[List[EventPropagationResult]] = None
    # Represents the workload (SharePoint Online, OneDrive for Business, Exchange Online) and identification information associated with a retention event.
    event_queries: Optional[List[EventQuery]] = None
    # Status of event propogation to the scoped locations after the event has been created.
    event_status: Optional[RetentionEventStatus] = None
    # Optional time when the event should be triggered.
    event_trigger_date_time: Optional[datetime.datetime] = None
    # The user who last modified the retentionEvent.
    last_modified_by: Optional[IdentitySet] = None
    # The latest date time when the retentionEvent was modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Last time the status of the event was updated.
    last_status_update_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the event that will start the retention period for labels that use this event type when an event is created.
    retention_event_type: Optional[RetentionEventType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetentionEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetentionEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetentionEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .event_propagation_result import EventPropagationResult
        from .event_query import EventQuery
        from .retention_event_status import RetentionEventStatus
        from .retention_event_type import RetentionEventType

        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .event_propagation_result import EventPropagationResult
        from .event_query import EventQuery
        from .retention_event_status import RetentionEventStatus
        from .retention_event_type import RetentionEventType

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "eventPropagationResults": lambda n : setattr(self, 'event_propagation_results', n.get_collection_of_object_values(EventPropagationResult)),
            "eventQueries": lambda n : setattr(self, 'event_queries', n.get_collection_of_object_values(EventQuery)),
            "eventStatus": lambda n : setattr(self, 'event_status', n.get_object_value(RetentionEventStatus)),
            "eventTriggerDateTime": lambda n : setattr(self, 'event_trigger_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastStatusUpdateDateTime": lambda n : setattr(self, 'last_status_update_date_time', n.get_datetime_value()),
            "retentionEventType": lambda n : setattr(self, 'retention_event_type', n.get_object_value(RetentionEventType)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("eventPropagationResults", self.event_propagation_results)
        writer.write_collection_of_object_values("eventQueries", self.event_queries)
        writer.write_object_value("eventStatus", self.event_status)
        writer.write_datetime_value("eventTriggerDateTime", self.event_trigger_date_time)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("lastStatusUpdateDateTime", self.last_status_update_date_time)
        writer.write_object_value("retentionEventType", self.retention_event_type)
    

