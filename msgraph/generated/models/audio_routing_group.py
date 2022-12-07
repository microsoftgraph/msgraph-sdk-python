from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
routing_mode = lazy_import('msgraph.generated.models.routing_mode')

class AudioRoutingGroup(entity.Entity):
    """
    Provides operations to manage the cloudCommunications singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new audioRoutingGroup and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The receivers property
        self._receivers: Optional[List[str]] = None
        # The routingMode property
        self._routing_mode: Optional[routing_mode.RoutingMode] = None
        # The sources property
        self._sources: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AudioRoutingGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AudioRoutingGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AudioRoutingGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "receivers": lambda n : setattr(self, 'receivers', n.get_collection_of_primitive_values(str)),
            "routing_mode": lambda n : setattr(self, 'routing_mode', n.get_enum_value(routing_mode.RoutingMode)),
            "sources": lambda n : setattr(self, 'sources', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def receivers(self,) -> Optional[List[str]]:
        """
        Gets the receivers property value. The receivers property
        Returns: Optional[List[str]]
        """
        return self._receivers
    
    @receivers.setter
    def receivers(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the receivers property value. The receivers property
        Args:
            value: Value to set for the receivers property.
        """
        self._receivers = value
    
    @property
    def routing_mode(self,) -> Optional[routing_mode.RoutingMode]:
        """
        Gets the routingMode property value. The routingMode property
        Returns: Optional[routing_mode.RoutingMode]
        """
        return self._routing_mode
    
    @routing_mode.setter
    def routing_mode(self,value: Optional[routing_mode.RoutingMode] = None) -> None:
        """
        Sets the routingMode property value. The routingMode property
        Args:
            value: Value to set for the routingMode property.
        """
        self._routing_mode = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("receivers", self.receivers)
        writer.write_enum_value("routingMode", self.routing_mode)
        writer.write_collection_of_primitive_values("sources", self.sources)
    
    @property
    def sources(self,) -> Optional[List[str]]:
        """
        Gets the sources property value. The sources property
        Returns: Optional[List[str]]
        """
        return self._sources
    
    @sources.setter
    def sources(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the sources property value. The sources property
        Args:
            value: Value to set for the sources property.
        """
        self._sources = value
    

