from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

password_credential = lazy_import('msgraph.generated.models.password_credential')

class AddPasswordPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the addPassword method.
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
        Instantiates a new addPasswordPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The passwordCredential property
        self._password_credential: Optional[password_credential.PasswordCredential] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddPasswordPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddPasswordPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddPasswordPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "password_credential": lambda n : setattr(self, 'password_credential', n.get_object_value(password_credential.PasswordCredential)),
        }
        return fields
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("passwordCredential", self.password_credential)
        writer.write_additional_data_value(self.additional_data)
    

