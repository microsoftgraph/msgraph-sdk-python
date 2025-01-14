from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.prompt import Prompt

@dataclass
class RecordResponsePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The bargeInAllowed property
    barge_in_allowed: Optional[bool] = None
    # The clientContext property
    client_context: Optional[str] = None
    # The initialSilenceTimeoutInSeconds property
    initial_silence_timeout_in_seconds: Optional[int] = None
    # The maxRecordDurationInSeconds property
    max_record_duration_in_seconds: Optional[int] = None
    # The maxSilenceTimeoutInSeconds property
    max_silence_timeout_in_seconds: Optional[int] = None
    # The playBeep property
    play_beep: Optional[bool] = None
    # The prompts property
    prompts: Optional[list[Prompt]] = None
    # The stopTones property
    stop_tones: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecordResponsePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecordResponsePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecordResponsePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.prompt import Prompt

        from .....models.prompt import Prompt

        fields: dict[str, Callable[[Any], None]] = {
            "bargeInAllowed": lambda n : setattr(self, 'barge_in_allowed', n.get_bool_value()),
            "clientContext": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "initialSilenceTimeoutInSeconds": lambda n : setattr(self, 'initial_silence_timeout_in_seconds', n.get_int_value()),
            "maxRecordDurationInSeconds": lambda n : setattr(self, 'max_record_duration_in_seconds', n.get_int_value()),
            "maxSilenceTimeoutInSeconds": lambda n : setattr(self, 'max_silence_timeout_in_seconds', n.get_int_value()),
            "playBeep": lambda n : setattr(self, 'play_beep', n.get_bool_value()),
            "prompts": lambda n : setattr(self, 'prompts', n.get_collection_of_object_values(Prompt)),
            "stopTones": lambda n : setattr(self, 'stop_tones', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("bargeInAllowed", self.barge_in_allowed)
        writer.write_str_value("clientContext", self.client_context)
        writer.write_int_value("initialSilenceTimeoutInSeconds", self.initial_silence_timeout_in_seconds)
        writer.write_int_value("maxRecordDurationInSeconds", self.max_record_duration_in_seconds)
        writer.write_int_value("maxSilenceTimeoutInSeconds", self.max_silence_timeout_in_seconds)
        writer.write_bool_value("playBeep", self.play_beep)
        writer.write_collection_of_object_values("prompts", self.prompts)
        writer.write_collection_of_primitive_values("stopTones", self.stop_tones)
        writer.write_additional_data_value(self.additional_data)
    

