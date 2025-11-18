from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_events_flow import AuthenticationEventsFlow
    from .authentication_event_listener import AuthenticationEventListener
    from .b2x_identity_user_flow import B2xIdentityUserFlow
    from .conditional_access_root import ConditionalAccessRoot
    from .custom_authentication_extension import CustomAuthenticationExtension
    from .entity import Entity
    from .identity_api_connector import IdentityApiConnector
    from .identity_provider_base import IdentityProviderBase
    from .identity_user_flow_attribute import IdentityUserFlowAttribute
    from .risk_prevention_container import RiskPreventionContainer

from .entity import Entity

@dataclass
class IdentityContainer(Entity, Parsable):
    # Represents entry point for API connectors.
    api_connectors: Optional[list[IdentityApiConnector]] = None
    # Represents listeners for custom authentication extension events in Azure AD for workforce and customers.
    authentication_event_listeners: Optional[list[AuthenticationEventListener]] = None
    # Represents the entry point for self-service sign-up and sign-in user flows in both Microsoft Entra workforce and external tenants.
    authentication_events_flows: Optional[list[AuthenticationEventsFlow]] = None
    # Represents entry point for B2X/self-service sign-up identity userflows.
    b2x_user_flows: Optional[list[B2xIdentityUserFlow]] = None
    # the entry point for the Conditional Access (CA) object model.
    conditional_access: Optional[ConditionalAccessRoot] = None
    # Represents custom extensions to authentication flows in Azure AD for workforce and customers.
    custom_authentication_extensions: Optional[list[CustomAuthenticationExtension]] = None
    # The identityProviders property
    identity_providers: Optional[list[IdentityProviderBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the entry point for fraud and risk prevention configurations in Microsoft Entra External ID, including third-party provider settings.
    risk_prevention: Optional[RiskPreventionContainer] = None
    # Represents entry point for identity userflow attributes.
    user_flow_attributes: Optional[list[IdentityUserFlowAttribute]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityContainer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdentityContainer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_events_flow import AuthenticationEventsFlow
        from .authentication_event_listener import AuthenticationEventListener
        from .b2x_identity_user_flow import B2xIdentityUserFlow
        from .conditional_access_root import ConditionalAccessRoot
        from .custom_authentication_extension import CustomAuthenticationExtension
        from .entity import Entity
        from .identity_api_connector import IdentityApiConnector
        from .identity_provider_base import IdentityProviderBase
        from .identity_user_flow_attribute import IdentityUserFlowAttribute
        from .risk_prevention_container import RiskPreventionContainer

        from .authentication_events_flow import AuthenticationEventsFlow
        from .authentication_event_listener import AuthenticationEventListener
        from .b2x_identity_user_flow import B2xIdentityUserFlow
        from .conditional_access_root import ConditionalAccessRoot
        from .custom_authentication_extension import CustomAuthenticationExtension
        from .entity import Entity
        from .identity_api_connector import IdentityApiConnector
        from .identity_provider_base import IdentityProviderBase
        from .identity_user_flow_attribute import IdentityUserFlowAttribute
        from .risk_prevention_container import RiskPreventionContainer

        fields: dict[str, Callable[[Any], None]] = {
            "apiConnectors": lambda n : setattr(self, 'api_connectors', n.get_collection_of_object_values(IdentityApiConnector)),
            "authenticationEventListeners": lambda n : setattr(self, 'authentication_event_listeners', n.get_collection_of_object_values(AuthenticationEventListener)),
            "authenticationEventsFlows": lambda n : setattr(self, 'authentication_events_flows', n.get_collection_of_object_values(AuthenticationEventsFlow)),
            "b2xUserFlows": lambda n : setattr(self, 'b2x_user_flows', n.get_collection_of_object_values(B2xIdentityUserFlow)),
            "conditionalAccess": lambda n : setattr(self, 'conditional_access', n.get_object_value(ConditionalAccessRoot)),
            "customAuthenticationExtensions": lambda n : setattr(self, 'custom_authentication_extensions', n.get_collection_of_object_values(CustomAuthenticationExtension)),
            "identityProviders": lambda n : setattr(self, 'identity_providers', n.get_collection_of_object_values(IdentityProviderBase)),
            "riskPrevention": lambda n : setattr(self, 'risk_prevention', n.get_object_value(RiskPreventionContainer)),
            "userFlowAttributes": lambda n : setattr(self, 'user_flow_attributes', n.get_collection_of_object_values(IdentityUserFlowAttribute)),
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
        writer.write_collection_of_object_values("apiConnectors", self.api_connectors)
        writer.write_collection_of_object_values("authenticationEventListeners", self.authentication_event_listeners)
        writer.write_collection_of_object_values("authenticationEventsFlows", self.authentication_events_flows)
        writer.write_collection_of_object_values("b2xUserFlows", self.b2x_user_flows)
        writer.write_object_value("conditionalAccess", self.conditional_access)
        writer.write_collection_of_object_values("customAuthenticationExtensions", self.custom_authentication_extensions)
        writer.write_collection_of_object_values("identityProviders", self.identity_providers)
        writer.write_object_value("riskPrevention", self.risk_prevention)
        writer.write_collection_of_object_values("userFlowAttributes", self.user_flow_attributes)
    

