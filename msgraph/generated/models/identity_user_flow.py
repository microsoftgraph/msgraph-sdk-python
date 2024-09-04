from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .b2x_identity_user_flow import B2xIdentityUserFlow
    from .entity import Entity
    from .user_flow_type import UserFlowType

from .entity import Entity

@dataclass
class IdentityUserFlow(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The userFlowType property
    user_flow_type: Optional[UserFlowType] = None
    # The userFlowTypeVersion property
    user_flow_type_version: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityUserFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityUserFlow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.b2xIdentityUserFlow".casefold():
            from .b2x_identity_user_flow import B2xIdentityUserFlow

            return B2xIdentityUserFlow()
        return IdentityUserFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .b2x_identity_user_flow import B2xIdentityUserFlow
        from .entity import Entity
        from .user_flow_type import UserFlowType

        from .b2x_identity_user_flow import B2xIdentityUserFlow
        from .entity import Entity
        from .user_flow_type import UserFlowType

        fields: Dict[str, Callable[[Any], None]] = {
            "userFlowType": lambda n : setattr(self, 'user_flow_type', n.get_enum_value(UserFlowType)),
            "userFlowTypeVersion": lambda n : setattr(self, 'user_flow_type_version', n.get_float_value()),
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
        writer.write_enum_value("userFlowType", self.user_flow_type)
        writer.write_float_value("userFlowTypeVersion", self.user_flow_type_version)
    

