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
    from .......models.on_authentication_method_load_start_external_users_self_service_sign_up import OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp
    from .......models.o_data_errors.o_data_error import ODataError
    from .identity_providers.identity_providers_request_builder import IdentityProvidersRequestBuilder

class GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder(BaseRequestBuilder):
    """
    Casts the previous resource to onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow/onAuthenticationMethodLoadStart/graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp]:
        """
        Get the item of type microsoft.graph.onAuthenticationMethodLoadStartHandler as microsoft.graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.on_authentication_method_load_start_external_users_self_service_sign_up import OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp

        return await self.request_adapter.send_async(request_info, OnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Get the item of type microsoft.graph.onAuthenticationMethodLoadStartHandler as microsoft.graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def identity_providers(self) -> IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the identityProviders property of the microsoft.graph.onAuthenticationMethodLoadStartExternalUsersSelfServiceSignUp entity.
        """
        from .identity_providers.identity_providers_request_builder import IdentityProvidersRequestBuilder

        return IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GraphOnAuthenticationMethodLoadStartExternalUsersSelfServiceSignUpRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

