from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import incoming_call_options, media_config, modality

@dataclass
class AnswerPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The acceptedModalities property
    accepted_modalities: Optional[List[modality.Modality]] = None
    # The callOptions property
    call_options: Optional[incoming_call_options.IncomingCallOptions] = None
    # The callbackUri property
    callback_uri: Optional[str] = None
    # The mediaConfig property
    media_config: Optional[media_config.MediaConfig] = None
    # The participantCapacity property
    participant_capacity: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AnswerPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AnswerPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AnswerPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import incoming_call_options, media_config, modality

        fields: Dict[str, Callable[[Any], None]] = {
            "acceptedModalities": lambda n : setattr(self, 'accepted_modalities', n.get_collection_of_enum_values(modality.Modality)),
            "callbackUri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "callOptions": lambda n : setattr(self, 'call_options', n.get_object_value(incoming_call_options.IncomingCallOptions)),
            "mediaConfig": lambda n : setattr(self, 'media_config', n.get_object_value(media_config.MediaConfig)),
            "participantCapacity": lambda n : setattr(self, 'participant_capacity', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("acceptedModalities", self.accepted_modalities)
        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_object_value("callOptions", self.call_options)
        writer.write_object_value("mediaConfig", self.media_config)
        writer.write_int_value("participantCapacity", self.participant_capacity)
        writer.write_additional_data_value(self.additional_data)
    

