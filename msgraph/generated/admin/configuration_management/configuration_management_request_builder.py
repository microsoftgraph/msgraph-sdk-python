from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .configuration_drifts.configuration_drifts_request_builder import ConfigurationDriftsRequestBuilder
    from .configuration_monitoring_results.configuration_monitoring_results_request_builder import ConfigurationMonitoringResultsRequestBuilder
    from .configuration_monitors.configuration_monitors_request_builder import ConfigurationMonitorsRequestBuilder
    from .configuration_snapshots.configuration_snapshots_request_builder import ConfigurationSnapshotsRequestBuilder
    from .configuration_snapshot_jobs.configuration_snapshot_jobs_request_builder import ConfigurationSnapshotJobsRequestBuilder

class ConfigurationManagementRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /admin/configurationManagement
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ConfigurationManagementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin/configurationManagement", path_parameters)
    
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
    

