from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
teams_app_publishing_state = lazy_import('msgraph.generated.models.teams_app_publishing_state')
teamwork_bot = lazy_import('msgraph.generated.models.teamwork_bot')

class TeamsAppDefinition(entity.Entity):
    """
    Provides operations to manage the appCatalogs singleton.
    """
    @property
    def bot(self,) -> Optional[teamwork_bot.TeamworkBot]:
        """
        Gets the bot property value. The details of the bot specified in the Teams app manifest.
        Returns: Optional[teamwork_bot.TeamworkBot]
        """
        return self._bot
    
    @bot.setter
    def bot(self,value: Optional[teamwork_bot.TeamworkBot] = None) -> None:
        """
        Sets the bot property value. The details of the bot specified in the Teams app manifest.
        Args:
            value: Value to set for the bot property.
        """
        self._bot = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamsAppDefinition and sets the default values.
        """
        super().__init__()
        # The details of the bot specified in the Teams app manifest.
        self._bot: Optional[teamwork_bot.TeamworkBot] = None
        # The createdBy property
        self._created_by: Optional[identity_set.IdentitySet] = None
        # Verbose description of the application.
        self._description: Optional[str] = None
        # The name of the app provided by the app developer.
        self._display_name: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The published status of a specific version of a Teams app. Possible values are:submitted — The specific version of the Teams app has been submitted and is under review. published  — The request to publish the specific version of the Teams app has been approved by the admin and the app is published.  rejected — The request to publish the specific version of the Teams app was rejected by the admin.
        self._publishing_state: Optional[teams_app_publishing_state.TeamsAppPublishingState] = None
        # Short description of the application.
        self._short_description: Optional[str] = None
        # The ID from the Teams app manifest.
        self._teams_app_id: Optional[str] = None
        # The version number of the application.
        self._version: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAppDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsAppDefinition()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Verbose description of the application.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Verbose description of the application.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the app provided by the app developer.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the app provided by the app developer.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bot": lambda n : setattr(self, 'bot', n.get_object_value(teamwork_bot.TeamworkBot)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "publishing_state": lambda n : setattr(self, 'publishing_state', n.get_enum_value(teams_app_publishing_state.TeamsAppPublishingState)),
            "short_description": lambda n : setattr(self, 'short_description', n.get_str_value()),
            "teams_app_id": lambda n : setattr(self, 'teams_app_id', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def publishing_state(self,) -> Optional[teams_app_publishing_state.TeamsAppPublishingState]:
        """
        Gets the publishingState property value. The published status of a specific version of a Teams app. Possible values are:submitted — The specific version of the Teams app has been submitted and is under review. published  — The request to publish the specific version of the Teams app has been approved by the admin and the app is published.  rejected — The request to publish the specific version of the Teams app was rejected by the admin.
        Returns: Optional[teams_app_publishing_state.TeamsAppPublishingState]
        """
        return self._publishing_state
    
    @publishing_state.setter
    def publishing_state(self,value: Optional[teams_app_publishing_state.TeamsAppPublishingState] = None) -> None:
        """
        Sets the publishingState property value. The published status of a specific version of a Teams app. Possible values are:submitted — The specific version of the Teams app has been submitted and is under review. published  — The request to publish the specific version of the Teams app has been approved by the admin and the app is published.  rejected — The request to publish the specific version of the Teams app was rejected by the admin.
        Args:
            value: Value to set for the publishingState property.
        """
        self._publishing_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("bot", self.bot)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("publishingState", self.publishing_state)
        writer.write_str_value("shortDescription", self.short_description)
        writer.write_str_value("teamsAppId", self.teams_app_id)
        writer.write_str_value("version", self.version)
    
    @property
    def short_description(self,) -> Optional[str]:
        """
        Gets the shortDescription property value. Short description of the application.
        Returns: Optional[str]
        """
        return self._short_description
    
    @short_description.setter
    def short_description(self,value: Optional[str] = None) -> None:
        """
        Sets the shortDescription property value. Short description of the application.
        Args:
            value: Value to set for the shortDescription property.
        """
        self._short_description = value
    
    @property
    def teams_app_id(self,) -> Optional[str]:
        """
        Gets the teamsAppId property value. The ID from the Teams app manifest.
        Returns: Optional[str]
        """
        return self._teams_app_id
    
    @teams_app_id.setter
    def teams_app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the teamsAppId property value. The ID from the Teams app manifest.
        Args:
            value: Value to set for the teamsAppId property.
        """
        self._teams_app_id = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The version number of the application.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The version number of the application.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

