from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .associated_team_info import AssociatedTeamInfo
    from .entity import Entity
    from .shared_with_channel_team_info import SharedWithChannelTeamInfo
    from .team import Team

from .entity import Entity

@dataclass
class TeamInfo(Entity):
    # The name of the team.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The team property
    team: Optional[Team] = None
    # The ID of the Microsoft Entra tenant.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.associatedTeamInfo".casefold():
            from .associated_team_info import AssociatedTeamInfo

            return AssociatedTeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedWithChannelTeamInfo".casefold():
            from .shared_with_channel_team_info import SharedWithChannelTeamInfo

            return SharedWithChannelTeamInfo()
        return TeamInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .associated_team_info import AssociatedTeamInfo
        from .entity import Entity
        from .shared_with_channel_team_info import SharedWithChannelTeamInfo
        from .team import Team

        from .associated_team_info import AssociatedTeamInfo
        from .entity import Entity
        from .shared_with_channel_team_info import SharedWithChannelTeamInfo
        from .team import Team

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "team": lambda n : setattr(self, 'team', n.get_object_value(Team)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("team", self.team)
        writer.write_str_value("tenantId", self.tenant_id)
    

