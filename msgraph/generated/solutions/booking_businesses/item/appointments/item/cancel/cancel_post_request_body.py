from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CancelPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the cancel method.
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
    def cancellation_message(self,) -> Optional[str]:
        """
        Gets the cancellationMessage property value. The cancellationMessage property
        Returns: Optional[str]
        """
        return self._cancellation_message
    
    @cancellation_message.setter
    def cancellation_message(self,value: Optional[str] = None) -> None:
        """
        Sets the cancellationMessage property value. The cancellationMessage property
        Args:
            value: Value to set for the cancellationMessage property.
        """
        self._cancellation_message = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new cancelPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cancellationMessage property
        self._cancellation_message: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CancelPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CancelPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CancelPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cancellation_message": lambda n : setattr(self, 'cancellation_message', n.get_str_value()),
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
        writer.write_str_value("cancellationMessage", self.cancellation_message)
        writer.write_additional_data_value(self.additional_data)
    

