from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import b2x_identity_user_flow, entity, user_flow_type

from . import entity

@dataclass
class IdentityUserFlow(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The userFlowType property
    user_flow_type: Optional[user_flow_type.UserFlowType] = None
    # The userFlowTypeVersion property
    user_flow_type_version: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityUserFlow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityUserFlow
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.b2xIdentityUserFlow".casefold():
            from . import b2x_identity_user_flow

            return b2x_identity_user_flow.B2xIdentityUserFlow()
        return IdentityUserFlow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import b2x_identity_user_flow, entity, user_flow_type

        from . import b2x_identity_user_flow, entity, user_flow_type

        fields: Dict[str, Callable[[Any], None]] = {
            "userFlowType": lambda n : setattr(self, 'user_flow_type', n.get_enum_value(user_flow_type.UserFlowType)),
            "userFlowTypeVersion": lambda n : setattr(self, 'user_flow_type_version', n.get_float_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("userFlowType", self.user_flow_type)
        writer.write_float_value("userFlowTypeVersion", self.user_flow_type_version)
    

