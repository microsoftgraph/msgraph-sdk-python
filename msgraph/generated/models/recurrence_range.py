from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import recurrence_range_type

@dataclass
class RecurrenceRange(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The date to stop applying the recurrence pattern. Depending on the recurrence pattern of the event, the last occurrence of the meeting may not be this date. Required if type is endDate.
    end_date: Optional[date] = None
    # The number of times to repeat the event. Required and must be positive if type is numbered.
    number_of_occurrences: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Time zone for the startDate and endDate properties. Optional. If not specified, the time zone of the event is used.
    recurrence_time_zone: Optional[str] = None
    # The date to start applying the recurrence pattern. The first occurrence of the meeting may be this date or later, depending on the recurrence pattern of the event. Must be the same value as the start property of the recurring event. Required.
    start_date: Optional[date] = None
    # The recurrence range. The possible values are: endDate, noEnd, numbered. Required.
    type: Optional[recurrence_range_type.RecurrenceRangeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecurrenceRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecurrenceRange
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecurrenceRange()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import recurrence_range_type

        fields: Dict[str, Callable[[Any], None]] = {
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "numberOfOccurrences": lambda n : setattr(self, 'number_of_occurrences', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrenceTimeZone": lambda n : setattr(self, 'recurrence_time_zone', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(recurrence_range_type.RecurrenceRangeType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_date_value("endDate", self.end_date)
        writer.write_int_value("numberOfOccurrences", self.number_of_occurrences)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("recurrenceTimeZone", self.recurrence_time_zone)
        writer.write_date_value("startDate", self.start_date)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

