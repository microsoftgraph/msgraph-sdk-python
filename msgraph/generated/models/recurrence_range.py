from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .recurrence_range_type import RecurrenceRangeType

@dataclass
class RecurrenceRange(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The date to stop applying the recurrence pattern. Depending on the recurrence pattern of the event, the last occurrence of the meeting may not be this date. Required if type is endDate.
    end_date: Optional[datetime.date] = None
    # The number of times to repeat the event. Required and must be positive if type is numbered.
    number_of_occurrences: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Time zone for the startDate and endDate properties. Optional. If not specified, the time zone of the event is used.
    recurrence_time_zone: Optional[str] = None
    # The date to start applying the recurrence pattern. The first occurrence of the meeting may be this date or later, depending on the recurrence pattern of the event. Must be the same value as the start property of the recurring event. Required.
    start_date: Optional[datetime.date] = None
    # The recurrence range. The possible values are: endDate, noEnd, numbered. Required.
    type: Optional[RecurrenceRangeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecurrenceRange:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecurrenceRange
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecurrenceRange()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .recurrence_range_type import RecurrenceRangeType

        from .recurrence_range_type import RecurrenceRangeType

        fields: dict[str, Callable[[Any], None]] = {
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "numberOfOccurrences": lambda n : setattr(self, 'number_of_occurrences', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrenceTimeZone": lambda n : setattr(self, 'recurrence_time_zone', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(RecurrenceRangeType)),
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
        writer.write_date_value("endDate", self.end_date)
        writer.write_int_value("numberOfOccurrences", self.number_of_occurrences)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("recurrenceTimeZone", self.recurrence_time_zone)
        writer.write_date_value("startDate", self.start_date)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

