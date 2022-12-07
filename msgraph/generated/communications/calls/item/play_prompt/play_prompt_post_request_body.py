from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

prompt = lazy_import('msgraph.generated.models.prompt')

class PlayPromptPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the playPrompt method.
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
        Instantiates a new playPromptPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The clientContext property
        self._client_context: Optional[str] = None
        # The prompts property
        self._prompts: Optional[List[prompt.Prompt]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlayPromptPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlayPromptPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlayPromptPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "client_context": lambda n : setattr(self, 'client_context', n.get_str_value()),
            "prompts": lambda n : setattr(self, 'prompts', n.get_collection_of_object_values(prompt.Prompt)),
        }
        return fields
    
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
        writer.write_str_value("clientContext", self.client_context)
        writer.write_collection_of_object_values("prompts", self.prompts)
        writer.write_additional_data_value(self.additional_data)
    

