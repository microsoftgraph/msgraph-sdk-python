from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attendee_base = lazy_import('msgraph.generated.models.attendee_base')
response_status = lazy_import('msgraph.generated.models.response_status')
time_slot = lazy_import('msgraph.generated.models.time_slot')

class Attendee(attendee_base.AttendeeBase):
    def __init__(self,) -> None:
        """
        Instantiates a new Attendee and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.attendee"
        # An alternate date/time proposed by the attendee for a meeting request to start and end. If the attendee hasn't proposed another time, then this property is not included in a response of a GET event.
        self._proposed_new_time: Optional[time_slot.TimeSlot] = None
        # The attendee's response (none, accepted, declined, etc.) for the event and date-time that the response was sent.
        self._status: Optional[response_status.ResponseStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Attendee:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Attendee
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Attendee()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "proposed_new_time": lambda n : setattr(self, 'proposed_new_time', n.get_object_value(time_slot.TimeSlot)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(response_status.ResponseStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def proposed_new_time(self,) -> Optional[time_slot.TimeSlot]:
        """
        Gets the proposedNewTime property value. An alternate date/time proposed by the attendee for a meeting request to start and end. If the attendee hasn't proposed another time, then this property is not included in a response of a GET event.
        Returns: Optional[time_slot.TimeSlot]
        """
        return self._proposed_new_time
    
    @proposed_new_time.setter
    def proposed_new_time(self,value: Optional[time_slot.TimeSlot] = None) -> None:
        """
        Sets the proposedNewTime property value. An alternate date/time proposed by the attendee for a meeting request to start and end. If the attendee hasn't proposed another time, then this property is not included in a response of a GET event.
        Args:
            value: Value to set for the proposedNewTime property.
        """
        self._proposed_new_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("proposedNewTime", self.proposed_new_time)
        writer.write_object_value("status", self.status)
    
    @property
    def status(self,) -> Optional[response_status.ResponseStatus]:
        """
        Gets the status property value. The attendee's response (none, accepted, declined, etc.) for the event and date-time that the response was sent.
        Returns: Optional[response_status.ResponseStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[response_status.ResponseStatus] = None) -> None:
        """
        Sets the status property value. The attendee's response (none, accepted, declined, etc.) for the event and date-time that the response was sent.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

