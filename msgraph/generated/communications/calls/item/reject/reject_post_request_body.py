from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.reject_reason import RejectReason

@dataclass
class RejectPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The callbackUri property
    callback_uri: Optional[str] = None
    # The reason property
    reason: Optional[RejectReason] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RejectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RejectPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RejectPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.reject_reason import RejectReason

        from .....models.reject_reason import RejectReason

        fields: Dict[str, Callable[[Any], None]] = {
            "callbackUri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(RejectReason)),
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
        from .....models.reject_reason import RejectReason

        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_enum_value("reason", self.reason)
        writer.write_additional_data_value(self.additional_data)
    

