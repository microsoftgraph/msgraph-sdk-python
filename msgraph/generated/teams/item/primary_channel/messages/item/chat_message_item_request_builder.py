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

chat_message = lazy_import('msgraph.generated.models.chat_message')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
hosted_contents_request_builder = lazy_import('msgraph.generated.teams.item.primary_channel.messages.item.hosted_contents.hosted_contents_request_builder')
chat_message_hosted_content_item_request_builder = lazy_import('msgraph.generated.teams.item.primary_channel.messages.item.hosted_contents.item.chat_message_hosted_content_item_request_builder')
soft_delete_request_builder = lazy_import('msgraph.generated.teams.item.primary_channel.messages.item.microsoft_graph_soft_delete.soft_delete_request_builder')
undo_soft_delete_request_builder = lazy_import('msgraph.generated.teams.item.primary_channel.messages.item.microsoft_graph_undo_soft_delete.undo_soft_delete_request_builder')
replies_request_builder = lazy_import('msgraph.generated.teams.item.primary_channel.messages.item.replies.replies_request_builder')
chat_message_item_request_builder = lazy_import('msgraph.generated.teams.item.primary_channel.messages.item.replies.item.chat_message_item_request_builder')

class ChatMessageItemRequestBuilder():
    """
    Provides operations to manage the messages property of the microsoft.graph.channel entity.
    """
    @property
    def hosted_contents(self) -> hosted_contents_request_builder.HostedContentsRequestBuilder:
        """
        Provides operations to manage the hostedContents property of the microsoft.graph.chatMessage entity.
        """
        return hosted_contents_request_builder.HostedContentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_soft_delete(self) -> soft_delete_request_builder.SoftDeleteRequestBuilder:
        """
        Provides operations to call the softDelete method.
        """
        return soft_delete_request_builder.SoftDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_undo_soft_delete(self) -> undo_soft_delete_request_builder.UndoSoftDeleteRequestBuilder:
        """
        Provides operations to call the undoSoftDelete method.
        """
        return undo_soft_delete_request_builder.UndoSoftDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def replies(self) -> replies_request_builder.RepliesRequestBuilder:
        """
        Provides operations to manage the replies property of the microsoft.graph.chatMessage entity.
        """
        return replies_request_builder.RepliesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, chat_message_id: Optional[str] = None) -> None:
        """
        Instantiates a new ChatMessageItemRequestBuilder and sets the default values.
        Args:
            chatMessageId: key: id of chatMessage
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/teams/{team%2Did}/primaryChannel/messages/{chatMessage%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params["chatMessage%2Did"] = chatMessageId
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ChatMessageItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property messages for teams
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ChatMessageItemRequestBuilderGetRequestConfiguration] = None) -> Optional[chat_message.ChatMessage]:
        """
        A collection of all the messages in the channel. A navigation property. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[chat_message.ChatMessage]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, chat_message.ChatMessage, error_mapping)
    
    def hosted_contents_by_id(self,id: str) -> chat_message_hosted_content_item_request_builder.ChatMessageHostedContentItemRequestBuilder:
        """
        Provides operations to manage the hostedContents property of the microsoft.graph.chatMessage entity.
        Args:
            id: Unique identifier of the item
        Returns: chat_message_hosted_content_item_request_builder.ChatMessageHostedContentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chatMessageHostedContent%2Did"] = id
        return chat_message_hosted_content_item_request_builder.ChatMessageHostedContentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[chat_message.ChatMessage] = None, request_configuration: Optional[ChatMessageItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[chat_message.ChatMessage]:
        """
        Update the navigation property messages in teams
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[chat_message.ChatMessage]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, chat_message.ChatMessage, error_mapping)
    
    def replies_by_id(self,id: str) -> ChatMessageItemRequestBuilder:
        """
        Provides operations to manage the replies property of the microsoft.graph.chatMessage entity.
        Args:
            id: Unique identifier of the item
        Returns: ChatMessageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chatMessage%2Did1"] = id
        return ChatMessageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[ChatMessageItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property messages for teams
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
    
    def to_get_request_information(self,request_configuration: Optional[ChatMessageItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A collection of all the messages in the channel. A navigation property. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[chat_message.ChatMessage] = None, request_configuration: Optional[ChatMessageItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property messages in teams
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
    
    @dataclass
    class ChatMessageItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ChatMessageItemRequestBuilderGetQueryParameters():
        """
        A collection of all the messages in the channel. A navigation property. Nullable.
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
    class ChatMessageItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ChatMessageItemRequestBuilder.ChatMessageItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ChatMessageItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

