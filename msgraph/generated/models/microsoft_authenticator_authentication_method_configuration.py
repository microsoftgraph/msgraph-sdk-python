from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_configuration = lazy_import('msgraph.generated.models.authentication_method_configuration')
microsoft_authenticator_authentication_method_target = lazy_import('msgraph.generated.models.microsoft_authenticator_authentication_method_target')
microsoft_authenticator_feature_settings = lazy_import('msgraph.generated.models.microsoft_authenticator_feature_settings')

class MicrosoftAuthenticatorAuthenticationMethodConfiguration(authentication_method_configuration.AuthenticationMethodConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new MicrosoftAuthenticatorAuthenticationMethodConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration"
        # A collection of Microsoft Authenticator settings such as application context and location context, and whether they are enabled for all users or specific users only.
        self._feature_settings: Optional[microsoft_authenticator_feature_settings.MicrosoftAuthenticatorFeatureSettings] = None
        # A collection of users or groups who are enabled to use the authentication method. Expanded by default.
        self._include_targets: Optional[List[microsoft_authenticator_authentication_method_target.MicrosoftAuthenticatorAuthenticationMethodTarget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftAuthenticatorAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAuthenticatorAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftAuthenticatorAuthenticationMethodConfiguration()
    
    @property
    def feature_settings(self,) -> Optional[microsoft_authenticator_feature_settings.MicrosoftAuthenticatorFeatureSettings]:
        """
        Gets the featureSettings property value. A collection of Microsoft Authenticator settings such as application context and location context, and whether they are enabled for all users or specific users only.
        Returns: Optional[microsoft_authenticator_feature_settings.MicrosoftAuthenticatorFeatureSettings]
        """
        return self._feature_settings
    
    @feature_settings.setter
    def feature_settings(self,value: Optional[microsoft_authenticator_feature_settings.MicrosoftAuthenticatorFeatureSettings] = None) -> None:
        """
        Sets the featureSettings property value. A collection of Microsoft Authenticator settings such as application context and location context, and whether they are enabled for all users or specific users only.
        Args:
            value: Value to set for the featureSettings property.
        """
        self._feature_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "feature_settings": lambda n : setattr(self, 'feature_settings', n.get_object_value(microsoft_authenticator_feature_settings.MicrosoftAuthenticatorFeatureSettings)),
            "include_targets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(microsoft_authenticator_authentication_method_target.MicrosoftAuthenticatorAuthenticationMethodTarget)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def include_targets(self,) -> Optional[List[microsoft_authenticator_authentication_method_target.MicrosoftAuthenticatorAuthenticationMethodTarget]]:
        """
        Gets the includeTargets property value. A collection of users or groups who are enabled to use the authentication method. Expanded by default.
        Returns: Optional[List[microsoft_authenticator_authentication_method_target.MicrosoftAuthenticatorAuthenticationMethodTarget]]
        """
        return self._include_targets
    
    @include_targets.setter
    def include_targets(self,value: Optional[List[microsoft_authenticator_authentication_method_target.MicrosoftAuthenticatorAuthenticationMethodTarget]] = None) -> None:
        """
        Sets the includeTargets property value. A collection of users or groups who are enabled to use the authentication method. Expanded by default.
        Args:
            value: Value to set for the includeTargets property.
        """
        self._include_targets = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("featureSettings", self.feature_settings)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
    

