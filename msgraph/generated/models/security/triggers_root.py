from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import retention_event
    from .. import entity

from .. import entity

class TriggersRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new triggersRoot and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The retentionEvents property
        self._retention_events: Optional[List[retention_event.RetentionEvent]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TriggersRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TriggersRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TriggersRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import retention_event
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "retentionEvents": lambda n : setattr(self, 'retention_events', n.get_collection_of_object_values(retention_event.RetentionEvent)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def retention_events(self,) -> Optional[List[retention_event.RetentionEvent]]:
        """
        Gets the retentionEvents property value. The retentionEvents property
        Returns: Optional[List[retention_event.RetentionEvent]]
        """
        return self._retention_events
    
    @retention_events.setter
    def retention_events(self,value: Optional[List[retention_event.RetentionEvent]] = None) -> None:
        """
        Sets the retentionEvents property value. The retentionEvents property
        Args:
            value: Value to set for the retention_events property.
        """
        self._retention_events = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("retentionEvents", self.retention_events)
    

