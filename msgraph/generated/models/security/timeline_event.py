from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .event_source import EventSource
    from .timeline_event_type import TimelineEventType

@dataclass
class TimelineEvent(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The date and time when the event occurred.
    event_date_time: Optional[datetime.datetime] = None
    # Additional details or context about the event.
    event_details: Optional[str] = None
    # The outcome or result of the event, such as delivery location or action taken.
    event_result: Optional[str] = None
    # The origin or actor that triggered the event. The possible values are: system, admin, user, unknownFutureValue.
    event_source: Optional[EventSource] = None
    # Collection of threats identified or associated with this event.
    event_threats: Optional[list[str]] = None
    # The type of event that occurred. The possible values are: originalDelivery, systemTimeTravel, dynamicDelivery, userUrlClick, reprocessed, zap, quarantineRelease, air, unknown, unknownFutureValue.
    event_type: Optional[TimelineEventType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimelineEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimelineEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimelineEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .event_source import EventSource
        from .timeline_event_type import TimelineEventType

        from .event_source import EventSource
        from .timeline_event_type import TimelineEventType

        fields: dict[str, Callable[[Any], None]] = {
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "eventDetails": lambda n : setattr(self, 'event_details', n.get_str_value()),
            "eventResult": lambda n : setattr(self, 'event_result', n.get_str_value()),
            "eventSource": lambda n : setattr(self, 'event_source', n.get_enum_value(EventSource)),
            "eventThreats": lambda n : setattr(self, 'event_threats', n.get_collection_of_primitive_values(str)),
            "eventType": lambda n : setattr(self, 'event_type', n.get_enum_value(TimelineEventType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventDetails", self.event_details)
        writer.write_str_value("eventResult", self.event_result)
        writer.write_enum_value("eventSource", self.event_source)
        writer.write_collection_of_primitive_values("eventThreats", self.event_threats)
        writer.write_enum_value("eventType", self.event_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

