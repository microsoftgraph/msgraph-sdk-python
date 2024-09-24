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
    from ...models.identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer
    from ...models.o_data_errors.o_data_error import ODataError
    from .custom_task_extensions.custom_task_extensions_request_builder import CustomTaskExtensionsRequestBuilder
    from .deleted_items.deleted_items_request_builder import DeletedItemsRequestBuilder
    from .insights.insights_request_builder import InsightsRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .task_definitions.task_definitions_request_builder import TaskDefinitionsRequestBuilder
    from .workflows.workflows_request_builder import WorkflowsRequestBuilder
    from .workflow_templates.workflow_templates_request_builder import WorkflowTemplatesRequestBuilder

class LifecycleWorkflowsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the lifecycleWorkflows property of the microsoft.graph.identityGovernance entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new LifecycleWorkflowsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property lifecycleWorkflows for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[LifecycleWorkflowsRequestBuilderGetQueryParameters]] = None) -> Optional[LifecycleWorkflowsContainer]:
        """
        Get lifecycleWorkflows from identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LifecycleWorkflowsContainer]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer

        return await self.request_adapter.send_async(request_info, LifecycleWorkflowsContainer, error_mapping)
    
    async def patch(self,body: LifecycleWorkflowsContainer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LifecycleWorkflowsContainer]:
        """
        Update the navigation property lifecycleWorkflows in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LifecycleWorkflowsContainer]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer

        return await self.request_adapter.send_async(request_info, LifecycleWorkflowsContainer, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property lifecycleWorkflows for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LifecycleWorkflowsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get lifecycleWorkflows from identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: LifecycleWorkflowsContainer, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property lifecycleWorkflows in identityGovernance
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
    
    def with_url(self,raw_url: str) -> LifecycleWorkflowsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LifecycleWorkflowsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LifecycleWorkflowsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def custom_task_extensions(self) -> CustomTaskExtensionsRequestBuilder:
        """
        Provides operations to manage the customTaskExtensions property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        from .custom_task_extensions.custom_task_extensions_request_builder import CustomTaskExtensionsRequestBuilder

        return CustomTaskExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deleted_items(self) -> DeletedItemsRequestBuilder:
        """
        Provides operations to manage the deletedItems property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        from .deleted_items.deleted_items_request_builder import DeletedItemsRequestBuilder

        return DeletedItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def insights(self) -> InsightsRequestBuilder:
        """
        Provides operations to manage the insights property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        from .insights.insights_request_builder import InsightsRequestBuilder

        return InsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_definitions(self) -> TaskDefinitionsRequestBuilder:
        """
        Provides operations to manage the taskDefinitions property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        from .task_definitions.task_definitions_request_builder import TaskDefinitionsRequestBuilder

        return TaskDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workflow_templates(self) -> WorkflowTemplatesRequestBuilder:
        """
        Provides operations to manage the workflowTemplates property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        from .workflow_templates.workflow_templates_request_builder import WorkflowTemplatesRequestBuilder

        return WorkflowTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workflows(self) -> WorkflowsRequestBuilder:
        """
        Provides operations to manage the workflows property of the microsoft.graph.identityGovernance.lifecycleWorkflowsContainer entity.
        """
        from .workflows.workflows_request_builder import WorkflowsRequestBuilder

        return WorkflowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class LifecycleWorkflowsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LifecycleWorkflowsRequestBuilderGetQueryParameters():
        """
        Get lifecycleWorkflows from identityGovernance
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
    class LifecycleWorkflowsRequestBuilderGetRequestConfiguration(RequestConfiguration[LifecycleWorkflowsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LifecycleWorkflowsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

