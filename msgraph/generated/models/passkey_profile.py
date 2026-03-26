from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attestation_enforcement import AttestationEnforcement
    from .entity import Entity
    from .fido2_key_restrictions import Fido2KeyRestrictions
    from .passkey_types import PasskeyTypes

from .entity import Entity

@dataclass
class PasskeyProfile(Entity, Parsable):
    # The attestationEnforcement property
    attestation_enforcement: Optional[AttestationEnforcement] = None
    # Controls whether key restrictions are enforced on passkeys (FIDO2), either allowing or disallowing certain key types as defined by Authenticator Attestation GUID (AAGUID), an identifier that indicates the type (for example, make and model) of the authenticator. Required.
    key_restrictions: Optional[Fido2KeyRestrictions] = None
    # Name of the passkey profile. Required.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies which types of passkeys are targeted in this passkey profile. Required. The possible values are: deviceBound, synced, unknownFutureValue.
    passkey_types: Optional[PasskeyTypes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasskeyProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasskeyProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasskeyProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attestation_enforcement import AttestationEnforcement
        from .entity import Entity
        from .fido2_key_restrictions import Fido2KeyRestrictions
        from .passkey_types import PasskeyTypes

        from .attestation_enforcement import AttestationEnforcement
        from .entity import Entity
        from .fido2_key_restrictions import Fido2KeyRestrictions
        from .passkey_types import PasskeyTypes

        fields: dict[str, Callable[[Any], None]] = {
            "attestationEnforcement": lambda n : setattr(self, 'attestation_enforcement', n.get_enum_value(AttestationEnforcement)),
            "keyRestrictions": lambda n : setattr(self, 'key_restrictions', n.get_object_value(Fido2KeyRestrictions)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "passkeyTypes": lambda n : setattr(self, 'passkey_types', n.get_collection_of_enum_values(PasskeyTypes)),
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
        writer.write_enum_value("attestationEnforcement", self.attestation_enforcement)
        writer.write_object_value("keyRestrictions", self.key_restrictions)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("passkeyTypes", self.passkey_types)
    

