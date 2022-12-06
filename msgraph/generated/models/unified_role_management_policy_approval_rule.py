from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

approval_settings = lazy_import('msgraph.generated.models.approval_settings')
unified_role_management_policy_rule = lazy_import('msgraph.generated.models.unified_role_management_policy_rule')

class UnifiedRoleManagementPolicyApprovalRule(unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule):
    def __init__(self,) -> None:
        """
        Instantiates a new UnifiedRoleManagementPolicyApprovalRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule"
        # The settings for approval of the role assignment.
        self._setting: Optional[approval_settings.ApprovalSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyApprovalRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyApprovalRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementPolicyApprovalRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "setting": lambda n : setattr(self, 'setting', n.get_object_value(approval_settings.ApprovalSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("setting", self.setting)
    
    @property
    def setting(self,) -> Optional[approval_settings.ApprovalSettings]:
        """
        Gets the setting property value. The settings for approval of the role assignment.
        Returns: Optional[approval_settings.ApprovalSettings]
        """
        return self._setting
    
    @setting.setter
    def setting(self,value: Optional[approval_settings.ApprovalSettings] = None) -> None:
        """
        Sets the setting property value. The settings for approval of the role assignment.
        Args:
            value: Value to set for the setting property.
        """
        self._setting = value
    

