from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import key_credential, password_credential

@dataclass
class AddKeyPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The keyCredential property
    key_credential: Optional[key_credential.KeyCredential] = None
    # The passwordCredential property
    password_credential: Optional[password_credential.PasswordCredential] = None
    # The proof property
    proof: Optional[str] = None
    
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
        from ....models import key_credential, password_credential

        fields: Dict[str, Callable[[Any], None]] = {
            "keyCredential": lambda n : setattr(self, 'key_credential', n.get_object_value(key_credential.KeyCredential)),
            "passwordCredential": lambda n : setattr(self, 'password_credential', n.get_object_value(password_credential.PasswordCredential)),
            "proof": lambda n : setattr(self, 'proof', n.get_str_value()),
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
        writer.write_object_value("keyCredential", self.key_credential)
        writer.write_object_value("passwordCredential", self.password_credential)
        writer.write_str_value("proof", self.proof)
        writer.write_additional_data_value(self.additional_data)
    

