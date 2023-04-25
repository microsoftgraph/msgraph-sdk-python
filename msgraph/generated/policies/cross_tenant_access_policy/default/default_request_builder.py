from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import cross_tenant_access_policy_configuration_default
    from ....models.o_data_errors import o_data_error
    from .reset_to_system_default import reset_to_system_default_request_builder

class DefaultRequestBuilder():
    """
    Provides operations to manage the default property of the microsoft.graph.crossTenantAccessPolicy entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DefaultRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/policies/crossTenantAccessPolicy/default{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[DefaultRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property default for policies
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[DefaultRequestBuilderGetRequestConfiguration] = None) -> Optional[cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault]:
        """
        Defines the default configuration for how your organization interacts with external Azure Active Directory organizations.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import cross_tenant_access_policy_configuration_default

        return await self.request_adapter.send_async(request_info, cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault, error_mapping)
    
    async def patch(self,body: Optional[cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault] = None, request_configuration: Optional[DefaultRequestBuilderPatchRequestConfiguration] = None) -> Optional[cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault]:
        """
        Update the navigation property default in policies
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import cross_tenant_access_policy_configuration_default

        return await self.request_adapter.send_async(request_info, cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DefaultRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property default for policies
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[DefaultRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Defines the default configuration for how your organization interacts with external Azure Active Directory organizations.
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
    
    def to_patch_request_information(self,body: Optional[cross_tenant_access_policy_configuration_default.CrossTenantAccessPolicyConfigurationDefault] = None, request_configuration: Optional[DefaultRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property default in policies
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
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
    def reset_to_system_default(self) -> reset_to_system_default_request_builder.ResetToSystemDefaultRequestBuilder:
        """
        Provides operations to call the resetToSystemDefault method.
        """
        from .reset_to_system_default import reset_to_system_default_request_builder

        return reset_to_system_default_request_builder.ResetToSystemDefaultRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DefaultRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DefaultRequestBuilderGetQueryParameters():
        """
        Defines the default configuration for how your organization interacts with external Azure Active Directory organizations.
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class DefaultRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DefaultRequestBuilder.DefaultRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DefaultRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

