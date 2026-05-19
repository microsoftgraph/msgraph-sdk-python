from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
    from .app_management_restriction_state import AppManagementRestrictionState

@dataclass
class IdentifierUriRestriction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Collection of custom security attribute exemptions. If an actor user or service principal has the custom security attribute defined in this section, they're exempted from the restriction.  This means that calls the user or service principal makes to create or update apps are exempt from this policy enforcement.
    exclude_actors: Optional[AppManagementPolicyActorExemptions] = None
    # If true, the restriction isn't enforced for applications that are configured to receive V2 tokens in Microsoft Entra ID; else, the restriction is enforced for those applications.
    exclude_apps_receiving_v2_tokens: Optional[bool] = None
    # If true, the restriction isn't enforced for SAML applications in Microsoft Entra ID; else, the restriction is enforced for those applications.
    exclude_saml: Optional[bool] = None
    # If true, Microsoft sets the identifierUriRestriction state. If false, the tenant modifies the identifierUriRestriction state. Read-only.
    is_state_set_by_microsoft: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the date from which the policy restriction applies to newly created applications. For existing applications, the enforcement date can be retroactively applied.
    restrict_for_apps_created_after_date_time: Optional[datetime.datetime] = None
    # The state property
    state: Optional[AppManagementRestrictionState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentifierUriRestriction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentifierUriRestriction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdentifierUriRestriction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState

        from .app_management_policy_actor_exemptions import AppManagementPolicyActorExemptions
        from .app_management_restriction_state import AppManagementRestrictionState

        fields: dict[str, Callable[[Any], None]] = {
            "excludeActors": lambda n : setattr(self, 'exclude_actors', n.get_object_value(AppManagementPolicyActorExemptions)),
            "excludeAppsReceivingV2Tokens": lambda n : setattr(self, 'exclude_apps_receiving_v2_tokens', n.get_bool_value()),
            "excludeSaml": lambda n : setattr(self, 'exclude_saml', n.get_bool_value()),
            "isStateSetByMicrosoft": lambda n : setattr(self, 'is_state_set_by_microsoft', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restrictForAppsCreatedAfterDateTime": lambda n : setattr(self, 'restrict_for_apps_created_after_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AppManagementRestrictionState)),
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
        writer.write_object_value("excludeActors", self.exclude_actors)
        writer.write_bool_value("excludeAppsReceivingV2Tokens", self.exclude_apps_receiving_v2_tokens)
        writer.write_bool_value("excludeSaml", self.exclude_saml)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("restrictForAppsCreatedAfterDateTime", self.restrict_for_apps_created_after_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

