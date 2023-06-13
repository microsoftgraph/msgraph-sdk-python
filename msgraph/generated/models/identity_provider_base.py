from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_managed_identity_provider, built_in_identity_provider, entity, internal_domain_federation, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, social_identity_provider

from . import entity

@dataclass
class IdentityProviderBase(entity.Entity):
    # The display name of the identity provider.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityProviderBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityProviderBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.appleManagedIdentityProvider":
                from . import apple_managed_identity_provider

                return apple_managed_identity_provider.AppleManagedIdentityProvider()
            if mapping_value == "#microsoft.graph.builtInIdentityProvider":
                from . import built_in_identity_provider

                return built_in_identity_provider.BuiltInIdentityProvider()
            if mapping_value == "#microsoft.graph.internalDomainFederation":
                from . import internal_domain_federation

                return internal_domain_federation.InternalDomainFederation()
            if mapping_value == "#microsoft.graph.samlOrWsFedExternalDomainFederation":
                from . import saml_or_ws_fed_external_domain_federation

                return saml_or_ws_fed_external_domain_federation.SamlOrWsFedExternalDomainFederation()
            if mapping_value == "#microsoft.graph.samlOrWsFedProvider":
                from . import saml_or_ws_fed_provider

                return saml_or_ws_fed_provider.SamlOrWsFedProvider()
            if mapping_value == "#microsoft.graph.socialIdentityProvider":
                from . import social_identity_provider

                return social_identity_provider.SocialIdentityProvider()
        return IdentityProviderBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_managed_identity_provider, built_in_identity_provider, entity, internal_domain_federation, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, social_identity_provider

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
    

