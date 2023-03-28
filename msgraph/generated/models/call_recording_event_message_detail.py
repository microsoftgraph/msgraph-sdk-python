from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import call_recording_status, event_message_detail, identity_set

from . import event_message_detail

class CallRecordingEventMessageDetail(event_message_detail.EventMessageDetail):
    def __init__(self,) -> None:
        """
        Instantiates a new CallRecordingEventMessageDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.callRecordingEventMessageDetail"
        # Unique identifier of the call.
        self._call_id: Optional[str] = None
        # Display name for the call recording.
        self._call_recording_display_name: Optional[str] = None
        # Duration of the call recording.
        self._call_recording_duration: Optional[timedelta] = None
        # Status of the call recording. Possible values are: success, failure, initial, chunkFinished, unknownFutureValue.
        self._call_recording_status: Optional[call_recording_status.CallRecordingStatus] = None
        # Call recording URL.
        self._call_recording_url: Optional[str] = None
        # Initiator of the event.
        self._initiator: Optional[identity_set.IdentitySet] = None
        # Organizer of the meeting.
        self._meeting_organizer: Optional[identity_set.IdentitySet] = None
    
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
            value: Value to set for the call_id property.
        """
        self._call_id = value
    
    @property
    def call_recording_display_name(self,) -> Optional[str]:
        """
        Gets the callRecordingDisplayName property value. Display name for the call recording.
        Returns: Optional[str]
        """
        return self._call_recording_display_name
    
    @call_recording_display_name.setter
    def call_recording_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the callRecordingDisplayName property value. Display name for the call recording.
        Args:
            value: Value to set for the call_recording_display_name property.
        """
        self._call_recording_display_name = value
    
    @property
    def call_recording_duration(self,) -> Optional[timedelta]:
        """
        Gets the callRecordingDuration property value. Duration of the call recording.
        Returns: Optional[timedelta]
        """
        return self._call_recording_duration
    
    @call_recording_duration.setter
    def call_recording_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the callRecordingDuration property value. Duration of the call recording.
        Args:
            value: Value to set for the call_recording_duration property.
        """
        self._call_recording_duration = value
    
    @property
    def call_recording_status(self,) -> Optional[call_recording_status.CallRecordingStatus]:
        """
        Gets the callRecordingStatus property value. Status of the call recording. Possible values are: success, failure, initial, chunkFinished, unknownFutureValue.
        Returns: Optional[call_recording_status.CallRecordingStatus]
        """
        return self._call_recording_status
    
    @call_recording_status.setter
    def call_recording_status(self,value: Optional[call_recording_status.CallRecordingStatus] = None) -> None:
        """
        Sets the callRecordingStatus property value. Status of the call recording. Possible values are: success, failure, initial, chunkFinished, unknownFutureValue.
        Args:
            value: Value to set for the call_recording_status property.
        """
        self._call_recording_status = value
    
    @property
    def call_recording_url(self,) -> Optional[str]:
        """
        Gets the callRecordingUrl property value. Call recording URL.
        Returns: Optional[str]
        """
        return self._call_recording_url
    
    @call_recording_url.setter
    def call_recording_url(self,value: Optional[str] = None) -> None:
        """
        Sets the callRecordingUrl property value. Call recording URL.
        Args:
            value: Value to set for the call_recording_url property.
        """
        self._call_recording_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallRecordingEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallRecordingEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CallRecordingEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import call_recording_status, event_message_detail, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "callId": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "callRecordingDisplayName": lambda n : setattr(self, 'call_recording_display_name', n.get_str_value()),
            "callRecordingDuration": lambda n : setattr(self, 'call_recording_duration', n.get_timedelta_value()),
            "callRecordingStatus": lambda n : setattr(self, 'call_recording_status', n.get_enum_value(call_recording_status.CallRecordingStatus)),
            "callRecordingUrl": lambda n : setattr(self, 'call_recording_url', n.get_str_value()),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "meetingOrganizer": lambda n : setattr(self, 'meeting_organizer', n.get_object_value(identity_set.IdentitySet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiator(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the initiator property value. Initiator of the event.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._initiator
    
    @initiator.setter
    def initiator(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the initiator property value. Initiator of the event.
        Args:
            value: Value to set for the initiator property.
        """
        self._initiator = value
    
    @property
    def meeting_organizer(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the meetingOrganizer property value. Organizer of the meeting.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._meeting_organizer
    
    @meeting_organizer.setter
    def meeting_organizer(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the meetingOrganizer property value. Organizer of the meeting.
        Args:
            value: Value to set for the meeting_organizer property.
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
        writer.write_str_value("callRecordingDisplayName", self.call_recording_display_name)
        writer.write_timedelta_value("callRecordingDuration", self.call_recording_duration)
        writer.write_enum_value("callRecordingStatus", self.call_recording_status)
        writer.write_str_value("callRecordingUrl", self.call_recording_url)
        writer.write_object_value("initiator", self.initiator)
        writer.write_object_value("meetingOrganizer", self.meeting_organizer)
    

