from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

channel_membership_type = lazy_import('msgraph.generated.models.channel_membership_type')
chat_message = lazy_import('msgraph.generated.models.chat_message')
conversation_member = lazy_import('msgraph.generated.models.conversation_member')
drive_item = lazy_import('msgraph.generated.models.drive_item')
entity = lazy_import('msgraph.generated.models.entity')
shared_with_channel_team_info = lazy_import('msgraph.generated.models.shared_with_channel_team_info')
teams_tab = lazy_import('msgraph.generated.models.teams_tab')

class Channel(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new channel and sets the default values.
        """
        super().__init__()
        # Read only. Timestamp at which the channel was created.
        self._created_date_time: Optional[datetime] = None
        # Optional textual description for the channel.
        self._description: Optional[str] = None
        # Channel name as it will appear to the user in Microsoft Teams. The maximum length is 50 characters.
        self._display_name: Optional[str] = None
        # The email address for sending messages to the channel. Read-only.
        self._email: Optional[str] = None
        # Metadata for the location where the channel's files are stored.
        self._files_folder: Optional[drive_item.DriveItem] = None
        # Indicates whether the channel should automatically be marked 'favorite' for all members of the team. Can only be set programmatically with Create team. Default: false.
        self._is_favorite_by_default: Optional[bool] = None
        # A collection of membership records associated with the channel.
        self._members: Optional[List[conversation_member.ConversationMember]] = None
        # The type of the channel. Can be set during creation and can't be changed. The possible values are: standard, private, unknownFutureValue, shared. The default value is standard. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value in this evolvable enum: shared.
        self._membership_type: Optional[channel_membership_type.ChannelMembershipType] = None
        # A collection of all the messages in the channel. A navigation property. Nullable.
        self._messages: Optional[List[chat_message.ChatMessage]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of teams with which a channel is shared.
        self._shared_with_teams: Optional[List[shared_with_channel_team_info.SharedWithChannelTeamInfo]] = None
        # A collection of all the tabs in the channel. A navigation property.
        self._tabs: Optional[List[teams_tab.TeamsTab]] = None
        # The ID of the Azure Active Directory tenant.
        self._tenant_id: Optional[str] = None
        # A hyperlink that will go to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.
        self._web_url: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Read only. Timestamp at which the channel was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Read only. Timestamp at which the channel was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Channel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Channel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Channel()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Optional textual description for the channel.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Optional textual description for the channel.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Channel name as it will appear to the user in Microsoft Teams. The maximum length is 50 characters.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Channel name as it will appear to the user in Microsoft Teams. The maximum length is 50 characters.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email address for sending messages to the channel. Read-only.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email address for sending messages to the channel. Read-only.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    @property
    def files_folder(self,) -> Optional[drive_item.DriveItem]:
        """
        Gets the filesFolder property value. Metadata for the location where the channel's files are stored.
        Returns: Optional[drive_item.DriveItem]
        """
        return self._files_folder
    
    @files_folder.setter
    def files_folder(self,value: Optional[drive_item.DriveItem] = None) -> None:
        """
        Sets the filesFolder property value. Metadata for the location where the channel's files are stored.
        Args:
            value: Value to set for the filesFolder property.
        """
        self._files_folder = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "files_folder": lambda n : setattr(self, 'files_folder', n.get_object_value(drive_item.DriveItem)),
            "is_favorite_by_default": lambda n : setattr(self, 'is_favorite_by_default', n.get_bool_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(conversation_member.ConversationMember)),
            "membership_type": lambda n : setattr(self, 'membership_type', n.get_enum_value(channel_membership_type.ChannelMembershipType)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(chat_message.ChatMessage)),
            "shared_with_teams": lambda n : setattr(self, 'shared_with_teams', n.get_collection_of_object_values(shared_with_channel_team_info.SharedWithChannelTeamInfo)),
            "tabs": lambda n : setattr(self, 'tabs', n.get_collection_of_object_values(teams_tab.TeamsTab)),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_favorite_by_default(self,) -> Optional[bool]:
        """
        Gets the isFavoriteByDefault property value. Indicates whether the channel should automatically be marked 'favorite' for all members of the team. Can only be set programmatically with Create team. Default: false.
        Returns: Optional[bool]
        """
        return self._is_favorite_by_default
    
    @is_favorite_by_default.setter
    def is_favorite_by_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFavoriteByDefault property value. Indicates whether the channel should automatically be marked 'favorite' for all members of the team. Can only be set programmatically with Create team. Default: false.
        Args:
            value: Value to set for the isFavoriteByDefault property.
        """
        self._is_favorite_by_default = value
    
    @property
    def members(self,) -> Optional[List[conversation_member.ConversationMember]]:
        """
        Gets the members property value. A collection of membership records associated with the channel.
        Returns: Optional[List[conversation_member.ConversationMember]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[conversation_member.ConversationMember]] = None) -> None:
        """
        Sets the members property value. A collection of membership records associated with the channel.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    @property
    def membership_type(self,) -> Optional[channel_membership_type.ChannelMembershipType]:
        """
        Gets the membershipType property value. The type of the channel. Can be set during creation and can't be changed. The possible values are: standard, private, unknownFutureValue, shared. The default value is standard. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value in this evolvable enum: shared.
        Returns: Optional[channel_membership_type.ChannelMembershipType]
        """
        return self._membership_type
    
    @membership_type.setter
    def membership_type(self,value: Optional[channel_membership_type.ChannelMembershipType] = None) -> None:
        """
        Sets the membershipType property value. The type of the channel. Can be set during creation and can't be changed. The possible values are: standard, private, unknownFutureValue, shared. The default value is standard. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value in this evolvable enum: shared.
        Args:
            value: Value to set for the membershipType property.
        """
        self._membership_type = value
    
    @property
    def messages(self,) -> Optional[List[chat_message.ChatMessage]]:
        """
        Gets the messages property value. A collection of all the messages in the channel. A navigation property. Nullable.
        Returns: Optional[List[chat_message.ChatMessage]]
        """
        return self._messages
    
    @messages.setter
    def messages(self,value: Optional[List[chat_message.ChatMessage]] = None) -> None:
        """
        Sets the messages property value. A collection of all the messages in the channel. A navigation property. Nullable.
        Args:
            value: Value to set for the messages property.
        """
        self._messages = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_object_value("filesFolder", self.files_folder)
        writer.write_bool_value("isFavoriteByDefault", self.is_favorite_by_default)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_enum_value("membershipType", self.membership_type)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_collection_of_object_values("sharedWithTeams", self.shared_with_teams)
        writer.write_collection_of_object_values("tabs", self.tabs)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("webUrl", self.web_url)
    
    @property
    def shared_with_teams(self,) -> Optional[List[shared_with_channel_team_info.SharedWithChannelTeamInfo]]:
        """
        Gets the sharedWithTeams property value. A collection of teams with which a channel is shared.
        Returns: Optional[List[shared_with_channel_team_info.SharedWithChannelTeamInfo]]
        """
        return self._shared_with_teams
    
    @shared_with_teams.setter
    def shared_with_teams(self,value: Optional[List[shared_with_channel_team_info.SharedWithChannelTeamInfo]] = None) -> None:
        """
        Sets the sharedWithTeams property value. A collection of teams with which a channel is shared.
        Args:
            value: Value to set for the sharedWithTeams property.
        """
        self._shared_with_teams = value
    
    @property
    def tabs(self,) -> Optional[List[teams_tab.TeamsTab]]:
        """
        Gets the tabs property value. A collection of all the tabs in the channel. A navigation property.
        Returns: Optional[List[teams_tab.TeamsTab]]
        """
        return self._tabs
    
    @tabs.setter
    def tabs(self,value: Optional[List[teams_tab.TeamsTab]] = None) -> None:
        """
        Sets the tabs property value. A collection of all the tabs in the channel. A navigation property.
        Args:
            value: Value to set for the tabs property.
        """
        self._tabs = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The ID of the Azure Active Directory tenant.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The ID of the Azure Active Directory tenant.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. A hyperlink that will go to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. A hyperlink that will go to the channel in Microsoft Teams. This is the URL that you get when you right-click a channel in Microsoft Teams and select Get link to channel. This URL should be treated as an opaque blob, and not parsed. Read-only.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

