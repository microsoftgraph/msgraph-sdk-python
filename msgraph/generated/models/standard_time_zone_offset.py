from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import daylight_time_zone_offset, day_of_week

class StandardTimeZoneOffset(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new standardTimeZoneOffset and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents the nth occurrence of the day of week that the transition from daylight saving time to standard time occurs.
        self._day_occurrence: Optional[int] = None
        # Represents the day of the week when the transition from daylight saving time to standard time.
        self._day_of_week: Optional[day_of_week.DayOfWeek] = None
        # Represents the month of the year when the transition from daylight saving time to standard time occurs.
        self._month: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Represents the time of day when the transition from daylight saving time to standard time occurs.
        self._time: Optional[time] = None
        # Represents how frequently in terms of years the change from daylight saving time to standard time occurs. For example, a value of 0 means every year.
        self._year: Optional[int] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> StandardTimeZoneOffset:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: StandardTimeZoneOffset
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.daylightTimeZoneOffset":
                from . import daylight_time_zone_offset

                return daylight_time_zone_offset.DaylightTimeZoneOffset()
        return StandardTimeZoneOffset()
    
    @property
    def day_occurrence(self,) -> Optional[int]:
        """
        Gets the dayOccurrence property value. Represents the nth occurrence of the day of week that the transition from daylight saving time to standard time occurs.
        Returns: Optional[int]
        """
        return self._day_occurrence
    
    @day_occurrence.setter
    def day_occurrence(self,value: Optional[int] = None) -> None:
        """
        Sets the dayOccurrence property value. Represents the nth occurrence of the day of week that the transition from daylight saving time to standard time occurs.
        Args:
            value: Value to set for the day_occurrence property.
        """
        self._day_occurrence = value
    
    @property
    def day_of_week(self,) -> Optional[day_of_week.DayOfWeek]:
        """
        Gets the dayOfWeek property value. Represents the day of the week when the transition from daylight saving time to standard time.
        Returns: Optional[day_of_week.DayOfWeek]
        """
        return self._day_of_week
    
    @day_of_week.setter
    def day_of_week(self,value: Optional[day_of_week.DayOfWeek] = None) -> None:
        """
        Sets the dayOfWeek property value. Represents the day of the week when the transition from daylight saving time to standard time.
        Args:
            value: Value to set for the day_of_week property.
        """
        self._day_of_week = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import daylight_time_zone_offset, day_of_week

        fields: Dict[str, Callable[[Any], None]] = {
            "dayOccurrence": lambda n : setattr(self, 'day_occurrence', n.get_int_value()),
            "dayOfWeek": lambda n : setattr(self, 'day_of_week', n.get_enum_value(day_of_week.DayOfWeek)),
            "month": lambda n : setattr(self, 'month', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "time": lambda n : setattr(self, 'time', n.get_time_value()),
            "year": lambda n : setattr(self, 'year', n.get_int_value()),
        }
        return fields
    
    @property
    def month(self,) -> Optional[int]:
        """
        Gets the month property value. Represents the month of the year when the transition from daylight saving time to standard time occurs.
        Returns: Optional[int]
        """
        return self._month
    
    @month.setter
    def month(self,value: Optional[int] = None) -> None:
        """
        Sets the month property value. Represents the month of the year when the transition from daylight saving time to standard time occurs.
        Args:
            value: Value to set for the month property.
        """
        self._month = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_int_value("dayOccurrence", self.day_occurrence)
        writer.write_enum_value("dayOfWeek", self.day_of_week)
        writer.write_int_value("month", self.month)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_time_value("time", self.time)
        writer.write_int_value("year", self.year)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time(self,) -> Optional[time]:
        """
        Gets the time property value. Represents the time of day when the transition from daylight saving time to standard time occurs.
        Returns: Optional[time]
        """
        return self._time
    
    @time.setter
    def time(self,value: Optional[time] = None) -> None:
        """
        Sets the time property value. Represents the time of day when the transition from daylight saving time to standard time occurs.
        Args:
            value: Value to set for the time property.
        """
        self._time = value
    
    @property
    def year(self,) -> Optional[int]:
        """
        Gets the year property value. Represents how frequently in terms of years the change from daylight saving time to standard time occurs. For example, a value of 0 means every year.
        Returns: Optional[int]
        """
        return self._year
    
    @year.setter
    def year(self,value: Optional[int] = None) -> None:
        """
        Sets the year property value. Represents how frequently in terms of years the change from daylight saving time to standard time occurs. For example, a value of 0 means every year.
        Args:
            value: Value to set for the year property.
        """
        self._year = value
    

