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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
    from .app_health_metrics.app_health_metrics_request_builder import AppHealthMetricsRequestBuilder
    from .battery_health_metrics.battery_health_metrics_request_builder import BatteryHealthMetricsRequestBuilder
    from .best_practices_metrics.best_practices_metrics_request_builder import BestPracticesMetricsRequestBuilder
    from .device_boot_performance_metrics.device_boot_performance_metrics_request_builder import DeviceBootPerformanceMetricsRequestBuilder
    from .reboot_analytics_metrics.reboot_analytics_metrics_request_builder import RebootAnalyticsMetricsRequestBuilder
    from .resource_performance_metrics.resource_performance_metrics_request_builder import ResourcePerformanceMetricsRequestBuilder
    from .work_from_anywhere_metrics.work_from_anywhere_metrics_request_builder import WorkFromAnywhereMetricsRequestBuilder

class UserExperienceAnalyticsBaselineItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the userExperienceAnalyticsBaselines property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UserExperienceAnalyticsBaselineItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/userExperienceAnalyticsBaselines/{userExperienceAnalyticsBaseline%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property userExperienceAnalyticsBaselines for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
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
    
    async def get(self,request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderGetRequestConfiguration] = None) -> Optional[UserExperienceAnalyticsBaseline]:
        """
        User experience analytics baselines
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserExperienceAnalyticsBaseline]
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
        from ....models.user_experience_analytics_baseline import UserExperienceAnalyticsBaseline

        return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsBaseline, error_mapping)
    
    async def patch(self,body: Optional[UserExperienceAnalyticsBaseline] = None, request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[UserExperienceAnalyticsBaseline]:
        """
        Update the navigation property userExperienceAnalyticsBaselines in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserExperienceAnalyticsBaseline]
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
        from ....models.user_experience_analytics_baseline import UserExperienceAnalyticsBaseline

        return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsBaseline, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property userExperienceAnalyticsBaselines for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        User experience analytics baselines
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
    
    def to_patch_request_information(self,body: Optional[UserExperienceAnalyticsBaseline] = None, request_configuration: Optional[UserExperienceAnalyticsBaselineItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property userExperienceAnalyticsBaselines in deviceManagement
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
    
    def with_url(self,raw_url: Optional[str] = None) -> UserExperienceAnalyticsBaselineItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UserExperienceAnalyticsBaselineItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return UserExperienceAnalyticsBaselineItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def app_health_metrics(self) -> AppHealthMetricsRequestBuilder:
        """
        Provides operations to manage the appHealthMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        from .app_health_metrics.app_health_metrics_request_builder import AppHealthMetricsRequestBuilder

        return AppHealthMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def battery_health_metrics(self) -> BatteryHealthMetricsRequestBuilder:
        """
        Provides operations to manage the batteryHealthMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        from .battery_health_metrics.battery_health_metrics_request_builder import BatteryHealthMetricsRequestBuilder

        return BatteryHealthMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def best_practices_metrics(self) -> BestPracticesMetricsRequestBuilder:
        """
        Provides operations to manage the bestPracticesMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        from .best_practices_metrics.best_practices_metrics_request_builder import BestPracticesMetricsRequestBuilder

        return BestPracticesMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_boot_performance_metrics(self) -> DeviceBootPerformanceMetricsRequestBuilder:
        """
        Provides operations to manage the deviceBootPerformanceMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        from .device_boot_performance_metrics.device_boot_performance_metrics_request_builder import DeviceBootPerformanceMetricsRequestBuilder

        return DeviceBootPerformanceMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot_analytics_metrics(self) -> RebootAnalyticsMetricsRequestBuilder:
        """
        Provides operations to manage the rebootAnalyticsMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        from .reboot_analytics_metrics.reboot_analytics_metrics_request_builder import RebootAnalyticsMetricsRequestBuilder

        return RebootAnalyticsMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_performance_metrics(self) -> ResourcePerformanceMetricsRequestBuilder:
        """
        Provides operations to manage the resourcePerformanceMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        from .resource_performance_metrics.resource_performance_metrics_request_builder import ResourcePerformanceMetricsRequestBuilder

        return ResourcePerformanceMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def work_from_anywhere_metrics(self) -> WorkFromAnywhereMetricsRequestBuilder:
        """
        Provides operations to manage the workFromAnywhereMetrics property of the microsoft.graph.userExperienceAnalyticsBaseline entity.
        """
        from .work_from_anywhere_metrics.work_from_anywhere_metrics_request_builder import WorkFromAnywhereMetricsRequestBuilder

        return WorkFromAnywhereMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class UserExperienceAnalyticsBaselineItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class UserExperienceAnalyticsBaselineItemRequestBuilderGetQueryParameters():
        """
        User experience analytics baselines
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
    class UserExperienceAnalyticsBaselineItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[UserExperienceAnalyticsBaselineItemRequestBuilder.UserExperienceAnalyticsBaselineItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class UserExperienceAnalyticsBaselineItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

