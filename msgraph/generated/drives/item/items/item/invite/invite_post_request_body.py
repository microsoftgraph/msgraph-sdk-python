from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.drive_recipient import DriveRecipient

@dataclass
class InvitePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The expirationDateTime property
    expiration_date_time: Optional[str] = None
    # The message property
    message: Optional[str] = None
    # The password property
    password: Optional[str] = None
    # The recipients property
    recipients: Optional[List[DriveRecipient]] = None
    # The requireSignIn property
    require_sign_in: Optional[bool] = None
    # The retainInheritedPermissions property
    retain_inherited_permissions: Optional[bool] = None
    # The roles property
    roles: Optional[List[str]] = None
    # The sendInvitation property
    send_invitation: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InvitePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InvitePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InvitePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.drive_recipient import DriveRecipient

        from ......models.drive_recipient import DriveRecipient

        fields: Dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "recipients": lambda n : setattr(self, 'recipients', n.get_collection_of_object_values(DriveRecipient)),
            "requireSignIn": lambda n : setattr(self, 'require_sign_in', n.get_bool_value()),
            "retainInheritedPermissions": lambda n : setattr(self, 'retain_inherited_permissions', n.get_bool_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
            "sendInvitation": lambda n : setattr(self, 'send_invitation', n.get_bool_value()),
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
        writer.write_str_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("message", self.message)
        writer.write_str_value("password", self.password)
        writer.write_collection_of_object_values("recipients", self.recipients)
        writer.write_bool_value("requireSignIn", self.require_sign_in)
        writer.write_bool_value("retainInheritedPermissions", self.retain_inherited_permissions)
        writer.write_collection_of_primitive_values("roles", self.roles)
        writer.write_bool_value("sendInvitation", self.send_invitation)
        writer.write_additional_data_value(self.additional_data)
    

