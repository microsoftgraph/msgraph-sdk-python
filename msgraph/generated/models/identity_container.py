from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .b2x_identity_user_flow import B2xIdentityUserFlow
    from .conditional_access_root import ConditionalAccessRoot
    from .entity import Entity
    from .identity_api_connector import IdentityApiConnector
    from .identity_provider_base import IdentityProviderBase
    from .identity_user_flow_attribute import IdentityUserFlowAttribute

from .entity import Entity

@dataclass
class IdentityContainer(Entity):
    # Represents entry point for API connectors.
    api_connectors: Optional[List[IdentityApiConnector]] = None
    # Represents entry point for B2X/self-service sign-up identity userflows.
    b2x_user_flows: Optional[List[B2xIdentityUserFlow]] = None
    # the entry point for the Conditional Access (CA) object model.
    conditional_access: Optional[ConditionalAccessRoot] = None
    # The identityProviders property
    identity_providers: Optional[List[IdentityProviderBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents entry point for identity userflow attributes.
    user_flow_attributes: Optional[List[IdentityUserFlowAttribute]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityContainer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IdentityContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .b2x_identity_user_flow import B2xIdentityUserFlow
        from .conditional_access_root import ConditionalAccessRoot
        from .entity import Entity
        from .identity_api_connector import IdentityApiConnector
        from .identity_provider_base import IdentityProviderBase
        from .identity_user_flow_attribute import IdentityUserFlowAttribute

        from .b2x_identity_user_flow import B2xIdentityUserFlow
        from .conditional_access_root import ConditionalAccessRoot
        from .entity import Entity
        from .identity_api_connector import IdentityApiConnector
        from .identity_provider_base import IdentityProviderBase
        from .identity_user_flow_attribute import IdentityUserFlowAttribute

        fields: Dict[str, Callable[[Any], None]] = {
            "apiConnectors": lambda n : setattr(self, 'api_connectors', n.get_collection_of_object_values(IdentityApiConnector)),
            "b2xUserFlows": lambda n : setattr(self, 'b2x_user_flows', n.get_collection_of_object_values(B2xIdentityUserFlow)),
            "conditionalAccess": lambda n : setattr(self, 'conditional_access', n.get_object_value(ConditionalAccessRoot)),
            "identityProviders": lambda n : setattr(self, 'identity_providers', n.get_collection_of_object_values(IdentityProviderBase)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("apiConnectors", self.api_connectors)
        writer.write_collection_of_object_values("b2xUserFlows", self.b2x_user_flows)
        writer.write_object_value("conditionalAccess", self.conditional_access)
        writer.write_collection_of_object_values("identityProviders", self.identity_providers)
        writer.write_collection_of_object_values("userFlowAttributes", self.user_flow_attributes)
    

