from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models import identity_container
    from ..models.o_data_errors import o_data_error
    from .api_connectors import api_connectors_request_builder
    from .b2x_user_flows import b2x_user_flows_request_builder
    from .conditional_access import conditional_access_request_builder
    from .identity_providers import identity_providers_request_builder
    from .user_flow_attributes import user_flow_attributes_request_builder

class IdentityRequestBuilder():
    """
    Provides operations to manage the identityContainer singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new IdentityRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identity{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[IdentityRequestBuilderGetRequestConfiguration] = None) -> Optional[identity_container.IdentityContainer]:
        """
        Get identity
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[identity_container.IdentityContainer]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import identity_container

        return await self.request_adapter.send_async(request_info, identity_container.IdentityContainer, error_mapping)
    
    async def patch(self,body: Optional[identity_container.IdentityContainer] = None, request_configuration: Optional[IdentityRequestBuilderPatchRequestConfiguration] = None) -> Optional[identity_container.IdentityContainer]:
        """
        Update identity
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[identity_container.IdentityContainer]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import identity_container

        return await self.request_adapter.send_async(request_info, identity_container.IdentityContainer, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[IdentityRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get identity
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[identity_container.IdentityContainer] = None, request_configuration: Optional[IdentityRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update identity
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def api_connectors(self) -> api_connectors_request_builder.ApiConnectorsRequestBuilder:
        """
        Provides operations to manage the apiConnectors property of the microsoft.graph.identityContainer entity.
        """
        from .api_connectors import api_connectors_request_builder

        return api_connectors_request_builder.ApiConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def b2x_user_flows(self) -> b2x_user_flows_request_builder.B2xUserFlowsRequestBuilder:
        """
        Provides operations to manage the b2xUserFlows property of the microsoft.graph.identityContainer entity.
        """
        from .b2x_user_flows import b2x_user_flows_request_builder

        return b2x_user_flows_request_builder.B2xUserFlowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access(self) -> conditional_access_request_builder.ConditionalAccessRequestBuilder:
        """
        Provides operations to manage the conditionalAccess property of the microsoft.graph.identityContainer entity.
        """
        from .conditional_access import conditional_access_request_builder

        return conditional_access_request_builder.ConditionalAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_providers(self) -> identity_providers_request_builder.IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the identityProviders property of the microsoft.graph.identityContainer entity.
        """
        from .identity_providers import identity_providers_request_builder

        return identity_providers_request_builder.IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_flow_attributes(self) -> user_flow_attributes_request_builder.UserFlowAttributesRequestBuilder:
        """
        Provides operations to manage the userFlowAttributes property of the microsoft.graph.identityContainer entity.
        """
        from .user_flow_attributes import user_flow_attributes_request_builder

        return user_flow_attributes_request_builder.UserFlowAttributesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IdentityRequestBuilderGetQueryParameters():
        """
        Get identity
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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
    class IdentityRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[IdentityRequestBuilder.IdentityRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class IdentityRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

