from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity = lazy_import('msgraph.generated.models.identity')

class ScopedRoleMembership(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def administrative_unit_id(self,) -> Optional[str]:
        """
        Gets the administrativeUnitId property value. Unique identifier for the administrative unit that the directory role is scoped to
        Returns: Optional[str]
        """
        return self._administrative_unit_id
    
    @administrative_unit_id.setter
    def administrative_unit_id(self,value: Optional[str] = None) -> None:
        """
        Sets the administrativeUnitId property value. Unique identifier for the administrative unit that the directory role is scoped to
        Args:
            value: Value to set for the administrativeUnitId property.
        """
        self._administrative_unit_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new scopedRoleMembership and sets the default values.
        """
        super().__init__()
        # Unique identifier for the administrative unit that the directory role is scoped to
        self._administrative_unit_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Unique identifier for the directory role that the member is in.
        self._role_id: Optional[str] = None
        # The roleMemberInfo property
        self._role_member_info: Optional[identity.Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScopedRoleMembership:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScopedRoleMembership
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ScopedRoleMembership()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "administrative_unit_id": lambda n : setattr(self, 'administrative_unit_id', n.get_str_value()),
            "role_id": lambda n : setattr(self, 'role_id', n.get_str_value()),
            "role_member_info": lambda n : setattr(self, 'role_member_info', n.get_object_value(identity.Identity)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def role_id(self,) -> Optional[str]:
        """
        Gets the roleId property value. Unique identifier for the directory role that the member is in.
        Returns: Optional[str]
        """
        return self._role_id
    
    @role_id.setter
    def role_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleId property value. Unique identifier for the directory role that the member is in.
        Args:
            value: Value to set for the roleId property.
        """
        self._role_id = value
    
    @property
    def role_member_info(self,) -> Optional[identity.Identity]:
        """
        Gets the roleMemberInfo property value. The roleMemberInfo property
        Returns: Optional[identity.Identity]
        """
        return self._role_member_info
    
    @role_member_info.setter
    def role_member_info(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the roleMemberInfo property value. The roleMemberInfo property
        Args:
            value: Value to set for the roleMemberInfo property.
        """
        self._role_member_info = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("administrativeUnitId", self.administrative_unit_id)
        writer.write_str_value("roleId", self.role_id)
        writer.write_object_value("roleMemberInfo", self.role_member_info)
    

