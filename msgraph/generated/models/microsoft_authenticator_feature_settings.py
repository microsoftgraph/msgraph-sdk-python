from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_feature_configuration = lazy_import('msgraph.generated.models.authentication_method_feature_configuration')

class MicrosoftAuthenticatorFeatureSettings(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new microsoftAuthenticatorFeatureSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Determines whether the user's Authenticator app will show them the client app they are signing into.
        self._display_app_information_required_state: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None
        # Determines whether the user's Authenticator app will show them the geographic location of where the authentication request originated from.
        self._display_location_information_required_state: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftAuthenticatorFeatureSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAuthenticatorFeatureSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftAuthenticatorFeatureSettings()
    
    @property
    def display_app_information_required_state(self,) -> Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]:
        """
        Gets the displayAppInformationRequiredState property value. Determines whether the user's Authenticator app will show them the client app they are signing into.
        Returns: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]
        """
        return self._display_app_information_required_state
    
    @display_app_information_required_state.setter
    def display_app_information_required_state(self,value: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None) -> None:
        """
        Sets the displayAppInformationRequiredState property value. Determines whether the user's Authenticator app will show them the client app they are signing into.
        Args:
            value: Value to set for the displayAppInformationRequiredState property.
        """
        self._display_app_information_required_state = value
    
    @property
    def display_location_information_required_state(self,) -> Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]:
        """
        Gets the displayLocationInformationRequiredState property value. Determines whether the user's Authenticator app will show them the geographic location of where the authentication request originated from.
        Returns: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]
        """
        return self._display_location_information_required_state
    
    @display_location_information_required_state.setter
    def display_location_information_required_state(self,value: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None) -> None:
        """
        Sets the displayLocationInformationRequiredState property value. Determines whether the user's Authenticator app will show them the geographic location of where the authentication request originated from.
        Args:
            value: Value to set for the displayLocationInformationRequiredState property.
        """
        self._display_location_information_required_state = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_app_information_required_state": lambda n : setattr(self, 'display_app_information_required_state', n.get_object_value(authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration)),
            "display_location_information_required_state": lambda n : setattr(self, 'display_location_information_required_state', n.get_object_value(authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("displayAppInformationRequiredState", self.display_app_information_required_state)
        writer.write_object_value("displayLocationInformationRequiredState", self.display_location_information_required_state)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

