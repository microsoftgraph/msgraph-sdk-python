from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.incoming_call_options import IncomingCallOptions
    from .....models.media_config import MediaConfig
    from .....models.modality import Modality

@dataclass
class AnswerPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The acceptedModalities property
    accepted_modalities: Optional[list[Modality]] = None
    # The callOptions property
    call_options: Optional[IncomingCallOptions] = None
    # The callbackUri property
    callback_uri: Optional[str] = None
    # The mediaConfig property
    media_config: Optional[MediaConfig] = None
    # The participantCapacity property
    participant_capacity: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnswerPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnswerPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnswerPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.incoming_call_options import IncomingCallOptions
        from .....models.media_config import MediaConfig
        from .....models.modality import Modality

        from .....models.incoming_call_options import IncomingCallOptions
        from .....models.media_config import MediaConfig
        from .....models.modality import Modality

        fields: dict[str, Callable[[Any], None]] = {
            "acceptedModalities": lambda n : setattr(self, 'accepted_modalities', n.get_collection_of_enum_values(Modality)),
            "callOptions": lambda n : setattr(self, 'call_options', n.get_object_value(IncomingCallOptions)),
            "callbackUri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "mediaConfig": lambda n : setattr(self, 'media_config', n.get_object_value(MediaConfig)),
            "participantCapacity": lambda n : setattr(self, 'participant_capacity', n.get_int_value()),
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
        writer.write_collection_of_enum_values("acceptedModalities", self.accepted_modalities)
        writer.write_object_value("callOptions", self.call_options)
        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_object_value("mediaConfig", self.media_config)
        writer.write_int_value("participantCapacity", self.participant_capacity)
        writer.write_additional_data_value(self.additional_data)
    

