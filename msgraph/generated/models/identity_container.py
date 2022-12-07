from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

b2x_identity_user_flow = lazy_import('msgraph.generated.models.b2x_identity_user_flow')
conditional_access_root = lazy_import('msgraph.generated.models.conditional_access_root')
entity = lazy_import('msgraph.generated.models.entity')
identity_api_connector = lazy_import('msgraph.generated.models.identity_api_connector')
identity_provider_base = lazy_import('msgraph.generated.models.identity_provider_base')
identity_user_flow_attribute = lazy_import('msgraph.generated.models.identity_user_flow_attribute')

class IdentityContainer(entity.Entity):
    @property
    def api_connectors(self,) -> Optional[List[identity_api_connector.IdentityApiConnector]]:
        """
        Gets the apiConnectors property value. Represents entry point for API connectors.
        Returns: Optional[List[identity_api_connector.IdentityApiConnector]]
        """
        return self._api_connectors
    
    @api_connectors.setter
    def api_connectors(self,value: Optional[List[identity_api_connector.IdentityApiConnector]] = None) -> None:
        """
        Sets the apiConnectors property value. Represents entry point for API connectors.
        Args:
            value: Value to set for the apiConnectors property.
        """
        self._api_connectors = value
    
    @property
    def b2x_user_flows(self,) -> Optional[List[b2x_identity_user_flow.B2xIdentityUserFlow]]:
        """
        Gets the b2xUserFlows property value. Represents entry point for B2X/self-service sign-up identity userflows.
        Returns: Optional[List[b2x_identity_user_flow.B2xIdentityUserFlow]]
        """
        return self._b2x_user_flows
    
    @b2x_user_flows.setter
    def b2x_user_flows(self,value: Optional[List[b2x_identity_user_flow.B2xIdentityUserFlow]] = None) -> None:
        """
        Sets the b2xUserFlows property value. Represents entry point for B2X/self-service sign-up identity userflows.
        Args:
            value: Value to set for the b2xUserFlows property.
        """
        self._b2x_user_flows = value
    
    @property
    def conditional_access(self,) -> Optional[conditional_access_root.ConditionalAccessRoot]:
        """
        Gets the conditionalAccess property value. the entry point for the Conditional Access (CA) object model.
        Returns: Optional[conditional_access_root.ConditionalAccessRoot]
        """
        return self._conditional_access
    
    @conditional_access.setter
    def conditional_access(self,value: Optional[conditional_access_root.ConditionalAccessRoot] = None) -> None:
        """
        Sets the conditionalAccess property value. the entry point for the Conditional Access (CA) object model.
        Args:
            value: Value to set for the conditionalAccess property.
        """
        self._conditional_access = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IdentityContainer and sets the default values.
        """
        super().__init__()
        # Represents entry point for API connectors.
        self._api_connectors: Optional[List[identity_api_connector.IdentityApiConnector]] = None
        # Represents entry point for B2X/self-service sign-up identity userflows.
        self._b2x_user_flows: Optional[List[b2x_identity_user_flow.B2xIdentityUserFlow]] = None
        # the entry point for the Conditional Access (CA) object model.
        self._conditional_access: Optional[conditional_access_root.ConditionalAccessRoot] = None
        # The identityProviders property
        self._identity_providers: Optional[List[identity_provider_base.IdentityProviderBase]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents entry point for identity userflow attributes.
        self._user_flow_attributes: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityContainer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdentityContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "api_connectors": lambda n : setattr(self, 'api_connectors', n.get_collection_of_object_values(identity_api_connector.IdentityApiConnector)),
            "b2x_user_flows": lambda n : setattr(self, 'b2x_user_flows', n.get_collection_of_object_values(b2x_identity_user_flow.B2xIdentityUserFlow)),
            "conditional_access": lambda n : setattr(self, 'conditional_access', n.get_object_value(conditional_access_root.ConditionalAccessRoot)),
            "identity_providers": lambda n : setattr(self, 'identity_providers', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
            "user_flow_attributes": lambda n : setattr(self, 'user_flow_attributes', n.get_collection_of_object_values(identity_user_flow_attribute.IdentityUserFlowAttribute)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_providers(self,) -> Optional[List[identity_provider_base.IdentityProviderBase]]:
        """
        Gets the identityProviders property value. The identityProviders property
        Returns: Optional[List[identity_provider_base.IdentityProviderBase]]
        """
        return self._identity_providers
    
    @identity_providers.setter
    def identity_providers(self,value: Optional[List[identity_provider_base.IdentityProviderBase]] = None) -> None:
        """
        Sets the identityProviders property value. The identityProviders property
        Args:
            value: Value to set for the identityProviders property.
        """
        self._identity_providers = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("apiConnectors", self.api_connectors)
        writer.write_collection_of_object_values("b2xUserFlows", self.b2x_user_flows)
        writer.write_object_value("conditionalAccess", self.conditional_access)
        writer.write_collection_of_object_values("identityProviders", self.identity_providers)
        writer.write_collection_of_object_values("userFlowAttributes", self.user_flow_attributes)
    
    @property
    def user_flow_attributes(self,) -> Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]]:
        """
        Gets the userFlowAttributes property value. Represents entry point for identity userflow attributes.
        Returns: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]]
        """
        return self._user_flow_attributes
    
    @user_flow_attributes.setter
    def user_flow_attributes(self,value: Optional[List[identity_user_flow_attribute.IdentityUserFlowAttribute]] = None) -> None:
        """
        Sets the userFlowAttributes property value. Represents entry point for identity userflow attributes.
        Args:
            value: Value to set for the userFlowAttributes property.
        """
        self._user_flow_attributes = value
    

