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
    from ...models.authentication_events_flow import AuthenticationEventsFlow
    from ...models.authentication_events_flow_collection_response import AuthenticationEventsFlowCollectionResponse
    from ...models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .graph_external_users_self_service_sign_up_events_flow.graph_external_users_self_service_sign_up_events_flow_request_builder import GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilder
    from .item.authentication_events_flow_item_request_builder import AuthenticationEventsFlowItemRequestBuilder

class AuthenticationEventsFlowsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the authenticationEventsFlows property of the microsoft.graph.identityContainer entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AuthenticationEventsFlowsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/authenticationEventsFlows{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_authentication_events_flow_id(self,authentication_events_flow_id: str) -> AuthenticationEventsFlowItemRequestBuilder:
        """
        Provides operations to manage the authenticationEventsFlows property of the microsoft.graph.identityContainer entity.
        param authentication_events_flow_id: The unique identifier of authenticationEventsFlow
        Returns: AuthenticationEventsFlowItemRequestBuilder
        """
        if authentication_events_flow_id is None:
            raise TypeError("authentication_events_flow_id cannot be null.")
        from .item.authentication_events_flow_item_request_builder import AuthenticationEventsFlowItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authenticationEventsFlow%2Did"] = authentication_events_flow_id
        return AuthenticationEventsFlowItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AuthenticationEventsFlowsRequestBuilderGetQueryParameters]] = None) -> Optional[AuthenticationEventsFlowCollectionResponse]:
        """
        Get a collection of authentication events policies that are derived from authenticationEventsFlow. The following derived subtypes are supported: - externalUsersSelfServiceSignupEventsFlow
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuthenticationEventsFlowCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/identitycontainer-list-authenticationeventsflows?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.authentication_events_flow_collection_response import AuthenticationEventsFlowCollectionResponse

        return await self.request_adapter.send_async(request_info, AuthenticationEventsFlowCollectionResponse, error_mapping)
    
    async def post(self,body: AuthenticationEventsFlow, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AuthenticationEventsFlow]:
        """
        Create a new authenticationEventsFlow object that is of the type specified in the request body. The following derived subtypes are supported:- externalUsersSelfServiceSignupEventsFlow object type.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuthenticationEventsFlow]
        Find more info here: https://learn.microsoft.com/graph/api/identitycontainer-post-authenticationeventsflows?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.authentication_events_flow import AuthenticationEventsFlow

        return await self.request_adapter.send_async(request_info, AuthenticationEventsFlow, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AuthenticationEventsFlowsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get a collection of authentication events policies that are derived from authenticationEventsFlow. The following derived subtypes are supported: - externalUsersSelfServiceSignupEventsFlow
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: AuthenticationEventsFlow, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a new authenticationEventsFlow object that is of the type specified in the request body. The following derived subtypes are supported:- externalUsersSelfServiceSignupEventsFlow object type.
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
    
    def with_url(self,raw_url: str) -> AuthenticationEventsFlowsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AuthenticationEventsFlowsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AuthenticationEventsFlowsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_external_users_self_service_sign_up_events_flow(self) -> GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilder:
        """
        Casts the previous resource to externalUsersSelfServiceSignUpEventsFlow.
        """
        from .graph_external_users_self_service_sign_up_events_flow.graph_external_users_self_service_sign_up_events_flow_request_builder import GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilder

        return GraphExternalUsersSelfServiceSignUpEventsFlowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AuthenticationEventsFlowsRequestBuilderGetQueryParameters():
        """
        Get a collection of authentication events policies that are derived from authenticationEventsFlow. The following derived subtypes are supported: - externalUsersSelfServiceSignupEventsFlow
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
    class AuthenticationEventsFlowsRequestBuilderGetRequestConfiguration(RequestConfiguration[AuthenticationEventsFlowsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AuthenticationEventsFlowsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

