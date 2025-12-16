from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..identity_set import IdentitySet
    from .call_type import CallType
    from .modality import Modality
    from .organizer import Organizer
    from .participant import Participant
    from .session import Session

from ..entity import Entity

@dataclass
class CallRecord(Entity, Parsable):
    # UTC time when the last user left the call. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    end_date_time: Optional[datetime.datetime] = None
    # Meeting URL associated to the call. May not be available for a peerToPeer call record type.
    join_web_url: Optional[str] = None
    # UTC time when the call record was created. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime.datetime] = None
    # List of all the modalities used in the call. The possible values are: unknown, audio, video, videoBasedScreenSharing, data, screenSharing, unknownFutureValue.
    modalities: Optional[list[Modality]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organizing party's identity. The organizer property is deprecated and will stop returning data on June 30, 2026. Going forward, use the organizer_v2 relationship.
    organizer: Optional[IdentitySet] = None
    # Identity of the organizer of the call. This relationship is expanded by default in callRecord methods.
    organizer_v2: Optional[Organizer] = None
    # List of distinct identities involved in the call. Limited to 130 entries. The participants property is deprecated and will stop returning data on June 30, 2026. Going forward, use the participants_v2 relationship.
    participants: Optional[list[IdentitySet]] = None
    # List of distinct participants in the call.
    participants_v2: Optional[list[Participant]] = None
    # List of sessions involved in the call. Peer-to-peer calls typically only have one session, whereas group calls typically have at least one session per participant. Read-only. Nullable.
    sessions: Optional[list[Session]] = None
    # UTC time when the first user joined the call. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    start_date_time: Optional[datetime.datetime] = None
    # The type property
    type: Optional[CallType] = None
    # Monotonically increasing version of the call record. Higher version call records with the same id includes additional data compared to the lower version.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CallRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .call_type import CallType
        from .modality import Modality
        from .organizer import Organizer
        from .participant import Participant
        from .session import Session

        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .call_type import CallType
        from .modality import Modality
        from .organizer import Organizer
        from .participant import Participant
        from .session import Session

        fields: dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "joinWebUrl": lambda n : setattr(self, 'join_web_url', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "modalities": lambda n : setattr(self, 'modalities', n.get_collection_of_enum_values(Modality)),
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(IdentitySet)),
            "organizer_v2": lambda n : setattr(self, 'organizer_v2', n.get_object_value(Organizer)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(IdentitySet)),
            "participants_v2": lambda n : setattr(self, 'participants_v2', n.get_collection_of_object_values(Participant)),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(Session)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(CallType)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("joinWebUrl", self.join_web_url)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_enum_values("modalities", self.modalities)
        writer.write_object_value("organizer", self.organizer)
        writer.write_object_value("organizer_v2", self.organizer_v2)
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_collection_of_object_values("participants_v2", self.participants_v2)
        writer.write_collection_of_object_values("sessions", self.sessions)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("type", self.type)
        writer.write_int_value("version", self.version)
    

