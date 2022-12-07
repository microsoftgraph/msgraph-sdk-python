from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conversation_member = lazy_import('msgraph.generated.models.conversation_member')

class AnonymousGuestConversationMember(conversation_member.ConversationMember):
    @property
    def anonymous_guest_id(self,) -> Optional[str]:
        """
        Gets the anonymousGuestId property value. The anonymousGuestId property
        Returns: Optional[str]
        """
        return self._anonymous_guest_id
    
    @anonymous_guest_id.setter
    def anonymous_guest_id(self,value: Optional[str] = None) -> None:
        """
        Sets the anonymousGuestId property value. The anonymousGuestId property
        Args:
            value: Value to set for the anonymousGuestId property.
        """
        self._anonymous_guest_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AnonymousGuestConversationMember and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.anonymousGuestConversationMember"
        # The anonymousGuestId property
        self._anonymous_guest_id: Optional[str] = None
    
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
        fields = {
            "anonymous_guest_id": lambda n : setattr(self, 'anonymous_guest_id', n.get_str_value()),
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
    

