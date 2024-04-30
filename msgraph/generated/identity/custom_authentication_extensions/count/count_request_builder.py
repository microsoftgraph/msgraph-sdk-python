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
    from ....models.o_data_errors.o_data_error import ODataError

class CountRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to count the resources in the collection.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CountRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/customAuthenticationExtensions/$count{?%24filter,%24search}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[int]:
        """
        Get the number of the resource
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[int]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "int", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get the number of the resource
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CountRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CountRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CountRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CountRequestBuilderGetQueryParameters():
        """
        Get the number of the resource
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "filter":
                return "%24filter"
            if original_name == "search":
                return "%24search"
            return original_name
        
        # Filter items by property values
        filter: Optional[str] = None

        # Search items by search phrases
        search: Optional[str] = None

    

