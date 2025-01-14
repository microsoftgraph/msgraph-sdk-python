from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.prompt import Prompt

@dataclass
class PlayPromptPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The clientContext property
    client_context: Optional[str] = None
    # The prompts property
    prompts: Optional[list[Prompt]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlayPromptPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlayPromptPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlayPromptPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.prompt import Prompt

        from .....models.prompt import Prompt

        fields: dict[str, Callable[[Any], None]] = {
            "clientContext": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "prompts": lambda n : setattr(self, 'prompts', n.get_collection_of_object_values(Prompt)),
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
        writer.write_str_value("clientContext", self.client_context)
        writer.write_collection_of_object_values("prompts", self.prompts)
        writer.write_additional_data_value(self.additional_data)
    

