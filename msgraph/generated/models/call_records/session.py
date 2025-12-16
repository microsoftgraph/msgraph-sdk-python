from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .endpoint import Endpoint
    from .failure_info import FailureInfo
    from .modality import Modality
    from .segment import Segment

from ..entity import Entity

@dataclass
class Session(Entity, Parsable):
    # Endpoint that answered the session.
    callee: Optional[Endpoint] = None
    # Endpoint that initiated the session.
    caller: Optional[Endpoint] = None
    # UTC time when the last user left the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    end_date_time: Optional[datetime.datetime] = None
    # Failure information associated with the session if the session failed.
    failure_info: Optional[FailureInfo] = None
    # Specifies whether the session is a test.
    is_test: Optional[bool] = None
    # List of modalities present in the session. The possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.
    modalities: Optional[list[Modality]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of segments involved in the session. Read-only. Nullable.
    segments: Optional[list[Segment]] = None
    # UTC time when the first user joined the session. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Session:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Session
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Session()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .endpoint import Endpoint
        from .failure_info import FailureInfo
        from .modality import Modality
        from .segment import Segment

        from ..entity import Entity
        from .endpoint import Endpoint
        from .failure_info import FailureInfo
        from .modality import Modality
        from .segment import Segment

        fields: dict[str, Callable[[Any], None]] = {
            "callee": lambda n : setattr(self, 'callee', n.get_object_value(Endpoint)),
            "caller": lambda n : setattr(self, 'caller', n.get_object_value(Endpoint)),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "failureInfo": lambda n : setattr(self, 'failure_info', n.get_object_value(FailureInfo)),
            "isTest": lambda n : setattr(self, 'is_test', n.get_bool_value()),
            "modalities": lambda n : setattr(self, 'modalities', n.get_collection_of_enum_values(Modality)),
            "segments": lambda n : setattr(self, 'segments', n.get_collection_of_object_values(Segment)),
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
        writer.write_bool_value("isTest", self.is_test)
        writer.write_collection_of_enum_values("modalities", self.modalities)
        writer.write_collection_of_object_values("segments", self.segments)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    

