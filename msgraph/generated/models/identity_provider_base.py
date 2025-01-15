from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apple_managed_identity_provider import AppleManagedIdentityProvider
    from .built_in_identity_provider import BuiltInIdentityProvider
    from .entity import Entity
    from .internal_domain_federation import InternalDomainFederation
    from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
    from .saml_or_ws_fed_provider import SamlOrWsFedProvider
    from .social_identity_provider import SocialIdentityProvider

from .entity import Entity

@dataclass
class IdentityProviderBase(Entity, Parsable):
    # The display name of the identity provider.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityProviderBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityProviderBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleManagedIdentityProvider".casefold():
            from .apple_managed_identity_provider import AppleManagedIdentityProvider

            return AppleManagedIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.builtInIdentityProvider".casefold():
            from .built_in_identity_provider import BuiltInIdentityProvider

            return BuiltInIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internalDomainFederation".casefold():
            from .internal_domain_federation import InternalDomainFederation

            return InternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedExternalDomainFederation".casefold():
            from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation

            return SamlOrWsFedExternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedProvider".casefold():
            from .saml_or_ws_fed_provider import SamlOrWsFedProvider

            return SamlOrWsFedProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.socialIdentityProvider".casefold():
            from .social_identity_provider import SocialIdentityProvider

            return SocialIdentityProvider()
        return IdentityProviderBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .apple_managed_identity_provider import AppleManagedIdentityProvider
        from .built_in_identity_provider import BuiltInIdentityProvider
        from .entity import Entity
        from .internal_domain_federation import InternalDomainFederation
        from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider
        from .social_identity_provider import SocialIdentityProvider

        from .apple_managed_identity_provider import AppleManagedIdentityProvider
        from .built_in_identity_provider import BuiltInIdentityProvider
        from .entity import Entity
        from .internal_domain_federation import InternalDomainFederation
        from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider
        from .social_identity_provider import SocialIdentityProvider

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
    

