from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .scoped_role_membership import ScopedRoleMembership

from .directory_object import DirectoryObject

@dataclass
class DirectoryRole(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.directoryRole"
    # The description for the directory role. Read-only. Supports $filter (eq), $search, $select.
    description: Optional[str] = None
    # The display name for the directory role. Read-only. Supports $filter (eq), $search, $select.
    display_name: Optional[str] = None
    # Users that are members of this directory role. HTTP Methods: GET, POST, DELETE. Read-only. Nullable. Supports $expand.
    members: Optional[list[DirectoryObject]] = None
    # The id of the directoryRoleTemplate that this role is based on. The property must be specified when activating a directory role in a tenant with a POST operation. After the directory role has been activated, the property is read only. Supports $filter (eq), $select.
    role_template_id: Optional[str] = None
    # Members of this directory role that are scoped to administrative units. Read-only. Nullable.
    scoped_members: Optional[list[ScopedRoleMembership]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DirectoryRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryRole
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DirectoryRole()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .scoped_role_membership import ScopedRoleMembership

        from .directory_object import DirectoryObject
        from .scoped_role_membership import ScopedRoleMembership

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(DirectoryObject)),
            "roleTemplateId": lambda n : setattr(self, 'role_template_id', n.get_str_value()),
            "scopedMembers": lambda n : setattr(self, 'scoped_members', n.get_collection_of_object_values(ScopedRoleMembership)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("roleTemplateId", self.role_template_id)
        writer.write_collection_of_object_values("scopedMembers", self.scoped_members)
    

