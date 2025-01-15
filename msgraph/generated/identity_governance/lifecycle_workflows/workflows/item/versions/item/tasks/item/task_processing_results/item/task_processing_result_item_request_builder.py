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
    from ...........models.identity_governance.task_processing_result import TaskProcessingResult
    from ...........models.o_data_errors.o_data_error import ODataError
    from .microsoft_graph_identity_governance_resume.microsoft_graph_identity_governance_resume_request_builder import MicrosoftGraphIdentityGovernanceResumeRequestBuilder
    from .subject.subject_request_builder import SubjectRequestBuilder
    from .task.task_request_builder import TaskRequestBuilder

class TaskProcessingResultItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the taskProcessingResults property of the microsoft.graph.identityGovernance.task entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TaskProcessingResultItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/workflows/{workflow%2Did}/versions/{workflowVersion%2DversionNumber}/tasks/{task%2Did}/taskProcessingResults/{taskProcessingResult%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[TaskProcessingResultItemRequestBuilderGetQueryParameters]] = None) -> Optional[TaskProcessingResult]:
        """
        The result of processing the task.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TaskProcessingResult]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...........models.identity_governance.task_processing_result import TaskProcessingResult

        return await self.request_adapter.send_async(request_info, TaskProcessingResult, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TaskProcessingResultItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The result of processing the task.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TaskProcessingResultItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TaskProcessingResultItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TaskProcessingResultItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def microsoft_graph_identity_governance_resume(self) -> MicrosoftGraphIdentityGovernanceResumeRequestBuilder:
        """
        Provides operations to call the resume method.
        """
        from .microsoft_graph_identity_governance_resume.microsoft_graph_identity_governance_resume_request_builder import MicrosoftGraphIdentityGovernanceResumeRequestBuilder

        return MicrosoftGraphIdentityGovernanceResumeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subject(self) -> SubjectRequestBuilder:
        """
        Provides operations to manage the subject property of the microsoft.graph.identityGovernance.taskProcessingResult entity.
        """
        from .subject.subject_request_builder import SubjectRequestBuilder

        return SubjectRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task(self) -> TaskRequestBuilder:
        """
        Provides operations to manage the task property of the microsoft.graph.identityGovernance.taskProcessingResult entity.
        """
        from .task.task_request_builder import TaskRequestBuilder

        return TaskRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TaskProcessingResultItemRequestBuilderGetQueryParameters():
        """
        The result of processing the task.
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
    class TaskProcessingResultItemRequestBuilderGetRequestConfiguration(RequestConfiguration[TaskProcessingResultItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

