from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import chat_message
    from ........models.o_data_errors import o_data_error
    from .hosted_contents import hosted_contents_request_builder
    from .replies import replies_request_builder
    from .soft_delete import soft_delete_request_builder
    from .undo_soft_delete import undo_soft_delete_request_builder

class ChatMessageItemRequestBuilder():
    """
    Provides operations to manage the messages property of the microsoft.graph.channel entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ChatMessageItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/joinedTeams/{team%2Did}/primaryChannel/messages/{chatMessage%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ChatMessageItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property messages for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ChatMessageItemRequestBuilderGetRequestConfiguration] = None) -> Optional[chat_message.ChatMessage]:
        """
        Retrieve a single message or a message reply in a channel or a chat.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[chat_message.ChatMessage]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models import chat_message

        return await self.request_adapter.send_async(request_info, chat_message.ChatMessage, error_mapping)
    
    async def patch(self,body: Optional[chat_message.ChatMessage] = None, request_configuration: Optional[ChatMessageItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[chat_message.ChatMessage]:
        """
        Update a chatMessage object. With the exception of the **policyViolation** property, all properties of a **chatMessage** can be updated in delegated permissions scenarios.Only the **policyViolation** property of a **chatMessage** can be updated in application permissions scenarios. The update only works for chats where members are Microsoft Teams users. If one of the participants is using Skype, the operation will fail. This method does not support federation. Only the user in the tenant who sent the message can perform data loss prevention (DLP) updates on the specified chat message.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[chat_message.ChatMessage]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models import chat_message

        return await self.request_adapter.send_async(request_info, chat_message.ChatMessage, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ChatMessageItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property messages for users
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
        Retrieve a single message or a message reply in a channel or a chat.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[chat_message.ChatMessage] = None, request_configuration: Optional[ChatMessageItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update a chatMessage object. With the exception of the **policyViolation** property, all properties of a **chatMessage** can be updated in delegated permissions scenarios.Only the **policyViolation** property of a **chatMessage** can be updated in application permissions scenarios. The update only works for chats where members are Microsoft Teams users. If one of the participants is using Skype, the operation will fail. This method does not support federation. Only the user in the tenant who sent the message can perform data loss prevention (DLP) updates on the specified chat message.
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def hosted_contents(self) -> hosted_contents_request_builder.HostedContentsRequestBuilder:
        """
        Provides operations to manage the hostedContents property of the microsoft.graph.chatMessage entity.
        """
        from .hosted_contents import hosted_contents_request_builder

        return hosted_contents_request_builder.HostedContentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def replies(self) -> replies_request_builder.RepliesRequestBuilder:
        """
        Provides operations to manage the replies property of the microsoft.graph.chatMessage entity.
        """
        from .replies import replies_request_builder

        return replies_request_builder.RepliesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def soft_delete(self) -> soft_delete_request_builder.SoftDeleteRequestBuilder:
        """
        Provides operations to call the softDelete method.
        """
        from .soft_delete import soft_delete_request_builder

        return soft_delete_request_builder.SoftDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def undo_soft_delete(self) -> undo_soft_delete_request_builder.UndoSoftDeleteRequestBuilder:
        """
        Provides operations to call the undoSoftDelete method.
        """
        from .undo_soft_delete import undo_soft_delete_request_builder

        return undo_soft_delete_request_builder.UndoSoftDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChatMessageItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ChatMessageItemRequestBuilderGetQueryParameters():
        """
        Retrieve a single message or a message reply in a channel or a chat.
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class ChatMessageItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

