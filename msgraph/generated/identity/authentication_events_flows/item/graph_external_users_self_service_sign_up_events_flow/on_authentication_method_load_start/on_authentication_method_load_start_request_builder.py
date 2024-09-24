from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler
    from ......models.o_data_errors.o_data_error import ODataError
    from .graph_on_authentication_method_load_start_external_users_self_service_sign_up.graph_on_authentication_method_load_start_external_users_self_service_sign_up_request_builder import GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder

class OnAuthenticationMethodLoadStartRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /identity/authenticationEventsFlows/{authenticationEventsFlow-id}/graph.externalUsersSelfServiceSignUpEventsFlow/onAuthenticationMethodLoadStart
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new OnAuthenticationMethodLoadStartRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow/onAuthenticationMethodLoadStart{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[OnAuthenticationMethodLoadStartRequestBuilderGetQueryParameters]] = None) -> Optional[OnAuthenticationMethodLoadStartHandler]:
        """
        Required. The configuration for what to invoke when authentication methods are ready to be presented to the user. Must have at least one identity provider linked.  Supports $filter (eq). See support for filtering on user flows for syntax information.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnAuthenticationMethodLoadStartHandler]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.on_authentication_method_load_start_handler import OnAuthenticationMethodLoadStartHandler

        return await self.request_adapter.send_async(request_info, OnAuthenticationMethodLoadStartHandler, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[OnAuthenticationMethodLoadStartRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Required. The configuration for what to invoke when authentication methods are ready to be presented to the user. Must have at least one identity provider linked.  Supports $filter (eq). See support for filtering on user flows for syntax information.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> OnAuthenticationMethodLoadStartRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OnAuthenticationMethodLoadStartRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OnAuthenticationMethodLoadStartRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def graph_on_authentication_method_load_start_external_users_self_service_sign_up(self) -> GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder:
        """
        Casts the previous resource to onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp.
        """
        from .graph_on_authentication_method_load_start_external_users_self_service_sign_up.graph_on_authentication_method_load_start_external_users_self_service_sign_up_request_builder import GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder

        return GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OnAuthenticationMethodLoadStartRequestBuilderGetQueryParameters():
        """
        Required. The configuration for what to invoke when authentication methods are ready to be presented to the user. Must have at least one identity provider linked.  Supports $filter (eq). See support for filtering on user flows for syntax information.
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class OnAuthenticationMethodLoadStartRequestBuilderGetRequestConfiguration(RequestConfiguration[OnAuthenticationMethodLoadStartRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

