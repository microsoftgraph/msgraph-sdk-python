from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.mail_tips_type import MailTipsType

@dataclass
class GetMailTipsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The EmailAddresses property
    email_addresses: Optional[list[str]] = None
    # The MailTipsOptions property
    mail_tips_options: Optional[MailTipsType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetMailTipsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetMailTipsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetMailTipsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....models.mail_tips_type import MailTipsType

        from ....models.mail_tips_type import MailTipsType

        fields: dict[str, Callable[[Any], None]] = {
            "EmailAddresses": lambda n : setattr(self, 'email_addresses', n.get_collection_of_primitive_values(str)),
            "MailTipsOptions": lambda n : setattr(self, 'mail_tips_options', n.get_collection_of_enum_values(MailTipsType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("EmailAddresses", self.email_addresses)
        writer.write_enum_value("MailTipsOptions", self.mail_tips_options)
        writer.write_additional_data_value(self.additional_data)
    

