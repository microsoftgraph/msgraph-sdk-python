from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conversation_member

from . import conversation_member

class AnonymousGuestConversationMember(conversation_member.ConversationMember):
    def __init__(self,) -> None:
        """
        Instantiates a new AnonymousGuestConversationMember and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.anonymousGuestConversationMember"
        # Unique ID that represents the user. Note: This ID can change if the user leaves and rejoins the meeting, or joins from a different device.
        self._anonymous_guest_id: Optional[str] = None
    
    @property
    def anonymous_guest_id(self,) -> Optional[str]:
        """
        Gets the anonymousGuestId property value. Unique ID that represents the user. Note: This ID can change if the user leaves and rejoins the meeting, or joins from a different device.
        Returns: Optional[str]
        """
        return self._anonymous_guest_id
    
    @anonymous_guest_id.setter
    def anonymous_guest_id(self,value: Optional[str] = None) -> None:
        """
        Sets the anonymousGuestId property value. Unique ID that represents the user. Note: This ID can change if the user leaves and rejoins the meeting, or joins from a different device.
        Args:
            value: Value to set for the anonymous_guest_id property.
        """
        self._anonymous_guest_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AnonymousGuestConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AnonymousGuestConversationMember
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AnonymousGuestConversationMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conversation_member

        fields: Dict[str, Callable[[Any], None]] = {
            "anonymousGuestId": lambda n : setattr(self, 'anonymous_guest_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("anonymousGuestId", self.anonymous_guest_id)
    

