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
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.reference_create import ReferenceCreate
    from .....models.string_collection_response import StringCollectionResponse

class RefRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of servicePrincipal entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RefRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/tokenLifetimePolicies/$ref?@id={%40id}{&%24count,%24filter,%24orderby,%24search,%24skip,%24top}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[RefRequestBuilderDeleteQueryParameters]] = None) -> None:
        """
        Remove a tokenLifetimePolicy object from a service principal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-delete-tokenlifetimepolicies?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[RefRequestBuilderGetQueryParameters]] = None) -> Optional[StringCollectionResponse]:
        """
        List the tokenLifetimePolicy objects that are assigned to a servicePrincipal. Only one object is returned in the collection because only one tokenLifetimePolicy can be assigned to a service principal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StringCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-list-tokenlifetimepolicies?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.string_collection_response import StringCollectionResponse

        return await self.request_adapter.send_async(request_info, StringCollectionResponse, error_mapping)
    
    async def post(self,body: ReferenceCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Assign a tokenLifetimePolicy to a servicePrincipal. You can have multiple tokenLifetimePolicy policies in a tenant but can assign only one tokenLifetimePolicy per service principal.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-post-tokenlifetimepolicies?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[RefRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Remove a tokenLifetimePolicy object from a service principal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/tokenLifetimePolicies/$ref?@id={%40id}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[RefRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        List the tokenLifetimePolicy objects that are assigned to a servicePrincipal. Only one object is returned in the collection because only one tokenLifetimePolicy can be assigned to a service principal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, '{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/tokenLifetimePolicies/$ref{?%24count,%24filter,%24orderby,%24search,%24skip,%24top}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: ReferenceCreate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Assign a tokenLifetimePolicy to a servicePrincipal. You can have multiple tokenLifetimePolicy policies in a tenant but can assign only one tokenLifetimePolicy per service principal.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/tokenLifetimePolicies/$ref', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> RefRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RefRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RefRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RefRequestBuilderDeleteQueryParameters():
        """
        Remove a tokenLifetimePolicy object from a service principal.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "id":
                return "%40id"
            return original_name
        
        # The delete Uri
        id: Optional[str] = None

    
    @dataclass
    class RefRequestBuilderDeleteRequestConfiguration(RequestConfiguration[RefRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RefRequestBuilderGetQueryParameters():
        """
        List the tokenLifetimePolicy objects that are assigned to a servicePrincipal. Only one object is returned in the collection because only one tokenLifetimePolicy can be assigned to a service principal.
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
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[list[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class RefRequestBuilderGetRequestConfiguration(RequestConfiguration[RefRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RefRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

