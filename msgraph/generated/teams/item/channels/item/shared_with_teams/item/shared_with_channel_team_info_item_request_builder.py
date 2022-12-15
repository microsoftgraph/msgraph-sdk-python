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

shared_with_channel_team_info = lazy_import('msgraph.generated.models.shared_with_channel_team_info')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
allowed_members_request_builder = lazy_import('msgraph.generated.teams.item.channels.item.shared_with_teams.item.allowed_members.allowed_members_request_builder')
conversation_member_item_request_builder = lazy_import('msgraph.generated.teams.item.channels.item.shared_with_teams.item.allowed_members.item.conversation_member_item_request_builder')

class SharedWithChannelTeamInfoItemRequestBuilder():
    """
    Provides operations to manage the sharedWithTeams property of the microsoft.graph.channel entity.
    """
    @property
    def allowed_members(self) -> allowed_members_request_builder.AllowedMembersRequestBuilder:
        """
        Provides operations to manage the allowedMembers property of the microsoft.graph.sharedWithChannelTeamInfo entity.
        """
        return allowed_members_request_builder.AllowedMembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def allowed_members_by_id(self,id: str) -> conversation_member_item_request_builder.ConversationMemberItemRequestBuilder:
        """
        Provides operations to manage the allowedMembers property of the microsoft.graph.sharedWithChannelTeamInfo entity.
        Args:
            id: Unique identifier of the item
        Returns: conversation_member_item_request_builder.ConversationMemberItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conversationMember%2Did"] = id
        return conversation_member_item_request_builder.ConversationMemberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SharedWithChannelTeamInfoItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/teams/{team%2Did}/channels/{channel%2Did}/sharedWithTeams/{sharedWithChannelTeamInfo%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property sharedWithTeams for teams
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
    
    def create_get_request_information(self,request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A collection of teams with which a channel is shared.
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
    
    def create_patch_request_information(self,body: Optional[shared_with_channel_team_info.SharedWithChannelTeamInfo] = None, request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property sharedWithTeams in teams
        Args:
            body: The request body
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
    
    async def delete(self,request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property sharedWithTeams for teams
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
    
    async def get(self,request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[shared_with_channel_team_info.SharedWithChannelTeamInfo]:
        """
        A collection of teams with which a channel is shared.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[shared_with_channel_team_info.SharedWithChannelTeamInfo]
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
        return await self.request_adapter.send_async(request_info, shared_with_channel_team_info.SharedWithChannelTeamInfo, response_handler, error_mapping)
    
    async def patch(self,body: Optional[shared_with_channel_team_info.SharedWithChannelTeamInfo] = None, request_configuration: Optional[SharedWithChannelTeamInfoItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[shared_with_channel_team_info.SharedWithChannelTeamInfo]:
        """
        Update the navigation property sharedWithTeams in teams
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[shared_with_channel_team_info.SharedWithChannelTeamInfo]
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
        return await self.request_adapter.send_async(request_info, shared_with_channel_team_info.SharedWithChannelTeamInfo, response_handler, error_mapping)
    
    @dataclass
    class SharedWithChannelTeamInfoItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SharedWithChannelTeamInfoItemRequestBuilderGetQueryParameters():
        """
        A collection of teams with which a channel is shared.
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
    class SharedWithChannelTeamInfoItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SharedWithChannelTeamInfoItemRequestBuilder.SharedWithChannelTeamInfoItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SharedWithChannelTeamInfoItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

