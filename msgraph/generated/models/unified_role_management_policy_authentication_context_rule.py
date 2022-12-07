from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

unified_role_management_policy_rule = lazy_import('msgraph.generated.models.unified_role_management_policy_rule')

class UnifiedRoleManagementPolicyAuthenticationContextRule(unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule):
    @property
    def claim_value(self,) -> Optional[str]:
        """
        Gets the claimValue property value. The value of the authentication context claim.
        Returns: Optional[str]
        """
        return self._claim_value
    
    @claim_value.setter
    def claim_value(self,value: Optional[str] = None) -> None:
        """
        Sets the claimValue property value. The value of the authentication context claim.
        Args:
            value: Value to set for the claimValue property.
        """
        self._claim_value = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new UnifiedRoleManagementPolicyAuthenticationContextRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule"
        # The value of the authentication context claim.
        self._claim_value: Optional[str] = None
        # Whether this rule is enabled.
        self._is_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyAuthenticationContextRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyAuthenticationContextRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementPolicyAuthenticationContextRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "claim_value": lambda n : setattr(self, 'claim_value', n.get_str_value()),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Whether this rule is enabled.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Whether this rule is enabled.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("claimValue", self.claim_value)
        writer.write_bool_value("isEnabled", self.is_enabled)
    

