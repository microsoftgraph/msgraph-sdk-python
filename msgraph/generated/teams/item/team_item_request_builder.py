from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.team import Team
    from .all_channels.all_channels_request_builder import AllChannelsRequestBuilder
    from .archive.archive_request_builder import ArchiveRequestBuilder
    from .channels.channels_request_builder import ChannelsRequestBuilder
    from .clone.clone_request_builder import CloneRequestBuilder
    from .complete_migration.complete_migration_request_builder import CompleteMigrationRequestBuilder
    from .group.group_request_builder import GroupRequestBuilder
    from .incoming_channels.incoming_channels_request_builder import IncomingChannelsRequestBuilder
    from .installed_apps.installed_apps_request_builder import InstalledAppsRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder
    from .photo.photo_request_builder import PhotoRequestBuilder
    from .primary_channel.primary_channel_request_builder import PrimaryChannelRequestBuilder
    from .schedule.schedule_request_builder import ScheduleRequestBuilder
    from .send_activity_notification.send_activity_notification_request_builder import SendActivityNotificationRequestBuilder
    from .tags.tags_request_builder import TagsRequestBuilder
    from .template.template_request_builder import TemplateRequestBuilder
    from .unarchive.unarchive_request_builder import UnarchiveRequestBuilder

class TeamItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of team entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TeamItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/teams/{team%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete entity from teams
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[TeamItemRequestBuilderGetQueryParameters]] = None) -> Optional[Team]:
        """
        Retrieve the properties and relationships of the specified team.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Team]
        Find more info here: https://learn.microsoft.com/graph/api/team-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.team import Team

        return await self.request_adapter.send_async(request_info, Team, error_mapping)
    
    async def patch(self,body: Team, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Team]:
        """
        Update the properties of the specified team.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Team]
        Find more info here: https://learn.microsoft.com/graph/api/team-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.team import Team

        return await self.request_adapter.send_async(request_info, Team, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete entity from teams
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TeamItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of the specified team.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Team, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of the specified team.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> TeamItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TeamItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TeamItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def all_channels(self) -> AllChannelsRequestBuilder:
        """
        Provides operations to manage the allChannels property of the microsoft.graph.team entity.
        """
        from .all_channels.all_channels_request_builder import AllChannelsRequestBuilder

        return AllChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def archive(self) -> ArchiveRequestBuilder:
        """
        Provides operations to call the archive method.
        """
        from .archive.archive_request_builder import ArchiveRequestBuilder

        return ArchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def channels(self) -> ChannelsRequestBuilder:
        """
        Provides operations to manage the channels property of the microsoft.graph.team entity.
        """
        from .channels.channels_request_builder import ChannelsRequestBuilder

        return ChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clone(self) -> CloneRequestBuilder:
        """
        Provides operations to call the clone method.
        """
        from .clone.clone_request_builder import CloneRequestBuilder

        return CloneRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def complete_migration(self) -> CompleteMigrationRequestBuilder:
        """
        Provides operations to call the completeMigration method.
        """
        from .complete_migration.complete_migration_request_builder import CompleteMigrationRequestBuilder

        return CompleteMigrationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group(self) -> GroupRequestBuilder:
        """
        Provides operations to manage the group property of the microsoft.graph.team entity.
        """
        from .group.group_request_builder import GroupRequestBuilder

        return GroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incoming_channels(self) -> IncomingChannelsRequestBuilder:
        """
        Provides operations to manage the incomingChannels property of the microsoft.graph.team entity.
        """
        from .incoming_channels.incoming_channels_request_builder import IncomingChannelsRequestBuilder

        return IncomingChannelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def installed_apps(self) -> InstalledAppsRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.team entity.
        """
        from .installed_apps.installed_apps_request_builder import InstalledAppsRequestBuilder

        return InstalledAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.team entity.
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.team entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.team entity.
        """
        from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder

        return PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photo(self) -> PhotoRequestBuilder:
        """
        Provides operations to manage the photo property of the microsoft.graph.team entity.
        """
        from .photo.photo_request_builder import PhotoRequestBuilder

        return PhotoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def primary_channel(self) -> PrimaryChannelRequestBuilder:
        """
        Provides operations to manage the primaryChannel property of the microsoft.graph.team entity.
        """
        from .primary_channel.primary_channel_request_builder import PrimaryChannelRequestBuilder

        return PrimaryChannelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schedule(self) -> ScheduleRequestBuilder:
        """
        Provides operations to manage the schedule property of the microsoft.graph.team entity.
        """
        from .schedule.schedule_request_builder import ScheduleRequestBuilder

        return ScheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_activity_notification(self) -> SendActivityNotificationRequestBuilder:
        """
        Provides operations to call the sendActivityNotification method.
        """
        from .send_activity_notification.send_activity_notification_request_builder import SendActivityNotificationRequestBuilder

        return SendActivityNotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> TagsRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.team entity.
        """
        from .tags.tags_request_builder import TagsRequestBuilder

        return TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def template(self) -> TemplateRequestBuilder:
        """
        Provides operations to manage the template property of the microsoft.graph.team entity.
        """
        from .template.template_request_builder import TemplateRequestBuilder

        return TemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unarchive(self) -> UnarchiveRequestBuilder:
        """
        Provides operations to call the unarchive method.
        """
        from .unarchive.unarchive_request_builder import UnarchiveRequestBuilder

        return UnarchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TeamItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TeamItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of the specified team.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class TeamItemRequestBuilderGetRequestConfiguration(RequestConfiguration[TeamItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TeamItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

