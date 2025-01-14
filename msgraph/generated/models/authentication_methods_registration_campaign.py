from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .advanced_config_state import AdvancedConfigState
    from .authentication_methods_registration_campaign_include_target import AuthenticationMethodsRegistrationCampaignIncludeTarget
    from .exclude_target import ExcludeTarget

@dataclass
class AuthenticationMethodsRegistrationCampaign(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Users and groups of users that are excluded from being prompted to set up the authentication method.
    exclude_targets: Optional[list[ExcludeTarget]] = None
    # Users and groups of users that are prompted to set up the authentication method.
    include_targets: Optional[list[AuthenticationMethodsRegistrationCampaignIncludeTarget]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the number of days that the user sees a prompt again if they select 'Not now' and snoozes the prompt. Minimum: 0 days. Maximum: 14 days. If the value is '0', the user is prompted during every MFA attempt.
    snooze_duration_in_days: Optional[int] = None
    # The state property
    state: Optional[AdvancedConfigState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationMethodsRegistrationCampaign:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodsRegistrationCampaign
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationMethodsRegistrationCampaign()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .advanced_config_state import AdvancedConfigState
        from .authentication_methods_registration_campaign_include_target import AuthenticationMethodsRegistrationCampaignIncludeTarget
        from .exclude_target import ExcludeTarget

        from .advanced_config_state import AdvancedConfigState
        from .authentication_methods_registration_campaign_include_target import AuthenticationMethodsRegistrationCampaignIncludeTarget
        from .exclude_target import ExcludeTarget

        fields: dict[str, Callable[[Any], None]] = {
            "excludeTargets": lambda n : setattr(self, 'exclude_targets', n.get_collection_of_object_values(ExcludeTarget)),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(AuthenticationMethodsRegistrationCampaignIncludeTarget)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "snoozeDurationInDays": lambda n : setattr(self, 'snooze_duration_in_days', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AdvancedConfigState)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("excludeTargets", self.exclude_targets)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("snoozeDurationInDays", self.snooze_duration_in_days)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

