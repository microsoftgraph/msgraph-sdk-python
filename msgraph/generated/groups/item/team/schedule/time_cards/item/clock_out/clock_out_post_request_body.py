from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.item_body import ItemBody

@dataclass
class ClockOutPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The isAtApprovedLocation property
    is_at_approved_location: Optional[bool] = None
    # The notes property
    notes: Optional[ItemBody] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClockOutPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClockOutPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClockOutPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ........models.item_body import ItemBody

        from ........models.item_body import ItemBody

        fields: dict[str, Callable[[Any], None]] = {
            "isAtApprovedLocation": lambda n : setattr(self, 'is_at_approved_location', n.get_bool_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(ItemBody)),
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
        writer.write_bool_value("isAtApprovedLocation", self.is_at_approved_location)
        writer.write_object_value("notes", self.notes)
        writer.write_additional_data_value(self.additional_data)
    

