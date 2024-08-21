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
    # Represents the location that a user selected in Microsoft Teams and doesn't follow the Office's locale setting. A user’s locale is represented by their preferred language and country or region. For example, en-us. The language component follows two-letter codes as defined in ISO 639-1, and the country component follows two-letter codes as defined in ISO 3166-1 alpha-2.
    locale: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the region of the organization or the user. For users with multigeo licenses, the property contains the user's region (if available). For users without multigeo licenses, the property contains the organization's region.The region value can be any region supported by the Teams payload. The possible values are: Americas, Europe and MiddleEast, Asia Pacific, UAE, Australia, Brazil, Canada, Switzerland, Germany, France, India, Japan, South Korea, Norway, Singapore, United Kingdom, South Africa, Sweden, Qatar, Poland, Italy, Israel, Spain, Mexico, USGov Community Cloud, USGov Community Cloud High, USGov Department of Defense, and China.
    region: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserTeamwork:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserTeamwork
        """
        if parse_node is None:
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
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
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
        writer.write_collection_of_object_values("associatedTeams", self.associated_teams)
        writer.write_collection_of_object_values("installedApps", self.installed_apps)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("region", self.region)
    

