from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .response_emotion_type import ResponseEmotionType
    from .response_feedback_type import ResponseFeedbackType

from .entity import Entity

@dataclass
class ReflectCheckInResponse(Entity, Parsable):
    # Identifier for the Reflect check-in.
    check_in_id: Optional[str] = None
    # The question or prompt of the Reflect check-in that this response addresses.
    check_in_title: Optional[str] = None
    # ID of the class associated with the Reflect check-in.
    class_id: Optional[str] = None
    # Date and time when the Reflect check-in was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # ID of the user who created the Reflect check-in.
    creator_id: Optional[str] = None
    # Indicates whether the Reflect check-in is closed (true) or open (false).
    is_closed: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the user who responded to the Reflect check-in.
    responder_id: Optional[str] = None
    # The responseEmotion property
    response_emotion: Optional[ResponseEmotionType] = None
    # The responseFeedback property
    response_feedback: Optional[ResponseFeedbackType] = None
    # Date and time when the response to the Reflect check-in was submitted. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    submit_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReflectCheckInResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReflectCheckInResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReflectCheckInResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .response_emotion_type import ResponseEmotionType
        from .response_feedback_type import ResponseFeedbackType

        from .entity import Entity
        from .response_emotion_type import ResponseEmotionType
        from .response_feedback_type import ResponseFeedbackType

        fields: dict[str, Callable[[Any], None]] = {
            "checkInId": lambda n : setattr(self, 'check_in_id', n.get_str_value()),
            "checkInTitle": lambda n : setattr(self, 'check_in_title', n.get_str_value()),
            "classId": lambda n : setattr(self, 'class_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "creatorId": lambda n : setattr(self, 'creator_id', n.get_str_value()),
            "isClosed": lambda n : setattr(self, 'is_closed', n.get_bool_value()),
            "responderId": lambda n : setattr(self, 'responder_id', n.get_str_value()),
            "responseEmotion": lambda n : setattr(self, 'response_emotion', n.get_enum_value(ResponseEmotionType)),
            "responseFeedback": lambda n : setattr(self, 'response_feedback', n.get_enum_value(ResponseFeedbackType)),
            "submitDateTime": lambda n : setattr(self, 'submit_date_time', n.get_datetime_value()),
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
        writer.write_str_value("checkInId", self.check_in_id)
        writer.write_str_value("checkInTitle", self.check_in_title)
        writer.write_str_value("classId", self.class_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("creatorId", self.creator_id)
        writer.write_bool_value("isClosed", self.is_closed)
        writer.write_str_value("responderId", self.responder_id)
        writer.write_enum_value("responseEmotion", self.response_emotion)
        writer.write_enum_value("responseFeedback", self.response_feedback)
        writer.write_datetime_value("submitDateTime", self.submit_date_time)
    

