from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bookings_availability import BookingsAvailability

from .bookings_availability import BookingsAvailability

@dataclass
class BookingsAvailabilityWindow(BookingsAvailability):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.bookingsAvailabilityWindow"
    # End date of the availability window.
    end_date: Optional[datetime.date] = None
    # Start date of the availability window.
    start_date: Optional[datetime.date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingsAvailabilityWindow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingsAvailabilityWindow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingsAvailabilityWindow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .bookings_availability import BookingsAvailability

        from .bookings_availability import BookingsAvailability

        fields: Dict[str, Callable[[Any], None]] = {
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
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
        writer.write_date_value("endDate", self.end_date)
        writer.write_date_value("startDate", self.start_date)
    

