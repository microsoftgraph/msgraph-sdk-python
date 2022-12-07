from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

all_channels_request_builder = lazy_import('msgraph.generated.groups.item.team.all_channels.all_channels_request_builder')
channel_item_request_builder = lazy_import('msgraph.generated.groups.item.team.all_channels.item.channel_item_request_builder')
archive_request_builder = lazy_import('msgraph.generated.groups.item.team.archive.archive_request_builder')
channels_request_builder = lazy_import('msgraph.generated.groups.item.team.channels.channels_request_builder')
channel_item_request_builder = lazy_import('msgraph.generated.groups.item.team.channels.item.channel_item_request_builder')
clone_request_builder = lazy_import('msgraph.generated.groups.item.team.clone.clone_request_builder')
complete_migration_request_builder = lazy_import('msgraph.generated.groups.item.team.complete_migration.complete_migration_request_builder')
group_request_builder = lazy_import('msgraph.generated.groups.item.team.group.group_request_builder')
incoming_channels_request_builder = lazy_import('msgraph.generated.groups.item.team.incoming_channels.incoming_channels_request_builder')
channel_item_request_builder = lazy_import('msgraph.generated.groups.item.team.incoming_channels.item.channel_item_request_builder')
installed_apps_request_builder = lazy_import('msgraph.generated.groups.item.team.installed_apps.installed_apps_request_builder')
teams_app_installation_item_request_builder = lazy_import('msgraph.generated.groups.item.team.installed_apps.item.teams_app_installation_item_request_builder')
members_request_builder = lazy_import('msgraph.generated.groups.item.team.members.members_request_builder')
conversation_member_item_request_builder = lazy_import('msgraph.generated.groups.item.team.members.item.conversation_member_item_request_builder')
operations_request_builder = lazy_import('msgraph.generated.groups.item.team.operations.operations_request_builder')
teams_async_operation_item_request_builder = lazy_import('msgraph.generated.groups.item.team.operations.item.teams_async_operation_item_request_builder')
photo_request_builder = lazy_import('msgraph.generated.groups.item.team.photo.photo_request_builder')
primary_channel_request_builder = lazy_import('msgraph.generated.groups.item.team.primary_channel.primary_channel_request_builder')
schedule_request_builder = lazy_import('msgraph.generated.groups.item.team.schedule.schedule_request_builder')
send_activity_notification_request_builder = lazy_import('msgraph.generated.groups.item.team.send_activity_notification.send_activity_notification_request_builder')
tags_request_builder = lazy_import('msgraph.generated.groups.item.team.tags.tags_request_builder')
teamwork_tag_item_request_builder = lazy_import('msgraph.generated.groups.item.team.tags.item.teamwork_tag_item_request_builder')
template_request_builder = lazy_import('msgraph.generated.groups.item.team.template.template_request_builder')
unarchive_request_builder = lazy_import('msgraph.generated.groups.item.team.unarchive.unarchive_request_builder')
team = lazy_import('msgraph.generated.models.team')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class TeamRequestBuilder():
    """
    Provides operations to manage the team property of the microsoft.graph.group entity.
    """
    def all_channels(self) -> all_channels_request_builder.AllChannelsRequestBuilder:
        """
        Provides operations to manage the allChannels property of the microsoft.graph.team entity.
        """
        return all_channels_request_builder.AllChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def archive(self) -> archive_request_builder.ArchiveRequestBuilder:
        """
        Provides operations to call the archive method.
        """
        return archive_request_builder.ArchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    def channels(self) -> channels_request_builder.ChannelsRequestBuilder:
        """
        Provides operations to manage the channels property of the microsoft.graph.team entity.
        """
        return channels_request_builder.ChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def clone(self) -> clone_request_builder.CloneRequestBuilder:
        """
        Provides operations to call the clone method.
        """
        return clone_request_builder.CloneRequestBuilder(self.request_adapter, self.path_parameters)
    
    def complete_migration(self) -> complete_migration_request_builder.CompleteMigrationRequestBuilder:
        """
        Provides operations to call the completeMigration method.
        """
        return complete_migration_request_builder.CompleteMigrationRequestBuilder(self.request_adapter, self.path_parameters)
    
    def group(self) -> group_request_builder.GroupRequestBuilder:
        """
        Provides operations to manage the group property of the microsoft.graph.team entity.
        """
        return group_request_builder.GroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    def incoming_channels(self) -> incoming_channels_request_builder.IncomingChannelsRequestBuilder:
        """
        Provides operations to manage the incomingChannels property of the microsoft.graph.team entity.
        """
        return incoming_channels_request_builder.IncomingChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def installed_apps(self) -> installed_apps_request_builder.InstalledAppsRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.team entity.
        """
        return installed_apps_request_builder.InstalledAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.team entity.
        """
        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.team entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def photo(self) -> photo_request_builder.PhotoRequestBuilder:
        """
        Provides operations to manage the photo property of the microsoft.graph.team entity.
        """
        return photo_request_builder.PhotoRequestBuilder(self.request_adapter, self.path_parameters)
    
    def primary_channel(self) -> primary_channel_request_builder.PrimaryChannelRequestBuilder:
        """
        Provides operations to manage the primaryChannel property of the microsoft.graph.team entity.
        """
        return primary_channel_request_builder.PrimaryChannelRequestBuilder(self.request_adapter, self.path_parameters)
    
    def schedule(self) -> schedule_request_builder.ScheduleRequestBuilder:
        """
        Provides operations to manage the schedule property of the microsoft.graph.team entity.
        """
        return schedule_request_builder.ScheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    def send_activity_notification(self) -> send_activity_notification_request_builder.SendActivityNotificationRequestBuilder:
        """
        Provides operations to call the sendActivityNotification method.
        """
        return send_activity_notification_request_builder.SendActivityNotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    def tags(self) -> tags_request_builder.TagsRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.team entity.
        """
        return tags_request_builder.TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def template(self) -> template_request_builder.TemplateRequestBuilder:
        """
        Provides operations to manage the template property of the microsoft.graph.team entity.
        """
        return template_request_builder.TemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    def unarchive(self) -> unarchive_request_builder.UnarchiveRequestBuilder:
        """
        Provides operations to call the unarchive method.
        """
        return unarchive_request_builder.UnarchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    def all_channels_by_id(self,id: str) -> channel_item_request_builder.ChannelItemRequestBuilder:
        """
        Provides operations to manage the allChannels property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: channel_item_request_builder.ChannelItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["channel%2Did"] = id
        return channel_item_request_builder.ChannelItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def channels_by_id(self,id: str) -> channel_item_request_builder.ChannelItemRequestBuilder:
        """
        Provides operations to manage the channels property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: channel_item_request_builder.ChannelItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["channel%2Did"] = id
        return channel_item_request_builder.ChannelItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TeamRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/team{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[TeamRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property team for groups
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_get_request_information(self,request_configuration: Optional[TeamRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The team associated with this group.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[team.Team] = None, request_configuration: Optional[TeamRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Create a new team under a group. In order to create a team, the group must have a least one owner. If the group was created less than 15 minutes ago, it's possible for the Create team call to fail with a 404 error code due to replication delays. The recommended pattern is to retry the Create team call three times, with a 10 second delay between calls.
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[TeamRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property team for groups
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[TeamRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[team.Team]:
        """
        The team associated with this group.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[team.Team]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, team.Team, response_handler, error_mapping)
    
    def incoming_channels_by_id(self,id: str) -> channel_item_request_builder.ChannelItemRequestBuilder:
        """
        Provides operations to manage the incomingChannels property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: channel_item_request_builder.ChannelItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["channel%2Did"] = id
        return channel_item_request_builder.ChannelItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def installed_apps_by_id(self,id: str) -> teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsAppInstallation%2Did"] = id
        return teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def members_by_id(self,id: str) -> conversation_member_item_request_builder.ConversationMemberItemRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: conversation_member_item_request_builder.ConversationMemberItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conversationMember%2Did"] = id
        return conversation_member_item_request_builder.ConversationMemberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> teams_async_operation_item_request_builder.TeamsAsyncOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: teams_async_operation_item_request_builder.TeamsAsyncOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsAsyncOperation%2Did"] = id
        return teams_async_operation_item_request_builder.TeamsAsyncOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[team.Team] = None, request_configuration: Optional[TeamRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[team.Team]:
        """
        Create a new team under a group. In order to create a team, the group must have a least one owner. If the group was created less than 15 minutes ago, it's possible for the Create team call to fail with a 404 error code due to replication delays. The recommended pattern is to retry the Create team call three times, with a 10 second delay between calls.
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[team.Team]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, team.Team, response_handler, error_mapping)
    
    def tags_by_id(self,id: str) -> teamwork_tag_item_request_builder.TeamworkTagItemRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.team entity.
        Args:
            id: Unique identifier of the item
        Returns: teamwork_tag_item_request_builder.TeamworkTagItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamworkTag%2Did"] = id
        return teamwork_tag_item_request_builder.TeamworkTagItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class TeamRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TeamRequestBuilderGetQueryParameters():
        """
        The team associated with this group.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class TeamRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TeamRequestBuilder.TeamRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TeamRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

