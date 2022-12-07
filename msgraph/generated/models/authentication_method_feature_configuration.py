from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

advanced_config_state = lazy_import('msgraph.generated.models.advanced_config_state')
feature_target = lazy_import('msgraph.generated.models.feature_target')

class AuthenticationMethodFeatureConfiguration(AdditionalDataHolder, Parsable):
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
        Instantiates a new authenticationMethodFeatureConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A single entity that is excluded from this feature.
        self._exclude_target: Optional[feature_target.FeatureTarget] = None
        # A single entity that is included in this feature.
        self._include_target: Optional[feature_target.FeatureTarget] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Enable or disable the feature. Possible values are: default, enabled, disabled, unknownFutureValue. The default value is used when the configuration hasn't been explicitly set and uses the default behavior of Azure AD for the setting. The default value is disabled.
        self._state: Optional[advanced_config_state.AdvancedConfigState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodFeatureConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodFeatureConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationMethodFeatureConfiguration()
    
    @property
    def exclude_target(self,) -> Optional[feature_target.FeatureTarget]:
        """
        Gets the excludeTarget property value. A single entity that is excluded from this feature.
        Returns: Optional[feature_target.FeatureTarget]
        """
        return self._exclude_target
    
    @exclude_target.setter
    def exclude_target(self,value: Optional[feature_target.FeatureTarget] = None) -> None:
        """
        Sets the excludeTarget property value. A single entity that is excluded from this feature.
        Args:
            value: Value to set for the excludeTarget property.
        """
        self._exclude_target = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exclude_target": lambda n : setattr(self, 'exclude_target', n.get_object_value(feature_target.FeatureTarget)),
            "include_target": lambda n : setattr(self, 'include_target', n.get_object_value(feature_target.FeatureTarget)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(advanced_config_state.AdvancedConfigState)),
        }
        return fields
    
    @property
    def include_target(self,) -> Optional[feature_target.FeatureTarget]:
        """
        Gets the includeTarget property value. A single entity that is included in this feature.
        Returns: Optional[feature_target.FeatureTarget]
        """
        return self._include_target
    
    @include_target.setter
    def include_target(self,value: Optional[feature_target.FeatureTarget] = None) -> None:
        """
        Sets the includeTarget property value. A single entity that is included in this feature.
        Args:
            value: Value to set for the includeTarget property.
        """
        self._include_target = value
    
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
        writer.write_object_value("excludeTarget", self.exclude_target)
        writer.write_object_value("includeTarget", self.include_target)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[advanced_config_state.AdvancedConfigState]:
        """
        Gets the state property value. Enable or disable the feature. Possible values are: default, enabled, disabled, unknownFutureValue. The default value is used when the configuration hasn't been explicitly set and uses the default behavior of Azure AD for the setting. The default value is disabled.
        Returns: Optional[advanced_config_state.AdvancedConfigState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[advanced_config_state.AdvancedConfigState] = None) -> None:
        """
        Sets the state property value. Enable or disable the feature. Possible values are: default, enabled, disabled, unknownFutureValue. The default value is used when the configuration hasn't been explicitly set and uses the default behavior of Azure AD for the setting. The default value is disabled.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

