from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .deleted_chat import DeletedChat
    from .deleted_team import DeletedTeam
    from .entity import Entity
    from .teams_app_settings import TeamsAppSettings
    from .workforce_integration import WorkforceIntegration

from .entity import Entity

@dataclass
class Teamwork(Entity, Parsable):
    # A collection of deleted chats.
    deleted_chats: Optional[list[DeletedChat]] = None
    # The deleted team.
    deleted_teams: Optional[list[DeletedTeam]] = None
    # Indicates whether Microsoft Teams is enabled for the organization.
    is_teams_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the region of the organization or the tenant. The region value can be any region supported by the Teams payload. The possible values are: Americas, Europe and MiddleEast, Asia Pacific, UAE, Australia, Brazil, Canada, Switzerland, Germany, France, India, Japan, South Korea, Norway, Singapore, United Kingdom, South Africa, Sweden, Qatar, Poland, Italy, Israel, Spain, Mexico, USGov Community Cloud, USGov Community Cloud High, USGov Department of Defense, and China.
    region: Optional[str] = None
    # Represents tenant-wide settings for all Teams apps in the tenant.
    teams_app_settings: Optional[TeamsAppSettings] = None
    # The workforceIntegrations property
    workforce_integrations: Optional[list[WorkforceIntegration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Teamwork:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Teamwork
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Teamwork()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .deleted_chat import DeletedChat
        from .deleted_team import DeletedTeam
        from .entity import Entity
        from .teams_app_settings import TeamsAppSettings
        from .workforce_integration import WorkforceIntegration

        from .deleted_chat import DeletedChat
        from .deleted_team import DeletedTeam
        from .entity import Entity
        from .teams_app_settings import TeamsAppSettings
        from .workforce_integration import WorkforceIntegration

        fields: dict[str, Callable[[Any], None]] = {
            "deletedChats": lambda n : setattr(self, 'deleted_chats', n.get_collection_of_object_values(DeletedChat)),
            "deletedTeams": lambda n : setattr(self, 'deleted_teams', n.get_collection_of_object_values(DeletedTeam)),
            "isTeamsEnabled": lambda n : setattr(self, 'is_teams_enabled', n.get_bool_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "teamsAppSettings": lambda n : setattr(self, 'teams_app_settings', n.get_object_value(TeamsAppSettings)),
            "workforceIntegrations": lambda n : setattr(self, 'workforce_integrations', n.get_collection_of_object_values(WorkforceIntegration)),
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
        writer.write_collection_of_object_values("deletedChats", self.deleted_chats)
        writer.write_collection_of_object_values("deletedTeams", self.deleted_teams)
        writer.write_bool_value("isTeamsEnabled", self.is_teams_enabled)
        writer.write_str_value("region", self.region)
        writer.write_object_value("teamsAppSettings", self.teams_app_settings)
        writer.write_collection_of_object_values("workforceIntegrations", self.workforce_integrations)
    

