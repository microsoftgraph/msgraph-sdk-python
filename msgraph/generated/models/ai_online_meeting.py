from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call_ai_insight import CallAiInsight
    from .entity import Entity

from .entity import Entity

@dataclass
class AiOnlineMeeting(Entity, Parsable):
    # The aiInsights property
    ai_insights: Optional[list[CallAiInsight]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AiOnlineMeeting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AiOnlineMeeting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AiOnlineMeeting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .call_ai_insight import CallAiInsight
        from .entity import Entity

        from .call_ai_insight import CallAiInsight
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "aiInsights": lambda n : setattr(self, 'ai_insights', n.get_collection_of_object_values(CallAiInsight)),
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
        writer.write_collection_of_object_values("aiInsights", self.ai_insights)
    

