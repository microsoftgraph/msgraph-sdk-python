from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .endpoint import Endpoint
    from .failure_info import FailureInfo
    from .media import Media

from ..entity import Entity

@dataclass
class Segment(Entity):
    # Endpoint that answered this segment.
    callee: Optional[Endpoint] = None
    # Endpoint that initiated this segment.
    caller: Optional[Endpoint] = None
    # UTC time when the segment ended. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    end_date_time: Optional[datetime.datetime] = None
    # Failure information associated with the segment if it failed.
    failure_info: Optional[FailureInfo] = None
    # Media associated with this segment.
    media: Optional[List[Media]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # UTC time when the segment started. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Segment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Segment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Segment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .endpoint import Endpoint
        from .failure_info import FailureInfo
        from .media import Media

        from ..entity import Entity
        from .endpoint import Endpoint
        from .failure_info import FailureInfo
        from .media import Media

        fields: Dict[str, Callable[[Any], None]] = {
            "callee": lambda n : setattr(self, 'callee', n.get_object_value(Endpoint)),
            "caller": lambda n : setattr(self, 'caller', n.get_object_value(Endpoint)),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "failureInfo": lambda n : setattr(self, 'failure_info', n.get_object_value(FailureInfo)),
            "media": lambda n : setattr(self, 'media', n.get_collection_of_object_values(Media)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_object_value("callee", self.callee)
        writer.write_object_value("caller", self.caller)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("failureInfo", self.failure_info)
        writer.write_collection_of_object_values("media", self.media)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    

