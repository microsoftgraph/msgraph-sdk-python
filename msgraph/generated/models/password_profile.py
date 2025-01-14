from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PasswordProfile(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # true if the user must change their password on the next sign-in; otherwise false.
    force_change_password_next_sign_in: Optional[bool] = None
    # If true, at next sign-in, the user must perform a multifactor authentication (MFA) before being forced to change their password. The behavior is identical to forceChangePasswordNextSignIn except that the user is required to first perform a multifactor authentication before password change. After a password change, this property will be automatically reset to false. If not set, default is false.
    force_change_password_next_sign_in_with_mfa: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The password for the user. This property is required when a user is created. It can be updated, but the user will be required to change the password on the next sign-in. The password must satisfy minimum requirements as specified by the user's passwordPolicies property. By default, a strong password is required.
    password: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasswordProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasswordProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasswordProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "forceChangePasswordNextSignIn": lambda n : setattr(self, 'force_change_password_next_sign_in', n.get_bool_value()),
            "forceChangePasswordNextSignInWithMfa": lambda n : setattr(self, 'force_change_password_next_sign_in_with_mfa', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
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
        writer.write_bool_value("forceChangePasswordNextSignIn", self.force_change_password_next_sign_in)
        writer.write_bool_value("forceChangePasswordNextSignInWithMfa", self.force_change_password_next_sign_in_with_mfa)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("password", self.password)
        writer.write_additional_data_value(self.additional_data)
    

