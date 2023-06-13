from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, teams_app, teams_app_definition, user_scope_teams_app_installation

from . import entity

@dataclass
class TeamsAppInstallation(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The app that is installed.
    teams_app: Optional[teams_app.TeamsApp] = None
    # The details of this version of the app.
    teams_app_definition: Optional[teams_app_definition.TeamsAppDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppInstallation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppInstallation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.userScopeTeamsAppInstallation":
                from . import user_scope_teams_app_installation

                return user_scope_teams_app_installation.UserScopeTeamsAppInstallation()
        return TeamsAppInstallation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, teams_app, teams_app_definition, user_scope_teams_app_installation

        fields: Dict[str, Callable[[Any], None]] = {
            "teamsApp": lambda n : setattr(self, 'teams_app', n.get_object_value(teams_app.TeamsApp)),
            "teamsAppDefinition": lambda n : setattr(self, 'teams_app_definition', n.get_object_value(teams_app_definition.TeamsAppDefinition)),
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
        writer.write_object_value("teamsApp", self.teams_app)
        writer.write_object_value("teamsAppDefinition", self.teams_app_definition)
    

