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
    from .....models.related_tenant import RelatedTenant
    from .app_b2_b_sign_in_activity_metrics.app_b2_b_sign_in_activity_metrics_request_builder import AppB2BSignInActivityMetricsRequestBuilder
    from .b2_b_registration_metrics.b2_b_registration_metrics_request_builder import B2BRegistrationMetricsRequestBuilder
    from .b2_b_sign_in_activity_metrics.b2_b_sign_in_activity_metrics_request_builder import B2BSignInActivityMetricsRequestBuilder
    from .billing_metrics.billing_metrics_request_builder import BillingMetricsRequestBuilder
    from .multi_tenant_application_metrics.multi_tenant_application_metrics_request_builder import MultiTenantApplicationMetricsRequestBuilder

class RelatedTenantItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the relatedTenants property of the microsoft.graph.tenantGovernance entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RelatedTenantItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/directory/tenantGovernance/relatedTenants/{relatedTenant%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property relatedTenants for directory
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[RelatedTenantItemRequestBuilderGetQueryParameters]] = None) -> Optional[RelatedTenant]:
        """
        Get relatedTenants from directory
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RelatedTenant]
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
        from .....models.related_tenant import RelatedTenant

        return await self.request_adapter.send_async(request_info, RelatedTenant, error_mapping)
    
    async def patch(self,body: RelatedTenant, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RelatedTenant]:
        """
        Update the navigation property relatedTenants in directory
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RelatedTenant]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.related_tenant import RelatedTenant

        return await self.request_adapter.send_async(request_info, RelatedTenant, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property relatedTenants for directory
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[RelatedTenantItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get relatedTenants from directory
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: RelatedTenant, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property relatedTenants in directory
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
    
    def with_url(self,raw_url: str) -> RelatedTenantItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RelatedTenantItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RelatedTenantItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def app_b2_b_sign_in_activity_metrics(self) -> AppB2BSignInActivityMetricsRequestBuilder:
        """
        Provides operations to manage the appB2BSignInActivityMetrics property of the microsoft.graph.relatedTenant entity.
        """
        from .app_b2_b_sign_in_activity_metrics.app_b2_b_sign_in_activity_metrics_request_builder import AppB2BSignInActivityMetricsRequestBuilder

        return AppB2BSignInActivityMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def b2_b_registration_metrics(self) -> B2BRegistrationMetricsRequestBuilder:
        """
        Provides operations to manage the b2BRegistrationMetrics property of the microsoft.graph.relatedTenant entity.
        """
        from .b2_b_registration_metrics.b2_b_registration_metrics_request_builder import B2BRegistrationMetricsRequestBuilder

        return B2BRegistrationMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def b2_b_sign_in_activity_metrics(self) -> B2BSignInActivityMetricsRequestBuilder:
        """
        Provides operations to manage the b2BSignInActivityMetrics property of the microsoft.graph.relatedTenant entity.
        """
        from .b2_b_sign_in_activity_metrics.b2_b_sign_in_activity_metrics_request_builder import B2BSignInActivityMetricsRequestBuilder

        return B2BSignInActivityMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def billing_metrics(self) -> BillingMetricsRequestBuilder:
        """
        Provides operations to manage the billingMetrics property of the microsoft.graph.relatedTenant entity.
        """
        from .billing_metrics.billing_metrics_request_builder import BillingMetricsRequestBuilder

        return BillingMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def multi_tenant_application_metrics(self) -> MultiTenantApplicationMetricsRequestBuilder:
        """
        Provides operations to manage the multiTenantApplicationMetrics property of the microsoft.graph.relatedTenant entity.
        """
        from .multi_tenant_application_metrics.multi_tenant_application_metrics_request_builder import MultiTenantApplicationMetricsRequestBuilder

        return MultiTenantApplicationMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RelatedTenantItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RelatedTenantItemRequestBuilderGetQueryParameters():
        """
        Get relatedTenants from directory
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
    class RelatedTenantItemRequestBuilderGetRequestConfiguration(RequestConfiguration[RelatedTenantItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RelatedTenantItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

