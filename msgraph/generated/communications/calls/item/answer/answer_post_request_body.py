from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import incoming_call_options, media_config, modality

class AnswerPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new answerPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The acceptedModalities property
        self._accepted_modalities: Optional[List[modality.Modality]] = None
        # The callOptions property
        self._call_options: Optional[incoming_call_options.IncomingCallOptions] = None
        # The callbackUri property
        self._callback_uri: Optional[str] = None
        # The mediaConfig property
        self._media_config: Optional[media_config.MediaConfig] = None
        # The participantCapacity property
        self._participant_capacity: Optional[int] = None
    
    @property
    def accepted_modalities(self,) -> Optional[List[modality.Modality]]:
        """
        Gets the acceptedModalities property value. The acceptedModalities property
        Returns: Optional[List[modality.Modality]]
        """
        return self._accepted_modalities
    
    @accepted_modalities.setter
    def accepted_modalities(self,value: Optional[List[modality.Modality]] = None) -> None:
        """
        Sets the acceptedModalities property value. The acceptedModalities property
        Args:
            value: Value to set for the accepted_modalities property.
        """
        self._accepted_modalities = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def call_options(self,) -> Optional[incoming_call_options.IncomingCallOptions]:
        """
        Gets the callOptions property value. The callOptions property
        Returns: Optional[incoming_call_options.IncomingCallOptions]
        """
        return self._call_options
    
    @call_options.setter
    def call_options(self,value: Optional[incoming_call_options.IncomingCallOptions] = None) -> None:
        """
        Sets the callOptions property value. The callOptions property
        Args:
            value: Value to set for the call_options property.
        """
        self._call_options = value
    
    @property
    def callback_uri(self,) -> Optional[str]:
        """
        Gets the callbackUri property value. The callbackUri property
        Returns: Optional[str]
        """
        return self._callback_uri
    
    @callback_uri.setter
    def callback_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the callbackUri property value. The callbackUri property
        Args:
            value: Value to set for the callback_uri property.
        """
        self._callback_uri = value
    
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
    
    @property
    def media_config(self,) -> Optional[media_config.MediaConfig]:
        """
        Gets the mediaConfig property value. The mediaConfig property
        Returns: Optional[media_config.MediaConfig]
        """
        return self._media_config
    
    @media_config.setter
    def media_config(self,value: Optional[media_config.MediaConfig] = None) -> None:
        """
        Sets the mediaConfig property value. The mediaConfig property
        Args:
            value: Value to set for the media_config property.
        """
        self._media_config = value
    
    @property
    def participant_capacity(self,) -> Optional[int]:
        """
        Gets the participantCapacity property value. The participantCapacity property
        Returns: Optional[int]
        """
        return self._participant_capacity
    
    @participant_capacity.setter
    def participant_capacity(self,value: Optional[int] = None) -> None:
        """
        Sets the participantCapacity property value. The participantCapacity property
        Args:
            value: Value to set for the participant_capacity property.
        """
        self._participant_capacity = value
    
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
    

