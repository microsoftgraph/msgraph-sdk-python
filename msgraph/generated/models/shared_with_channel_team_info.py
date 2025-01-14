from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conversation_member import ConversationMember
    from .team_info import TeamInfo

from .team_info import TeamInfo

@dataclass
class SharedWithChannelTeamInfo(TeamInfo, Parsable):
    # A collection of team members who have access to the shared channel.
    allowed_members: Optional[list[ConversationMember]] = None
    # Indicates whether the team is the host of the channel.
    is_host_team: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharedWithChannelTeamInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharedWithChannelTeamInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharedWithChannelTeamInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conversation_member import ConversationMember
        from .team_info import TeamInfo

        from .conversation_member import ConversationMember
        from .team_info import TeamInfo

        fields: dict[str, Callable[[Any], None]] = {
            "allowedMembers": lambda n : setattr(self, 'allowed_members', n.get_collection_of_object_values(ConversationMember)),
            "isHostTeam": lambda n : setattr(self, 'is_host_team', n.get_bool_value()),
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
        writer.write_collection_of_object_values("allowedMembers", self.allowed_members)
        writer.write_bool_value("isHostTeam", self.is_host_team)
    

