from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .retention_event_type import RetentionEventType

from ..entity import Entity

@dataclass
class TriggerTypesRoot(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The retentionEventTypes property
    retention_event_types: Optional[List[RetentionEventType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TriggerTypesRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TriggerTypesRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TriggerTypesRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .retention_event_type import RetentionEventType

        from ..entity import Entity
        from .retention_event_type import RetentionEventType

        fields: Dict[str, Callable[[Any], None]] = {
            "retentionEventTypes": lambda n : setattr(self, 'retention_event_types', n.get_collection_of_object_values(RetentionEventType)),
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
        writer.write_collection_of_object_values("retentionEventTypes", self.retention_event_types)
    

