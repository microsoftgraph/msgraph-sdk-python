from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
teamwork_tag_member = lazy_import('msgraph.generated.models.teamwork_tag_member')
teamwork_tag_type = lazy_import('msgraph.generated.models.teamwork_tag_type')

class TeamworkTag(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkTag and sets the default values.
        """
        super().__init__()
        # The description of the tag as it will appear to the user in Microsoft Teams.
        self._description: Optional[str] = None
        # The name of the tag as it will appear to the user in Microsoft Teams.
        self._display_name: Optional[str] = None
        # The number of users assigned to the tag.
        self._member_count: Optional[int] = None
        # Users assigned to the tag.
        self._members: Optional[List[teamwork_tag_member.TeamworkTagMember]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The type of the tag. Default is standard.
        self._tag_type: Optional[teamwork_tag_type.TeamworkTagType] = None
        # ID of the team in which the tag is defined.
        self._team_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkTag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkTag
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkTag()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the tag as it will appear to the user in Microsoft Teams.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the tag as it will appear to the user in Microsoft Teams.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the tag as it will appear to the user in Microsoft Teams.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the tag as it will appear to the user in Microsoft Teams.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "member_count": lambda n : setattr(self, 'member_count', n.get_int_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(teamwork_tag_member.TeamworkTagMember)),
            "tag_type": lambda n : setattr(self, 'tag_type', n.get_enum_value(teamwork_tag_type.TeamworkTagType)),
            "team_id": lambda n : setattr(self, 'team_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def member_count(self,) -> Optional[int]:
        """
        Gets the memberCount property value. The number of users assigned to the tag.
        Returns: Optional[int]
        """
        return self._member_count
    
    @member_count.setter
    def member_count(self,value: Optional[int] = None) -> None:
        """
        Sets the memberCount property value. The number of users assigned to the tag.
        Args:
            value: Value to set for the memberCount property.
        """
        self._member_count = value
    
    @property
    def members(self,) -> Optional[List[teamwork_tag_member.TeamworkTagMember]]:
        """
        Gets the members property value. Users assigned to the tag.
        Returns: Optional[List[teamwork_tag_member.TeamworkTagMember]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[teamwork_tag_member.TeamworkTagMember]] = None) -> None:
        """
        Sets the members property value. Users assigned to the tag.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("memberCount", self.member_count)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_enum_value("tagType", self.tag_type)
        writer.write_str_value("teamId", self.team_id)
    
    @property
    def tag_type(self,) -> Optional[teamwork_tag_type.TeamworkTagType]:
        """
        Gets the tagType property value. The type of the tag. Default is standard.
        Returns: Optional[teamwork_tag_type.TeamworkTagType]
        """
        return self._tag_type
    
    @tag_type.setter
    def tag_type(self,value: Optional[teamwork_tag_type.TeamworkTagType] = None) -> None:
        """
        Sets the tagType property value. The type of the tag. Default is standard.
        Args:
            value: Value to set for the tagType property.
        """
        self._tag_type = value
    
    @property
    def team_id(self,) -> Optional[str]:
        """
        Gets the teamId property value. ID of the team in which the tag is defined.
        Returns: Optional[str]
        """
        return self._team_id
    
    @team_id.setter
    def team_id(self,value: Optional[str] = None) -> None:
        """
        Sets the teamId property value. ID of the team in which the tag is defined.
        Args:
            value: Value to set for the teamId property.
        """
        self._team_id = value
    

