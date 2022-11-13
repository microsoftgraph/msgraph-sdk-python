from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import comms_operation, invitation_participant_info

class InviteParticipantsOperation(comms_operation.CommsOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new InviteParticipantsOperation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.inviteParticipantsOperation"
        # The participants to invite.
        self._participants: Optional[List[invitation_participant_info.InvitationParticipantInfo]] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InviteParticipantsOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InviteParticipantsOperation
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return InviteParticipantsOperation()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(invitation_participant_info.InvitationParticipantInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    @property
    def participants(self,) -> Optional[List[invitation_participant_info.InvitationParticipantInfo]]:
        """
        Gets the participants property value. The participants to invite.
        Returns: Optional[List[invitation_participant_info.InvitationParticipantInfo]]
        """
        return self._participants

    @participants.setter
    def participants(self,value: Optional[List[invitation_participant_info.InvitationParticipantInfo]] = None) -> None:
        """
        Sets the participants property value. The participants to invite.
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
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("participants", self.participants)


