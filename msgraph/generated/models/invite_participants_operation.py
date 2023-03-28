from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

comms_operation = lazy_import('msgraph.generated.models.comms_operation')
invitation_participant_info = lazy_import('msgraph.generated.models.invitation_participant_info')

class InviteParticipantsOperation(comms_operation.CommsOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new InviteParticipantsOperation and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
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
        if parse_node is None:
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("participants", self.participants)
    

