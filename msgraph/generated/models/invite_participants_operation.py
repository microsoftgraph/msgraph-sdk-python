from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import comms_operation, invitation_participant_info

from . import comms_operation

@dataclass
class InviteParticipantsOperation(comms_operation.CommsOperation):
    # The OdataType property
    odata_type: Optional[str] = None
    # The participants to invite.
    participants: Optional[List[invitation_participant_info.InvitationParticipantInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InviteParticipantsOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InviteParticipantsOperation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InviteParticipantsOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import comms_operation, invitation_participant_info

        from . import comms_operation, invitation_participant_info

        fields: Dict[str, Callable[[Any], None]] = {
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(invitation_participant_info.InvitationParticipantInfo)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("participants", self.participants)
    

