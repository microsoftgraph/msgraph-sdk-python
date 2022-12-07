from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

key_credential = lazy_import('msgraph.generated.models.key_credential')
password_credential = lazy_import('msgraph.generated.models.password_credential')

class AddKeyPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the addKey method.
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
        Instantiates a new addKeyPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The keyCredential property
        self._key_credential: Optional[key_credential.KeyCredential] = None
        # The passwordCredential property
        self._password_credential: Optional[password_credential.PasswordCredential] = None
        # The proof property
        self._proof: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddKeyPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddKeyPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddKeyPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "key_credential": lambda n : setattr(self, 'key_credential', n.get_object_value(key_credential.KeyCredential)),
            "password_credential": lambda n : setattr(self, 'password_credential', n.get_object_value(password_credential.PasswordCredential)),
            "proof": lambda n : setattr(self, 'proof', n.get_str_value()),
        }
        return fields
    
    @property
    def key_credential(self,) -> Optional[key_credential.KeyCredential]:
        """
        Gets the keyCredential property value. The keyCredential property
        Returns: Optional[key_credential.KeyCredential]
        """
        return self._key_credential
    
    @key_credential.setter
    def key_credential(self,value: Optional[key_credential.KeyCredential] = None) -> None:
        """
        Sets the keyCredential property value. The keyCredential property
        Args:
            value: Value to set for the keyCredential property.
        """
        self._key_credential = value
    
    @property
    def password_credential(self,) -> Optional[password_credential.PasswordCredential]:
        """
        Gets the passwordCredential property value. The passwordCredential property
        Returns: Optional[password_credential.PasswordCredential]
        """
        return self._password_credential
    
    @password_credential.setter
    def password_credential(self,value: Optional[password_credential.PasswordCredential] = None) -> None:
        """
        Sets the passwordCredential property value. The passwordCredential property
        Args:
            value: Value to set for the passwordCredential property.
        """
        self._password_credential = value
    
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
        writer.write_object_value("keyCredential", self.key_credential)
        writer.write_object_value("passwordCredential", self.password_credential)
        writer.write_str_value("proof", self.proof)
        writer.write_additional_data_value(self.additional_data)
    

