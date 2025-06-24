from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .group import Group
    from .privileged_access_group_assignment_type import PrivilegedAccessGroupAssignmentType
    from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
    from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
    from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
    from .privileged_access_schedule import PrivilegedAccessSchedule

from .privileged_access_schedule import PrivilegedAccessSchedule

@dataclass
class PrivilegedAccessGroupAssignmentSchedule(PrivilegedAccessSchedule, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.privilegedAccessGroupAssignmentSchedule"
    # The identifier of the membership or ownership assignment to the group that is governed through PIM. Required. The possible values are: owner, member, unknownFutureValue. Supports $filter (eq).
    access_id: Optional[PrivilegedAccessGroupRelationships] = None
    # When the request activates an ownership or membership assignment in PIM for Groups, this object represents the eligibility relationship. Otherwise, it's null. Supports $expand.
    activated_using: Optional[PrivilegedAccessGroupEligibilitySchedule] = None
    # Indicates whether the membership or ownership assignment for the principal is granted through activation or direct assignment. Required. The possible values are: assigned, activated, unknownFutureValue. Supports $filter (eq).
    assignment_type: Optional[PrivilegedAccessGroupAssignmentType] = None
    # References the group that is the scope of the membership or ownership assignment through PIM for Groups. Supports $expand and $select nested in $expand for select properties like id, displayName, and mail.
    group: Optional[Group] = None
    # The identifier of the group representing the scope of the membership or ownership assignment through PIM for Groups. Required. Supports $filter (eq).
    group_id: Optional[str] = None
    # Indicates whether the assignment is derived from a direct group assignment or through a transitive assignment. The possible values are: direct, group, unknownFutureValue. Supports $filter (eq).
    member_type: Optional[PrivilegedAccessGroupMemberType] = None
    # References the principal that's in the scope of this membership or ownership assignment request to the group that's governed through PIM. Supports $expand and $select nested in $expand for id only.
    principal: Optional[DirectoryObject] = None
    # The identifier of the principal whose membership or ownership assignment is granted through PIM for Groups. Required. Supports $filter (eq).
    principal_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedAccessGroupAssignmentSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroupAssignmentSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedAccessGroupAssignmentSchedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .group import Group
        from .privileged_access_group_assignment_type import PrivilegedAccessGroupAssignmentType
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
        from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
        from .privileged_access_schedule import PrivilegedAccessSchedule

        from .directory_object import DirectoryObject
        from .group import Group
        from .privileged_access_group_assignment_type import PrivilegedAccessGroupAssignmentType
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
        from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
        from .privileged_access_schedule import PrivilegedAccessSchedule

        fields: dict[str, Callable[[Any], None]] = {
            "accessId": lambda n : setattr(self, 'access_id', n.get_enum_value(PrivilegedAccessGroupRelationships)),
            "activatedUsing": lambda n : setattr(self, 'activated_using', n.get_object_value(PrivilegedAccessGroupEligibilitySchedule)),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_enum_value(PrivilegedAccessGroupAssignmentType)),
            "group": lambda n : setattr(self, 'group', n.get_object_value(Group)),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_enum_value(PrivilegedAccessGroupMemberType)),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(DirectoryObject)),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
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
        writer.write_enum_value("accessId", self.access_id)
        writer.write_object_value("activatedUsing", self.activated_using)
        writer.write_enum_value("assignmentType", self.assignment_type)
        writer.write_object_value("group", self.group)
        writer.write_str_value("groupId", self.group_id)
        writer.write_enum_value("memberType", self.member_type)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
    

