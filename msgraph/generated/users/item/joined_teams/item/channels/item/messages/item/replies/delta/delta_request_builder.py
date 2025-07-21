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
    from ...........models.o_data_errors.o_data_error import ODataError
    from .delta_get_response import DeltaGetResponse

class DeltaRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the delta method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DeltaRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/joinedTeams/{team%2Did}/channels/{channel%2Did}/messages/{chatMessage%2Did}/replies/delta(){?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DeltaRequestBuilderGetQueryParameters]] = None) -> Optional[DeltaGetResponse]:
        """
        Get the list of messages from all chats in which a user is a participant, including one-on-one chats, group chats, and meeting chats. When you use delta query, you can get new or updated messages. To get the replies for a message, use the list message replies or the get message reply operations. A GET request with the delta function returns one of the following: State tokens are opaque to the client. To proceed with a round of change tracking, copy and apply the @odata.nextLink or @odata.deltaLink URL returned from the last GET request to the next delta function call. An @odata.deltaLink returned in a response signifies that the current round of change tracking is complete. You can save and use the @odata.deltaLink URL when you begin to retrieve more changes (messages changed or posted after you acquire @odata.deltaLink). For more information, see the delta query documentation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeltaGetResponse]
        Find more info here: https://learn.microsoft.com/graph/api/chatmessage-delta?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .delta_get_response import DeltaGetResponse

        return await self.request_adapter.send_async(request_info, DeltaGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DeltaRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the list of messages from all chats in which a user is a participant, including one-on-one chats, group chats, and meeting chats. When you use delta query, you can get new or updated messages. To get the replies for a message, use the list message replies or the get message reply operations. A GET request with the delta function returns one of the following: State tokens are opaque to the client. To proceed with a round of change tracking, copy and apply the @odata.nextLink or @odata.deltaLink URL returned from the last GET request to the next delta function call. An @odata.deltaLink returned in a response signifies that the current round of change tracking is complete. You can save and use the @odata.deltaLink URL when you begin to retrieve more changes (messages changed or posted after you acquire @odata.deltaLink). For more information, see the delta query documentation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> DeltaRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeltaRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DeltaRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class DeltaRequestBuilderGetQueryParameters():
        """
        Get the list of messages from all chats in which a user is a participant, including one-on-one chats, group chats, and meeting chats. When you use delta query, you can get new or updated messages. To get the replies for a message, use the list message replies or the get message reply operations. A GET request with the delta function returns one of the following: State tokens are opaque to the client. To proceed with a round of change tracking, copy and apply the @odata.nextLink or @odata.deltaLink URL returned from the last GET request to the next delta function call. An @odata.deltaLink returned in a response signifies that the current round of change tracking is complete. You can save and use the @odata.deltaLink URL when you begin to retrieve more changes (messages changed or posted after you acquire @odata.deltaLink). For more information, see the delta query documentation.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[list[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[list[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class DeltaRequestBuilderGetRequestConfiguration(RequestConfiguration[DeltaRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

