from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class RemoveKeyPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the removeKey method.
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new removeKeyPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The keyId property
        self._key_id: Optional[Guid] = None
        # The proof property
        self._proof: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoveKeyPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoveKeyPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RemoveKeyPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "key_id": lambda n : setattr(self, 'key_id', n.get_object_value(Guid)),
            "proof": lambda n : setattr(self, 'proof', n.get_str_value()),
        }
        return fields
    
    @property
    def key_id(self,) -> Optional[Guid]:
        """
        Gets the keyId property value. The keyId property
        Returns: Optional[Guid]
        """
        return self._key_id
    
    @key_id.setter
    def key_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the keyId property value. The keyId property
        Args:
            value: Value to set for the keyId property.
        """
        self._key_id = value
    
    @property
    def proof(self,) -> Optional[str]:
        """
        Gets the proof property value. The proof property
        Returns: Optional[str]
        """
        return self._proof
    
    @proof.setter
    def proof(self,value: Optional[str] = None) -> None:
        """
        Sets the proof property value. The proof property
        Args:
            value: Value to set for the proof property.
        """
        self._proof = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("keyId", self.key_id)
        writer.write_str_value("proof", self.proof)
        writer.write_additional_data_value(self.additional_data)
    

