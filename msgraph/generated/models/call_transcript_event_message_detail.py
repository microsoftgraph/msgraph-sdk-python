from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

event_message_detail = lazy_import('msgraph.generated.models.event_message_detail')
identity_set = lazy_import('msgraph.generated.models.identity_set')

class CallTranscriptEventMessageDetail(event_message_detail.EventMessageDetail):
    @property
    def call_id(self,) -> Optional[str]:
        """
        Gets the callId property value. Unique identifier of the call.
        Returns: Optional[str]
        """
        return self._call_id
    
    @call_id.setter
    def call_id(self,value: Optional[str] = None) -> None:
        """
        Sets the callId property value. Unique identifier of the call.
        Args:
            value: Value to set for the callId property.
        """
        self._call_id = value
    
    @property
    def call_transcript_i_cal_uid(self,) -> Optional[str]:
        """
        Gets the callTranscriptICalUid property value. Unique identifier for a call transcript.
        Returns: Optional[str]
        """
        return self._call_transcript_i_cal_uid
    
    @call_transcript_i_cal_uid.setter
    def call_transcript_i_cal_uid(self,value: Optional[str] = None) -> None:
        """
        Sets the callTranscriptICalUid property value. Unique identifier for a call transcript.
        Args:
            value: Value to set for the callTranscriptICalUid property.
        """
        self._call_transcript_i_cal_uid = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CallTranscriptEventMessageDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.callTranscriptEventMessageDetail"
        # Unique identifier of the call.
        self._call_id: Optional[str] = None
        # Unique identifier for a call transcript.
        self._call_transcript_i_cal_uid: Optional[str] = None
        # The organizer of the meeting.
        self._meeting_organizer: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallTranscriptEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallTranscriptEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CallTranscriptEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "call_id": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "call_transcript_i_cal_uid": lambda n : setattr(self, 'call_transcript_i_cal_uid', n.get_str_value()),
            "meeting_organizer": lambda n : setattr(self, 'meeting_organizer', n.get_object_value(identity_set.IdentitySet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def meeting_organizer(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the meetingOrganizer property value. The organizer of the meeting.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._meeting_organizer
    
    @meeting_organizer.setter
    def meeting_organizer(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the meetingOrganizer property value. The organizer of the meeting.
        Args:
            value: Value to set for the meetingOrganizer property.
        """
        self._meeting_organizer = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("callId", self.call_id)
        writer.write_str_value("callTranscriptICalUid", self.call_transcript_i_cal_uid)
        writer.write_object_value("meetingOrganizer", self.meeting_organizer)
    

