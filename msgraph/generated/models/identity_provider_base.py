from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_managed_identity_provider, built_in_identity_provider, entity, internal_domain_federation, saml_or_ws_fed_external_domain_federation, saml_or_ws_fed_provider, social_identity_provider

from . import entity

class IdentityProviderBase(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new identityProviderBase and sets the default values.
        """
        super().__init__()
        # The display name of the identity provider.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the identity provider.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the identity provider.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
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
    

