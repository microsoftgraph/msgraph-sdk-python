from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call import Call
    from .entity import Entity

from .entity import Entity

@dataclass
class ParticipantLeftNotification(Entity, Parsable):
    # The call property
    call: Optional[Call] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the participant under the policy who has left the meeting.
    participant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ParticipantLeftNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ParticipantLeftNotification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ParticipantLeftNotification()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .call import Call
        from .entity import Entity

        from .call import Call
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "call": lambda n : setattr(self, 'call', n.get_object_value(Call)),
            "participantId": lambda n : setattr(self, 'participant_id', n.get_str_value()),
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
        writer.write_object_value("call", self.call)
        writer.write_str_value("participantId", self.participant_id)
    

