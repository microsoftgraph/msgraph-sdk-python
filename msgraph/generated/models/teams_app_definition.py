from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .teams_app_authorization import TeamsAppAuthorization
    from .teams_app_publishing_state import TeamsAppPublishingState
    from .teamwork_bot import TeamworkBot

from .entity import Entity

@dataclass
class TeamsAppDefinition(Entity, Parsable):
    # Authorization requirements specified in the Teams app manifest.
    authorization: Optional[TeamsAppAuthorization] = None
    # The details of the bot specified in the Teams app manifest.
    bot: Optional[TeamworkBot] = None
    # The createdBy property
    created_by: Optional[IdentitySet] = None
    # Verbose description of the application.
    description: Optional[str] = None
    # The name of the app provided by the app developer.
    display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The published status of a specific version of a Teams app. The possible values are:submitted—The specific version of the Teams app was submitted and is under review.published—The request to publish the specific version of the Teams app was approved by the admin and the app is published.rejected—The admin rejected the request to publish the specific version of the Teams app.
    publishing_state: Optional[TeamsAppPublishingState] = None
    # Short description of the application.
    short_description: Optional[str] = None
    # The ID from the Teams app manifest.
    teams_app_id: Optional[str] = None
    # The version number of the application.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .teams_app_authorization import TeamsAppAuthorization
        from .teams_app_publishing_state import TeamsAppPublishingState
        from .teamwork_bot import TeamworkBot

        from .entity import Entity
        from .identity_set import IdentitySet
        from .teams_app_authorization import TeamsAppAuthorization
        from .teams_app_publishing_state import TeamsAppPublishingState
        from .teamwork_bot import TeamworkBot

        fields: dict[str, Callable[[Any], None]] = {
            "authorization": lambda n : setattr(self, 'authorization', n.get_object_value(TeamsAppAuthorization)),
            "bot": lambda n : setattr(self, 'bot', n.get_object_value(TeamworkBot)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publishingState": lambda n : setattr(self, 'publishing_state', n.get_enum_value(TeamsAppPublishingState)),
            "shortDescription": lambda n : setattr(self, 'short_description', n.get_str_value()),
            "teamsAppId": lambda n : setattr(self, 'teams_app_id', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("authorization", self.authorization)
        writer.write_object_value("bot", self.bot)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("publishingState", self.publishing_state)
        writer.write_str_value("shortDescription", self.short_description)
        writer.write_str_value("teamsAppId", self.teams_app_id)
        writer.write_str_value("version", self.version)
    

