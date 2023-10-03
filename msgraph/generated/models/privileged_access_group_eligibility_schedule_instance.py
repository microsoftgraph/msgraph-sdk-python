from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .group import Group
    from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
    from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
    from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance

from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance

@dataclass
class PrivilegedAccessGroupEligibilityScheduleInstance(PrivilegedAccessScheduleInstance):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.privilegedAccessGroupEligibilityScheduleInstance"
    # The accessId property
    access_id: Optional[PrivilegedAccessGroupRelationships] = None
    # The eligibilityScheduleId property
    eligibility_schedule_id: Optional[str] = None
    # The group property
    group: Optional[Group] = None
    # The groupId property
    group_id: Optional[str] = None
    # The memberType property
    member_type: Optional[PrivilegedAccessGroupMemberType] = None
    # The principal property
    principal: Optional[DirectoryObject] = None
    # The principalId property
    principal_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessGroupEligibilityScheduleInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroupEligibilityScheduleInstance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedAccessGroupEligibilityScheduleInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .group import Group
        from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
        from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
        from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance

        from .directory_object import DirectoryObject
        from .group import Group
        from .privileged_access_group_member_type import PrivilegedAccessGroupMemberType
        from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
        from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance

        fields: Dict[str, Callable[[Any], None]] = {
            "accessId": lambda n : setattr(self, 'access_id', n.get_enum_value(PrivilegedAccessGroupRelationships)),
            "eligibilityScheduleId": lambda n : setattr(self, 'eligibility_schedule_id', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("accessId", self.access_id)
        writer.write_str_value("eligibilityScheduleId", self.eligibility_schedule_id)
        writer.write_object_value("group", self.group)
        writer.write_str_value("groupId", self.group_id)
        writer.write_enum_value("memberType", self.member_type)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
    

