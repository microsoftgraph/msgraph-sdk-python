from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')
scoped_role_membership = lazy_import('msgraph.generated.models.scoped_role_membership')

class DirectoryRole(directory_object.DirectoryObject):
    def __init__(self,) -> None:
        """
        Instantiates a new DirectoryRole and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.directoryRole"
        # The description for the directory role. Read-only. Supports $filter (eq), $search, $select.
        self._description: Optional[str] = None
        # The display name for the directory role. Read-only. Supports $filter (eq), $search, $select.
        self._display_name: Optional[str] = None
        # Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable. Supports $expand.
        self._members: Optional[List[directory_object.DirectoryObject]] = None
        # The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only. Supports $filter (eq), $select.
        self._role_template_id: Optional[str] = None
        # Members of this directory role that are scoped to administrative units. Read-only. Nullable.
        self._scoped_members: Optional[List[scoped_role_membership.ScopedRoleMembership]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryRole
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DirectoryRole()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description for the directory role. Read-only. Supports $filter (eq), $search, $select.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description for the directory role. Read-only. Supports $filter (eq), $search, $select.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the directory role. Read-only. Supports $filter (eq), $search, $select.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the directory role. Read-only. Supports $filter (eq), $search, $select.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "role_template_id": lambda n : setattr(self, 'role_template_id', n.get_str_value()),
            "scoped_members": lambda n : setattr(self, 'scoped_members', n.get_collection_of_object_values(scoped_role_membership.ScopedRoleMembership)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def members(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the members property value. Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the members property value. Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    @property
    def role_template_id(self,) -> Optional[str]:
        """
        Gets the roleTemplateId property value. The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only. Supports $filter (eq), $select.
        Returns: Optional[str]
        """
        return self._role_template_id
    
    @role_template_id.setter
    def role_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleTemplateId property value. The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only. Supports $filter (eq), $select.
        Args:
            value: Value to set for the roleTemplateId property.
        """
        self._role_template_id = value
    
    @property
    def scoped_members(self,) -> Optional[List[scoped_role_membership.ScopedRoleMembership]]:
        """
        Gets the scopedMembers property value. Members of this directory role that are scoped to administrative units. Read-only. Nullable.
        Returns: Optional[List[scoped_role_membership.ScopedRoleMembership]]
        """
        return self._scoped_members
    
    @scoped_members.setter
    def scoped_members(self,value: Optional[List[scoped_role_membership.ScopedRoleMembership]] = None) -> None:
        """
        Sets the scopedMembers property value. Members of this directory role that are scoped to administrative units. Read-only. Nullable.
        Args:
            value: Value to set for the scopedMembers property.
        """
        self._scoped_members = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("roleTemplateId", self.role_template_id)
        writer.write_collection_of_object_values("scopedMembers", self.scoped_members)
    

