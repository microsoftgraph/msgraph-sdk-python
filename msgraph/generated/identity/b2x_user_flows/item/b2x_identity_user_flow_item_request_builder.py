from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.b2x_identity_user_flow import B2xIdentityUserFlow
    from ....models.o_data_errors.o_data_error import ODataError
    from .api_connector_configuration.api_connector_configuration_request_builder import ApiConnectorConfigurationRequestBuilder
    from .identity_providers.identity_providers_request_builder import IdentityProvidersRequestBuilder
    from .languages.languages_request_builder import LanguagesRequestBuilder
    from .user_attribute_assignments.user_attribute_assignments_request_builder import UserAttributeAssignmentsRequestBuilder
    from .user_flow_identity_providers.user_flow_identity_providers_request_builder import UserFlowIdentityProvidersRequestBuilder

class B2xIdentityUserFlowItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the b2xUserFlows property of the microsoft.graph.identityContainer entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new B2xIdentityUserFlowItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/b2xUserFlows/{b2xIdentityUserFlow%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[B2xIdentityUserFlowItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a b2xIdentityUserFlow object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/b2xidentityuserflow-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[B2xIdentityUserFlowItemRequestBuilderGetRequestConfiguration] = None) -> Optional[B2xIdentityUserFlow]:
        """
        Retrieve the properties and relationships of a b2xIdentityUserFlow object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[B2xIdentityUserFlow]
        Find more info here: https://learn.microsoft.com/graph/api/b2xidentityuserflow-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.b2x_identity_user_flow import B2xIdentityUserFlow

        return await self.request_adapter.send_async(request_info, B2xIdentityUserFlow, error_mapping)
    
    async def patch(self,body: Optional[B2xIdentityUserFlow] = None, request_configuration: Optional[B2xIdentityUserFlowItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[B2xIdentityUserFlow]:
        """
        Update the navigation property b2xUserFlows in identity
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[B2xIdentityUserFlow]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.b2x_identity_user_flow import B2xIdentityUserFlow

        return await self.request_adapter.send_async(request_info, B2xIdentityUserFlow, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[B2xIdentityUserFlowItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a b2xIdentityUserFlow object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[B2xIdentityUserFlowItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a b2xIdentityUserFlow object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[B2xIdentityUserFlow] = None, request_configuration: Optional[B2xIdentityUserFlowItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property b2xUserFlows in identity
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> B2xIdentityUserFlowItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: B2xIdentityUserFlowItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return B2xIdentityUserFlowItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def api_connector_configuration(self) -> ApiConnectorConfigurationRequestBuilder:
        """
        The apiConnectorConfiguration property
        """
        from .api_connector_configuration.api_connector_configuration_request_builder import ApiConnectorConfigurationRequestBuilder

        return ApiConnectorConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def identity_providers(self) -> IdentityProvidersRequestBuilder:
        """
        Provides operations to manage the identityProviders property of the microsoft.graph.b2xIdentityUserFlow entity.
        """
        from .identity_providers.identity_providers_request_builder import IdentityProvidersRequestBuilder

        return IdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def languages(self) -> LanguagesRequestBuilder:
        """
        Provides operations to manage the languages property of the microsoft.graph.b2xIdentityUserFlow entity.
        """
        from .languages.languages_request_builder import LanguagesRequestBuilder

        return LanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_attribute_assignments(self) -> UserAttributeAssignmentsRequestBuilder:
        """
        Provides operations to manage the userAttributeAssignments property of the microsoft.graph.b2xIdentityUserFlow entity.
        """
        from .user_attribute_assignments.user_attribute_assignments_request_builder import UserAttributeAssignmentsRequestBuilder

        return UserAttributeAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_flow_identity_providers(self) -> UserFlowIdentityProvidersRequestBuilder:
        """
        Provides operations to manage the userFlowIdentityProviders property of the microsoft.graph.b2xIdentityUserFlow entity.
        """
        from .user_flow_identity_providers.user_flow_identity_providers_request_builder import UserFlowIdentityProvidersRequestBuilder

        return UserFlowIdentityProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class B2xIdentityUserFlowItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class B2xIdentityUserFlowItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a b2xIdentityUserFlow object.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class B2xIdentityUserFlowItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[B2xIdentityUserFlowItemRequestBuilder.B2xIdentityUserFlowItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class B2xIdentityUserFlowItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

