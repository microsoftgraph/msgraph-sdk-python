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
    from ..models.identity_container import IdentityContainer
    from ..models.o_data_errors.o_data_error import ODataError
    from .api_connectors.api_connectors_request_builder import ApiConnectorsRequestBuilder
    from .authentication_events_flows.authentication_events_flows_request_builder import AuthenticationEventsFlowsRequestBuilder
    from .authentication_event_listeners.authentication_event_listeners_request_builder import AuthenticationEventListenersRequestBuilder
    from .b2x_user_flows.b2x_user_flows_request_builder import B2xUserFlowsRequestBuilder
    from .conditional_access.conditional_access_request_builder import ConditionalAccessRequestBuilder
    from .custom_authentication_extensions.custom_authentication_extensions_request_builder import CustomAuthenticationExtensionsRequestBuilder
    from .identity_providers.identity_providers_request_builder import IdentityProvidersRequestBuilder
    from .risk_prevention.risk_prevention_request_builder import RiskPreventionRequestBuilder
    from .user_flow_attributes.user_flow_attributes_request_builder import UserFlowAttributesRequestBuilder

class IdentityRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the identityContainer singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IdentityRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IdentityRequestBuilderGetQueryParameters]] = None) -> Optional[IdentityContainer]:
        """
        Get identity
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IdentityContainer]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.identity_container import IdentityContainer

        return await self.request_adapter.send_async(request_info, IdentityContainer, error_mapping)
    
    async def patch(self,body: IdentityContainer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[IdentityContainer]:
        """
        Update identity
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IdentityContainer]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.identity_container import IdentityContainer

        return await self.request_adapter.send_async(request_info, IdentityContainer, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IdentityRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get identity
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: IdentityContainer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update identity
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> IdentityRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IdentityRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IdentityRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def api_connectors(self) -> ApiConnectorsRequestBuilder:
        """
        Provides operations to manage the apiConnectors property of the microsoft.graph.identityContainer entity.
        """
        from .api_connectors.api_connectors_request_builder import ApiConnectorsRequestBuilder

        return ApiConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_event_listeners(self) -> AuthenticationEventListenersRequestBuilder:
        """
        Provides operations to manage the authenticationEventListeners property of the microsoft.graph.identityContainer entity.
        """
        from .authentication_event_listeners.authentication_event_listeners_request_builder import AuthenticationEventListenersRequestBuilder

        return AuthenticationEventListenersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_events_flows(self) -> AuthenticationEventsFlowsRequestBuilder:
        """
        Provides operations to manage the authenticationEventsFlows property of the microsoft.graph.identityContainer entity.
        """
        from .authentication_events_flows.authentication_events_flows_request_builder import AuthenticationEventsFlowsRequestBuilder

        return AuthenticationEventsFlowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def b2x_user_flows(self) -> B2xUserFlowsRequestBuilder:
        """
        Provides operations to manage the b2xUserFlows property of the microsoft.graph.identityContainer entity.
        """
        from .b2x_user_flows.b2x_user_flows_request_builder import B2xUserFlowsRequestBuilder

        return B2xUserFlowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access(self) -> ConditionalAccessRequestBuilder:
        """
        The conditionalAccess property
        """
        from .conditional_access.conditional_access_request_builder import ConditionalAccessRequestBuilder

        return ConditionalAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_authentication_extensions(self) -> CustomAuthenticationExtensionsRequestBuilder:
        """
        Provides operations to manage the customAuthenticationExtensions property of the microsoft.graph.identityContainer entity.
        """
        from .custom_authentication_extensions.custom_authentication_extensions_request_builder import CustomAuthenticationExtensionsRequestBuilder

        return CustomAuthenticationExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_providers(self) -> IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the identityProviders property of the microsoft.graph.identityContainer entity.
        """
        from .identity_providers.identity_providers_request_builder import IdentityProvidersRequestBuilder

        return IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def risk_prevention(self) -> RiskPreventionRequestBuilder:
        """
        Provides operations to manage the riskPrevention property of the microsoft.graph.identityContainer entity.
        """
        from .risk_prevention.risk_prevention_request_builder import RiskPreventionRequestBuilder

        return RiskPreventionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_flow_attributes(self) -> UserFlowAttributesRequestBuilder:
        """
        Provides operations to manage the userFlowAttributes property of the microsoft.graph.identityContainer entity.
        """
        from .user_flow_attributes.user_flow_attributes_request_builder import UserFlowAttributesRequestBuilder

        return UserFlowAttributesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IdentityRequestBuilderGetQueryParameters():
        """
        Get identity
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
    class IdentityRequestBuilderGetRequestConfiguration(RequestConfiguration[IdentityRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class IdentityRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

