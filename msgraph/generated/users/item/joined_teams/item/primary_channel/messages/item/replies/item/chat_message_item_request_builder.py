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
    from ..........models.chat_message import ChatMessage
    from ..........models.o_data_errors.o_data_error import ODataError
    from .hosted_contents.hosted_contents_request_builder import HostedContentsRequestBuilder
    from .set_reaction.set_reaction_request_builder import SetReactionRequestBuilder
    from .soft_delete.soft_delete_request_builder import SoftDeleteRequestBuilder
    from .undo_soft_delete.undo_soft_delete_request_builder import UndoSoftDeleteRequestBuilder
    from .unset_reaction.unset_reaction_request_builder import UnsetReactionRequestBuilder

class ChatMessageItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the replies property of the microsoft.graph.chatMessage entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ChatMessageItemRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/joinedTeams/{team%2Did}/primaryChannel/messages/{chatMessage%2Did}/replies/{chatMessage%2Did1}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[ChatMessageItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property replies for users
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ChatMessageItemRequestBuilderGetRequestConfiguration] = None) -> Optional[ChatMessage]:
        """
        Retrieve a single message or a message reply in a channel or a chat.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChatMessage]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.chat_message import ChatMessage

        return await self.request_adapter.send_async(request_info, ChatMessage, error_mapping)
    
    async def patch(self,body: Optional[ChatMessage] = None, request_configuration: Optional[ChatMessageItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[ChatMessage]:
        """
        Update the navigation property replies in users
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ChatMessage]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.chat_message import ChatMessage

        return await self.request_adapter.send_async(request_info, ChatMessage, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ChatMessageItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property replies for users
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_patch_request_information(self,body: Optional[ChatMessage] = None, request_configuration: Optional[ChatMessageItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property replies in users
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    def hosted_contents(self) -> HostedContentsRequestBuilder:
        """
        Provides operations to manage the hostedContents property of the microsoft.graph.chatMessage entity.
        """
        from .hosted_contents.hosted_contents_request_builder import HostedContentsRequestBuilder

        return HostedContentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_reaction(self) -> SetReactionRequestBuilder:
        """
        Provides operations to call the setReaction method.
        """
        from .set_reaction.set_reaction_request_builder import SetReactionRequestBuilder

        return SetReactionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def soft_delete(self) -> SoftDeleteRequestBuilder:
        """
        Provides operations to call the softDelete method.
        """
        from .soft_delete.soft_delete_request_builder import SoftDeleteRequestBuilder

        return SoftDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def undo_soft_delete(self) -> UndoSoftDeleteRequestBuilder:
        """
        Provides operations to call the undoSoftDelete method.
        """
        from .undo_soft_delete.undo_soft_delete_request_builder import UndoSoftDeleteRequestBuilder

        return UndoSoftDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unset_reaction(self) -> UnsetReactionRequestBuilder:
        """
        Provides operations to call the unsetReaction method.
        """
        from .unset_reaction.unset_reaction_request_builder import UnsetReactionRequestBuilder

        return UnsetReactionRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ChatMessageItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class ChatMessageItemRequestBuilderGetQueryParameters():
        """
        Retrieve a single message or a message reply in a channel or a chat.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
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
    class ChatMessageItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ChatMessageItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ChatMessageItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

