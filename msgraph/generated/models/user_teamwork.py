from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import associated_team_info, entity, user_scope_teams_app_installation

class UserTeamwork(entity.Entity):
    @property
    def associated_teams(self,) -> Optional[List[associated_team_info.AssociatedTeamInfo]]:
        """
        Gets the associatedTeams property value. The list of associatedTeamInfo objects that a user is associated with.
        Returns: Optional[List[associated_team_info.AssociatedTeamInfo]]
        """
        return self._associated_teams

    @associated_teams.setter
    def associated_teams(self,value: Optional[List[associated_team_info.AssociatedTeamInfo]] = None) -> None:
        """
        Sets the associatedTeams property value. The list of associatedTeamInfo objects that a user is associated with.
        Args:
            value: Value to set for the associatedTeams property.
        """
        self._associated_teams = value

    def __init__(self,) -> None:
        """
        Instantiates a new userTeamwork and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.userTeamwork"
        # The list of associatedTeamInfo objects that a user is associated with.
        self._associated_teams: Optional[List[associated_team_info.AssociatedTeamInfo]] = None
        # The apps installed in the personal scope of this user.
        self._installed_apps: Optional[List[user_scope_teams_app_installation.UserScopeTeamsAppInstallation]] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserTeamwork:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserTeamwork
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return UserTeamwork()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "associated_teams": lambda n : setattr(self, 'associated_teams', n.get_collection_of_object_values(associated_team_info.AssociatedTeamInfo)),
            "installed_apps": lambda n : setattr(self, 'installed_apps', n.get_collection_of_object_values(user_scope_teams_app_installation.UserScopeTeamsAppInstallation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    @property
    def installed_apps(self,) -> Optional[List[user_scope_teams_app_installation.UserScopeTeamsAppInstallation]]:
        """
        Gets the installedApps property value. The apps installed in the personal scope of this user.
        Returns: Optional[List[user_scope_teams_app_installation.UserScopeTeamsAppInstallation]]
        """
        return self._installed_apps

    @installed_apps.setter
    def installed_apps(self,value: Optional[List[user_scope_teams_app_installation.UserScopeTeamsAppInstallation]] = None) -> None:
        """
        Sets the installedApps property value. The apps installed in the personal scope of this user.
        Args:
            value: Value to set for the installedApps property.
        """
        self._installed_apps = value

    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("associatedTeams", self.associated_teams)
        writer.write_collection_of_object_values("installedApps", self.installed_apps)


