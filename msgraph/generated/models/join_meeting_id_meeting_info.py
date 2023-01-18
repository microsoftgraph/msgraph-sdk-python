from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

meeting_info = lazy_import('msgraph.generated.models.meeting_info')

class JoinMeetingIdMeetingInfo(meeting_info.MeetingInfo):
    def __init__(self,) -> None:
        """
        Instantiates a new JoinMeetingIdMeetingInfo and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.joinMeetingIdMeetingInfo"
        # The ID used to join the meeting.
        self._join_meeting_id: Optional[str] = None
        # The passcode used to join the meeting. Optional.
        self._passcode: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> JoinMeetingIdMeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: JoinMeetingIdMeetingInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return JoinMeetingIdMeetingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "join_meeting_id": lambda n : setattr(self, 'join_meeting_id', n.get_str_value()),
            "passcode": lambda n : setattr(self, 'passcode', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def join_meeting_id(self,) -> Optional[str]:
        """
        Gets the joinMeetingId property value. The ID used to join the meeting.
        Returns: Optional[str]
        """
        return self._join_meeting_id
    
    @join_meeting_id.setter
    def join_meeting_id(self,value: Optional[str] = None) -> None:
        """
        Sets the joinMeetingId property value. The ID used to join the meeting.
        Args:
            value: Value to set for the joinMeetingId property.
        """
        self._join_meeting_id = value
    
    @property
    def passcode(self,) -> Optional[str]:
        """
        Gets the passcode property value. The passcode used to join the meeting. Optional.
        Returns: Optional[str]
        """
        return self._passcode
    
    @passcode.setter
    def passcode(self,value: Optional[str] = None) -> None:
        """
        Sets the passcode property value. The passcode used to join the meeting. Optional.
        Args:
            value: Value to set for the passcode property.
        """
        self._passcode = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("joinMeetingId", self.join_meeting_id)
        writer.write_str_value("passcode", self.passcode)
    

