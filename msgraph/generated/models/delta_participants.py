from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .participant import Participant

from .entity import Entity

@dataclass
class DeltaParticipants(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of participants that were updated since the last roster update.
    participants: Optional[list[Participant]] = None
    # The sequence number for the roster update that is used to identify the notification order.
    sequence_number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeltaParticipants:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeltaParticipants
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeltaParticipants()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .participant import Participant

        from .entity import Entity
        from .participant import Participant

        fields: dict[str, Callable[[Any], None]] = {
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(Participant)),
            "sequenceNumber": lambda n : setattr(self, 'sequence_number', n.get_int_value()),
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
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_int_value("sequenceNumber", self.sequence_number)
    

