from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conversation_member = lazy_import('msgraph.generated.models.conversation_member')
team_info = lazy_import('msgraph.generated.models.team_info')

class SharedWithChannelTeamInfo(team_info.TeamInfo):
    @property
    def allowed_members(self,) -> Optional[List[conversation_member.ConversationMember]]:
        """
        Gets the allowedMembers property value. A collection of team members who have access to the shared channel.
        Returns: Optional[List[conversation_member.ConversationMember]]
        """
        return self._allowed_members
    
    @allowed_members.setter
    def allowed_members(self,value: Optional[List[conversation_member.ConversationMember]] = None) -> None:
        """
        Sets the allowedMembers property value. A collection of team members who have access to the shared channel.
        Args:
            value: Value to set for the allowedMembers property.
        """
        self._allowed_members = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new SharedWithChannelTeamInfo and sets the default values.
        """
        super().__init__()
        # A collection of team members who have access to the shared channel.
        self._allowed_members: Optional[List[conversation_member.ConversationMember]] = None
        # Indicates whether the team is the host of the channel.
        self._is_host_team: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedWithChannelTeamInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedWithChannelTeamInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedWithChannelTeamInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_members": lambda n : setattr(self, 'allowed_members', n.get_collection_of_object_values(conversation_member.ConversationMember)),
            "is_host_team": lambda n : setattr(self, 'is_host_team', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_host_team(self,) -> Optional[bool]:
        """
        Gets the isHostTeam property value. Indicates whether the team is the host of the channel.
        Returns: Optional[bool]
        """
        return self._is_host_team
    
    @is_host_team.setter
    def is_host_team(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHostTeam property value. Indicates whether the team is the host of the channel.
        Args:
            value: Value to set for the isHostTeam property.
        """
        self._is_host_team = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("allowedMembers", self.allowed_members)
        writer.write_bool_value("isHostTeam", self.is_host_team)
    

