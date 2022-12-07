from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')
extension = lazy_import('msgraph.generated.models.extension')
scoped_role_membership = lazy_import('msgraph.generated.models.scoped_role_membership')

class AdministrativeUnit(directory_object.DirectoryObject):
    def __init__(self,) -> None:
        """
        Instantiates a new AdministrativeUnit and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.administrativeUnit"
        # An optional description for the administrative unit. Supports $filter (eq, ne, in, startsWith), $search.
        self._description: Optional[str] = None
        # Display name for the administrative unit. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        self._display_name: Optional[str] = None
        # The collection of open extensions defined for this administrative unit. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # Users and groups that are members of this administrative unit. Supports $expand.
        self._members: Optional[List[directory_object.DirectoryObject]] = None
        # Scoped-role members of this administrative unit.
        self._scoped_role_members: Optional[List[scoped_role_membership.ScopedRoleMembership]] = None
        # Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership. If not set (value is null), the default behavior is public. When set to HiddenMembership, only members of the administrative unit can list other members of the administrative unit.
        self._visibility: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdministrativeUnit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AdministrativeUnit
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AdministrativeUnit()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. An optional description for the administrative unit. Supports $filter (eq, ne, in, startsWith), $search.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. An optional description for the administrative unit. Supports $filter (eq, ne, in, startsWith), $search.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name for the administrative unit. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name for the administrative unit. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderBy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for this administrative unit. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for this administrative unit. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "scoped_role_members": lambda n : setattr(self, 'scoped_role_members', n.get_collection_of_object_values(scoped_role_membership.ScopedRoleMembership)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def members(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the members property value. Users and groups that are members of this administrative unit. Supports $expand.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the members property value. Users and groups that are members of this administrative unit. Supports $expand.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    @property
    def scoped_role_members(self,) -> Optional[List[scoped_role_membership.ScopedRoleMembership]]:
        """
        Gets the scopedRoleMembers property value. Scoped-role members of this administrative unit.
        Returns: Optional[List[scoped_role_membership.ScopedRoleMembership]]
        """
        return self._scoped_role_members
    
    @scoped_role_members.setter
    def scoped_role_members(self,value: Optional[List[scoped_role_membership.ScopedRoleMembership]] = None) -> None:
        """
        Sets the scopedRoleMembers property value. Scoped-role members of this administrative unit.
        Args:
            value: Value to set for the scopedRoleMembers property.
        """
        self._scoped_role_members = value
    
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
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_collection_of_object_values("scopedRoleMembers", self.scoped_role_members)
        writer.write_str_value("visibility", self.visibility)
    
    @property
    def visibility(self,) -> Optional[str]:
        """
        Gets the visibility property value. Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership. If not set (value is null), the default behavior is public. When set to HiddenMembership, only members of the administrative unit can list other members of the administrative unit.
        Returns: Optional[str]
        """
        return self._visibility
    
    @visibility.setter
    def visibility(self,value: Optional[str] = None) -> None:
        """
        Sets the visibility property value. Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership. If not set (value is null), the default behavior is public. When set to HiddenMembership, only members of the administrative unit can list other members of the administrative unit.
        Args:
            value: Value to set for the visibility property.
        """
        self._visibility = value
    

