from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import unified_role_management_policy_rule

from . import unified_role_management_policy_rule

class UnifiedRoleManagementPolicyExpirationRule(unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule):
    def __init__(self,) -> None:
        """
        Instantiates a new UnifiedRoleManagementPolicyExpirationRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule"
        # Indicates whether expiration is required or if it's a permanently active assignment or eligibility.
        self._is_expiration_required: Optional[bool] = None
        # The maximum duration allowed for eligibility or assignment which is not permanent. Required when isExpirationRequired is true.
        self._maximum_duration: Optional[timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyExpirationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyExpirationRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementPolicyExpirationRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import unified_role_management_policy_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "isExpirationRequired": lambda n : setattr(self, 'is_expiration_required', n.get_bool_value()),
            "maximumDuration": lambda n : setattr(self, 'maximum_duration', n.get_timedelta_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_expiration_required(self,) -> Optional[bool]:
        """
        Gets the isExpirationRequired property value. Indicates whether expiration is required or if it's a permanently active assignment or eligibility.
        Returns: Optional[bool]
        """
        return self._is_expiration_required
    
    @is_expiration_required.setter
    def is_expiration_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isExpirationRequired property value. Indicates whether expiration is required or if it's a permanently active assignment or eligibility.
        Args:
            value: Value to set for the is_expiration_required property.
        """
        self._is_expiration_required = value
    
    @property
    def maximum_duration(self,) -> Optional[timedelta]:
        """
        Gets the maximumDuration property value. The maximum duration allowed for eligibility or assignment which is not permanent. Required when isExpirationRequired is true.
        Returns: Optional[timedelta]
        """
        return self._maximum_duration
    
    @maximum_duration.setter
    def maximum_duration(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the maximumDuration property value. The maximum duration allowed for eligibility or assignment which is not permanent. Required when isExpirationRequired is true.
        Args:
            value: Value to set for the maximum_duration property.
        """
        self._maximum_duration = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isExpirationRequired", self.is_expiration_required)
        writer.write_timedelta_value("maximumDuration", self.maximum_duration)
    

