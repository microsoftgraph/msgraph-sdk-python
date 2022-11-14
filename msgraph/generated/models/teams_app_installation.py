from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import entity, teams_app, teams_app_definition

class TeamsAppInstallation(entity.Entity):
    """
    Provides operations to manage the collection of agreementAcceptance entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new teamsAppInstallation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.teamsAppInstallation"
        # The app that is installed.
        self._teams_app: Optional[teams_app.TeamsApp] = None
        # The details of this version of the app.
        self._teams_app_definition: Optional[teams_app_definition.TeamsAppDefinition] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppInstallation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppInstallation
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return TeamsAppInstallation()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "teams_app": lambda n : setattr(self, 'teams_app', n.get_object_value(teams_app.TeamsApp)),
            "teams_app_definition": lambda n : setattr(self, 'teams_app_definition', n.get_object_value(teams_app_definition.TeamsAppDefinition)),
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
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("teamsApp", self.teams_app)
        writer.write_object_value("teamsAppDefinition", self.teams_app_definition)

    @property
    def teams_app(self,) -> Optional[teams_app.TeamsApp]:
        """
        Gets the teamsApp property value. The app that is installed.
        Returns: Optional[teams_app.TeamsApp]
        """
        return self._teams_app

    @teams_app.setter
    def teams_app(self,value: Optional[teams_app.TeamsApp] = None) -> None:
        """
        Sets the teamsApp property value. The app that is installed.
        Args:
            value: Value to set for the teamsApp property.
        """
        self._teams_app = value

    @property
    def teams_app_definition(self,) -> Optional[teams_app_definition.TeamsAppDefinition]:
        """
        Gets the teamsAppDefinition property value. The details of this version of the app.
        Returns: Optional[teams_app_definition.TeamsAppDefinition]
        """
        return self._teams_app_definition

    @teams_app_definition.setter
    def teams_app_definition(self,value: Optional[teams_app_definition.TeamsAppDefinition] = None) -> None:
        """
        Sets the teamsAppDefinition property value. The details of this version of the app.
        Args:
            value: Value to set for the teamsAppDefinition property.
        """
        self._teams_app_definition = value


