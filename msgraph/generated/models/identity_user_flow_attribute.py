from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
    from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
    from .identity_user_flow_attribute_data_type import IdentityUserFlowAttributeDataType
    from .identity_user_flow_attribute_type import IdentityUserFlowAttributeType

from .entity import Entity

@dataclass
class IdentityUserFlowAttribute(Entity):
    # The dataType property
    data_type: Optional[IdentityUserFlowAttributeDataType] = None
    # The description of the user flow attribute that's shown to the user at the time of sign up.
    description: Optional[str] = None
    # The display name of the user flow attribute.  Supports $filter (eq, ne).
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The userFlowAttributeType property
    user_flow_attribute_type: Optional[IdentityUserFlowAttributeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityUserFlowAttribute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityUserFlowAttribute
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityBuiltInUserFlowAttribute".casefold():
            from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute

            return IdentityBuiltInUserFlowAttribute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityCustomUserFlowAttribute".casefold():
            from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute

            return IdentityCustomUserFlowAttribute()
        return IdentityUserFlowAttribute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
        from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
        from .identity_user_flow_attribute_data_type import IdentityUserFlowAttributeDataType
        from .identity_user_flow_attribute_type import IdentityUserFlowAttributeType

        from .entity import Entity
        from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
        from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
        from .identity_user_flow_attribute_data_type import IdentityUserFlowAttributeDataType
        from .identity_user_flow_attribute_type import IdentityUserFlowAttributeType

        fields: Dict[str, Callable[[Any], None]] = {
            "dataType": lambda n : setattr(self, 'data_type', n.get_enum_value(IdentityUserFlowAttributeDataType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "userFlowAttributeType": lambda n : setattr(self, 'user_flow_attribute_type', n.get_enum_value(IdentityUserFlowAttributeType)),
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
        writer.write_enum_value("dataType", self.data_type)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("userFlowAttributeType", self.user_flow_attribute_type)
    

