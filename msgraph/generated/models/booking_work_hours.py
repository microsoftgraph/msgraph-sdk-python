from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_work_time_slot import BookingWorkTimeSlot
    from .day_of_week import DayOfWeek

@dataclass
class BookingWorkHours(AdditionalDataHolder, BackedModel, Parsable):
    """
    This type represents the set of working hours in a single day of the week.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The day property
    day: Optional[DayOfWeek] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A list of start/end times during a day.
    time_slots: Optional[list[BookingWorkTimeSlot]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BookingWorkHours:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingWorkHours
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BookingWorkHours()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .booking_work_time_slot import BookingWorkTimeSlot
        from .day_of_week import DayOfWeek

        from .booking_work_time_slot import BookingWorkTimeSlot
        from .day_of_week import DayOfWeek

        fields: dict[str, Callable[[Any], None]] = {
            "day": lambda n : setattr(self, 'day', n.get_enum_value(DayOfWeek)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeSlots": lambda n : setattr(self, 'time_slots', n.get_collection_of_object_values(BookingWorkTimeSlot)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("day", self.day)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("timeSlots", self.time_slots)
        writer.write_additional_data_value(self.additional_data)
    

