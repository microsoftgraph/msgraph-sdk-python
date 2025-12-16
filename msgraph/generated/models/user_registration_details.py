from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .sign_in_user_type import SignInUserType
    from .user_default_authentication_method import UserDefaultAuthenticationMethod

from .entity import Entity

@dataclass
class UserRegistrationDetails(Entity, Parsable):
    # Indicates whether the user has an admin role in the tenant. This value can be used to check the authentication methods that privileged accounts are registered for and capable of.
    is_admin: Optional[bool] = None
    # Indicates whether the user has registered a strong authentication method for multifactor authentication. The method must be allowed by the authentication methods policy. Supports $filter (eq).
    is_mfa_capable: Optional[bool] = None
    # Indicates whether the user has registered a strong authentication method for multifactor authentication. The method may not necessarily be allowed by the authentication methods policy. Supports $filter (eq).
    is_mfa_registered: Optional[bool] = None
    # Indicates whether the user has registered a passwordless strong authentication method (including FIDO2, Windows Hello for Business, and Microsoft Authenticator (Passwordless)) that is allowed by the authentication methods policy. Supports $filter (eq).
    is_passwordless_capable: Optional[bool] = None
    # Indicates whether the user has registered the required number of authentication methods for self-service password reset and the user is allowed to perform self-service password reset by policy. Supports $filter (eq).
    is_sspr_capable: Optional[bool] = None
    # Indicates whether the user is allowed to perform self-service password reset by policy. The user may not necessarily have registered the required number of authentication methods for self-service password reset. Supports $filter (eq).
    is_sspr_enabled: Optional[bool] = None
    # Indicates whether the user has registered the required number of authentication methods for self-service password reset. The user may not necessarily be allowed to perform self-service password reset by policy. Supports $filter (eq).
    is_sspr_registered: Optional[bool] = None
    # Indicates whether system preferred authentication method is enabled. If enabled, the system dynamically determines the most secure authentication method among the methods registered by the user. Supports $filter (eq).
    is_system_preferred_authentication_method_enabled: Optional[bool] = None
    # The date and time (UTC) when the report was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_updated_date_time: Optional[datetime.datetime] = None
    # Collection of authentication methods registered, such as mobilePhone, email, passKeyDeviceBound. Supports $filter (any with eq).
    methods_registered: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of authentication methods that the system determined to be the most secure authentication methods among the registered methods for second factor authentication. The possible values are: push, oath, voiceMobile, voiceAlternateMobile, voiceOffice, sms, none, unknownFutureValue. Supports $filter (any with eq).
    system_preferred_authentication_methods: Optional[list[str]] = None
    # The user display name, such as Adele Vance. Supports $filter (eq, startsWith) and $orderby.
    user_display_name: Optional[str] = None
    # The method the user selected as the default second-factor for performing multifactor authentication. The possible values are: push, oath, voiceMobile, voiceAlternateMobile, voiceOffice, sms, none, unknownFutureValue. This property is used as preferred MFA method when isSystemPreferredAuthenticationMethodEnabled is false. Supports $filter (any with eq).
    user_preferred_method_for_secondary_authentication: Optional[UserDefaultAuthenticationMethod] = None
    # The user principal name, such as AdeleV@contoso.com. Supports $filter (eq, startsWith) and $orderby.
    user_principal_name: Optional[str] = None
    # Identifies whether the user is a member or guest in the tenant. The possible values are: member, guest, unknownFutureValue.
    user_type: Optional[SignInUserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserRegistrationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserRegistrationDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserRegistrationDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .sign_in_user_type import SignInUserType
        from .user_default_authentication_method import UserDefaultAuthenticationMethod

        from .entity import Entity
        from .sign_in_user_type import SignInUserType
        from .user_default_authentication_method import UserDefaultAuthenticationMethod

        fields: dict[str, Callable[[Any], None]] = {
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
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
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_collection_of_primitive_values("methodsRegistered", self.methods_registered)
        writer.write_collection_of_primitive_values("systemPreferredAuthenticationMethods", self.system_preferred_authentication_methods)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_enum_value("userPreferredMethodForSecondaryAuthentication", self.user_preferred_method_for_secondary_authentication)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_enum_value("userType", self.user_type)
    

