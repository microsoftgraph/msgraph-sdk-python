from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import advanced_config_state, authentication_methods_registration_campaign_include_target, exclude_target

@dataclass
class AuthenticationMethodsRegistrationCampaign(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Users and groups of users that are excluded from being prompted to set up the authentication method.
    exclude_targets: Optional[List[exclude_target.ExcludeTarget]] = None
    # Users and groups of users that are prompted to set up the authentication method.
    include_targets: Optional[List[authentication_methods_registration_campaign_include_target.AuthenticationMethodsRegistrationCampaignIncludeTarget]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the number of days that the user sees a prompt again if they select 'Not now' and snoozes the prompt. Minimum: 0 days. Maximum: 14 days. If the value is '0', the user is prompted during every MFA attempt.
    snooze_duration_in_days: Optional[int] = None
    # The state property
    state: Optional[advanced_config_state.AdvancedConfigState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodsRegistrationCampaign:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodsRegistrationCampaign
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationMethodsRegistrationCampaign()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import advanced_config_state, authentication_methods_registration_campaign_include_target, exclude_target

        from . import advanced_config_state, authentication_methods_registration_campaign_include_target, exclude_target

        fields: Dict[str, Callable[[Any], None]] = {
            "excludeTargets": lambda n : setattr(self, 'exclude_targets', n.get_collection_of_object_values(exclude_target.ExcludeTarget)),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(authentication_methods_registration_campaign_include_target.AuthenticationMethodsRegistrationCampaignIncludeTarget)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "snoozeDurationInDays": lambda n : setattr(self, 'snooze_duration_in_days', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(advanced_config_state.AdvancedConfigState)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("excludeTargets", self.exclude_targets)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("snoozeDurationInDays", self.snooze_duration_in_days)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

