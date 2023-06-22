from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set, routing_type

@dataclass
class CallRoute(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The final property
    final: Optional[identity_set.IdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The original property
    original: Optional[identity_set.IdentitySet] = None
    # The routingType property
    routing_type: Optional[routing_type.RoutingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallRoute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallRoute
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CallRoute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set, routing_type

        from . import identity_set, routing_type

        fields: Dict[str, Callable[[Any], None]] = {
            "final": lambda n : setattr(self, 'final', n.get_object_value(identity_set.IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "original": lambda n : setattr(self, 'original', n.get_object_value(identity_set.IdentitySet)),
            "routingType": lambda n : setattr(self, 'routing_type', n.get_enum_value(routing_type.RoutingType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("final", self.final)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("original", self.original)
        writer.write_enum_value("routingType", self.routing_type)
        writer.write_additional_data_value(self.additional_data)
    

