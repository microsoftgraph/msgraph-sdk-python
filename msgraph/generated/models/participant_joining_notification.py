from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import call, entity

from . import entity

class ParticipantJoiningNotification(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ParticipantJoiningNotification and sets the default values.
        """
        super().__init__()
        # The call property
        self._call: Optional[call.Call] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def call(self,) -> Optional[call.Call]:
        """
        Gets the call property value. The call property
        Returns: Optional[call.Call]
        """
        return self._call
    
    @call.setter
    def call(self,value: Optional[call.Call] = None) -> None:
        """
        Sets the call property value. The call property
        Args:
            value: Value to set for the call property.
        """
        self._call = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParticipantJoiningNotification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParticipantJoiningNotification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ParticipantJoiningNotification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import call, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "call": lambda n : setattr(self, 'call', n.get_object_value(call.Call)),
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
    

