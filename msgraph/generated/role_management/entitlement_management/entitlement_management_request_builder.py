from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

rbac_application = lazy_import('msgraph.generated.models.rbac_application')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
role_assignments_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_assignments.role_assignments_request_builder')
unified_role_assignment_item_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_assignments.item.unified_role_assignment_item_request_builder')
role_assignment_schedule_instances_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_assignment_schedule_instances.role_assignment_schedule_instances_request_builder')
unified_role_assignment_schedule_instance_item_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_assignment_schedule_instances.item.unified_role_assignment_schedule_instance_item_request_builder')
role_assignment_schedule_requests_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_assignment_schedule_requests.role_assignment_schedule_requests_request_builder')
unified_role_assignment_schedule_request_item_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_assignment_schedule_requests.item.unified_role_assignment_schedule_request_item_request_builder')
role_assignment_schedules_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_assignment_schedules.role_assignment_schedules_request_builder')
unified_role_assignment_schedule_item_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_assignment_schedules.item.unified_role_assignment_schedule_item_request_builder')
role_definitions_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_definitions.role_definitions_request_builder')
unified_role_definition_item_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_definitions.item.unified_role_definition_item_request_builder')
role_eligibility_schedule_instances_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_eligibility_schedule_instances.role_eligibility_schedule_instances_request_builder')
unified_role_eligibility_schedule_instance_item_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_eligibility_schedule_instances.item.unified_role_eligibility_schedule_instance_item_request_builder')
role_eligibility_schedule_requests_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_eligibility_schedule_requests.role_eligibility_schedule_requests_request_builder')
unified_role_eligibility_schedule_request_item_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_eligibility_schedule_requests.item.unified_role_eligibility_schedule_request_item_request_builder')
role_eligibility_schedules_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_eligibility_schedules.role_eligibility_schedules_request_builder')
unified_role_eligibility_schedule_item_request_builder = lazy_import('msgraph.generated.role_management.entitlement_management.role_eligibility_schedules.item.unified_role_eligibility_schedule_item_request_builder')

