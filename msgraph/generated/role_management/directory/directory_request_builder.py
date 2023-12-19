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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.rbac_application import RbacApplication
    from .resource_namespaces.resource_namespaces_request_builder import ResourceNamespacesRequestBuilder
    from .role_assignments.role_assignments_request_builder import RoleAssignmentsRequestBuilder
    from .role_assignment_schedules.role_assignment_schedules_request_builder import RoleAssignmentSchedulesRequestBuilder
    from .role_assignment_schedule_instances.role_assignment_schedule_instances_request_builder import RoleAssignmentScheduleInstancesRequestBuilder
    from .role_assignment_schedule_requests.role_assignment_schedule_requests_request_builder import RoleAssignmentScheduleRequestsRequestBuilder
    from .role_definitions.role_definitions_request_builder import RoleDefinitionsRequestBuilder
    from .role_eligibility_schedules.role_eligibility_schedules_request_builder import RoleEligibilitySchedulesRequestBuilder
    from .role_eligibility_schedule_instances.role_eligibility_schedule_instances_request_builder import RoleEligibilityScheduleInstancesRequestBuilder
    from .role_eligibility_schedule_requests.role_eligibility_schedule_requests_request_builder import RoleEligibilityScheduleRequestsRequestBuilder

class DirectoryRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the directory property of the microsoft.graph.roleManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DirectoryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/roleManagement/directory{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[DirectoryRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property directory for roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[DirectoryRequestBuilderGetRequestConfiguration] = None) -> Optional[RbacApplication]:
        """
        Get directory from roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RbacApplication]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.rbac_application import RbacApplication

        return await self.request_adapter.send_async(request_info, RbacApplication, error_mapping)
    
    async def patch(self,body: Optional[RbacApplication] = None, request_configuration: Optional[DirectoryRequestBuilderPatchRequestConfiguration] = None) -> Optional[RbacApplication]:
        """
        Update the navigation property directory in roleManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RbacApplication]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.rbac_application import RbacApplication

        return await self.request_adapter.send_async(request_info, RbacApplication, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DirectoryRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property directory for roleManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[DirectoryRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get directory from roleManagement
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
    
    def to_patch_request_information(self,body: Optional[RbacApplication] = None, request_configuration: Optional[DirectoryRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property directory in roleManagement
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
    
    def with_url(self,raw_url: Optional[str] = None) -> DirectoryRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DirectoryRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return DirectoryRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def resource_namespaces(self) -> ResourceNamespacesRequestBuilder:
        """
        Provides operations to manage the resourceNamespaces property of the microsoft.graph.rbacApplication entity.
        """
        from .resource_namespaces.resource_namespaces_request_builder import ResourceNamespacesRequestBuilder

        return ResourceNamespacesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignment_schedule_instances(self) -> RoleAssignmentScheduleInstancesRequestBuilder:
        """
        Provides operations to manage the roleAssignmentScheduleInstances property of the microsoft.graph.rbacApplication entity.
        """
        from .role_assignment_schedule_instances.role_assignment_schedule_instances_request_builder import RoleAssignmentScheduleInstancesRequestBuilder

        return RoleAssignmentScheduleInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignment_schedule_requests(self) -> RoleAssignmentScheduleRequestsRequestBuilder:
        """
        Provides operations to manage the roleAssignmentScheduleRequests property of the microsoft.graph.rbacApplication entity.
        """
        from .role_assignment_schedule_requests.role_assignment_schedule_requests_request_builder import RoleAssignmentScheduleRequestsRequestBuilder

        return RoleAssignmentScheduleRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignment_schedules(self) -> RoleAssignmentSchedulesRequestBuilder:
        """
        Provides operations to manage the roleAssignmentSchedules property of the microsoft.graph.rbacApplication entity.
        """
        from .role_assignment_schedules.role_assignment_schedules_request_builder import RoleAssignmentSchedulesRequestBuilder

        return RoleAssignmentSchedulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignments(self) -> RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.rbacApplication entity.
        """
        from .role_assignments.role_assignments_request_builder import RoleAssignmentsRequestBuilder

        return RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definitions(self) -> RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.rbacApplication entity.
        """
        from .role_definitions.role_definitions_request_builder import RoleDefinitionsRequestBuilder

        return RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_eligibility_schedule_instances(self) -> RoleEligibilityScheduleInstancesRequestBuilder:
        """
        Provides operations to manage the roleEligibilityScheduleInstances property of the microsoft.graph.rbacApplication entity.
        """
        from .role_eligibility_schedule_instances.role_eligibility_schedule_instances_request_builder import RoleEligibilityScheduleInstancesRequestBuilder

        return RoleEligibilityScheduleInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_eligibility_schedule_requests(self) -> RoleEligibilityScheduleRequestsRequestBuilder:
        """
        Provides operations to manage the roleEligibilityScheduleRequests property of the microsoft.graph.rbacApplication entity.
        """
        from .role_eligibility_schedule_requests.role_eligibility_schedule_requests_request_builder import RoleEligibilityScheduleRequestsRequestBuilder

        return RoleEligibilityScheduleRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_eligibility_schedules(self) -> RoleEligibilitySchedulesRequestBuilder:
        """
        Provides operations to manage the roleEligibilitySchedules property of the microsoft.graph.rbacApplication entity.
        """
        from .role_eligibility_schedules.role_eligibility_schedules_request_builder import RoleEligibilitySchedulesRequestBuilder

        return RoleEligibilitySchedulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DirectoryRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class DirectoryRequestBuilderGetQueryParameters():
        """
        Get directory from roleManagement
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
    class DirectoryRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DirectoryRequestBuilder.DirectoryRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DirectoryRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

