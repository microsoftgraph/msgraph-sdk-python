from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import list_item, list_item_collection_response
    from .....models.o_data_errors import o_data_error
    from .item import list_item_item_request_builder

class ItemsRequestBuilder():
    """
    Provides operations to manage the items property of the microsoft.graph.list entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ItemsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/shares/{sharedDriveItem%2Did}/list/items{?%24top,%24skip,%24search,%24filter,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def by_list_item_id(self,list_item_id: str) -> list_item_item_request_builder.ListItemItemRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.list entity.
        Args:
            list_item_id: Unique identifier of the item
        Returns: list_item_item_request_builder.ListItemItemRequestBuilder
        """
        if list_item_id is None:
            raise Exception("list_item_id cannot be undefined")
        from .item import list_item_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["listItem%2Did"] = list_item_id
        return list_item_item_request_builder.ListItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ItemsRequestBuilderGetRequestConfiguration] = None) -> Optional[list_item_collection_response.ListItemCollectionResponse]:
        """
        Get the collection of [items][item] in a [list][].
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list_item_collection_response.ListItemCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import list_item_collection_response

        return await self.request_adapter.send_async(request_info, list_item_collection_response.ListItemCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[list_item.ListItem] = None, request_configuration: Optional[ItemsRequestBuilderPostRequestConfiguration] = None) -> Optional[list_item.ListItem]:
        """
        Create a new [listItem][] in a [list][].
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list_item.ListItem]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import list_item

        return await self.request_adapter.send_async(request_info, list_item.ListItem, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[ItemsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the collection of [items][item] in a [list][].
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
    
    def to_post_request_information(self,body: Optional[list_item.ListItem] = None, request_configuration: Optional[ItemsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create a new [listItem][] in a [list][].
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
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class ItemsRequestBuilderGetQueryParameters():
        """
        Get the collection of [items][item] in a [list][].
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class ItemsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ItemsRequestBuilder.ItemsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ItemsRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

