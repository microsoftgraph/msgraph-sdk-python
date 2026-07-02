from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_identity import EmailIdentity
    from .notification_recipients_type import NotificationRecipientsType

@dataclass
class NotificationRecipients(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # A list of users or groups that receive notifications. Only specify this property when role is set to custom.
    custom_recipients: Optional[list[EmailIdentity]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The role property
    role: Optional[NotificationRecipientsType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NotificationRecipients:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NotificationRecipients
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NotificationRecipients()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_identity import EmailIdentity
        from .notification_recipients_type import NotificationRecipientsType

        from .email_identity import EmailIdentity
        from .notification_recipients_type import NotificationRecipientsType

        fields: dict[str, Callable[[Any], None]] = {
            "customRecipients": lambda n : setattr(self, 'custom_recipients', n.get_collection_of_object_values(EmailIdentity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_collection_of_enum_values(NotificationRecipientsType)),
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
        writer.write_collection_of_object_values("customRecipients", self.custom_recipients)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

