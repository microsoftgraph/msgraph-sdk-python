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
    from ........models.identity_governance.task_report import TaskReport
    from ........models.o_data_errors.o_data_error import ODataError
    from .task.task_request_builder import TaskRequestBuilder
    from .task_definition.task_definition_request_builder import TaskDefinitionRequestBuilder
    from .task_processing_results.task_processing_results_request_builder import TaskProcessingResultsRequestBuilder

class TaskReportItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the taskReports property of the microsoft.graph.identityGovernance.workflow entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TaskReportItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}/taskReports/{taskReport%2Did}{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[TaskReportItemRequestBuilderGetRequestConfiguration] = None) -> Optional[TaskReport]:
        """
        Represents the aggregation of task execution data for tasks within a workflow object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TaskReport]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.identity_governance.task_report import TaskReport

        return await self.request_adapter.send_async(request_info, TaskReport, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[TaskReportItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents the aggregation of task execution data for tasks within a workflow object.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> TaskReportItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TaskReportItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TaskReportItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def task(self) -> TaskRequestBuilder:
        """
        Provides operations to manage the task property of the microsoft.graph.identityGovernance.taskReport entity.
        """
        from .task.task_request_builder import TaskRequestBuilder

        return TaskRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_definition(self) -> TaskDefinitionRequestBuilder:
        """
        Provides operations to manage the taskDefinition property of the microsoft.graph.identityGovernance.taskReport entity.
        """
        from .task_definition.task_definition_request_builder import TaskDefinitionRequestBuilder

        return TaskDefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_processing_results(self) -> TaskProcessingResultsRequestBuilder:
        """
        Provides operations to manage the taskProcessingResults property of the microsoft.graph.identityGovernance.taskReport entity.
        """
        from .task_processing_results.task_processing_results_request_builder import TaskProcessingResultsRequestBuilder

        return TaskProcessingResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TaskReportItemRequestBuilderGetQueryParameters():
        """
        Represents the aggregation of task execution data for tasks within a workflow object.
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
    class TaskReportItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[TaskReportItemRequestBuilder.TaskReportItemRequestBuilderGetQueryParameters] = None

    

