from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import date_time_time_zone

@dataclass
class GetSchedulePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The AvailabilityViewInterval property
    availability_view_interval: Optional[int] = None
    # The EndTime property
    end_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    # The Schedules property
    schedules: Optional[List[str]] = None
    # The StartTime property
    start_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetSchedulePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetSchedulePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetSchedulePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import date_time_time_zone

        fields: Dict[str, Callable[[Any], None]] = {
            "AvailabilityViewInterval": lambda n : setattr(self, 'availability_view_interval', n.get_int_value()),
            "EndTime": lambda n : setattr(self, 'end_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "Schedules": lambda n : setattr(self, 'schedules', n.get_collection_of_primitive_values(str)),
            "StartTime": lambda n : setattr(self, 'start_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
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
        writer.write_int_value("AvailabilityViewInterval", self.availability_view_interval)
        writer.write_object_value("EndTime", self.end_time)
        writer.write_collection_of_primitive_values("Schedules", self.schedules)
        writer.write_object_value("StartTime", self.start_time)
        writer.write_additional_data_value(self.additional_data)
    

