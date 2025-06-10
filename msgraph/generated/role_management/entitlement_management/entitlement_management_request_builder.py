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

class EntitlementManagementRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the entitlementManagement property of the microsoft.graph.roleManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EntitlementManagementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/roleManagement/entitlementManagement{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property entitlementManagement for roleManagement
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[EntitlementManagementRequestBuilderGetQueryParameters]] = None) -> Optional[RbacApplication]:
        """
        Container for roles and assignments for entitlement management resources.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RbacApplication]
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
        from ...models.rbac_application import RbacApplication

        return await self.request_adapter.send_async(request_info, RbacApplication, error_mapping)
    
    async def patch(self,body: RbacApplication, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RbacApplication]:
        """
        Update the navigation property entitlementManagement in roleManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RbacApplication]
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
        from ...models.rbac_application import RbacApplication

        return await self.request_adapter.send_async(request_info, RbacApplication, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property entitlementManagement for roleManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[EntitlementManagementRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Container for roles and assignments for entitlement management resources.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: RbacApplication, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property entitlementManagement in roleManagement
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
    
    def with_url(self,raw_url: str) -> EntitlementManagementRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EntitlementManagementRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EntitlementManagementRequestBuilder(self.request_adapter, raw_url)
    
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
    
    @dataclass
    class EntitlementManagementRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EntitlementManagementRequestBuilderGetQueryParameters():
        """
        Container for roles and assignments for entitlement management resources.
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
    class EntitlementManagementRequestBuilderGetRequestConfiguration(RequestConfiguration[EntitlementManagementRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EntitlementManagementRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

