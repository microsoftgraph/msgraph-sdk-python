from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

api_connectors_request_builder = lazy_import('msgraph.generated.identity.api_connectors.api_connectors_request_builder')
identity_api_connector_item_request_builder = lazy_import('msgraph.generated.identity.api_connectors.item.identity_api_connector_item_request_builder')
b2x_user_flows_request_builder = lazy_import('msgraph.generated.identity.b2x_user_flows.b2x_user_flows_request_builder')
b2x_identity_user_flow_item_request_builder = lazy_import('msgraph.generated.identity.b2x_user_flows.item.b2x_identity_user_flow_item_request_builder')
conditional_access_request_builder = lazy_import('msgraph.generated.identity.conditional_access.conditional_access_request_builder')
identity_providers_request_builder = lazy_import('msgraph.generated.identity.identity_providers.identity_providers_request_builder')
identity_provider_base_item_request_builder = lazy_import('msgraph.generated.identity.identity_providers.item.identity_provider_base_item_request_builder')
user_flow_attributes_request_builder = lazy_import('msgraph.generated.identity.user_flow_attributes.user_flow_attributes_request_builder')
identity_user_flow_attribute_item_request_builder = lazy_import('msgraph.generated.identity.user_flow_attributes.item.identity_user_flow_attribute_item_request_builder')
identity_container = lazy_import('msgraph.generated.models.identity_container')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class IdentityRequestBuilder():
    """
    Provides operations to manage the identityContainer singleton.
    """
    def api_connectors(self) -> api_connectors_request_builder.ApiConnectorsRequestBuilder:
        """
        Provides operations to manage the apiConnectors property of the microsoft.graph.identityContainer entity.
        """
        return api_connectors_request_builder.ApiConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def b2x_user_flows(self) -> b2x_user_flows_request_builder.B2xUserFlowsRequestBuilder:
        """
        Provides operations to manage the b2xUserFlows property of the microsoft.graph.identityContainer entity.
        """
        return b2x_user_flows_request_builder.B2xUserFlowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def conditional_access(self) -> conditional_access_request_builder.ConditionalAccessRequestBuilder:
        """
        Provides operations to manage the conditionalAccess property of the microsoft.graph.identityContainer entity.
        """
        return conditional_access_request_builder.ConditionalAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    def identity_providers(self) -> identity_providers_request_builder.IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the identityProviders property of the microsoft.graph.identityContainer entity.
        """
        return identity_providers_request_builder.IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def user_flow_attributes(self) -> user_flow_attributes_request_builder.UserFlowAttributesRequestBuilder:
        """
        Provides operations to manage the userFlowAttributes property of the microsoft.graph.identityContainer entity.
        """
        return user_flow_attributes_request_builder.UserFlowAttributesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def api_connectors_by_id(self,id: str) -> identity_api_connector_item_request_builder.IdentityApiConnectorItemRequestBuilder:
        """
        Provides operations to manage the apiConnectors property of the microsoft.graph.identityContainer entity.
        Args:
            id: Unique identifier of the item
        Returns: identity_api_connector_item_request_builder.IdentityApiConnectorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["identityApiConnector%2Did"] = id
        return identity_api_connector_item_request_builder.IdentityApiConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def b2x_user_flows_by_id(self,id: str) -> b2x_identity_user_flow_item_request_builder.B2xIdentityUserFlowItemRequestBuilder:
        """
        Provides operations to manage the b2xUserFlows property of the microsoft.graph.identityContainer entity.
        Args:
            id: Unique identifier of the item
        Returns: b2x_identity_user_flow_item_request_builder.B2xIdentityUserFlowItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["b2xIdentityUserFlow%2Did"] = id
        return b2x_identity_user_flow_item_request_builder.B2xIdentityUserFlowItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new IdentityRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identity{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[IdentityRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[identity_container.IdentityContainer] = None, request_configuration: Optional[IdentityRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update identity
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def get(self,request_configuration: Optional[IdentityRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[identity_container.IdentityContainer]:
        """
        Get identity
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[identity_container.IdentityContainer]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, identity_container.IdentityContainer, response_handler, error_mapping)
    
    def identity_providers_by_id(self,id: str) -> identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder:
        """
        Provides operations to manage the identityProviders property of the microsoft.graph.identityContainer entity.
        Args:
            id: Unique identifier of the item
        Returns: identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["identityProviderBase%2Did"] = id
        return identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[identity_container.IdentityContainer] = None, request_configuration: Optional[IdentityRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[identity_container.IdentityContainer]:
        """
        Update identity
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[identity_container.IdentityContainer]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, identity_container.IdentityContainer, response_handler, error_mapping)
    
    def user_flow_attributes_by_id(self,id: str) -> identity_user_flow_attribute_item_request_builder.IdentityUserFlowAttributeItemRequestBuilder:
        """
        Provides operations to manage the userFlowAttributes property of the microsoft.graph.identityContainer entity.
        Args:
            id: Unique identifier of the item
        Returns: identity_user_flow_attribute_item_request_builder.IdentityUserFlowAttributeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["identityUserFlowAttribute%2Did"] = id
        return identity_user_flow_attribute_item_request_builder.IdentityUserFlowAttributeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class IdentityRequestBuilderGetQueryParameters():
        """
        Get identity
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class IdentityRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

