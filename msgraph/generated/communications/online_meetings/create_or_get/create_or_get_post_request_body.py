from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.chat_info import ChatInfo
    from ....models.meeting_participants import MeetingParticipants

@dataclass
class CreateOrGetPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The chatInfo property
    chat_info: Optional[ChatInfo] = None
    # The endDateTime property
    end_date_time: Optional[datetime.datetime] = None
    # The externalId property
    external_id: Optional[str] = None
    # The participants property
    participants: Optional[MeetingParticipants] = None
    # The startDateTime property
    start_date_time: Optional[datetime.datetime] = None
    # The subject property
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateOrGetPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateOrGetPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateOrGetPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....models.chat_info import ChatInfo
        from ....models.meeting_participants import MeetingParticipants

        from ....models.chat_info import ChatInfo
        from ....models.meeting_participants import MeetingParticipants

        fields: dict[str, Callable[[Any], None]] = {
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(ChatInfo)),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "participants": lambda n : setattr(self, 'participants', n.get_object_value(MeetingParticipants)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("chatInfo", self.chat_info)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("participants", self.participants)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("subject", self.subject)
        writer.write_additional_data_value(self.additional_data)
    