class EntitlementManagementRequestBuilder():
    """
    Provides operations to manage the entitlementManagement property of the microsoft.graph.roleManagement entity.
    """
    def role_assignments(self) -> role_assignments_request_builder.RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.rbacApplication entity.
        """
        return role_assignments_request_builder.RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def role_assignment_schedule_instances(self) -> role_assignment_schedule_instances_request_builder.RoleAssignmentScheduleInstancesRequestBuilder:
        """
        Provides operations to manage the roleAssignmentScheduleInstances property of the microsoft.graph.rbacApplication entity.
        """
        return role_assignment_schedule_instances_request_builder.RoleAssignmentScheduleInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def role_assignment_schedule_requests(self) -> role_assignment_schedule_requests_request_builder.RoleAssignmentScheduleRequestsRequestBuilder:
        """
        Provides operations to manage the roleAssignmentScheduleRequests property of the microsoft.graph.rbacApplication entity.
        """
        return role_assignment_schedule_requests_request_builder.RoleAssignmentScheduleRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def role_assignment_schedules(self) -> role_assignment_schedules_request_builder.RoleAssignmentSchedulesRequestBuilder:
        """
        Provides operations to manage the roleAssignmentSchedules property of the microsoft.graph.rbacApplication entity.
        """
        return role_assignment_schedules_request_builder.RoleAssignmentSchedulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def role_definitions(self) -> role_definitions_request_builder.RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.rbacApplication entity.
        """
        return role_definitions_request_builder.RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def role_eligibility_schedule_instances(self) -> role_eligibility_schedule_instances_request_builder.RoleEligibilityScheduleInstancesRequestBuilder:
        """
        Provides operations to manage the roleEligibilityScheduleInstances property of the microsoft.graph.rbacApplication entity.
        """
        return role_eligibility_schedule_instances_request_builder.RoleEligibilityScheduleInstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def role_eligibility_schedule_requests(self) -> role_eligibility_schedule_requests_request_builder.RoleEligibilityScheduleRequestsRequestBuilder:
        """
        Provides operations to manage the roleEligibilityScheduleRequests property of the microsoft.graph.rbacApplication entity.
        """
        return role_eligibility_schedule_requests_request_builder.RoleEligibilityScheduleRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def role_eligibility_schedules(self) -> role_eligibility_schedules_request_builder.RoleEligibilitySchedulesRequestBuilder:
        """
        Provides operations to manage the roleEligibilitySchedules property of the microsoft.graph.rbacApplication entity.
        """
        return role_eligibility_schedules_request_builder.RoleEligibilitySchedulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EntitlementManagementRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/roleManagement/entitlementManagement{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[EntitlementManagementRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property entitlementManagement for roleManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_get_request_information(self,request_configuration: Optional[EntitlementManagementRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Container for roles and assignments for entitlement management resources.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[rbac_application.RbacApplication] = None, request_configuration: Optional[EntitlementManagementRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property entitlementManagement in roleManagement
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[EntitlementManagementRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property entitlementManagement for roleManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[EntitlementManagementRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[rbac_application.RbacApplication]:
        """
        Container for roles and assignments for entitlement management resources.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[rbac_application.RbacApplication]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, rbac_application.RbacApplication, response_handler, error_mapping)
    
    async def patch(self,body: Optional[rbac_application.RbacApplication] = None, request_configuration: Optional[EntitlementManagementRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[rbac_application.RbacApplication]:
        """
        Update the navigation property entitlementManagement in roleManagement
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[rbac_application.RbacApplication]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, rbac_application.RbacApplication, response_handler, error_mapping)
    
    def role_assignments_by_id(self,id: str) -> unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignment%2Did"] = id
        return unified_role_assignment_item_request_builder.UnifiedRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignment_schedule_instances_by_id(self,id: str) -> unified_role_assignment_schedule_instance_item_request_builder.UnifiedRoleAssignmentScheduleInstanceItemRequestBuilder:
        """
        Provides operations to manage the roleAssignmentScheduleInstances property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_schedule_instance_item_request_builder.UnifiedRoleAssignmentScheduleInstanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignmentScheduleInstance%2Did"] = id
        return unified_role_assignment_schedule_instance_item_request_builder.UnifiedRoleAssignmentScheduleInstanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignment_schedule_requests_by_id(self,id: str) -> unified_role_assignment_schedule_request_item_request_builder.UnifiedRoleAssignmentScheduleRequestItemRequestBuilder:
        """
        Provides operations to manage the roleAssignmentScheduleRequests property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_schedule_request_item_request_builder.UnifiedRoleAssignmentScheduleRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignmentScheduleRequest%2Did"] = id
        return unified_role_assignment_schedule_request_item_request_builder.UnifiedRoleAssignmentScheduleRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_assignment_schedules_by_id(self,id: str) -> unified_role_assignment_schedule_item_request_builder.UnifiedRoleAssignmentScheduleItemRequestBuilder:
        """
        Provides operations to manage the roleAssignmentSchedules property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_assignment_schedule_item_request_builder.UnifiedRoleAssignmentScheduleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleAssignmentSchedule%2Did"] = id
        return unified_role_assignment_schedule_item_request_builder.UnifiedRoleAssignmentScheduleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_definitions_by_id(self,id: str) -> unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleDefinition%2Did"] = id
        return unified_role_definition_item_request_builder.UnifiedRoleDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_eligibility_schedule_instances_by_id(self,id: str) -> unified_role_eligibility_schedule_instance_item_request_builder.UnifiedRoleEligibilityScheduleInstanceItemRequestBuilder:
        """
        Provides operations to manage the roleEligibilityScheduleInstances property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_eligibility_schedule_instance_item_request_builder.UnifiedRoleEligibilityScheduleInstanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleEligibilityScheduleInstance%2Did"] = id
        return unified_role_eligibility_schedule_instance_item_request_builder.UnifiedRoleEligibilityScheduleInstanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_eligibility_schedule_requests_by_id(self,id: str) -> unified_role_eligibility_schedule_request_item_request_builder.UnifiedRoleEligibilityScheduleRequestItemRequestBuilder:
        """
        Provides operations to manage the roleEligibilityScheduleRequests property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_eligibility_schedule_request_item_request_builder.UnifiedRoleEligibilityScheduleRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleEligibilityScheduleRequest%2Did"] = id
        return unified_role_eligibility_schedule_request_item_request_builder.UnifiedRoleEligibilityScheduleRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def role_eligibility_schedules_by_id(self,id: str) -> unified_role_eligibility_schedule_item_request_builder.UnifiedRoleEligibilityScheduleItemRequestBuilder:
        """
        Provides operations to manage the roleEligibilitySchedules property of the microsoft.graph.rbacApplication entity.
        Args:
            id: Unique identifier of the item
        Returns: unified_role_eligibility_schedule_item_request_builder.UnifiedRoleEligibilityScheduleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["unifiedRoleEligibilitySchedule%2Did"] = id
        return unified_role_eligibility_schedule_item_request_builder.UnifiedRoleEligibilityScheduleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class EntitlementManagementRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EntitlementManagementRequestBuilderGetQueryParameters():
        """
        Container for roles and assignments for entitlement management resources.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class EntitlementManagementRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EntitlementManagementRequestBuilder.EntitlementManagementRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EntitlementManagementRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

