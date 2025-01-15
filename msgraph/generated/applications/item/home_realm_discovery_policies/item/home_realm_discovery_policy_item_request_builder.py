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
    from .....models.home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .....models.o_data_errors.o_data_error import ODataError

class HomeRealmDiscoveryPolicyItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the homeRealmDiscoveryPolicies property of the microsoft.graph.application entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new HomeRealmDiscoveryPolicyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/homeRealmDiscoveryPolicies/{homeRealmDiscoveryPolicy%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[HomeRealmDiscoveryPolicyItemRequestBuilderGetQueryParameters]] = None) -> Optional[HomeRealmDiscoveryPolicy]:
        """
        Get homeRealmDiscoveryPolicies from applications
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[HomeRealmDiscoveryPolicy]
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
        from .....models.home_realm_discovery_policy import HomeRealmDiscoveryPolicy

        return await self.request_adapter.send_async(request_info, HomeRealmDiscoveryPolicy, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[HomeRealmDiscoveryPolicyItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get homeRealmDiscoveryPolicies from applications
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> HomeRealmDiscoveryPolicyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: HomeRealmDiscoveryPolicyItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return HomeRealmDiscoveryPolicyItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class HomeRealmDiscoveryPolicyItemRequestBuilderGetQueryParameters():
        """
        Get homeRealmDiscoveryPolicies from applications
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class HomeRealmDiscoveryPolicyItemRequestBuilderGetRequestConfiguration(RequestConfiguration[HomeRealmDiscoveryPolicyItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

