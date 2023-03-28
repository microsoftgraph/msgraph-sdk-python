from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_built_in_user_flow_attribute, identity_custom_user_flow_attribute, identity_user_flow_attribute_data_type, identity_user_flow_attribute_type

from . import entity

class IdentityUserFlowAttribute(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new identityUserFlowAttribute and sets the default values.
        """
        super().__init__()
        # The dataType property
        self._data_type: Optional[identity_user_flow_attribute_data_type.IdentityUserFlowAttributeDataType] = None
        # The description of the user flow attribute that's shown to the user at the time of sign-up.
        self._description: Optional[str] = None
        # The display name of the user flow attribute.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The userFlowAttributeType property
        self._user_flow_attribute_type: Optional[identity_user_flow_attribute_type.IdentityUserFlowAttributeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityUserFlowAttribute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityUserFlowAttribute
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.identityBuiltInUserFlowAttribute":
                from . import identity_built_in_user_flow_attribute

                return identity_built_in_user_flow_attribute.IdentityBuiltInUserFlowAttribute()
            if mapping_value == "#microsoft.graph.identityCustomUserFlowAttribute":
                from . import identity_custom_user_flow_attribute

                return identity_custom_user_flow_attribute.IdentityCustomUserFlowAttribute()
        return IdentityUserFlowAttribute()
    
    @property
    def data_type(self,) -> Optional[identity_user_flow_attribute_data_type.IdentityUserFlowAttributeDataType]:
        """
        Gets the dataType property value. The dataType property
        Returns: Optional[identity_user_flow_attribute_data_type.IdentityUserFlowAttributeDataType]
        """
        return self._data_type
    
    @data_type.setter
    def data_type(self,value: Optional[identity_user_flow_attribute_data_type.IdentityUserFlowAttributeDataType] = None) -> None:
        """
        Sets the dataType property value. The dataType property
        Args:
            value: Value to set for the data_type property.
        """
        self._data_type = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the user flow attribute that's shown to the user at the time of sign-up.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the user flow attribute that's shown to the user at the time of sign-up.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the user flow attribute.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the user flow attribute.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_built_in_user_flow_attribute, identity_custom_user_flow_attribute, identity_user_flow_attribute_data_type, identity_user_flow_attribute_type

        fields: Dict[str, Callable[[Any], None]] = {
            "dataType": lambda n : setattr(self, 'data_type', n.get_enum_value(identity_user_flow_attribute_data_type.IdentityUserFlowAttributeDataType)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "userFlowAttributeType": lambda n : setattr(self, 'user_flow_attribute_type', n.get_enum_value(identity_user_flow_attribute_type.IdentityUserFlowAttributeType)),
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
        writer.write_enum_value("dataType", self.data_type)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("userFlowAttributeType", self.user_flow_attribute_type)
    
    @property
    def user_flow_attribute_type(self,) -> Optional[identity_user_flow_attribute_type.IdentityUserFlowAttributeType]:
        """
        Gets the userFlowAttributeType property value. The userFlowAttributeType property
        Returns: Optional[identity_user_flow_attribute_type.IdentityUserFlowAttributeType]
        """
        return self._user_flow_attribute_type
    
    @user_flow_attribute_type.setter
    def user_flow_attribute_type(self,value: Optional[identity_user_flow_attribute_type.IdentityUserFlowAttributeType] = None) -> None:
        """
        Sets the userFlowAttributeType property value. The userFlowAttributeType property
        Args:
            value: Value to set for the user_flow_attribute_type property.
        """
        self._user_flow_attribute_type = value
    

