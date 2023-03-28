from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import password_credential

class AddPasswordPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new addPasswordPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The passwordCredential property
        self._password_credential: Optional[password_credential.PasswordCredential] = None
    
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
        from ....models import password_credential

        fields: Dict[str, Callable[[Any], None]] = {
            "passwordCredential": lambda n : setattr(self, 'password_credential', n.get_object_value(password_credential.PasswordCredential)),
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
            value: Value to set for the password_credential property.
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
    

