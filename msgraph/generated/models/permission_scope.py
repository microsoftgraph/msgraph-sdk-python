from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class PermissionScope(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A description of the delegated permissions, intended to be read by an administrator granting the permission on behalf of all users. This text appears in tenant-wide admin consent experiences.
    admin_consent_description: Optional[str] = None
    # The permission's title, intended to be read by an administrator granting the permission on behalf of all users.
    admin_consent_display_name: Optional[str] = None
    # Unique delegated permission identifier inside the collection of delegated permissions defined for a resource application.
    id: Optional[UUID] = None
    # When you create or update a permission, this property must be set to true (which is the default). To delete a permission, this property must first be set to false.  At that point, in a subsequent call, the permission may be removed.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The origin property
    origin: Optional[str] = None
    # The possible values are: User and Admin. Specifies whether this delegated permission should be considered safe for non-admin users to consent to on behalf of themselves, or whether an administrator consent should always be required. While Microsoft Graph defines the default consent requirement for each permission, the tenant administrator may override the behavior in their organization (by allowing, restricting, or limiting user consent to this delegated permission). For more information, see Configure how users consent to applications.
    type: Optional[str] = None
    # A description of the delegated permissions, intended to be read by a user granting the permission on their own behalf. This text appears in consent experiences where the user is consenting only on behalf of themselves.
    user_consent_description: Optional[str] = None
    # A title for the permission, intended to be read by a user granting the permission on their own behalf. This text appears in consent experiences where the user is consenting only on behalf of themselves.
    user_consent_display_name: Optional[str] = None
    # Specifies the value to include in the scp (scope) claim in access tokens. Must not exceed 120 characters in length. Allowed characters are : ! # $ % & ' ( ) * + , - . / : ;  =  ? @ [ ] ^ + _  {  } ~, and characters in the ranges 0-9, A-Z and a-z. Any other character, including the space character, aren't allowed. May not begin with ..
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PermissionScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PermissionScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "adminConsentDescription": lambda n : setattr(self, 'admin_consent_description', n.get_str_value()),
            "adminConsentDisplayName": lambda n : setattr(self, 'admin_consent_display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "origin": lambda n : setattr(self, 'origin', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "userConsentDescription": lambda n : setattr(self, 'user_consent_description', n.get_str_value()),
            "userConsentDisplayName": lambda n : setattr(self, 'user_consent_display_name', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("adminConsentDescription", self.admin_consent_description)
        writer.write_str_value("adminConsentDisplayName", self.admin_consent_display_name)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("origin", self.origin)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userConsentDescription", self.user_consent_description)
        writer.write_str_value("userConsentDisplayName", self.user_consent_display_name)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

