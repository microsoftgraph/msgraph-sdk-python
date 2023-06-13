from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import associated_team_info, entity, user_scope_teams_app_installation

from . import entity

@dataclass
class UserTeamwork(entity.Entity):
    # The list of associatedTeamInfo objects that a user is associated with.
    associated_teams: Optional[List[associated_team_info.AssociatedTeamInfo]] = None
    # The apps installed in the personal scope of this user.
    installed_apps: Optional[List[user_scope_teams_app_installation.UserScopeTeamsAppInstallation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserTeamwork:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserTeamwork
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserTeamwork()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import associated_team_info, entity, user_scope_teams_app_installation

        fields: Dict[str, Callable[[Any], None]] = {
            "associatedTeams": lambda n : setattr(self, 'associated_teams', n.get_collection_of_object_values(associated_team_info.AssociatedTeamInfo)),
            "installedApps": lambda n : setattr(self, 'installed_apps', n.get_collection_of_object_values(user_scope_teams_app_installation.UserScopeTeamsAppInstallation)),
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
        writer.write_collection_of_object_values("associatedTeams", self.associated_teams)
        writer.write_collection_of_object_values("installedApps", self.installed_apps)
    

