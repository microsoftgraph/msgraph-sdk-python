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
    from ...models.configuration_management import ConfigurationManagement
    from ...models.o_data_errors.o_data_error import ODataError
    from .configuration_drifts.configuration_drifts_request_builder import ConfigurationDriftsRequestBuilder
    from .configuration_monitoring_results.configuration_monitoring_results_request_builder import ConfigurationMonitoringResultsRequestBuilder
    from .configuration_monitors.configuration_monitors_request_builder import ConfigurationMonitorsRequestBuilder
    from .configuration_snapshots.configuration_snapshots_request_builder import ConfigurationSnapshotsRequestBuilder
    from .configuration_snapshot_jobs.configuration_snapshot_jobs_request_builder import ConfigurationSnapshotJobsRequestBuilder

class ConfigurationManagementRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the configurationManagement property of the microsoft.graph.admin entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConfigurationManagementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin/configurationManagement{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property configurationManagement for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ConfigurationManagementRequestBuilderGetQueryParameters]] = None) -> Optional[ConfigurationManagement]:
        """
        A container for Tenant Configuration Management (TCM) resources. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConfigurationManagement]
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
        from ...models.configuration_management import ConfigurationManagement

        return await self.request_adapter.send_async(request_info, ConfigurationManagement, error_mapping)
    
    async def patch(self,body: ConfigurationManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ConfigurationManagement]:
        """
        Update the navigation property configurationManagement in admin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConfigurationManagement]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.configuration_management import ConfigurationManagement

        return await self.request_adapter.send_async(request_info, ConfigurationManagement, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property configurationManagement for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ConfigurationManagementRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        A container for Tenant Configuration Management (TCM) resources. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ConfigurationManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property configurationManagement in admin
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
    
    def with_url(self,raw_url: str) -> ConfigurationManagementRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConfigurationManagementRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ConfigurationManagementRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def configuration_drifts(self) -> ConfigurationDriftsRequestBuilder:
        """
        Provides operations to manage the configurationDrifts property of the microsoft.graph.configurationManagement entity.
        """
        from .configuration_drifts.configuration_drifts_request_builder import ConfigurationDriftsRequestBuilder

        return ConfigurationDriftsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_monitoring_results(self) -> ConfigurationMonitoringResultsRequestBuilder:
        """
        Provides operations to manage the configurationMonitoringResults property of the microsoft.graph.configurationManagement entity.
        """
        from .configuration_monitoring_results.configuration_monitoring_results_request_builder import ConfigurationMonitoringResultsRequestBuilder

        return ConfigurationMonitoringResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_monitors(self) -> ConfigurationMonitorsRequestBuilder:
        """
        Provides operations to manage the configurationMonitors property of the microsoft.graph.configurationManagement entity.
        """
        from .configuration_monitors.configuration_monitors_request_builder import ConfigurationMonitorsRequestBuilder

        return ConfigurationMonitorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_snapshot_jobs(self) -> ConfigurationSnapshotJobsRequestBuilder:
        """
        Provides operations to manage the configurationSnapshotJobs property of the microsoft.graph.configurationManagement entity.
        """
        from .configuration_snapshot_jobs.configuration_snapshot_jobs_request_builder import ConfigurationSnapshotJobsRequestBuilder

        return ConfigurationSnapshotJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def configuration_snapshots(self) -> ConfigurationSnapshotsRequestBuilder:
        """
        Provides operations to manage the configurationSnapshots property of the microsoft.graph.configurationManagement entity.
        """
        from .configuration_snapshots.configuration_snapshots_request_builder import ConfigurationSnapshotsRequestBuilder

        return ConfigurationSnapshotsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ConfigurationManagementRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ConfigurationManagementRequestBuilderGetQueryParameters():
        """
        A container for Tenant Configuration Management (TCM) resources. Read-only.
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
    class ConfigurationManagementRequestBuilderGetRequestConfiguration(RequestConfiguration[ConfigurationManagementRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ConfigurationManagementRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

