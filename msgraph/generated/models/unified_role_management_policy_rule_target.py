from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .unified_role_management_policy_rule_target_operations import UnifiedRoleManagementPolicyRuleTargetOperations

@dataclass
class UnifiedRoleManagementPolicyRuleTarget(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The type of caller that's the target of the policy rule. Allowed values are: None, Admin, EndUser.
    caller: Optional[str] = None
    # The list of role settings that are enforced and cannot be overridden by child scopes. Use All for all settings.
    enforced_settings: Optional[list[str]] = None
    # The list of role settings that can be inherited by child scopes. Use All for all settings.
    inheritable_settings: Optional[list[str]] = None
    # The role assignment type that's the target of policy rule. Allowed values are: Eligibility, Assignment.
    level: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The role management operations that are the target of the policy rule. Allowed values are: All, Activate, Deactivate, Assign, Update, Remove, Extend, Renew.
    operations: Optional[list[UnifiedRoleManagementPolicyRuleTargetOperations]] = None
    # The targetObjects property
    target_objects: Optional[list[DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleManagementPolicyRuleTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyRuleTarget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementPolicyRuleTarget()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .unified_role_management_policy_rule_target_operations import UnifiedRoleManagementPolicyRuleTargetOperations

        from .directory_object import DirectoryObject
        from .unified_role_management_policy_rule_target_operations import UnifiedRoleManagementPolicyRuleTargetOperations

        fields: dict[str, Callable[[Any], None]] = {
            "caller": lambda n : setattr(self, 'caller', n.get_str_value()),
            "enforcedSettings": lambda n : setattr(self, 'enforced_settings', n.get_collection_of_primitive_values(str)),
            "inheritableSettings": lambda n : setattr(self, 'inheritable_settings', n.get_collection_of_primitive_values(str)),
            "level": lambda n : setattr(self, 'level', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_enum_values(UnifiedRoleManagementPolicyRuleTargetOperations)),
            "targetObjects": lambda n : setattr(self, 'target_objects', n.get_collection_of_object_values(DirectoryObject)),
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
        writer.write_str_value("caller", self.caller)
        writer.write_collection_of_primitive_values("enforcedSettings", self.enforced_settings)
        writer.write_collection_of_primitive_values("inheritableSettings", self.inheritable_settings)
        writer.write_str_value("level", self.level)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_enum_values("operations", self.operations)
        writer.write_collection_of_object_values("targetObjects", self.target_objects)
        writer.write_additional_data_value(self.additional_data)
    

