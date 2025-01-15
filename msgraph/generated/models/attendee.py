from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attendee_base import AttendeeBase
    from .response_status import ResponseStatus
    from .time_slot import TimeSlot

from .attendee_base import AttendeeBase

@dataclass
class Attendee(AttendeeBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.attendee"
    # An alternate date/time proposed by the attendee for a meeting request to start and end. If the attendee hasn't proposed another time, then this property isn't included in a response of a GET event.
    proposed_new_time: Optional[TimeSlot] = None
    # The attendee's response (none, accepted, declined, etc.) for the event and date-time that the response was sent.
    status: Optional[ResponseStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Attendee:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Attendee
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Attendee()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attendee_base import AttendeeBase
        from .response_status import ResponseStatus
        from .time_slot import TimeSlot

        from .attendee_base import AttendeeBase
        from .response_status import ResponseStatus
        from .time_slot import TimeSlot

        fields: dict[str, Callable[[Any], None]] = {
            "proposedNewTime": lambda n : setattr(self, 'proposed_new_time', n.get_object_value(TimeSlot)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(ResponseStatus)),
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
        writer.write_object_value("proposedNewTime", self.proposed_new_time)
        writer.write_object_value("status", self.status)
    

