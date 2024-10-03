from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .community_privacy import CommunityPrivacy
    from .entity import Entity
    from .group import Group
    from .user import User

from .entity import Entity

@dataclass
class Community(Entity):
    """
    Represents a community in Viva Engage that is a central place for conversations,files, events, and updates for people sharing a common interest or goal.
    """
    # The description of the community. The maximum length is 1,024 characters.
    description: Optional[str] = None
    # The name of the community. The maximum length is 255 characters.
    display_name: Optional[str] = None
    # The Microsoft 365 group that manages the membership of this community.
    group: Optional[Group] = None
    # The ID of the Microsoft 365 group that manages the membership of this community.
    group_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The admins of the community. Limited to 100 users. If this property isn't specified when you create the community, the calling user is automatically assigned as the community owner.
    owners: Optional[List[User]] = None
    # Types of communityPrivacy.
    privacy: Optional[CommunityPrivacy] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Community:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Community
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Community()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .community_privacy import CommunityPrivacy
        from .entity import Entity
        from .group import Group
        from .user import User

        from .community_privacy import CommunityPrivacy
        from .entity import Entity
        from .group import Group
        from .user import User

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "group": lambda n : setattr(self, 'group', n.get_object_value(Group)),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_object_values(User)),
            "privacy": lambda n : setattr(self, 'privacy', n.get_enum_value(CommunityPrivacy)),
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
        writer.write_object_value("group", self.group)
        writer.write_str_value("groupId", self.group_id)
        writer.write_collection_of_object_values("owners", self.owners)
        writer.write_enum_value("privacy", self.privacy)
    

