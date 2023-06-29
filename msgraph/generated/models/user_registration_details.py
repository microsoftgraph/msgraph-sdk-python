from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .sign_in_user_type import SignInUserType
    from .user_default_authentication_method import UserDefaultAuthenticationMethod

from .entity import Entity

@dataclass
class UserRegistrationDetails(Entity):
    # The isAdmin property
    is_admin: Optional[bool] = None
    # The isMfaCapable property
    is_mfa_capable: Optional[bool] = None
    # The isMfaRegistered property
    is_mfa_registered: Optional[bool] = None
    # The isPasswordlessCapable property
    is_passwordless_capable: Optional[bool] = None
    # The isSsprCapable property
    is_sspr_capable: Optional[bool] = None
    # The isSsprEnabled property
    is_sspr_enabled: Optional[bool] = None
    # The isSsprRegistered property
    is_sspr_registered: Optional[bool] = None
    # The isSystemPreferredAuthenticationMethodEnabled property
    is_system_preferred_authentication_method_enabled: Optional[bool] = None
    # The lastUpdatedDateTime property
    last_updated_date_time: Optional[datetime.datetime] = None
    # The methodsRegistered property
    methods_registered: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The systemPreferredAuthenticationMethods property
    system_preferred_authentication_methods: Optional[List[str]] = None
    # The userDisplayName property
    user_display_name: Optional[str] = None
    # The userPreferredMethodForSecondaryAuthentication property
    user_preferred_method_for_secondary_authentication: Optional[UserDefaultAuthenticationMethod] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    # The userType property
    user_type: Optional[SignInUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserRegistrationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserRegistrationDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserRegistrationDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .sign_in_user_type import SignInUserType
        from .user_default_authentication_method import UserDefaultAuthenticationMethod

        from .entity import Entity
        from .sign_in_user_type import SignInUserType
        from .user_default_authentication_method import UserDefaultAuthenticationMethod

        fields: Dict[str, Callable[[Any], None]] = {
            "isAdmin": lambda n : setattr(self, 'is_admin', n.get_bool_value()),
            "isMfaCapable": lambda n : setattr(self, 'is_mfa_capable', n.get_bool_value()),
            "isMfaRegistered": lambda n : setattr(self, 'is_mfa_registered', n.get_bool_value()),
            "isPasswordlessCapable": lambda n : setattr(self, 'is_passwordless_capable', n.get_bool_value()),
            "isSsprCapable": lambda n : setattr(self, 'is_sspr_capable', n.get_bool_value()),
            "isSsprEnabled": lambda n : setattr(self, 'is_sspr_enabled', n.get_bool_value()),
            "isSsprRegistered": lambda n : setattr(self, 'is_sspr_registered', n.get_bool_value()),
            "isSystemPreferredAuthenticationMethodEnabled": lambda n : setattr(self, 'is_system_preferred_authentication_method_enabled', n.get_bool_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "methodsRegistered": lambda n : setattr(self, 'methods_registered', n.get_collection_of_primitive_values(str)),
            "systemPreferredAuthenticationMethods": lambda n : setattr(self, 'system_preferred_authentication_methods', n.get_collection_of_primitive_values(str)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userPreferredMethodForSecondaryAuthentication": lambda n : setattr(self, 'user_preferred_method_for_secondary_authentication', n.get_enum_value(UserDefaultAuthenticationMethod)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userType": lambda n : setattr(self, 'user_type', n.get_enum_value(SignInUserType)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("isAdmin", self.is_admin)
        writer.write_bool_value("isMfaCapable", self.is_mfa_capable)
        writer.write_bool_value("isMfaRegistered", self.is_mfa_registered)
        writer.write_bool_value("isPasswordlessCapable", self.is_passwordless_capable)
        writer.write_bool_value("isSsprCapable", self.is_sspr_capable)
        writer.write_bool_value("isSsprEnabled", self.is_sspr_enabled)
        writer.write_bool_value("isSsprRegistered", self.is_sspr_registered)
        writer.write_bool_value("isSystemPreferredAuthenticationMethodEnabled", self.is_system_preferred_authentication_method_enabled)
        writer.write_datetime_value()("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_collection_of_primitive_values("methodsRegistered", self.methods_registered)
        writer.write_collection_of_primitive_values("systemPreferredAuthenticationMethods", self.system_preferred_authentication_methods)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_enum_value("userPreferredMethodForSecondaryAuthentication", self.user_preferred_method_for_secondary_authentication)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_enum_value("userType", self.user_type)
    

