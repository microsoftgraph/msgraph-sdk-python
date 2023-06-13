from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import call, entity

from . import entity

@dataclass
class ParticipantLeftNotification(entity.Entity):
    # The call property
    call: Optional[call.Call] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the participant under the policy who has left the meeting.
    participant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParticipantLeftNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParticipantLeftNotification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ParticipantLeftNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import call, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "call": lambda n : setattr(self, 'call', n.get_object_value(call.Call)),
            "participantId": lambda n : setattr(self, 'participant_id', n.get_str_value()),
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
        writer.write_object_value("call", self.call)
        writer.write_str_value("participantId", self.participant_id)
    

