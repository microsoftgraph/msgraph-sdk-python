from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import associated_team_info, entity, shared_with_channel_team_info, team

from . import entity

class TeamInfo(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new teamInfo and sets the default values.
        """
        super().__init__()
        # The name of the team.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The team property
        self._team: Optional[team.Team] = None
        # The ID of the Azure Active Directory tenant.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.associatedTeamInfo":
                from . import associated_team_info

                return associated_team_info.AssociatedTeamInfo()
            if mapping_value == "#microsoft.graph.sharedWithChannelTeamInfo":
                from . import shared_with_channel_team_info

                return shared_with_channel_team_info.SharedWithChannelTeamInfo()
        return TeamInfo()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the team.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the team.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("team", self.team)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def team(self,) -> Optional[team.Team]:
        """
        Gets the team property value. The team property
        Returns: Optional[team.Team]
        """
        return self._team
    
    @team.setter
    def team(self,value: Optional[team.Team] = None) -> None:
        """
        Sets the team property value. The team property
        Args:
            value: Value to set for the team property.
        """
        self._team = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The ID of the Azure Active Directory tenant.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The ID of the Azure Active Directory tenant.
        Args:
            value: Value to set for the tenant_id property.
        """
        self._tenant_id = value
    

