from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import chat_info, meeting_participants

class CreateOrGetPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new createOrGetPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The chatInfo property
        self._chat_info: Optional[chat_info.ChatInfo] = None
        # The endDateTime property
        self._end_date_time: Optional[datetime] = None
        # The externalId property
        self._external_id: Optional[str] = None
        # The participants property
        self._participants: Optional[meeting_participants.MeetingParticipants] = None
        # The startDateTime property
        self._start_date_time: Optional[datetime] = None
        # The subject property
        self._subject: Optional[str] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def chat_info(self,) -> Optional[chat_info.ChatInfo]:
        """
        Gets the chatInfo property value. The chatInfo property
        Returns: Optional[chat_info.ChatInfo]
        """
        return self._chat_info
    
    @chat_info.setter
    def chat_info(self,value: Optional[chat_info.ChatInfo] = None) -> None:
        """
        Sets the chatInfo property value. The chatInfo property
        Args:
            value: Value to set for the chat_info property.
        """
        self._chat_info = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreateOrGetPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CreateOrGetPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CreateOrGetPostRequestBody()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The endDateTime property
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The endDateTime property
        Args:
            value: Value to set for the end_date_time property.
        """
        self._end_date_time = value
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. The externalId property
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. The externalId property
        Args:
            value: Value to set for the external_id property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import chat_info, meeting_participants

        fields: Dict[str, Callable[[Any], None]] = {
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(chat_info.ChatInfo)),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "participants": lambda n : setattr(self, 'participants', n.get_object_value(meeting_participants.MeetingParticipants)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        return fields
    
    @property
    def participants(self,) -> Optional[meeting_participants.MeetingParticipants]:
        """
        Gets the participants property value. The participants property
        Returns: Optional[meeting_participants.MeetingParticipants]
        """
        return self._participants
    
    @participants.setter
    def participants(self,value: Optional[meeting_participants.MeetingParticipants] = None) -> None:
        """
        Sets the participants property value. The participants property
        Args:
            value: Value to set for the participants property.
        """
        self._participants = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("chatInfo", self.chat_info)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("participants", self.participants)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("subject", self.subject)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The startDateTime property
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The startDateTime property
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject property
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject property
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    

