from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import endpoint, failure_info, modality, segment
    from .. import entity

from .. import entity

@dataclass
class Session(entity.Entity):
    # Endpoint that answered the session.
    callee: Optional[endpoint.Endpoint] = None
    # Endpoint that initiated the session.
    caller: Optional[endpoint.Endpoint] = None
    # UTC time when the last user left the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    end_date_time: Optional[datetime] = None
    # Failure information associated with the session if the session failed.
    failure_info: Optional[failure_info.FailureInfo] = None
    # List of modalities present in the session. Possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.
    modalities: Optional[List[modality.Modality]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of segments involved in the session. Read-only. Nullable.
    segments: Optional[List[segment.Segment]] = None
    # UTC time when the first user joined the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Session:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Session
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Session()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import endpoint, failure_info, modality, segment
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "callee": lambda n : setattr(self, 'callee', n.get_object_value(endpoint.Endpoint)),
            "caller": lambda n : setattr(self, 'caller', n.get_object_value(endpoint.Endpoint)),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "failureInfo": lambda n : setattr(self, 'failure_info', n.get_object_value(failure_info.FailureInfo)),
            "modalities": lambda n : setattr(self, 'modalities', n.get_collection_of_enum_values(modality.Modality)),
            "segments": lambda n : setattr(self, 'segments', n.get_collection_of_object_values(segment.Segment)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("callee", self.callee)
        writer.write_object_value("caller", self.caller)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("failureInfo", self.failure_info)
        writer.write_enum_value("modalities", self.modalities)
        writer.write_collection_of_object_values("segments", self.segments)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    

