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
    from .....models.user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration
    from .post_attribute_collection.post_attribute_collection_request_builder import PostAttributeCollectionRequestBuilder
    from .post_federation_signup.post_federation_signup_request_builder import PostFederationSignupRequestBuilder

class ApiConnectorConfigurationRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /identity/b2xUserFlows/{b2xIdentityUserFlow-id}/apiConnectorConfiguration
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ApiConnectorConfigurationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/b2xUserFlows/{b2xIdentityUserFlow%2Did}/apiConnectorConfiguration{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ApiConnectorConfigurationRequestBuilderGetQueryParameters]] = None) -> Optional[UserFlowApiConnectorConfiguration]:
        """
        Get the apiConnectorConfiguration property in a b2xIdentityUserFlow to detail the API connectors enabled for the user flow.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserFlowApiConnectorConfiguration]
        Find more info here: https://learn.microsoft.com/graph/api/b2xidentityuserflow-get-apiconnectorconfiguration?view=graph-rest-1.0
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
        from .....models.user_flow_api_connector_configuration import UserFlowApiConnectorConfiguration

        return await self.request_adapter.send_async(request_info, UserFlowApiConnectorConfiguration, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ApiConnectorConfigurationRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the apiConnectorConfiguration property in a b2xIdentityUserFlow to detail the API connectors enabled for the user flow.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ApiConnectorConfigurationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ApiConnectorConfigurationRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ApiConnectorConfigurationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def post_attribute_collection(self) -> PostAttributeCollectionRequestBuilder:
        """
        Provides operations to manage the postAttributeCollection property of the microsoft.graph.userFlowApiConnectorConfiguration entity.
        """
        from .post_attribute_collection.post_attribute_collection_request_builder import PostAttributeCollectionRequestBuilder

        return PostAttributeCollectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def post_federation_signup(self) -> PostFederationSignupRequestBuilder:
        """
        Provides operations to manage the postFederationSignup property of the microsoft.graph.userFlowApiConnectorConfiguration entity.
        """
        from .post_federation_signup.post_federation_signup_request_builder import PostFederationSignupRequestBuilder

        return PostFederationSignupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ApiConnectorConfigurationRequestBuilderGetQueryParameters():
        """
        Get the apiConnectorConfiguration property in a b2xIdentityUserFlow to detail the API connectors enabled for the user flow.
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
    class ApiConnectorConfigurationRequestBuilderGetRequestConfiguration(RequestConfiguration[ApiConnectorConfigurationRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

