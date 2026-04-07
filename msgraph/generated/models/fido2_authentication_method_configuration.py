from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .fido2_key_restrictions import Fido2KeyRestrictions
    from .passkey_authentication_method_target import PasskeyAuthenticationMethodTarget
    from .passkey_profile import PasskeyProfile

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class Fido2AuthenticationMethodConfiguration(AuthenticationMethodConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.fido2AuthenticationMethodConfiguration"
    # The non-deletable baseline passkey profile, within the passkey profile collection. It's automatically created when migrating to passkey profiles and initially mirrors the tenant's legacy global passkey (FIDO2) authentication methods policy settings.
    default_passkey_profile: Optional[str] = None
    # A collection of groups that are enabled to use the authentication method.
    include_targets: Optional[list[PasskeyAuthenticationMethodTarget]] = None
    # Determines whether attestation must be enforced for passkey (FIDO2) registration. This property is deprecated and will be removed in October 2027. Use passkeyProfiles property.
    is_attestation_enforced: Optional[bool] = None
    # Determines if users can register new passkeys (FIDO2).
    is_self_service_registration_allowed: Optional[bool] = None
    # Controls whether key restrictions are enforced on passkeys (FIDO2), either allowing or disallowing certain key types as defined by Authenticator Attestation GUID (AAGUID), an identifier that indicates the type (for example, make and model) of the authenticator. This property is deprecated and will be removed in October 2027. Use the passkeyProfiles property.
    key_restrictions: Optional[Fido2KeyRestrictions] = None
    # A collection of configuration profiles that control the registration of and authentication with passkeys (FIDO2).
    passkey_profiles: Optional[list[PasskeyProfile]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Fido2AuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Fido2AuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Fido2AuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .fido2_key_restrictions import Fido2KeyRestrictions
        from .passkey_authentication_method_target import PasskeyAuthenticationMethodTarget
        from .passkey_profile import PasskeyProfile

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .fido2_key_restrictions import Fido2KeyRestrictions
        from .passkey_authentication_method_target import PasskeyAuthenticationMethodTarget
        from .passkey_profile import PasskeyProfile

        fields: dict[str, Callable[[Any], None]] = {
            "defaultPasskeyProfile": lambda n : setattr(self, 'default_passkey_profile', n.get_str_value()),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(PasskeyAuthenticationMethodTarget)),
            "isAttestationEnforced": lambda n : setattr(self, 'is_attestation_enforced', n.get_bool_value()),
            "isSelfServiceRegistrationAllowed": lambda n : setattr(self, 'is_self_service_registration_allowed', n.get_bool_value()),
            "keyRestrictions": lambda n : setattr(self, 'key_restrictions', n.get_object_value(Fido2KeyRestrictions)),
            "passkeyProfiles": lambda n : setattr(self, 'passkey_profiles', n.get_collection_of_object_values(PasskeyProfile)),
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
        writer.write_str_value("defaultPasskeyProfile", self.default_passkey_profile)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_bool_value("isAttestationEnforced", self.is_attestation_enforced)
        writer.write_bool_value("isSelfServiceRegistrationAllowed", self.is_self_service_registration_allowed)
        writer.write_object_value("keyRestrictions", self.key_restrictions)
        writer.write_collection_of_object_values("passkeyProfiles", self.passkey_profiles)
    

