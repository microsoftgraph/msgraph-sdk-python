from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ai_interaction_history import AiInteractionHistory
    from .ai_online_meeting import AiOnlineMeeting
    from .entity import Entity

from .entity import Entity

@dataclass
class AiUser(Entity, Parsable):
    # The interactionHistory property
    interaction_history: Optional[AiInteractionHistory] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The onlineMeetings property
    online_meetings: Optional[list[AiOnlineMeeting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AiUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AiUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AiUser()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ai_interaction_history import AiInteractionHistory
        from .ai_online_meeting import AiOnlineMeeting
        from .entity import Entity

        from .ai_interaction_history import AiInteractionHistory
        from .ai_online_meeting import AiOnlineMeeting
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "interactionHistory": lambda n : setattr(self, 'interaction_history', n.get_object_value(AiInteractionHistory)),
            "onlineMeetings": lambda n : setattr(self, 'online_meetings', n.get_collection_of_object_values(AiOnlineMeeting)),
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
        writer.write_object_value("interactionHistory", self.interaction_history)
        writer.write_collection_of_object_values("onlineMeetings", self.online_meetings)
    

