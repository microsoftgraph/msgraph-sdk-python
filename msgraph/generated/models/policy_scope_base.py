from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dlp_action_info import DlpActionInfo
    from .execution_mode import ExecutionMode
    from .policy_location import PolicyLocation
    from .policy_tenant_scope import PolicyTenantScope
    from .policy_user_scope import PolicyUserScope
    from .user_activity_types import UserActivityTypes

@dataclass
class PolicyScopeBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The activities property
    activities: Optional[UserActivityTypes] = None
    # The executionMode property
    execution_mode: Optional[ExecutionMode] = None
    # The locations (like domains or URLs) to be protected. Required.
    locations: Optional[list[PolicyLocation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The enforcement actions to take if the policy conditions are met within this scope. Required.
    policy_actions: Optional[list[DlpActionInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyScopeBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyScopeBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyTenantScope".casefold():
            from .policy_tenant_scope import PolicyTenantScope

            return PolicyTenantScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyUserScope".casefold():
            from .policy_user_scope import PolicyUserScope

            return PolicyUserScope()
        return PolicyScopeBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dlp_action_info import DlpActionInfo
        from .execution_mode import ExecutionMode
        from .policy_location import PolicyLocation
        from .policy_tenant_scope import PolicyTenantScope
        from .policy_user_scope import PolicyUserScope
        from .user_activity_types import UserActivityTypes

        from .dlp_action_info import DlpActionInfo
        from .execution_mode import ExecutionMode
        from .policy_location import PolicyLocation
        from .policy_tenant_scope import PolicyTenantScope
        from .policy_user_scope import PolicyUserScope
        from .user_activity_types import UserActivityTypes

        fields: dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_enum_values(UserActivityTypes)),
            "executionMode": lambda n : setattr(self, 'execution_mode', n.get_enum_value(ExecutionMode)),
            "locations": lambda n : setattr(self, 'locations', n.get_collection_of_object_values(PolicyLocation)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyActions": lambda n : setattr(self, 'policy_actions', n.get_collection_of_object_values(DlpActionInfo)),
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
        writer.write_enum_value("activities", self.activities)
        writer.write_enum_value("executionMode", self.execution_mode)
        writer.write_collection_of_object_values("locations", self.locations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("policyActions", self.policy_actions)
        writer.write_additional_data_value(self.additional_data)
    

