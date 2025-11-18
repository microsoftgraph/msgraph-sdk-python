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
    from ....models.fraud_protection_provider import FraudProtectionProvider
    from ....models.fraud_protection_provider_collection_response import FraudProtectionProviderCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.fraud_protection_provider_item_request_builder import FraudProtectionProviderItemRequestBuilder

class FraudProtectionProvidersRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the fraudProtectionProviders property of the microsoft.graph.riskPreventionContainer entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FraudProtectionProvidersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/riskPrevention/fraudProtectionProviders{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_fraud_protection_provider_id(self,fraud_protection_provider_id: str) -> FraudProtectionProviderItemRequestBuilder:
        """
        Provides operations to manage the fraudProtectionProviders property of the microsoft.graph.riskPreventionContainer entity.
        param fraud_protection_provider_id: The unique identifier of fraudProtectionProvider
        Returns: FraudProtectionProviderItemRequestBuilder
        """
        if fraud_protection_provider_id is None:
            raise TypeError("fraud_protection_provider_id cannot be null.")
        from .item.fraud_protection_provider_item_request_builder import FraudProtectionProviderItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fraudProtectionProvider%2Did"] = fraud_protection_provider_id
        return FraudProtectionProviderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[FraudProtectionProvidersRequestBuilderGetQueryParameters]] = None) -> Optional[FraudProtectionProviderCollectionResponse]:
        """
        Get a list of the fraudProtectionProvider object and their properties. The following derived types are supported:
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FraudProtectionProviderCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/riskpreventioncontainer-list-fraudprotectionproviders?view=graph-rest-1.0
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
        from ....models.fraud_protection_provider_collection_response import FraudProtectionProviderCollectionResponse

        return await self.request_adapter.send_async(request_info, FraudProtectionProviderCollectionResponse, error_mapping)
    
    async def post(self,body: FraudProtectionProvider, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FraudProtectionProvider]:
        """
        Create a new fraudProtectionProvider object. You can create one of the following subtypes that are derived from fraudProtectionProvider.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FraudProtectionProvider]
        Find more info here: https://learn.microsoft.com/graph/api/riskpreventioncontainer-post-fraudprotectionproviders?view=graph-rest-1.0
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
        from ....models.fraud_protection_provider import FraudProtectionProvider

        return await self.request_adapter.send_async(request_info, FraudProtectionProvider, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FraudProtectionProvidersRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get a list of the fraudProtectionProvider object and their properties. The following derived types are supported:
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: FraudProtectionProvider, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a new fraudProtectionProvider object. You can create one of the following subtypes that are derived from fraudProtectionProvider.
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
    
    def with_url(self,raw_url: str) -> FraudProtectionProvidersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FraudProtectionProvidersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FraudProtectionProvidersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FraudProtectionProvidersRequestBuilderGetQueryParameters():
        """
        Get a list of the fraudProtectionProvider object and their properties. The following derived types are supported:
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
    class FraudProtectionProvidersRequestBuilderGetRequestConfiguration(RequestConfiguration[FraudProtectionProvidersRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FraudProtectionProvidersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

