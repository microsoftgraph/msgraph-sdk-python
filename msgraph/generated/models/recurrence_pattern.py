from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .day_of_week import DayOfWeek
    from .recurrence_pattern_type import RecurrencePatternType
    from .week_index import WeekIndex

@dataclass
class RecurrencePattern(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The day of the month on which the event occurs. Required if type is absoluteMonthly or absoluteYearly.
    day_of_month: Optional[int] = None
    # A collection of the days of the week on which the event occurs. The possible values are: sunday, monday, tuesday, wednesday, thursday, friday, saturday. If type is relativeMonthly or relativeYearly, and daysOfWeek specifies more than one day, the event falls on the first day that satisfies the pattern.  Required if type is weekly, relativeMonthly, or relativeYearly.
    days_of_week: Optional[list[DayOfWeek]] = None
    # The first day of the week. The possible values are: sunday, monday, tuesday, wednesday, thursday, friday, saturday. Default is sunday. Required if type is weekly.
    first_day_of_week: Optional[DayOfWeek] = None
    # Specifies on which instance of the allowed days specified in daysOfWeek the event occurs, counted from the first instance in the month. The possible values are: first, second, third, fourth, last. Default is first. Optional and used if type is relativeMonthly or relativeYearly.
    index: Optional[WeekIndex] = None
    # The number of units between occurrences, where units can be in days, weeks, months, or years, depending on the type. Required.
    interval: Optional[int] = None
    # The month in which the event occurs.  This is a number from 1 to 12.
    month: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recurrence pattern type: daily, weekly, absoluteMonthly, relativeMonthly, absoluteYearly, relativeYearly. Required. For more information, see values of type property.
    type: Optional[RecurrencePatternType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecurrencePattern:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecurrencePattern
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecurrencePattern()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .day_of_week import DayOfWeek
        from .recurrence_pattern_type import RecurrencePatternType
        from .week_index import WeekIndex

        from .day_of_week import DayOfWeek
        from .recurrence_pattern_type import RecurrencePatternType
        from .week_index import WeekIndex

        fields: dict[str, Callable[[Any], None]] = {
            "dayOfMonth": lambda n : setattr(self, 'day_of_month', n.get_int_value()),
            "daysOfWeek": lambda n : setattr(self, 'days_of_week', n.get_collection_of_enum_values(DayOfWeek)),
            "firstDayOfWeek": lambda n : setattr(self, 'first_day_of_week', n.get_enum_value(DayOfWeek)),
            "index": lambda n : setattr(self, 'index', n.get_enum_value(WeekIndex)),
            "interval": lambda n : setattr(self, 'interval', n.get_int_value()),
            "month": lambda n : setattr(self, 'month', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(RecurrencePatternType)),
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
        writer.write_int_value("dayOfMonth", self.day_of_month)
        writer.write_collection_of_enum_values("daysOfWeek", self.days_of_week)
        writer.write_enum_value("firstDayOfWeek", self.first_day_of_week)
        writer.write_enum_value("index", self.index)
        writer.write_int_value("interval", self.interval)
        writer.write_int_value("month", self.month)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

