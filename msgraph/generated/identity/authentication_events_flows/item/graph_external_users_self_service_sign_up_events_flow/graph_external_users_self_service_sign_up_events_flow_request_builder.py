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
    from .....models.external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
    from .....models.o_data_errors.o_data_error import ODataError
    from .conditions.conditions_request_builder import ConditionsRequestBuilder
    from .on_attribute_collection.on_attribute_collection_request_builder import OnAttributeCollectionRequestBuilder
    from .on_authentication_method_load_start.on_authentication_method_load_start_request_builder import OnAuthenticationMethodLoadStartRequestBuilder

class GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilder(BaseRequestBuilder):
    """
    Casts the previous resource to externalUsersSelfServiceSignUpEventsFlow.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows/{authenticationEventsFlow%2Did}/graph.externalUsersSelfServiceSignUpEventsFlow{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilderGetQueryParameters]] = None) -> Optional[ExternalUsersSelfServiceSignUpEventsFlow]:
        """
        Get the item of type microsoft.graph.authenticationEventsFlow as microsoft.graph.externalUsersSelfServiceSignUpEventsFlow
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ExternalUsersSelfServiceSignUpEventsFlow]
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
        from .....models.external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

        return await self.request_adapter.send_async(request_info, ExternalUsersSelfServiceSignUpEventsFlow, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the item of type microsoft.graph.authenticationEventsFlow as microsoft.graph.externalUsersSelfServiceSignUpEventsFlow
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def conditions(self) -> ConditionsRequestBuilder:
        """
        The conditions property
        """
        from .conditions.conditions_request_builder import ConditionsRequestBuilder

        return ConditionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def on_attribute_collection(self) -> OnAttributeCollectionRequestBuilder:
        """
        The onAttributeCollection property
        """
        from .on_attribute_collection.on_attribute_collection_request_builder import OnAttributeCollectionRequestBuilder

        return OnAttributeCollectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def on_authentication_method_load_start(self) -> OnAuthenticationMethodLoadStartRequestBuilder:
        """
        The onAuthenticationMethodLoadStart property
        """
        from .on_authentication_method_load_start.on_authentication_method_load_start_request_builder import OnAuthenticationMethodLoadStartRequestBuilder

        return OnAuthenticationMethodLoadStartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilderGetQueryParameters():
        """
        Get the item of type microsoft.graph.authenticationEventsFlow as microsoft.graph.externalUsersSelfServiceSignUpEventsFlow
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
    class GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilderGetRequestConfiguration(RequestConfiguration[GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

