from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .teams_app import TeamsApp
    from .teams_app_definition import TeamsAppDefinition
    from .teams_app_permission_set import TeamsAppPermissionSet
    from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

from .entity import Entity

@dataclass
class TeamsAppInstallation(Entity, Parsable):
    # The set of resource-specific permissions consented to while installing or upgrading the teamsApp.
    consented_permission_set: Optional[TeamsAppPermissionSet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The app that is installed.
    teams_app: Optional[TeamsApp] = None
    # The details of this version of the app.
    teams_app_definition: Optional[TeamsAppDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppInstallation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppInstallation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userScopeTeamsAppInstallation".casefold():
            from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

            return UserScopeTeamsAppInstallation()
        return TeamsAppInstallation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .teams_app import TeamsApp
        from .teams_app_definition import TeamsAppDefinition
        from .teams_app_permission_set import TeamsAppPermissionSet
        from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

        from .entity import Entity
        from .teams_app import TeamsApp
        from .teams_app_definition import TeamsAppDefinition
        from .teams_app_permission_set import TeamsAppPermissionSet
        from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

        fields: dict[str, Callable[[Any], None]] = {
            "consentedPermissionSet": lambda n : setattr(self, 'consented_permission_set', n.get_object_value(TeamsAppPermissionSet)),
            "teamsApp": lambda n : setattr(self, 'teams_app', n.get_object_value(TeamsApp)),
            "teamsAppDefinition": lambda n : setattr(self, 'teams_app_definition', n.get_object_value(TeamsAppDefinition)),
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
        writer.write_object_value("consentedPermissionSet", self.consented_permission_set)
        writer.write_object_value("teamsApp", self.teams_app)
        writer.write_object_value("teamsAppDefinition", self.teams_app_definition)
    

