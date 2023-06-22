from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import associated_team_info, entity, shared_with_channel_team_info, team

from . import entity

@dataclass
class TeamInfo(entity.Entity):
    # The name of the team.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The team property
    team: Optional[team.Team] = None
    # The ID of the Azure Active Directory tenant.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamInfo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.associatedTeamInfo".casefold():
            from . import associated_team_info

            return associated_team_info.AssociatedTeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedWithChannelTeamInfo".casefold():
            from . import shared_with_channel_team_info

            return shared_with_channel_team_info.SharedWithChannelTeamInfo()
        return TeamInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import associated_team_info, entity, shared_with_channel_team_info, team

        from . import associated_team_info, entity, shared_with_channel_team_info, team

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "team": lambda n : setattr(self, 'team', n.get_object_value(team.Team)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("team", self.team)
        writer.write_str_value("tenantId", self.tenant_id)
    

