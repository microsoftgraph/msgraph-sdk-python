from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.on_premises_directory_synchronization import OnPremisesDirectorySynchronization
    from ...models.on_premises_directory_synchronization_collection_response import OnPremisesDirectorySynchronizationCollectionResponse
    from ...models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.on_premises_directory_synchronization_item_request_builder import OnPremisesDirectorySynchronizationItemRequestBuilder

class OnPremisesSynchronizationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the onPremisesSynchronization property of the microsoft.graph.directory entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new OnPremisesSynchronizationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/directory/onPremisesSynchronization{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_on_premises_directory_synchronization_id(self,on_premises_directory_synchronization_id: str) -> OnPremisesDirectorySynchronizationItemRequestBuilder:
        """
        Provides operations to manage the onPremisesSynchronization property of the microsoft.graph.directory entity.
        param on_premises_directory_synchronization_id: The unique identifier of onPremisesDirectorySynchronization
        Returns: OnPremisesDirectorySynchronizationItemRequestBuilder
        """
        if not on_premises_directory_synchronization_id:
            raise TypeError("on_premises_directory_synchronization_id cannot be null.")
        from .item.on_premises_directory_synchronization_item_request_builder import OnPremisesDirectorySynchronizationItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onPremisesDirectorySynchronization%2Did"] = on_premises_directory_synchronization_id
        return OnPremisesDirectorySynchronizationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[OnPremisesDirectorySynchronizationCollectionResponse]:
        """
        A container for on-premises directory synchronization functionalities that are available for the organization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnPremisesDirectorySynchronizationCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.on_premises_directory_synchronization_collection_response import OnPremisesDirectorySynchronizationCollectionResponse

        return await self.request_adapter.send_async(request_info, OnPremisesDirectorySynchronizationCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[OnPremisesDirectorySynchronization] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[OnPremisesDirectorySynchronization]:
        """
        Create new navigation property to onPremisesSynchronization for directory
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnPremisesDirectorySynchronization]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.on_premises_directory_synchronization import OnPremisesDirectorySynchronization

        return await self.request_adapter.send_async(request_info, OnPremisesDirectorySynchronization, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        A container for on-premises directory synchronization functionalities that are available for the organization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[OnPremisesDirectorySynchronization] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to onPremisesSynchronization for directory
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> OnPremisesSynchronizationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OnPremisesSynchronizationRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return OnPremisesSynchronizationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OnPremisesSynchronizationRequestBuilderGetQueryParameters():
        """
        A container for on-premises directory synchronization functionalities that are available for the organization.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    

