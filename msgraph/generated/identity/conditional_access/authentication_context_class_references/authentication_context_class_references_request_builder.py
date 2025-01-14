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
    from ....models.authentication_context_class_reference import AuthenticationContextClassReference
    from ....models.authentication_context_class_reference_collection_response import AuthenticationContextClassReferenceCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.authentication_context_class_reference_item_request_builder import AuthenticationContextClassReferenceItemRequestBuilder

class AuthenticationContextClassReferencesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the authenticationContextClassReferences property of the microsoft.graph.conditionalAccessRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AuthenticationContextClassReferencesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/conditionalAccess/authenticationContextClassReferences{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_authentication_context_class_reference_id(self,authentication_context_class_reference_id: str) -> AuthenticationContextClassReferenceItemRequestBuilder:
        """
        Provides operations to manage the authenticationContextClassReferences property of the microsoft.graph.conditionalAccessRoot entity.
        param authentication_context_class_reference_id: The unique identifier of authenticationContextClassReference
        Returns: AuthenticationContextClassReferenceItemRequestBuilder
        """
        if authentication_context_class_reference_id is None:
            raise TypeError("authentication_context_class_reference_id cannot be null.")
        from .item.authentication_context_class_reference_item_request_builder import AuthenticationContextClassReferenceItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authenticationContextClassReference%2Did"] = authentication_context_class_reference_id
        return AuthenticationContextClassReferenceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AuthenticationContextClassReferencesRequestBuilderGetQueryParameters]] = None) -> Optional[AuthenticationContextClassReferenceCollectionResponse]:
        """
        Retrieve a list of authenticationContextClassReference objects.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuthenticationContextClassReferenceCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/conditionalaccessroot-list-authenticationcontextclassreferences?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.authentication_context_class_reference_collection_response import AuthenticationContextClassReferenceCollectionResponse

        return await self.request_adapter.send_async(request_info, AuthenticationContextClassReferenceCollectionResponse, error_mapping)
    
    async def post(self,body: AuthenticationContextClassReference, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AuthenticationContextClassReference]:
        """
        Create new navigation property to authenticationContextClassReferences for identity
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuthenticationContextClassReference]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.authentication_context_class_reference import AuthenticationContextClassReference

        return await self.request_adapter.send_async(request_info, AuthenticationContextClassReference, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AuthenticationContextClassReferencesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve a list of authenticationContextClassReference objects.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: AuthenticationContextClassReference, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to authenticationContextClassReferences for identity
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AuthenticationContextClassReferencesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AuthenticationContextClassReferencesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AuthenticationContextClassReferencesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AuthenticationContextClassReferencesRequestBuilderGetQueryParameters():
        """
        Retrieve a list of authenticationContextClassReference objects.
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
    class AuthenticationContextClassReferencesRequestBuilderGetRequestConfiguration(RequestConfiguration[AuthenticationContextClassReferencesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AuthenticationContextClassReferencesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

