from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_configuration = lazy_import('msgraph.generated.models.authentication_method_configuration')
authentication_method_target = lazy_import('msgraph.generated.models.authentication_method_target')
fido2_key_restrictions = lazy_import('msgraph.generated.models.fido2_key_restrictions')

class Fido2AuthenticationMethodConfiguration(authentication_method_configuration.AuthenticationMethodConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new Fido2AuthenticationMethodConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.fido2AuthenticationMethodConfiguration"
        # A collection of users or groups who are enabled to use the authentication method.
        self._include_targets: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None
        # Determines whether attestation must be enforced for FIDO2 security key registration.
        self._is_attestation_enforced: Optional[bool] = None
        # Determines if users can register new FIDO2 security keys.
        self._is_self_service_registration_allowed: Optional[bool] = None
        # Controls whether key restrictions are enforced on FIDO2 security keys, either allowing or disallowing certain key types as defined by Authenticator Attestation GUID (AAGUID), an identifier that indicates the type (e.g. make and model) of the authenticator.
        self._key_restrictions: Optional[fido2_key_restrictions.Fido2KeyRestrictions] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Fido2AuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Fido2AuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Fido2AuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "include_targets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(authentication_method_target.AuthenticationMethodTarget)),
            "is_attestation_enforced": lambda n : setattr(self, 'is_attestation_enforced', n.get_bool_value()),
            "is_self_service_registration_allowed": lambda n : setattr(self, 'is_self_service_registration_allowed', n.get_bool_value()),
            "key_restrictions": lambda n : setattr(self, 'key_restrictions', n.get_object_value(fido2_key_restrictions.Fido2KeyRestrictions)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def include_targets(self,) -> Optional[List[authentication_method_target.AuthenticationMethodTarget]]:
        """
        Gets the includeTargets property value. A collection of users or groups who are enabled to use the authentication method.
        Returns: Optional[List[authentication_method_target.AuthenticationMethodTarget]]
        """
        return self._include_targets
    
    @include_targets.setter
    def include_targets(self,value: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None) -> None:
        """
        Sets the includeTargets property value. A collection of users or groups who are enabled to use the authentication method.
        Args:
            value: Value to set for the includeTargets property.
        """
        self._include_targets = value
    
    @property
    def is_attestation_enforced(self,) -> Optional[bool]:
        """
        Gets the isAttestationEnforced property value. Determines whether attestation must be enforced for FIDO2 security key registration.
        Returns: Optional[bool]
        """
        return self._is_attestation_enforced
    
    @is_attestation_enforced.setter
    def is_attestation_enforced(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAttestationEnforced property value. Determines whether attestation must be enforced for FIDO2 security key registration.
        Args:
            value: Value to set for the isAttestationEnforced property.
        """
        self._is_attestation_enforced = value
    
    @property
    def is_self_service_registration_allowed(self,) -> Optional[bool]:
        """
        Gets the isSelfServiceRegistrationAllowed property value. Determines if users can register new FIDO2 security keys.
        Returns: Optional[bool]
        """
        return self._is_self_service_registration_allowed
    
    @is_self_service_registration_allowed.setter
    def is_self_service_registration_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSelfServiceRegistrationAllowed property value. Determines if users can register new FIDO2 security keys.
        Args:
            value: Value to set for the isSelfServiceRegistrationAllowed property.
        """
        self._is_self_service_registration_allowed = value
    
    @property
    def key_restrictions(self,) -> Optional[fido2_key_restrictions.Fido2KeyRestrictions]:
        """
        Gets the keyRestrictions property value. Controls whether key restrictions are enforced on FIDO2 security keys, either allowing or disallowing certain key types as defined by Authenticator Attestation GUID (AAGUID), an identifier that indicates the type (e.g. make and model) of the authenticator.
        Returns: Optional[fido2_key_restrictions.Fido2KeyRestrictions]
        """
        return self._key_restrictions
    
    @key_restrictions.setter
    def key_restrictions(self,value: Optional[fido2_key_restrictions.Fido2KeyRestrictions] = None) -> None:
        """
        Sets the keyRestrictions property value. Controls whether key restrictions are enforced on FIDO2 security keys, either allowing or disallowing certain key types as defined by Authenticator Attestation GUID (AAGUID), an identifier that indicates the type (e.g. make and model) of the authenticator.
        Args:
            value: Value to set for the keyRestrictions property.
        """
        self._key_restrictions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_bool_value("isAttestationEnforced", self.is_attestation_enforced)
        writer.write_bool_value("isSelfServiceRegistrationAllowed", self.is_self_service_registration_allowed)
        writer.write_object_value("keyRestrictions", self.key_restrictions)
    

