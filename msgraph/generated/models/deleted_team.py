from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import channel, entity

from . import entity

class DeletedTeam(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new DeletedTeam and sets the default values.
        """
        super().__init__()
        # The channels that are either shared with this deleted team or created in this deleted team.
        self._channels: Optional[List[channel.Channel]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def channels(self,) -> Optional[List[channel.Channel]]:
        """
        Gets the channels property value. The channels that are either shared with this deleted team or created in this deleted team.
        Returns: Optional[List[channel.Channel]]
        """
        return self._channels
    
    @channels.setter
    def channels(self,value: Optional[List[channel.Channel]] = None) -> None:
        """
        Sets the channels property value. The channels that are either shared with this deleted team or created in this deleted team.
        Args:
            value: Value to set for the channels property.
        """
        self._channels = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeletedTeam:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeletedTeam
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeletedTeam()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import channel, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "channels": lambda n : setattr(self, 'channels', n.get_collection_of_object_values(channel.Channel)),
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
        writer.write_collection_of_object_values("channels", self.channels)
    

