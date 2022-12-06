from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_base = lazy_import('msgraph.generated.models.policy_base')

class IdentitySecurityDefaultsEnforcementPolicy(policy_base.PolicyBase):
    def __init__(self,) -> None:
        """
        Instantiates a new IdentitySecurityDefaultsEnforcementPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy"
        # If set to true, Azure Active Directory security defaults is enabled for the tenant.
        self._is_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentitySecurityDefaultsEnforcementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentitySecurityDefaultsEnforcementPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdentitySecurityDefaultsEnforcementPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. If set to true, Azure Active Directory security defaults is enabled for the tenant.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. If set to true, Azure Active Directory security defaults is enabled for the tenant.
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
        writer.write_bool_value("isEnabled", self.is_enabled)
    

