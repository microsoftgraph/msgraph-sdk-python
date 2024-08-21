from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.prompt import Prompt

@dataclass
class StartHoldMusicPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The clientContext property
    client_context: Optional[str] = None
    # The customPrompt property
    custom_prompt: Optional[Prompt] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StartHoldMusicPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StartHoldMusicPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StartHoldMusicPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models.prompt import Prompt

        from .......models.prompt import Prompt

        fields: Dict[str, Callable[[Any], None]] = {
            "clientContext": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "customPrompt": lambda n : setattr(self, 'custom_prompt', n.get_object_value(Prompt)),
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
        writer.write_object_value("customPrompt", self.custom_prompt)
        writer.write_additional_data_value(self.additional_data)
    

