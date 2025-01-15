from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .teamwork_tag_member import TeamworkTagMember
    from .teamwork_tag_type import TeamworkTagType

from .entity import Entity

@dataclass
class TeamworkTag(Entity, Parsable):
    # The description of the tag as it appears to the user in Microsoft Teams. A teamworkTag can't have more than 200 teamworkTagMembers.
    description: Optional[str] = None
    # The name of the tag as it appears to the user in Microsoft Teams.
    display_name: Optional[str] = None
    # The number of users assigned to the tag.
    member_count: Optional[int] = None
    # Users assigned to the tag.
    members: Optional[list[TeamworkTagMember]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of the tag. Default is standard.
    tag_type: Optional[TeamworkTagType] = None
    # ID of the team in which the tag is defined.
    team_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkTag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkTag
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkTag()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .teamwork_tag_member import TeamworkTagMember
        from .teamwork_tag_type import TeamworkTagType

        from .entity import Entity
        from .teamwork_tag_member import TeamworkTagMember
        from .teamwork_tag_type import TeamworkTagType

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "memberCount": lambda n : setattr(self, 'member_count', n.get_int_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(TeamworkTagMember)),
            "tagType": lambda n : setattr(self, 'tag_type', n.get_enum_value(TeamworkTagType)),
            "teamId": lambda n : setattr(self, 'team_id', n.get_str_value()),
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
        writer.write_int_value("memberCount", self.member_count)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_enum_value("tagType", self.tag_type)
        writer.write_str_value("teamId", self.team_id)
    

