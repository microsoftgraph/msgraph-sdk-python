from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')

class EmailIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new EmailIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.emailIdentity"
        # Email address of the user.
        self._email: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmailIdentity()
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. Email address of the user.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. Email address of the user.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("email", self.email)
    

