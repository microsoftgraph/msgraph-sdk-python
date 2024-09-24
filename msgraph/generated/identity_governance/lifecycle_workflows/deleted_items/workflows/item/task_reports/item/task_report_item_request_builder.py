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
    from ........models.identity_governance.task_report import TaskReport
    from ........models.o_data_errors.o_data_error import ODataError
    from .task.task_request_builder import TaskRequestBuilder
    from .task_definition.task_definition_request_builder import TaskDefinitionRequestBuilder
    from .task_processing_results.task_processing_results_request_builder import TaskProcessingResultsRequestBuilder

class TaskReportItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the taskReports property of the microsoft.graph.identityGovernance.workflow entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TaskReportItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}/taskReports/{taskReport%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[TaskReportItemRequestBuilderGetQueryParameters]] = None) -> Optional[TaskReport]:
        """
        Represents the aggregation of task execution data for tasks within a workflow object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TaskReport]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.identity_governance.task_report import TaskReport

        return await self.request_adapter.send_async(request_info, TaskReport, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TaskReportItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Represents the aggregation of task execution data for tasks within a workflow object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TaskReportItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TaskReportItemRequestBuilder
        """
        if raw_url is None:
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class TaskReportItemRequestBuilderGetRequestConfiguration(RequestConfiguration[TaskReportItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

