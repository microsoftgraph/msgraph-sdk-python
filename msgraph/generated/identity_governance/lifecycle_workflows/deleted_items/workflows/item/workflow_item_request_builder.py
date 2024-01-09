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
    from ......models.identity_governance.workflow import Workflow
    from ......models.o_data_errors.o_data_error import ODataError
    from .created_by.created_by_request_builder import CreatedByRequestBuilder
    from .execution_scope.execution_scope_request_builder import ExecutionScopeRequestBuilder
    from .last_modified_by.last_modified_by_request_builder import LastModifiedByRequestBuilder
    from .microsoft_graph_identity_governance_activate.microsoft_graph_identity_governance_activate_request_builder import MicrosoftGraphIdentityGovernanceActivateRequestBuilder
    from .microsoft_graph_identity_governance_create_new_version.microsoft_graph_identity_governance_create_new_version_request_builder import MicrosoftGraphIdentityGovernanceCreateNewVersionRequestBuilder
    from .microsoft_graph_identity_governance_restore.microsoft_graph_identity_governance_restore_request_builder import MicrosoftGraphIdentityGovernanceRestoreRequestBuilder
    from .runs.runs_request_builder import RunsRequestBuilder
    from .tasks.tasks_request_builder import TasksRequestBuilder
    from .task_reports.task_reports_request_builder import TaskReportsRequestBuilder
    from .user_processing_results.user_processing_results_request_builder import UserProcessingResultsRequestBuilder
    from .versions.versions_request_builder import VersionsRequestBuilder

class WorkflowItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the workflows property of the microsoft.graph.deletedItemContainer entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkflowItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/deletedItems/workflows/{workflow%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[WorkflowItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a workflow object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-deletedItemcontainer-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WorkflowItemRequestBuilderGetRequestConfiguration] = None) -> Optional[Workflow]:
        """
        Retrieve a deleted workflow object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Workflow]
        Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-deleteditemcontainer-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.identity_governance.workflow import Workflow

        return await self.request_adapter.send_async(request_info, Workflow, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[WorkflowItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a workflow object.
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
    
    def to_get_request_information(self,request_configuration: Optional[WorkflowItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a deleted workflow object.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> WorkflowItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WorkflowItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return WorkflowItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def created_by(self) -> CreatedByRequestBuilder:
        """
        Provides operations to manage the createdBy property of the microsoft.graph.identityGovernance.workflowBase entity.
        """
        from .created_by.created_by_request_builder import CreatedByRequestBuilder

        return CreatedByRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def execution_scope(self) -> ExecutionScopeRequestBuilder:
        """
        Provides operations to manage the executionScope property of the microsoft.graph.identityGovernance.workflow entity.
        """
        from .execution_scope.execution_scope_request_builder import ExecutionScopeRequestBuilder

        return ExecutionScopeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_modified_by(self) -> LastModifiedByRequestBuilder:
        """
        Provides operations to manage the lastModifiedBy property of the microsoft.graph.identityGovernance.workflowBase entity.
        """
        from .last_modified_by.last_modified_by_request_builder import LastModifiedByRequestBuilder

        return LastModifiedByRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_identity_governance_activate(self) -> MicrosoftGraphIdentityGovernanceActivateRequestBuilder:
        """
        Provides operations to call the activate method.
        """
        from .microsoft_graph_identity_governance_activate.microsoft_graph_identity_governance_activate_request_builder import MicrosoftGraphIdentityGovernanceActivateRequestBuilder

        return MicrosoftGraphIdentityGovernanceActivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_identity_governance_create_new_version(self) -> MicrosoftGraphIdentityGovernanceCreateNewVersionRequestBuilder:
        """
        Provides operations to call the createNewVersion method.
        """
        from .microsoft_graph_identity_governance_create_new_version.microsoft_graph_identity_governance_create_new_version_request_builder import MicrosoftGraphIdentityGovernanceCreateNewVersionRequestBuilder

        return MicrosoftGraphIdentityGovernanceCreateNewVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_identity_governance_restore(self) -> MicrosoftGraphIdentityGovernanceRestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .microsoft_graph_identity_governance_restore.microsoft_graph_identity_governance_restore_request_builder import MicrosoftGraphIdentityGovernanceRestoreRequestBuilder

        return MicrosoftGraphIdentityGovernanceRestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def runs(self) -> RunsRequestBuilder:
        """
        Provides operations to manage the runs property of the microsoft.graph.identityGovernance.workflow entity.
        """
        from .runs.runs_request_builder import RunsRequestBuilder

        return RunsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_reports(self) -> TaskReportsRequestBuilder:
        """
        Provides operations to manage the taskReports property of the microsoft.graph.identityGovernance.workflow entity.
        """
        from .task_reports.task_reports_request_builder import TaskReportsRequestBuilder

        return TaskReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tasks(self) -> TasksRequestBuilder:
        """
        Provides operations to manage the tasks property of the microsoft.graph.identityGovernance.workflowBase entity.
        """
        from .tasks.tasks_request_builder import TasksRequestBuilder

        return TasksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_processing_results(self) -> UserProcessingResultsRequestBuilder:
        """
        Provides operations to manage the userProcessingResults property of the microsoft.graph.identityGovernance.workflow entity.
        """
        from .user_processing_results.user_processing_results_request_builder import UserProcessingResultsRequestBuilder

        return UserProcessingResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.identityGovernance.workflow entity.
        """
        from .versions.versions_request_builder import VersionsRequestBuilder

        return VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WorkflowItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class WorkflowItemRequestBuilderGetQueryParameters():
        """
        Retrieve a deleted workflow object.
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
    class WorkflowItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[WorkflowItemRequestBuilder.WorkflowItemRequestBuilderGetQueryParameters] = None

    

