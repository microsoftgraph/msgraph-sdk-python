from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .group import Group
    from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
    from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
    from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest

from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest

@dataclass
class PrivilegedAccessGroupEligibilityScheduleRequest(PrivilegedAccessScheduleRequest):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest"
    # The identifier of membership or ownership eligibility relationship to the group. Required. The possible values are: owner, member, unknownFutureValue.
    access_id: Optional[PrivilegedAccessGroupRelationships] = None
    # References the group that is the scope of the membership or ownership eligibility request through PIM for groups. Supports $expand and $select nested in $expand for select properties like id, displayName, and mail.
    group: Optional[Group] = None
    # The identifier of the group representing the scope of the membership and ownership eligibility through PIM for groups. Required.
    group_id: Optional[str] = None
    # References the principal that's in the scope of the membership or ownership eligibility request through the group that's governed by PIM. Supports $expand and $select nested in $expand for id only.
    principal: Optional[DirectoryObject] = None
    # The identifier of the principal whose membership or ownership eligibility to the group is managed through PIM for groups. Required.
    principal_id: Optional[str] = None
    # Schedule created by this request.
    target_schedule: Optional[PrivilegedAccessGroupEligibilitySchedule] = None
    # The identifier of the schedule that's created from the eligibility request. Optional.
    target_schedule_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedAccessGroupEligibilityScheduleRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroupEligibilityScheduleRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedAccessGroupEligibilityScheduleRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .group import Group
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
        from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest

        from .directory_object import DirectoryObject
        from .group import Group
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .privileged_access_group_relationships import PrivilegedAccessGroupRelationships
        from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest

        fields: Dict[str, Callable[[Any], None]] = {
            "accessId": lambda n : setattr(self, 'access_id', n.get_enum_value(PrivilegedAccessGroupRelationships)),
            "group": lambda n : setattr(self, 'group', n.get_object_value(Group)),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(DirectoryObject)),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "targetSchedule": lambda n : setattr(self, 'target_schedule', n.get_object_value(PrivilegedAccessGroupEligibilitySchedule)),
            "targetScheduleId": lambda n : setattr(self, 'target_schedule_id', n.get_str_value()),
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
        writer.write_object_value("group", self.group)
        writer.write_str_value("groupId", self.group_id)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_object_value("targetSchedule", self.target_schedule)
        writer.write_str_value("targetScheduleId", self.target_schedule_id)
    

