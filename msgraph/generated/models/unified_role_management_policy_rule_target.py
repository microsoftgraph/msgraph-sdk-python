from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')
unified_role_management_policy_rule_target_operations = lazy_import('msgraph.generated.models.unified_role_management_policy_rule_target_operations')

class UnifiedRoleManagementPolicyRuleTarget(AdditionalDataHolder, Parsable):
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
    
    @property
    def caller(self,) -> Optional[str]:
        """
        Gets the caller property value. The type of caller that's the target of the policy rule. Allowed values are: None, Admin, EndUser.
        Returns: Optional[str]
        """
        return self._caller
    
    @caller.setter
    def caller(self,value: Optional[str] = None) -> None:
        """
        Sets the caller property value. The type of caller that's the target of the policy rule. Allowed values are: None, Admin, EndUser.
        Args:
            value: Value to set for the caller property.
        """
        self._caller = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleManagementPolicyRuleTarget and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The type of caller that's the target of the policy rule. Allowed values are: None, Admin, EndUser.
        self._caller: Optional[str] = None
        # The list of role settings that are enforced and cannot be overridden by child scopes. Use All for all settings.
        self._enforced_settings: Optional[List[str]] = None
        # The list of role settings that can be inherited by child scopes. Use All for all settings.
        self._inheritable_settings: Optional[List[str]] = None
        # The role assignment type that's the target of policy rule. Allowed values are: Eligibility, Assignment.
        self._level: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The role management operations that are the target of the policy rule. Allowed values are: All, Activate, Deactivate, Assign, Update, Remove, Extend, Renew.
        self._operations: Optional[List[unified_role_management_policy_rule_target_operations.UnifiedRoleManagementPolicyRuleTargetOperations]] = None
        # The targetObjects property
        self._target_objects: Optional[List[directory_object.DirectoryObject]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyRuleTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyRuleTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementPolicyRuleTarget()
    
    @property
    def enforced_settings(self,) -> Optional[List[str]]:
        """
        Gets the enforcedSettings property value. The list of role settings that are enforced and cannot be overridden by child scopes. Use All for all settings.
        Returns: Optional[List[str]]
        """
        return self._enforced_settings
    
    @enforced_settings.setter
    def enforced_settings(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enforcedSettings property value. The list of role settings that are enforced and cannot be overridden by child scopes. Use All for all settings.
        Args:
            value: Value to set for the enforcedSettings property.
        """
        self._enforced_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "caller": lambda n : setattr(self, 'caller', n.get_str_value()),
            "enforced_settings": lambda n : setattr(self, 'enforced_settings', n.get_collection_of_primitive_values(str)),
            "inheritable_settings": lambda n : setattr(self, 'inheritable_settings', n.get_collection_of_primitive_values(str)),
            "level": lambda n : setattr(self, 'level', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_enum_values(unified_role_management_policy_rule_target_operations.UnifiedRoleManagementPolicyRuleTargetOperations)),
            "target_objects": lambda n : setattr(self, 'target_objects', n.get_collection_of_object_values(directory_object.DirectoryObject)),
        }
        return fields
    
    @property
    def inheritable_settings(self,) -> Optional[List[str]]:
        """
        Gets the inheritableSettings property value. The list of role settings that can be inherited by child scopes. Use All for all settings.
        Returns: Optional[List[str]]
        """
        return self._inheritable_settings
    
    @inheritable_settings.setter
    def inheritable_settings(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the inheritableSettings property value. The list of role settings that can be inherited by child scopes. Use All for all settings.
        Args:
            value: Value to set for the inheritableSettings property.
        """
        self._inheritable_settings = value
    
    @property
    def level(self,) -> Optional[str]:
        """
        Gets the level property value. The role assignment type that's the target of policy rule. Allowed values are: Eligibility, Assignment.
        Returns: Optional[str]
        """
        return self._level
    
    @level.setter
    def level(self,value: Optional[str] = None) -> None:
        """
        Sets the level property value. The role assignment type that's the target of policy rule. Allowed values are: Eligibility, Assignment.
        Args:
            value: Value to set for the level property.
        """
        self._level = value
    
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
    
    @property
    def operations(self,) -> Optional[List[unified_role_management_policy_rule_target_operations.UnifiedRoleManagementPolicyRuleTargetOperations]]:
        """
        Gets the operations property value. The role management operations that are the target of the policy rule. Allowed values are: All, Activate, Deactivate, Assign, Update, Remove, Extend, Renew.
        Returns: Optional[List[unified_role_management_policy_rule_target_operations.UnifiedRoleManagementPolicyRuleTargetOperations]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[unified_role_management_policy_rule_target_operations.UnifiedRoleManagementPolicyRuleTargetOperations]] = None) -> None:
        """
        Sets the operations property value. The role management operations that are the target of the policy rule. Allowed values are: All, Activate, Deactivate, Assign, Update, Remove, Extend, Renew.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("caller", self.caller)
        writer.write_collection_of_primitive_values("enforcedSettings", self.enforced_settings)
        writer.write_collection_of_primitive_values("inheritableSettings", self.inheritable_settings)
        writer.write_str_value("level", self.level)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("operations", self.operations)
        writer.write_collection_of_object_values("targetObjects", self.target_objects)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target_objects(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the targetObjects property value. The targetObjects property
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._target_objects
    
    @target_objects.setter
    def target_objects(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the targetObjects property value. The targetObjects property
        Args:
            value: Value to set for the targetObjects property.
        """
        self._target_objects = value
    

