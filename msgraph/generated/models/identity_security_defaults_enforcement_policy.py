from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_base import PolicyBase

from .policy_base import PolicyBase

@dataclass
class IdentitySecurityDefaultsEnforcementPolicy(PolicyBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy"
    # If set to true, Microsoft Entra security defaults are enabled for the tenant.
    is_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentitySecurityDefaultsEnforcementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentitySecurityDefaultsEnforcementPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdentitySecurityDefaultsEnforcementPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .policy_base import PolicyBase

        from .policy_base import PolicyBase

        fields: Dict[str, Callable[[Any], None]] = {
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .policy_base import PolicyBase

        writer.write_bool_value("isEnabled", self.is_enabled)
    

