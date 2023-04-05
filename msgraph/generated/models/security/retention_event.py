from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_propagation_result, event_query, retention_event_status, retention_event_type
    from .. import entity, identity_set

from .. import entity

class RetentionEvent(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new retentionEvent and sets the default values.
        """
        super().__init__()
        # The user who created the retentionEvent.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The date time when the retentionEvent was created.
        self._created_date_time: Optional[datetime] = None
        # Optional information about the event.
        self._description: Optional[str] = None
        # Name of the event.
        self._display_name: Optional[str] = None
        # The eventPropagationResults property
        self._event_propagation_results: Optional[List[event_propagation_result.EventPropagationResult]] = None
        # Represents the workload (SharePoint Online, OneDrive for Business, Exchange Online) and identification information associated with a retention event.
        self._event_queries: Optional[List[event_query.EventQuery]] = None
        # The eventStatus property
        self._event_status: Optional[retention_event_status.RetentionEventStatus] = None
        # Optional time when the event should be triggered.
        self._event_trigger_date_time: Optional[datetime] = None
        # The user who last modified the retentionEvent.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The latest date time when the retentionEvent was modified.
        self._last_modified_date_time: Optional[datetime] = None
        # Last time the status of the event was updated.
        self._last_status_update_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies the event that will start the retention period for labels that use this event type when an event is created.
        self._retention_event_type: Optional[retention_event_type.RetentionEventType] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The user who created the retentionEvent.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The user who created the retentionEvent.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date time when the retentionEvent was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date time when the retentionEvent was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RetentionEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RetentionEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RetentionEvent()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Optional information about the event.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Optional information about the event.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the event.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the event.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def event_propagation_results(self,) -> Optional[List[event_propagation_result.EventPropagationResult]]:
        """
        Gets the eventPropagationResults property value. The eventPropagationResults property
        Returns: Optional[List[event_propagation_result.EventPropagationResult]]
        """
        return self._event_propagation_results
    
    @event_propagation_results.setter
    def event_propagation_results(self,value: Optional[List[event_propagation_result.EventPropagationResult]] = None) -> None:
        """
        Sets the eventPropagationResults property value. The eventPropagationResults property
        Args:
            value: Value to set for the event_propagation_results property.
        """
        self._event_propagation_results = value
    
    @property
    def event_queries(self,) -> Optional[List[event_query.EventQuery]]:
        """
        Gets the eventQueries property value. Represents the workload (SharePoint Online, OneDrive for Business, Exchange Online) and identification information associated with a retention event.
        Returns: Optional[List[event_query.EventQuery]]
        """
        return self._event_queries
    
    @event_queries.setter
    def event_queries(self,value: Optional[List[event_query.EventQuery]] = None) -> None:
        """
        Sets the eventQueries property value. Represents the workload (SharePoint Online, OneDrive for Business, Exchange Online) and identification information associated with a retention event.
        Args:
            value: Value to set for the event_queries property.
        """
        self._event_queries = value
    
    @property
    def event_status(self,) -> Optional[retention_event_status.RetentionEventStatus]:
        """
        Gets the eventStatus property value. The eventStatus property
        Returns: Optional[retention_event_status.RetentionEventStatus]
        """
        return self._event_status
    
    @event_status.setter
    def event_status(self,value: Optional[retention_event_status.RetentionEventStatus] = None) -> None:
        """
        Sets the eventStatus property value. The eventStatus property
        Args:
            value: Value to set for the event_status property.
        """
        self._event_status = value
    
    @property
    def event_trigger_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventTriggerDateTime property value. Optional time when the event should be triggered.
        Returns: Optional[datetime]
        """
        return self._event_trigger_date_time
    
    @event_trigger_date_time.setter
    def event_trigger_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventTriggerDateTime property value. Optional time when the event should be triggered.
        Args:
            value: Value to set for the event_trigger_date_time property.
        """
        self._event_trigger_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The user who last modified the retentionEvent.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The user who last modified the retentionEvent.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The latest date time when the retentionEvent was modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The latest date time when the retentionEvent was modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def last_status_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastStatusUpdateDateTime property value. Last time the status of the event was updated.
        Returns: Optional[datetime]
        """
        return self._last_status_update_date_time
    
    @last_status_update_date_time.setter
    def last_status_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastStatusUpdateDateTime property value. Last time the status of the event was updated.
        Args:
            value: Value to set for the last_status_update_date_time property.
        """
        self._last_status_update_date_time = value
    
    @property
    def retention_event_type(self,) -> Optional[retention_event_type.RetentionEventType]:
        """
        Gets the retentionEventType property value. Specifies the event that will start the retention period for labels that use this event type when an event is created.
        Returns: Optional[retention_event_type.RetentionEventType]
        """
        return self._retention_event_type
    
    @retention_event_type.setter
    def retention_event_type(self,value: Optional[retention_event_type.RetentionEventType] = None) -> None:
        """
        Sets the retentionEventType property value. Specifies the event that will start the retention period for labels that use this event type when an event is created.
        Args:
            value: Value to set for the retention_event_type property.
        """
        self._retention_event_type = value
    
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
    

