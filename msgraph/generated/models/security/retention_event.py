from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_propagation_result, event_query, retention_event_status, retention_event_type
    from .. import entity, identity_set

from .. import entity

@dataclass
class RetentionEvent(entity.Entity):
    # The user who created the retentionEvent.
    created_by: Optional[identity_set.IdentitySet] = None
    # The date time when the retentionEvent was created.
    created_date_time: Optional[datetime] = None
    # Optional information about the event.
    description: Optional[str] = None
    # Name of the event.
    display_name: Optional[str] = None
    # The eventPropagationResults property
    event_propagation_results: Optional[List[event_propagation_result.EventPropagationResult]] = None
    # Represents the workload (SharePoint Online, OneDrive for Business, Exchange Online) and identification information associated with a retention event.
    event_queries: Optional[List[event_query.EventQuery]] = None
    # The eventStatus property
    event_status: Optional[retention_event_status.RetentionEventStatus] = None
    # Optional time when the event should be triggered.
    event_trigger_date_time: Optional[datetime] = None
    # The user who last modified the retentionEvent.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The latest date time when the retentionEvent was modified.
    last_modified_date_time: Optional[datetime] = None
    # Last time the status of the event was updated.
    last_status_update_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the event that will start the retention period for labels that use this event type when an event is created.
    retention_event_type: Optional[retention_event_type.RetentionEventType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RetentionEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RetentionEvent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RetentionEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_propagation_result, event_query, retention_event_status, retention_event_type
        from .. import entity, identity_set

        from . import event_propagation_result, event_query, retention_event_status, retention_event_type
        from .. import entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "eventPropagationResults": lambda n : setattr(self, 'event_propagation_results', n.get_collection_of_object_values(event_propagation_result.EventPropagationResult)),
            "eventQueries": lambda n : setattr(self, 'event_queries', n.get_collection_of_object_values(event_query.EventQuery)),
            "eventStatus": lambda n : setattr(self, 'event_status', n.get_object_value(retention_event_status.RetentionEventStatus)),
            "eventTriggerDateTime": lambda n : setattr(self, 'event_trigger_date_time', n.get_datetime_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastStatusUpdateDateTime": lambda n : setattr(self, 'last_status_update_date_time', n.get_datetime_value()),
            "retentionEventType": lambda n : setattr(self, 'retention_event_type', n.get_object_value(retention_event_type.RetentionEventType)),
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
    

