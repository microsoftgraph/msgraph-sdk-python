from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .extension import Extension
    from .scoped_role_membership import ScopedRoleMembership

from .directory_object import DirectoryObject

@dataclass
class AdministrativeUnit(DirectoryObject):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.administrativeUnit"
    # An optional description for the administrative unit. Supports $filter (eq, ne, in, startsWith), $search.
    description: Optional[str] = None
    # Display name for the administrative unit. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    display_name: Optional[str] = None
    # The collection of open extensions defined for this administrative unit. Nullable.
    extensions: Optional[List[Extension]] = None
    # Users and groups that are members of this administrative unit. Supports $expand.
    members: Optional[List[DirectoryObject]] = None
    # Scoped-role members of this administrative unit.
    scoped_role_members: Optional[List[ScopedRoleMembership]] = None
    # Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership. If not set (value is null), the default behavior is public. When set to HiddenMembership, only members of the administrative unit can list other members of the administrative unit.
    visibility: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdministrativeUnit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdministrativeUnit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdministrativeUnit()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .extension import Extension
        from .scoped_role_membership import ScopedRoleMembership

        from .directory_object import DirectoryObject
        from .extension import Extension
        from .scoped_role_membership import ScopedRoleMembership

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(DirectoryObject)),
            "scopedRoleMembers": lambda n : setattr(self, 'scoped_role_members', n.get_collection_of_object_values(ScopedRoleMembership)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_str_value()),
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
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("scopedRoleMembers", self.scoped_role_members)
        writer.write_str_value("visibility", self.visibility)
    

