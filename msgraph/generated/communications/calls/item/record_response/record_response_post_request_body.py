from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

prompt = lazy_import('msgraph.generated.models.prompt')

class RecordResponsePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the recordResponse method.
    """
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
    def barge_in_allowed(self,) -> Optional[bool]:
        """
        Gets the bargeInAllowed property value. The bargeInAllowed property
        Returns: Optional[bool]
        """
        return self._barge_in_allowed
    
    @barge_in_allowed.setter
    def barge_in_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the bargeInAllowed property value. The bargeInAllowed property
        Args:
            value: Value to set for the bargeInAllowed property.
        """
        self._barge_in_allowed = value
    
    @property
    def client_context(self,) -> Optional[str]:
        """
        Gets the clientContext property value. The clientContext property
        Returns: Optional[str]
        """
        return self._client_context
    
    @client_context.setter
    def client_context(self,value: Optional[str] = None) -> None:
        """
        Sets the clientContext property value. The clientContext property
        Args:
            value: Value to set for the clientContext property.
        """
        self._client_context = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new recordResponsePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The bargeInAllowed property
        self._barge_in_allowed: Optional[bool] = None
        # The clientContext property
        self._client_context: Optional[str] = None
        # The initialSilenceTimeoutInSeconds property
        self._initial_silence_timeout_in_seconds: Optional[int] = None
        # The maxRecordDurationInSeconds property
        self._max_record_duration_in_seconds: Optional[int] = None
        # The maxSilenceTimeoutInSeconds property
        self._max_silence_timeout_in_seconds: Optional[int] = None
        # The playBeep property
        self._play_beep: Optional[bool] = None
        # The prompts property
        self._prompts: Optional[List[prompt.Prompt]] = None
        # The stopTones property
        self._stop_tones: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecordResponsePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecordResponsePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecordResponsePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "barge_in_allowed": lambda n : setattr(self, 'barge_in_allowed', n.get_bool_value()),
            "client_context": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "initial_silence_timeout_in_seconds": lambda n : setattr(self, 'initial_silence_timeout_in_seconds', n.get_int_value()),
            "max_record_duration_in_seconds": lambda n : setattr(self, 'max_record_duration_in_seconds', n.get_int_value()),
            "max_silence_timeout_in_seconds": lambda n : setattr(self, 'max_silence_timeout_in_seconds', n.get_int_value()),
            "play_beep": lambda n : setattr(self, 'play_beep', n.get_bool_value()),
            "prompts": lambda n : setattr(self, 'prompts', n.get_collection_of_object_values(prompt.Prompt)),
            "stop_tones": lambda n : setattr(self, 'stop_tones', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def initial_silence_timeout_in_seconds(self,) -> Optional[int]:
        """
        Gets the initialSilenceTimeoutInSeconds property value. The initialSilenceTimeoutInSeconds property
        Returns: Optional[int]
        """
        return self._initial_silence_timeout_in_seconds
    
    @initial_silence_timeout_in_seconds.setter
    def initial_silence_timeout_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the initialSilenceTimeoutInSeconds property value. The initialSilenceTimeoutInSeconds property
        Args:
            value: Value to set for the initialSilenceTimeoutInSeconds property.
        """
        self._initial_silence_timeout_in_seconds = value
    
    @property
    def max_record_duration_in_seconds(self,) -> Optional[int]:
        """
        Gets the maxRecordDurationInSeconds property value. The maxRecordDurationInSeconds property
        Returns: Optional[int]
        """
        return self._max_record_duration_in_seconds
    
    @max_record_duration_in_seconds.setter
    def max_record_duration_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the maxRecordDurationInSeconds property value. The maxRecordDurationInSeconds property
        Args:
            value: Value to set for the maxRecordDurationInSeconds property.
        """
        self._max_record_duration_in_seconds = value
    
    @property
    def max_silence_timeout_in_seconds(self,) -> Optional[int]:
        """
        Gets the maxSilenceTimeoutInSeconds property value. The maxSilenceTimeoutInSeconds property
        Returns: Optional[int]
        """
        return self._max_silence_timeout_in_seconds
    
    @max_silence_timeout_in_seconds.setter
    def max_silence_timeout_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the maxSilenceTimeoutInSeconds property value. The maxSilenceTimeoutInSeconds property
        Args:
            value: Value to set for the maxSilenceTimeoutInSeconds property.
        """
        self._max_silence_timeout_in_seconds = value
    
    @property
    def play_beep(self,) -> Optional[bool]:
        """
        Gets the playBeep property value. The playBeep property
        Returns: Optional[bool]
        """
        return self._play_beep
    
    @play_beep.setter
    def play_beep(self,value: Optional[bool] = None) -> None:
        """
        Sets the playBeep property value. The playBeep property
        Args:
            value: Value to set for the playBeep property.
        """
        self._play_beep = value
    
    @property
    def prompts(self,) -> Optional[List[prompt.Prompt]]:
        """
        Gets the prompts property value. The prompts property
        Returns: Optional[List[prompt.Prompt]]
        """
        return self._prompts
    
    @prompts.setter
    def prompts(self,value: Optional[List[prompt.Prompt]] = None) -> None:
        """
        Sets the prompts property value. The prompts property
        Args:
            value: Value to set for the prompts property.
        """
        self._prompts = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("bargeInAllowed", self.barge_in_allowed)
        writer.write_str_value("clientContext", self.client_context)
        writer.write_int_value("initialSilenceTimeoutInSeconds", self.initial_silence_timeout_in_seconds)
        writer.write_int_value("maxRecordDurationInSeconds", self.max_record_duration_in_seconds)
        writer.write_int_value("maxSilenceTimeoutInSeconds", self.max_silence_timeout_in_seconds)
        writer.write_bool_value("playBeep", self.play_beep)
        writer.write_collection_of_object_values("prompts", self.prompts)
        writer.write_collection_of_primitive_values("stopTones", self.stop_tones)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def stop_tones(self,) -> Optional[List[str]]:
        """
        Gets the stopTones property value. The stopTones property
        Returns: Optional[List[str]]
        """
        return self._stop_tones
    
    @stop_tones.setter
    def stop_tones(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the stopTones property value. The stopTones property
        Args:
            value: Value to set for the stopTones property.
        """
        self._stop_tones = value
    

