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
    from ...models.multi_tenant_organization import MultiTenantOrganization
    from ...models.o_data_errors.o_data_error import ODataError
    from .join_request.join_request_request_builder import JoinRequestRequestBuilder
    from .tenants.tenants_request_builder import TenantsRequestBuilder

class MultiTenantOrganizationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the multiTenantOrganization property of the microsoft.graph.tenantRelationship entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MultiTenantOrganizationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/tenantRelationships/multiTenantOrganization{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MultiTenantOrganizationRequestBuilderGetQueryParameters]] = None) -> Optional[MultiTenantOrganization]:
        """
        Get properties of the multitenant organization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MultiTenantOrganization]
        Find more info here: https://learn.microsoft.com/graph/api/multitenantorganization-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.multi_tenant_organization import MultiTenantOrganization

        return await self.request_adapter.send_async(request_info, MultiTenantOrganization, error_mapping)
    
    async def put(self,body: MultiTenantOrganization, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[MultiTenantOrganization]:
        """
        Create a new multitenant organization. By default, the creator tenant becomes an owner tenant upon successful creation. Only owner tenants can manage a multitenant organization.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MultiTenantOrganization]
        Find more info here: https://learn.microsoft.com/graph/api/tenantrelationship-put-multitenantorganization?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.multi_tenant_organization import MultiTenantOrganization

        return await self.request_adapter.send_async(request_info, MultiTenantOrganization, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MultiTenantOrganizationRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get properties of the multitenant organization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: MultiTenantOrganization, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a new multitenant organization. By default, the creator tenant becomes an owner tenant upon successful creation. Only owner tenants can manage a multitenant organization.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> MultiTenantOrganizationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MultiTenantOrganizationRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return MultiTenantOrganizationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def join_request(self) -> JoinRequestRequestBuilder:
        """
        Provides operations to manage the joinRequest property of the microsoft.graph.multiTenantOrganization entity.
        """
        from .join_request.join_request_request_builder import JoinRequestRequestBuilder

        return JoinRequestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tenants(self) -> TenantsRequestBuilder:
        """
        Provides operations to manage the tenants property of the microsoft.graph.multiTenantOrganization entity.
        """
        from .tenants.tenants_request_builder import TenantsRequestBuilder

        return TenantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MultiTenantOrganizationRequestBuilderGetQueryParameters():
        """
        Get properties of the multitenant organization.
        """
        def get_query_parameter(self,original_name: str) -> str:
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

    
    @dataclass
    class MultiTenantOrganizationRequestBuilderGetRequestConfiguration(RequestConfiguration[MultiTenantOrganizationRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MultiTenantOrganizationRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
