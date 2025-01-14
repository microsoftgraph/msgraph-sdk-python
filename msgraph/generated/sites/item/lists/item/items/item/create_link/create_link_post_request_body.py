from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.drive_recipient import DriveRecipient

@dataclass
class CreateLinkPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The expirationDateTime property
    expiration_date_time: Optional[datetime.datetime] = None
    # The message property
    message: Optional[str] = None
    # The password property
    password: Optional[str] = None
    # The recipients property
    recipients: Optional[list[DriveRecipient]] = None
    # The retainInheritedPermissions property
    retain_inherited_permissions: Optional[bool] = None
    # The scope property
    scope: Optional[str] = None
    # The sendNotification property
    send_notification: Optional[bool] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateLinkPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateLinkPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateLinkPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ........models.drive_recipient import DriveRecipient

        from ........models.drive_recipient import DriveRecipient

        fields: dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_object_values(DriveRecipient)),
            "retainInheritedPermissions": lambda n : setattr(self, 'retain_inherited_permissions', n.get_bool_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "sendNotification": lambda n : setattr(self, 'send_notification', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("message", self.message)
        writer.write_str_value("password", self.password)
        writer.write_collection_of_object_values("recipients", self.recipients)
        writer.write_bool_value("retainInheritedPermissions", self.retain_inherited_permissions)
        writer.write_str_value("scope", self.scope)
        writer.write_bool_value("sendNotification", self.send_notification)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

