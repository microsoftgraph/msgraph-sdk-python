from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.presence_status_message import PresenceStatusMessage

@dataclass
class SetStatusMessagePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The statusMessage property
    status_message: Optional[PresenceStatusMessage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SetStatusMessagePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SetStatusMessagePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SetStatusMessagePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.presence_status_message import PresenceStatusMessage

        from .....models.presence_status_message import PresenceStatusMessage

        fields: dict[str, Callable[[Any], None]] = {
            "statusMessage": lambda n : setattr(self, 'status_message', n.get_object_value(PresenceStatusMessage)),
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
        writer.write_object_value("statusMessage", self.status_message)
        writer.write_additional_data_value(self.additional_data)
    

