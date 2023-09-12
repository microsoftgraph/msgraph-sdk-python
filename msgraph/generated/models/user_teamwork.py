from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .associated_team_info import AssociatedTeamInfo
    from .entity import Entity
    from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

from .entity import Entity

@dataclass
class UserTeamwork(Entity):
    # The list of associatedTeamInfo objects that a user is associated with.
    associated_teams: Optional[List[AssociatedTeamInfo]] = None
    # The apps installed in the personal scope of this user.
    installed_apps: Optional[List[UserScopeTeamsAppInstallation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserTeamwork:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserTeamwork
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserTeamwork()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .associated_team_info import AssociatedTeamInfo
        from .entity import Entity
        from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

        from .associated_team_info import AssociatedTeamInfo
        from .entity import Entity
        from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

        fields: Dict[str, Callable[[Any], None]] = {
            "associatedTeams": lambda n : setattr(self, 'associated_teams', n.get_collection_of_object_values(AssociatedTeamInfo)),
            "installedApps": lambda n : setattr(self, 'installed_apps', n.get_collection_of_object_values(UserScopeTeamsAppInstallation)),
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
        writer.write_collection_of_object_values("associatedTeams", self.associated_teams)
        writer.write_collection_of_object_values("installedApps", self.installed_apps)
    

