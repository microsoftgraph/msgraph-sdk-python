from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_provider = lazy_import('msgraph.generated.models.identity_provider')
identity_provider_base = lazy_import('msgraph.generated.models.identity_provider_base')
identity_user_flow = lazy_import('msgraph.generated.models.identity_user_flow')
identity_user_flow_attribute_assignment = lazy_import('msgraph.generated.models.identity_user_flow_attribute_assignment')
user_flow_api_connector_configuration = lazy_import('msgraph.generated.models.user_flow_api_connector_configuration')
user_flow_language_configuration = lazy_import('msgraph.generated.models.user_flow_language_configuration')

class B2xIdentityUserFlow(identity_user_flow.IdentityUserFlow):
    @property
    def api_connector_configuration(self,) -> Optional[user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration]:
        """
        Gets the apiConnectorConfiguration property value. Configuration for enabling an API connector for use as part of the self-service sign-up user flow. You can only obtain the value of this object using Get userFlowApiConnectorConfiguration.
        Returns: Optional[user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration]
        """
        return self._api_connector_configuration
    
    @api_connector_configuration.setter
    def api_connector_configuration(self,value: Optional[user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration] = None) -> None:
        """
        Sets the apiConnectorConfiguration property value. Configuration for enabling an API connector for use as part of the self-service sign-up user flow. You can only obtain the value of this object using Get userFlowApiConnectorConfiguration.
        Args:
            value: Value to set for the apiConnectorConfiguration property.
        """
        self._api_connector_configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new B2xIdentityUserFlow and sets the default values.
        """
        super().__init__()
        # Configuration for enabling an API connector for use as part of the self-service sign-up user flow. You can only obtain the value of this object using Get userFlowApiConnectorConfiguration.
        self._api_connector_configuration: Optional[user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration] = None
        # The identity providers included in the user flow.
        self._identity_providers: Optional[List[identity_provider.IdentityProvider]] = None
        # The languages supported for customization within the user flow. Language customization is enabled by default in self-service sign-up user flow. You cannot create custom languages in self-service sign-up user flows.
        self._languages: Optional[List[user_flow_language_configuration.UserFlowLanguageConfiguration]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user attribute assignments included in the user flow.
        self._user_attribute_assignments: Optional[List[identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment]] = None
        # The userFlowIdentityProviders property
        self._user_flow_identity_providers: Optional[List[identity_provider_base.IdentityProviderBase]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> B2xIdentityUserFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: B2xIdentityUserFlow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return B2xIdentityUserFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "api_connector_configuration": lambda n : setattr(self, 'api_connector_configuration', n.get_object_value(user_flow_api_connector_configuration.UserFlowApiConnectorConfiguration)),
            "identity_providers": lambda n : setattr(self, 'identity_providers', n.get_collection_of_object_values(identity_provider.IdentityProvider)),
            "languages": lambda n : setattr(self, 'languages', n.get_collection_of_object_values(user_flow_language_configuration.UserFlowLanguageConfiguration)),
            "user_attribute_assignments": lambda n : setattr(self, 'user_attribute_assignments', n.get_collection_of_object_values(identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment)),
            "user_flow_identity_providers": lambda n : setattr(self, 'user_flow_identity_providers', n.get_collection_of_object_values(identity_provider_base.IdentityProviderBase)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_providers(self,) -> Optional[List[identity_provider.IdentityProvider]]:
        """
        Gets the identityProviders property value. The identity providers included in the user flow.
        Returns: Optional[List[identity_provider.IdentityProvider]]
        """
        return self._identity_providers
    
    @identity_providers.setter
    def identity_providers(self,value: Optional[List[identity_provider.IdentityProvider]] = None) -> None:
        """
        Sets the identityProviders property value. The identity providers included in the user flow.
        Args:
            value: Value to set for the identityProviders property.
        """
        self._identity_providers = value
    
    @property
    def languages(self,) -> Optional[List[user_flow_language_configuration.UserFlowLanguageConfiguration]]:
        """
        Gets the languages property value. The languages supported for customization within the user flow. Language customization is enabled by default in self-service sign-up user flow. You cannot create custom languages in self-service sign-up user flows.
        Returns: Optional[List[user_flow_language_configuration.UserFlowLanguageConfiguration]]
        """
        return self._languages
    
    @languages.setter
    def languages(self,value: Optional[List[user_flow_language_configuration.UserFlowLanguageConfiguration]] = None) -> None:
        """
        Sets the languages property value. The languages supported for customization within the user flow. Language customization is enabled by default in self-service sign-up user flow. You cannot create custom languages in self-service sign-up user flows.
        Args:
            value: Value to set for the languages property.
        """
        self._languages = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("apiConnectorConfiguration", self.api_connector_configuration)
        writer.write_collection_of_object_values("identityProviders", self.identity_providers)
        writer.write_collection_of_object_values("languages", self.languages)
        writer.write_collection_of_object_values("userAttributeAssignments", self.user_attribute_assignments)
        writer.write_collection_of_object_values("userFlowIdentityProviders", self.user_flow_identity_providers)
    
    @property
    def user_attribute_assignments(self,) -> Optional[List[identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment]]:
        """
        Gets the userAttributeAssignments property value. The user attribute assignments included in the user flow.
        Returns: Optional[List[identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment]]
        """
        return self._user_attribute_assignments
    
    @user_attribute_assignments.setter
    def user_attribute_assignments(self,value: Optional[List[identity_user_flow_attribute_assignment.IdentityUserFlowAttributeAssignment]] = None) -> None:
        """
        Sets the userAttributeAssignments property value. The user attribute assignments included in the user flow.
        Args:
            value: Value to set for the userAttributeAssignments property.
        """
        self._user_attribute_assignments = value
    
    @property
    def user_flow_identity_providers(self,) -> Optional[List[identity_provider_base.IdentityProviderBase]]:
        """
        Gets the userFlowIdentityProviders property value. The userFlowIdentityProviders property
        Returns: Optional[List[identity_provider_base.IdentityProviderBase]]
        """
        return self._user_flow_identity_providers
    
    @user_flow_identity_providers.setter
    def user_flow_identity_providers(self,value: Optional[List[identity_provider_base.IdentityProviderBase]] = None) -> None:
        """
        Sets the userFlowIdentityProviders property value. The userFlowIdentityProviders property
        Args:
            value: Value to set for the userFlowIdentityProviders property.
        """
        self._user_flow_identity_providers = value
    

