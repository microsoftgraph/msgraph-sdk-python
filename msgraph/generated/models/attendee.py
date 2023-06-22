from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attendee_base, response_status, time_slot

from . import attendee_base

@dataclass
class Attendee(attendee_base.AttendeeBase):
    odata_type = "#microsoft.graph.attendee"
    # An alternate date/time proposed by the attendee for a meeting request to start and end. If the attendee hasn't proposed another time, then this property is not included in a response of a GET event.
    proposed_new_time: Optional[time_slot.TimeSlot] = None
    # The attendee's response (none, accepted, declined, etc.) for the event and date-time that the response was sent.
    status: Optional[response_status.ResponseStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Attendee:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Attendee
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Attendee()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attendee_base, response_status, time_slot

        from . import attendee_base, response_status, time_slot

        fields: Dict[str, Callable[[Any], None]] = {
            "proposedNewTime": lambda n : setattr(self, 'proposed_new_time', n.get_object_value(time_slot.TimeSlot)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(response_status.ResponseStatus)),
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
        writer.write_object_value("proposedNewTime", self.proposed_new_time)
        writer.write_object_value("status", self.status)
    

