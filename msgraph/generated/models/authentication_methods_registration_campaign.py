from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

advanced_config_state = lazy_import('msgraph.generated.models.advanced_config_state')
authentication_methods_registration_campaign_include_target = lazy_import('msgraph.generated.models.authentication_methods_registration_campaign_include_target')
exclude_target = lazy_import('msgraph.generated.models.exclude_target')

class AuthenticationMethodsRegistrationCampaign(AdditionalDataHolder, Parsable):
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
        Instantiates a new authenticationMethodsRegistrationCampaign and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Users and groups of users that are excluded from being prompted to set up the authentication method.
        self._exclude_targets: Optional[List[exclude_target.ExcludeTarget]] = None
        # Users and groups of users that are prompted to set up the authentication method.
        self._include_targets: Optional[List[authentication_methods_registration_campaign_include_target.AuthenticationMethodsRegistrationCampaignIncludeTarget]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies the number of days that the user sees a prompt again if they select 'Not now' and snoozes the prompt. Minimum: 0 days. Maximum: 14 days. If the value is '0', the user is prompted during every MFA attempt.
        self._snooze_duration_in_days: Optional[int] = None
        # The state property
        self._state: Optional[advanced_config_state.AdvancedConfigState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodsRegistrationCampaign:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodsRegistrationCampaign
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationMethodsRegistrationCampaign()
    
    @property
    def exclude_targets(self,) -> Optional[List[exclude_target.ExcludeTarget]]:
        """
        Gets the excludeTargets property value. Users and groups of users that are excluded from being prompted to set up the authentication method.
        Returns: Optional[List[exclude_target.ExcludeTarget]]
        """
        return self._exclude_targets
    
    @exclude_targets.setter
    def exclude_targets(self,value: Optional[List[exclude_target.ExcludeTarget]] = None) -> None:
        """
        Sets the excludeTargets property value. Users and groups of users that are excluded from being prompted to set up the authentication method.
        Args:
            value: Value to set for the excludeTargets property.
        """
        self._exclude_targets = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "exclude_targets": lambda n : setattr(self, 'exclude_targets', n.get_collection_of_object_values(exclude_target.ExcludeTarget)),
            "include_targets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(authentication_methods_registration_campaign_include_target.AuthenticationMethodsRegistrationCampaignIncludeTarget)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "snooze_duration_in_days": lambda n : setattr(self, 'snooze_duration_in_days', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(advanced_config_state.AdvancedConfigState)),
        }
        return fields
    
    @property
    def include_targets(self,) -> Optional[List[authentication_methods_registration_campaign_include_target.AuthenticationMethodsRegistrationCampaignIncludeTarget]]:
        """
        Gets the includeTargets property value. Users and groups of users that are prompted to set up the authentication method.
        Returns: Optional[List[authentication_methods_registration_campaign_include_target.AuthenticationMethodsRegistrationCampaignIncludeTarget]]
        """
        return self._include_targets
    
    @include_targets.setter
    def include_targets(self,value: Optional[List[authentication_methods_registration_campaign_include_target.AuthenticationMethodsRegistrationCampaignIncludeTarget]] = None) -> None:
        """
        Sets the includeTargets property value. Users and groups of users that are prompted to set up the authentication method.
        Args:
            value: Value to set for the includeTargets property.
        """
        self._include_targets = value
    
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
        writer.write_collection_of_object_values("excludeTargets", self.exclude_targets)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("snoozeDurationInDays", self.snooze_duration_in_days)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def snooze_duration_in_days(self,) -> Optional[int]:
        """
        Gets the snoozeDurationInDays property value. Specifies the number of days that the user sees a prompt again if they select 'Not now' and snoozes the prompt. Minimum: 0 days. Maximum: 14 days. If the value is '0', the user is prompted during every MFA attempt.
        Returns: Optional[int]
        """
        return self._snooze_duration_in_days
    
    @snooze_duration_in_days.setter
    def snooze_duration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the snoozeDurationInDays property value. Specifies the number of days that the user sees a prompt again if they select 'Not now' and snoozes the prompt. Minimum: 0 days. Maximum: 14 days. If the value is '0', the user is prompted during every MFA attempt.
        Args:
            value: Value to set for the snoozeDurationInDays property.
        """
        self._snooze_duration_in_days = value
    
    @property
    def state(self,) -> Optional[advanced_config_state.AdvancedConfigState]:
        """
        Gets the state property value. The state property
        Returns: Optional[advanced_config_state.AdvancedConfigState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[advanced_config_state.AdvancedConfigState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

