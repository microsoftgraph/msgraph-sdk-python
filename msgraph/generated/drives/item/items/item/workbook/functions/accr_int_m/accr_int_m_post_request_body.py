from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class AccrIntMPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The basis property
    basis: Optional[Json] = None
    # The issue property
    issue: Optional[Json] = None
    # The par property
    par: Optional[Json] = None
    # The rate property
    rate: Optional[Json] = None
    # The settlement property
    settlement: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccrIntMPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccrIntMPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccrIntMPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "basis": lambda n : setattr(self, 'basis', n.get_object_value(Json)),
            "issue": lambda n : setattr(self, 'issue', n.get_object_value(Json)),
            "par": lambda n : setattr(self, 'par', n.get_object_value(Json)),
            "rate": lambda n : setattr(self, 'rate', n.get_object_value(Json)),
            "settlement": lambda n : setattr(self, 'settlement', n.get_object_value(Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("basis", self.basis)
        writer.write_object_value("issue", self.issue)
        writer.write_object_value("par", self.par)
        writer.write_object_value("rate", self.rate)
        writer.write_object_value("settlement", self.settlement)
        writer.write_additional_data_value(self.additional_data)
    

