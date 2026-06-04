from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .webauthn_authentication_extensions_client_inputs import WebauthnAuthenticationExtensionsClientInputs
    from .webauthn_authenticator_selection_criteria import WebauthnAuthenticatorSelectionCriteria
    from .webauthn_public_key_credential_descriptor import WebauthnPublicKeyCredentialDescriptor
    from .webauthn_public_key_credential_parameters import WebauthnPublicKeyCredentialParameters
    from .webauthn_public_key_credential_rp_entity import WebauthnPublicKeyCredentialRpEntity
    from .webauthn_public_key_credential_user_entity import WebauthnPublicKeyCredentialUserEntity

@dataclass
class WebauthnPublicKeyCredentialCreationOptions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Specifies the relying party's preference for attestation conveyance.
    attestation: Optional[str] = None
    # Criteria for selecting an appropriate authenticator for credential creation.
    authenticator_selection: Optional[WebauthnAuthenticatorSelectionCriteria] = None
    # The challenge that the authenticator must sign to prove possession of the credential. This value is Base64URL-encoded without padding.
    challenge: Optional[str] = None
    # A list of credentials that are already registered for this user, which should be excluded from selection.
    exclude_credentials: Optional[list[WebauthnPublicKeyCredentialDescriptor]] = None
    # Inputs for requested WebAuthn extensions.
    extensions: Optional[WebauthnAuthenticationExtensionsClientInputs] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The cryptographic parameters that the relying party supports, in order of preference.
    pub_key_cred_params: Optional[list[WebauthnPublicKeyCredentialParameters]] = None
    # Information about the relying party (RP) requesting credential creation.
    rp: Optional[WebauthnPublicKeyCredentialRpEntity] = None
    # The time, in milliseconds, that the caller is willing to wait for the operation to complete.
    timeout: Optional[int] = None
    # Information about the user account for which the credential is being created.
    user: Optional[WebauthnPublicKeyCredentialUserEntity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebauthnPublicKeyCredentialCreationOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebauthnPublicKeyCredentialCreationOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebauthnPublicKeyCredentialCreationOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .webauthn_authentication_extensions_client_inputs import WebauthnAuthenticationExtensionsClientInputs
        from .webauthn_authenticator_selection_criteria import WebauthnAuthenticatorSelectionCriteria
        from .webauthn_public_key_credential_descriptor import WebauthnPublicKeyCredentialDescriptor
        from .webauthn_public_key_credential_parameters import WebauthnPublicKeyCredentialParameters
        from .webauthn_public_key_credential_rp_entity import WebauthnPublicKeyCredentialRpEntity
        from .webauthn_public_key_credential_user_entity import WebauthnPublicKeyCredentialUserEntity

        from .webauthn_authentication_extensions_client_inputs import WebauthnAuthenticationExtensionsClientInputs
        from .webauthn_authenticator_selection_criteria import WebauthnAuthenticatorSelectionCriteria
        from .webauthn_public_key_credential_descriptor import WebauthnPublicKeyCredentialDescriptor
        from .webauthn_public_key_credential_parameters import WebauthnPublicKeyCredentialParameters
        from .webauthn_public_key_credential_rp_entity import WebauthnPublicKeyCredentialRpEntity
        from .webauthn_public_key_credential_user_entity import WebauthnPublicKeyCredentialUserEntity

        fields: dict[str, Callable[[Any], None]] = {
            "attestation": lambda n : setattr(self, 'attestation', n.get_str_value()),
            "authenticatorSelection": lambda n : setattr(self, 'authenticator_selection', n.get_object_value(WebauthnAuthenticatorSelectionCriteria)),
            "challenge": lambda n : setattr(self, 'challenge', n.get_str_value()),
            "excludeCredentials": lambda n : setattr(self, 'exclude_credentials', n.get_collection_of_object_values(WebauthnPublicKeyCredentialDescriptor)),
            "extensions": lambda n : setattr(self, 'extensions', n.get_object_value(WebauthnAuthenticationExtensionsClientInputs)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pubKeyCredParams": lambda n : setattr(self, 'pub_key_cred_params', n.get_collection_of_object_values(WebauthnPublicKeyCredentialParameters)),
            "rp": lambda n : setattr(self, 'rp', n.get_object_value(WebauthnPublicKeyCredentialRpEntity)),
            "timeout": lambda n : setattr(self, 'timeout', n.get_int_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(WebauthnPublicKeyCredentialUserEntity)),
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
        writer.write_str_value("attestation", self.attestation)
        writer.write_object_value("authenticatorSelection", self.authenticator_selection)
        writer.write_str_value("challenge", self.challenge)
        writer.write_collection_of_object_values("excludeCredentials", self.exclude_credentials)
        writer.write_object_value("extensions", self.extensions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("pubKeyCredParams", self.pub_key_cred_params)
        writer.write_object_value("rp", self.rp)
        writer.write_int_value("timeout", self.timeout)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

