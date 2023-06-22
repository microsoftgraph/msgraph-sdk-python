from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_provider, identity_provider_base, identity_user_flow, identity_user_flow_attribute_assignment, user_flow_api_connector_configuration, user_flow_language_configuration

from . import identity_user_flow

@dataclass
class B2xIdentityUserFlow(identity_user_flow.IdentityUserFlow):
    # Configuration for enabling an API connector for use as part of the self-service sign-up user flow. You can only obtain the value of this object using Get userFlowApiConnectorConfiguration.
    api_connector_configuration: Optional[user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration] = None
    # The identity providers included in the user flow.
    identity_providers: Optional[List[identity_provider.IdentityProvider]] = None
    # The languages supported for customization within the user flow. Language customization is enabled by default in self-service sign-up user flow. You cannot create custom languages in self-service sign-up user flows.
    languages: Optional[List[user_flow_language_configuration.UserFlowLanguageConfiguration]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user attribute assignments included in the user flow.
    user_attribute_assignments: Optional[List[identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment]] = None
    # The userFlowIdentityProviders property
    user_flow_identity_providers: Optional[List[identity_provider_base.IdentityProviderBase]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> B2xIdentityUserFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: B2xIdentityUserFlow
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return B2xIdentityUserFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_provider, identity_provider_base, identity_user_flow, identity_user_flow_attribute_assignment, user_flow_api_connector_configuration, user_flow_language_configuration

        from . import identity_provider, identity_provider_base, identity_user_flow, identity_user_flow_attribute_assignment, user_flow_api_connector_configuration, user_flow_language_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "apiConnectorConfiguration": lambda n : setattr(self, 'api_connector_configuration', n.get_object_value(user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration)),
            "identityProviders": lambda n : setattr(self, 'identity_providers', n.get_collection_of_object_values(identity_provider.IdentityProvider)),
            "languages": lambda n : setattr(self, 'languages', n.get_collection_of_object_values(user_flow_language_configuration.UserFlowLanguageConfiguration)),
            "userAttributeAssignments": lambda n : setattr(self, 'user_attribute_assignments', n.get_collection_of_object_values(identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment)),
            "userFlowIdentityProviders": lambda n : setattr(self, 'user_flow_identity_providers', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("apiConnectorConfiguration", self.api_connector_configuration)
        writer.write_collection_of_object_values("identityProviders", self.identity_providers)
        writer.write_collection_of_object_values("languages", self.languages)
        writer.write_collection_of_object_values("userAttributeAssignments", self.user_attribute_assignments)
        writer.write_collection_of_object_values("userFlowIdentityProviders", self.user_flow_identity_providers)
    

