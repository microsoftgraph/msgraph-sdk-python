from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet

from .entity import Entity

@dataclass
class CallRecording(Entity):
    # The content property
    content: Optional[bytes] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The meetingId property
    meeting_id: Optional[str] = None
    # The meetingOrganizer property
    meeting_organizer: Optional[IdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recordingContentUrl property
    recording_content_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallRecording:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallRecording
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CallRecording()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet

        from .entity import Entity
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "meetingId": lambda n : setattr(self, 'meeting_id', n.get_str_value()),
            "meetingOrganizer": lambda n : setattr(self, 'meeting_organizer', n.get_object_value(IdentitySet)),
            "recordingContentUrl": lambda n : setattr(self, 'recording_content_url', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bytes_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("meetingId", self.meeting_id)
        writer.write_object_value("meetingOrganizer", self.meeting_organizer)
        writer.write_str_value("recordingContentUrl", self.recording_content_url)
    

