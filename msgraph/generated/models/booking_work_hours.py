from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

booking_work_time_slot = lazy_import('msgraph.generated.models.booking_work_time_slot')
day_of_week = lazy_import('msgraph.generated.models.day_of_week')

class BookingWorkHours(AdditionalDataHolder, Parsable):
    """
    This type represents the set of working hours in a single day of the week.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new bookingWorkHours and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The day property
        self._day: Optional[day_of_week.DayOfWeek] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A list of start/end times during a day.
        self._time_slots: Optional[List[booking_work_time_slot.BookingWorkTimeSlot]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingWorkHours:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingWorkHours
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingWorkHours()
    
    @property
    def day(self,) -> Optional[day_of_week.DayOfWeek]:
        """
        Gets the day property value. The day property
        Returns: Optional[day_of_week.DayOfWeek]
        """
        return self._day
    
    @day.setter
    def day(self,value: Optional[day_of_week.DayOfWeek] = None) -> None:
        """
        Sets the day property value. The day property
        Args:
            value: Value to set for the day property.
        """
        self._day = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "day": lambda n : setattr(self, 'day', n.get_enum_value(day_of_week.DayOfWeek)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "time_slots": lambda n : setattr(self, 'time_slots', n.get_collection_of_object_values(booking_work_time_slot.BookingWorkTimeSlot)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("day", self.day)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("timeSlots", self.time_slots)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_slots(self,) -> Optional[List[booking_work_time_slot.BookingWorkTimeSlot]]:
        """
        Gets the timeSlots property value. A list of start/end times during a day.
        Returns: Optional[List[booking_work_time_slot.BookingWorkTimeSlot]]
        """
        return self._time_slots
    
    @time_slots.setter
    def time_slots(self,value: Optional[List[booking_work_time_slot.BookingWorkTimeSlot]] = None) -> None:
        """
        Sets the timeSlots property value. A list of start/end times during a day.
        Args:
            value: Value to set for the timeSlots property.
        """
        self._time_slots = value
    

