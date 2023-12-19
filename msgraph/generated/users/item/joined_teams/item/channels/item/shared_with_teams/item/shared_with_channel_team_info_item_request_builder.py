from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .........models.o_data_errors.o_data_error import ODataError
    from .........models.shared_with_channel_team_info import SharedWithChannelTeamInfo
    from .allowed_members.allowed_members_request_builder import AllowedMembersRequestBuilder
    from .team.team_request_builder import TeamRequestBuilder

class SharedWithChannelTeamInfoItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the sharedWithTeams property of the microsoft.graph.channel entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SharedWithChannelTeamInfoItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/joinedTeams/{team%2Did}/channels/{channel%2Did}/sharedWithTeams/{sharedWithChannelTeamInfo%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Unshare a channel with a team by deleting the corresponding sharedWithChannelTeamInfo resource. This operation is allowed only for channels with a membershipType value of shared.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/sharedwithchannelteaminfo-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderGetRequestConfiguration] = None) -> Optional[SharedWithChannelTeamInfo]:
        """
        Get a team that has been shared with a specified channel. This operation is allowed only for channels with a membershipType value of shared.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SharedWithChannelTeamInfo]
        Find more info here: https://learn.microsoft.com/graph/api/sharedwithchannelteaminfo-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.shared_with_channel_team_info import SharedWithChannelTeamInfo

        return await self.request_adapter.send_async(request_info, SharedWithChannelTeamInfo, error_mapping)
    
    async def patch(self,body: Optional[SharedWithChannelTeamInfo] = None, request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[SharedWithChannelTeamInfo]:
        """
        Update the navigation property sharedWithTeams in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SharedWithChannelTeamInfo]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.shared_with_channel_team_info import SharedWithChannelTeamInfo

        return await self.request_adapter.send_async(request_info, SharedWithChannelTeamInfo, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Unshare a channel with a team by deleting the corresponding sharedWithChannelTeamInfo resource. This operation is allowed only for channels with a membershipType value of shared.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get a team that has been shared with a specified channel. This operation is allowed only for channels with a membershipType value of shared.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[SharedWithChannelTeamInfo] = None, request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property sharedWithTeams in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> SharedWithChannelTeamInfoItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SharedWithChannelTeamInfoItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SharedWithChannelTeamInfoItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def allowed_members(self) -> AllowedMembersRequestBuilder:
        """
        Provides operations to manage the allowedMembers property of the microsoft.graph.sharedWithChannelTeamInfo entity.
        """
        from .allowed_members.allowed_members_request_builder import AllowedMembersRequestBuilder

        return AllowedMembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def team(self) -> TeamRequestBuilder:
        """
        Provides operations to manage the team property of the microsoft.graph.teamInfo entity.
        """
        from .team.team_request_builder import TeamRequestBuilder

        return TeamRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SharedWithChannelTeamInfoItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class SharedWithChannelTeamInfoItemRequestBuilderGetQueryParameters():
        """
        Get a team that has been shared with a specified channel. This operation is allowed only for channels with a membershipType value of shared.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SharedWithChannelTeamInfoItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[SharedWithChannelTeamInfoItemRequestBuilder.SharedWithChannelTeamInfoItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SharedWithChannelTeamInfoItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

