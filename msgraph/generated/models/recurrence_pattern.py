from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

day_of_week = lazy_import('msgraph.generated.models.day_of_week')
recurrence_pattern_type = lazy_import('msgraph.generated.models.recurrence_pattern_type')
week_index = lazy_import('msgraph.generated.models.week_index')

class RecurrencePattern(AdditionalDataHolder, Parsable):
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
        Instantiates a new recurrencePattern and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The day of the month on which the event occurs. Required if type is absoluteMonthly or absoluteYearly.
        self._day_of_month: Optional[int] = None
        # A collection of the days of the week on which the event occurs. The possible values are: sunday, monday, tuesday, wednesday, thursday, friday, saturday. If type is relativeMonthly or relativeYearly, and daysOfWeek specifies more than one day, the event falls on the first day that satisfies the pattern.  Required if type is weekly, relativeMonthly, or relativeYearly.
        self._days_of_week: Optional[List[day_of_week.DayOfWeek]] = None
        # The first day of the week. The possible values are: sunday, monday, tuesday, wednesday, thursday, friday, saturday. Default is sunday. Required if type is weekly.
        self._first_day_of_week: Optional[day_of_week.DayOfWeek] = None
        # Specifies on which instance of the allowed days specified in daysOfWeek the event occurs, counted from the first instance in the month. The possible values are: first, second, third, fourth, last. Default is first. Optional and used if type is relativeMonthly or relativeYearly.
        self._index: Optional[week_index.WeekIndex] = None
        # The number of units between occurrences, where units can be in days, weeks, months, or years, depending on the type. Required.
        self._interval: Optional[int] = None
        # The month in which the event occurs.  This is a number from 1 to 12.
        self._month: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The recurrence pattern type: daily, weekly, absoluteMonthly, relativeMonthly, absoluteYearly, relativeYearly. Required. For more information, see values of type property.
        self._type: Optional[recurrence_pattern_type.RecurrencePatternType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecurrencePattern:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecurrencePattern
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecurrencePattern()
    
    @property
    def day_of_month(self,) -> Optional[int]:
        """
        Gets the dayOfMonth property value. The day of the month on which the event occurs. Required if type is absoluteMonthly or absoluteYearly.
        Returns: Optional[int]
        """
        return self._day_of_month
    
    @day_of_month.setter
    def day_of_month(self,value: Optional[int] = None) -> None:
        """
        Sets the dayOfMonth property value. The day of the month on which the event occurs. Required if type is absoluteMonthly or absoluteYearly.
        Args:
            value: Value to set for the dayOfMonth property.
        """
        self._day_of_month = value
    
    @property
    def days_of_week(self,) -> Optional[List[day_of_week.DayOfWeek]]:
        """
        Gets the daysOfWeek property value. A collection of the days of the week on which the event occurs. The possible values are: sunday, monday, tuesday, wednesday, thursday, friday, saturday. If type is relativeMonthly or relativeYearly, and daysOfWeek specifies more than one day, the event falls on the first day that satisfies the pattern.  Required if type is weekly, relativeMonthly, or relativeYearly.
        Returns: Optional[List[day_of_week.DayOfWeek]]
        """
        return self._days_of_week
    
    @days_of_week.setter
    def days_of_week(self,value: Optional[List[day_of_week.DayOfWeek]] = None) -> None:
        """
        Sets the daysOfWeek property value. A collection of the days of the week on which the event occurs. The possible values are: sunday, monday, tuesday, wednesday, thursday, friday, saturday. If type is relativeMonthly or relativeYearly, and daysOfWeek specifies more than one day, the event falls on the first day that satisfies the pattern.  Required if type is weekly, relativeMonthly, or relativeYearly.
        Args:
            value: Value to set for the daysOfWeek property.
        """
        self._days_of_week = value
    
    @property
    def first_day_of_week(self,) -> Optional[day_of_week.DayOfWeek]:
        """
        Gets the firstDayOfWeek property value. The first day of the week. The possible values are: sunday, monday, tuesday, wednesday, thursday, friday, saturday. Default is sunday. Required if type is weekly.
        Returns: Optional[day_of_week.DayOfWeek]
        """
        return self._first_day_of_week
    
    @first_day_of_week.setter
    def first_day_of_week(self,value: Optional[day_of_week.DayOfWeek] = None) -> None:
        """
        Sets the firstDayOfWeek property value. The first day of the week. The possible values are: sunday, monday, tuesday, wednesday, thursday, friday, saturday. Default is sunday. Required if type is weekly.
        Args:
            value: Value to set for the firstDayOfWeek property.
        """
        self._first_day_of_week = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "day_of_month": lambda n : setattr(self, 'day_of_month', n.get_int_value()),
            "days_of_week": lambda n : setattr(self, 'days_of_week', n.get_collection_of_enum_values(day_of_week.DayOfWeek)),
            "first_day_of_week": lambda n : setattr(self, 'first_day_of_week', n.get_enum_value(day_of_week.DayOfWeek)),
            "index": lambda n : setattr(self, 'index', n.get_enum_value(week_index.WeekIndex)),
            "interval": lambda n : setattr(self, 'interval', n.get_int_value()),
            "month": lambda n : setattr(self, 'month', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(recurrence_pattern_type.RecurrencePatternType)),
        }
        return fields
    
    @property
    def index(self,) -> Optional[week_index.WeekIndex]:
        """
        Gets the index property value. Specifies on which instance of the allowed days specified in daysOfWeek the event occurs, counted from the first instance in the month. The possible values are: first, second, third, fourth, last. Default is first. Optional and used if type is relativeMonthly or relativeYearly.
        Returns: Optional[week_index.WeekIndex]
        """
        return self._index
    
    @index.setter
    def index(self,value: Optional[week_index.WeekIndex] = None) -> None:
        """
        Sets the index property value. Specifies on which instance of the allowed days specified in daysOfWeek the event occurs, counted from the first instance in the month. The possible values are: first, second, third, fourth, last. Default is first. Optional and used if type is relativeMonthly or relativeYearly.
        Args:
            value: Value to set for the index property.
        """
        self._index = value
    
    @property
    def interval(self,) -> Optional[int]:
        """
        Gets the interval property value. The number of units between occurrences, where units can be in days, weeks, months, or years, depending on the type. Required.
        Returns: Optional[int]
        """
        return self._interval
    
    @interval.setter
    def interval(self,value: Optional[int] = None) -> None:
        """
        Sets the interval property value. The number of units between occurrences, where units can be in days, weeks, months, or years, depending on the type. Required.
        Args:
            value: Value to set for the interval property.
        """
        self._interval = value
    
    @property
    def month(self,) -> Optional[int]:
        """
        Gets the month property value. The month in which the event occurs.  This is a number from 1 to 12.
        Returns: Optional[int]
        """
        return self._month
    
    @month.setter
    def month(self,value: Optional[int] = None) -> None:
        """
        Sets the month property value. The month in which the event occurs.  This is a number from 1 to 12.
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
        writer.write_int_value("dayOfMonth", self.day_of_month)
        writer.write_enum_value("daysOfWeek", self.days_of_week)
        writer.write_enum_value("firstDayOfWeek", self.first_day_of_week)
        writer.write_enum_value("index", self.index)
        writer.write_int_value("interval", self.interval)
        writer.write_int_value("month", self.month)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[recurrence_pattern_type.RecurrencePatternType]:
        """
        Gets the type property value. The recurrence pattern type: daily, weekly, absoluteMonthly, relativeMonthly, absoluteYearly, relativeYearly. Required. For more information, see values of type property.
        Returns: Optional[recurrence_pattern_type.RecurrencePatternType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[recurrence_pattern_type.RecurrencePatternType] = None) -> None:
        """
        Sets the type property value. The recurrence pattern type: daily, weekly, absoluteMonthly, relativeMonthly, absoluteYearly, relativeYearly. Required. For more information, see values of type property.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

