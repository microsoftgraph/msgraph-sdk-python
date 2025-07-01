from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .extension import Extension
    from .scoped_role_membership import ScopedRoleMembership

from .directory_object import DirectoryObject

@dataclass
class AdministrativeUnit(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.administrativeUnit"
    # An optional description for the administrative unit. Supports $filter (eq, ne, in, startsWith), $search.
    description: Optional[str] = None
    # Display name for the administrative unit. Maximum length is 256 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    display_name: Optional[str] = None
    # The collection of open extensions defined for this administrative unit. Nullable.
    extensions: Optional[list[Extension]] = None
    # true if members of this administrative unit should be treated as sensitive, which requires specific permissions to manage. If not set, the default value is null and the default behavior is false. Use this property to define administrative units with roles that don't inherit from tenant-level administrators, and where the management of individual member objects is limited to administrators scoped to a restricted management administrative unit. This property is immutable and can't be changed later.  For more information on how to work with restricted management administrative units, see Restricted management administrative units in Microsoft Entra ID.
    is_member_management_restricted: Optional[bool] = None
    # Users and groups that are members of this administrative unit. Supports $expand.
    members: Optional[list[DirectoryObject]] = None
    # The dynamic membership rule for the administrative unit. For more information about the rules you can use for dynamic administrative units and dynamic groups, see Manage rules for dynamic membership groups in Microsoft Entra ID.
    membership_rule: Optional[str] = None
    # Controls whether the dynamic membership rule is actively processed. Set to On to activate the dynamic membership rule, or Paused to stop updating membership dynamically.
    membership_rule_processing_state: Optional[str] = None
    # Indicates the membership type for the administrative unit. The possible values are: dynamic, assigned. If not set, the default value is null and the default behavior is assigned.
    membership_type: Optional[str] = None
    # Scoped-role members of this administrative unit.
    scoped_role_members: Optional[list[ScopedRoleMembership]] = None
    # Controls whether the administrative unit and its members are hidden or public. Can be set to HiddenMembership. If not set, the default value is null and the default behavior is public. When set to HiddenMembership, only members of the administrative unit can list other members of the administrative unit.
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
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .extension import Extension
        from .scoped_role_membership import ScopedRoleMembership

        from .directory_object import DirectoryObject
        from .extension import Extension
        from .scoped_role_membership import ScopedRoleMembership

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "isMemberManagementRestricted": lambda n : setattr(self, 'is_member_management_restricted', n.get_bool_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(DirectoryObject)),
            "membershipRule": lambda n : setattr(self, 'membership_rule', n.get_str_value()),
            "membershipRuleProcessingState": lambda n : setattr(self, 'membership_rule_processing_state', n.get_str_value()),
            "membershipType": lambda n : setattr(self, 'membership_type', n.get_str_value()),
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
        writer.write_bool_value("isMemberManagementRestricted", self.is_member_management_restricted)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("membershipRule", self.membership_rule)
        writer.write_str_value("membershipRuleProcessingState", self.membership_rule_processing_state)
        writer.write_str_value("membershipType", self.membership_type)
        writer.write_collection_of_object_values("scopedRoleMembers", self.scoped_role_members)
        writer.write_str_value("visibility", self.visibility)
    

