from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .authentication_method_target import AuthenticationMethodTarget
    from .fido2_key_restrictions import Fido2KeyRestrictions

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class Fido2AuthenticationMethodConfiguration(AuthenticationMethodConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.fido2AuthenticationMethodConfiguration"
    # A collection of groups that are enabled to use the authentication method.
    include_targets: Optional[list[AuthenticationMethodTarget]] = None
    # Determines whether attestation must be enforced for FIDO2 security key registration.
    is_attestation_enforced: Optional[bool] = None
    # Determines if users can register new FIDO2 security keys.
    is_self_service_registration_allowed: Optional[bool] = None
    # Controls whether key restrictions are enforced on FIDO2 security keys, either allowing or disallowing certain key types as defined by Authenticator Attestation GUID (AAGUID), an identifier that indicates the type (for example, make and model) of the authenticator.
    key_restrictions: Optional[Fido2KeyRestrictions] = None
    
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
        from .authentication_method_target import AuthenticationMethodTarget
        from .fido2_key_restrictions import Fido2KeyRestrictions

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget
        from .fido2_key_restrictions import Fido2KeyRestrictions

        fields: dict[str, Callable[[Any], None]] = {
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(AuthenticationMethodTarget)),
            "isAttestationEnforced": lambda n : setattr(self, 'is_attestation_enforced', n.get_bool_value()),
            "isSelfServiceRegistrationAllowed": lambda n : setattr(self, 'is_self_service_registration_allowed', n.get_bool_value()),
            "keyRestrictions": lambda n : setattr(self, 'key_restrictions', n.get_object_value(Fido2KeyRestrictions)),
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
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_bool_value("isAttestationEnforced", self.is_attestation_enforced)
        writer.write_bool_value("isSelfServiceRegistrationAllowed", self.is_self_service_registration_allowed)
        writer.write_object_value("keyRestrictions", self.key_restrictions)
    

