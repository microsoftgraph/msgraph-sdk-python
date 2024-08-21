from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet
    from .routing_type import RoutingType

@dataclass
class CallRoute(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The final property
    final: Optional[IdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The original property
    original: Optional[IdentitySet] = None
    # The routingType property
    routing_type: Optional[RoutingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallRoute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallRoute
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CallRoute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet
        from .routing_type import RoutingType

        from .identity_set import IdentitySet
        from .routing_type import RoutingType

        fields: Dict[str, Callable[[Any], None]] = {
            "final": lambda n : setattr(self, 'final', n.get_object_value(IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "original": lambda n : setattr(self, 'original', n.get_object_value(IdentitySet)),
            "routingType": lambda n : setattr(self, 'routing_type', n.get_enum_value(RoutingType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("final", self.final)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("original", self.original)
        writer.write_enum_value("routingType", self.routing_type)
        writer.write_additional_data_value(self.additional_data)
    

