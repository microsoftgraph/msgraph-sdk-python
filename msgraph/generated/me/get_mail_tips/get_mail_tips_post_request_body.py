from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import mail_tips_type

@dataclass
class GetMailTipsPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The EmailAddresses property
    email_addresses: Optional[List[str]] = None
    # The MailTipsOptions property
    mail_tips_options: Optional[mail_tips_type.MailTipsType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetMailTipsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetMailTipsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetMailTipsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models import mail_tips_type

        fields: Dict[str, Callable[[Any], None]] = {
            "EmailAddresses": lambda n : setattr(self, 'email_addresses', n.get_collection_of_primitive_values(str)),
            "MailTipsOptions": lambda n : setattr(self, 'mail_tips_options', n.get_enum_value(mail_tips_type.MailTipsType)),
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
        writer.write_collection_of_primitive_values("EmailAddresses", self.email_addresses)
        writer.write_enum_value("MailTipsOptions", self.mail_tips_options)
        writer.write_additional_data_value(self.additional_data)
    

