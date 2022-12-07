from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

event_message_detail = lazy_import('msgraph.generated.models.event_message_detail')
identity_set = lazy_import('msgraph.generated.models.identity_set')

class MeetingPolicyUpdatedEventMessageDetail(event_message_detail.EventMessageDetail):
    def __init__(self,) -> None:
        """
        Instantiates a new MeetingPolicyUpdatedEventMessageDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.meetingPolicyUpdatedEventMessageDetail"
        # Initiator of the event.
        self._initiator: Optional[identity_set.IdentitySet] = None
        # Represents whether the meeting chat is enabled or not.
        self._meeting_chat_enabled: Optional[bool] = None
        # Unique identifier of the meeting chat.
        self._meeting_chat_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingPolicyUpdatedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingPolicyUpdatedEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingPolicyUpdatedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "meeting_chat_enabled": lambda n : setattr(self, 'meeting_chat_enabled', n.get_bool_value()),
            "meeting_chat_id": lambda n : setattr(self, 'meeting_chat_id', n.get_str_value()),
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
    def meeting_chat_enabled(self,) -> Optional[bool]:
        """
        Gets the meetingChatEnabled property value. Represents whether the meeting chat is enabled or not.
        Returns: Optional[bool]
        """
        return self._meeting_chat_enabled
    
    @meeting_chat_enabled.setter
    def meeting_chat_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the meetingChatEnabled property value. Represents whether the meeting chat is enabled or not.
        Args:
            value: Value to set for the meetingChatEnabled property.
        """
        self._meeting_chat_enabled = value
    
    @property
    def meeting_chat_id(self,) -> Optional[str]:
        """
        Gets the meetingChatId property value. Unique identifier of the meeting chat.
        Returns: Optional[str]
        """
        return self._meeting_chat_id
    
    @meeting_chat_id.setter
    def meeting_chat_id(self,value: Optional[str] = None) -> None:
        """
        Sets the meetingChatId property value. Unique identifier of the meeting chat.
        Args:
            value: Value to set for the meetingChatId property.
        """
        self._meeting_chat_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("initiator", self.initiator)
        writer.write_bool_value("meetingChatEnabled", self.meeting_chat_enabled)
        writer.write_str_value("meetingChatId", self.meeting_chat_id)
    

