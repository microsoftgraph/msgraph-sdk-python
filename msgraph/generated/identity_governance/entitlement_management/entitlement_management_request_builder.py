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
    from ...models.entitlement_management import EntitlementManagement
    from ...models.o_data_errors.o_data_error import ODataError
    from .access_packages.access_packages_request_builder import AccessPackagesRequestBuilder
    from .access_package_assignment_approvals.access_package_assignment_approvals_request_builder import AccessPackageAssignmentApprovalsRequestBuilder
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .assignment_policies.assignment_policies_request_builder import AssignmentPoliciesRequestBuilder
    from .assignment_requests.assignment_requests_request_builder import AssignmentRequestsRequestBuilder
    from .catalogs.catalogs_request_builder import CatalogsRequestBuilder
    from .connected_organizations.connected_organizations_request_builder import ConnectedOrganizationsRequestBuilder
    from .resources.resources_request_builder import ResourcesRequestBuilder
    from .resource_environments.resource_environments_request_builder import ResourceEnvironmentsRequestBuilder
    from .resource_requests.resource_requests_request_builder import ResourceRequestsRequestBuilder
    from .resource_role_scopes.resource_role_scopes_request_builder import ResourceRoleScopesRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder

class EntitlementManagementRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the entitlementManagement property of the microsoft.graph.identityGovernance entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EntitlementManagementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/entitlementManagement{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property entitlementManagement for identityGovernance
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[EntitlementManagementRequestBuilderGetQueryParameters]] = None) -> Optional[EntitlementManagement]:
        """
        Get entitlementManagement from identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EntitlementManagement]
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
        from ...models.entitlement_management import EntitlementManagement

        return await self.request_adapter.send_async(request_info, EntitlementManagement, error_mapping)
    
    async def patch(self,body: EntitlementManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EntitlementManagement]:
        """
        Update the navigation property entitlementManagement in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EntitlementManagement]
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
        from ...models.entitlement_management import EntitlementManagement

        return await self.request_adapter.send_async(request_info, EntitlementManagement, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property entitlementManagement for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[EntitlementManagementRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get entitlementManagement from identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: EntitlementManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property entitlementManagement in identityGovernance
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
    def access_package_assignment_approvals(self) -> AccessPackageAssignmentApprovalsRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentApprovals property of the microsoft.graph.entitlementManagement entity.
        """
        from .access_package_assignment_approvals.access_package_assignment_approvals_request_builder import AccessPackageAssignmentApprovalsRequestBuilder

        return AccessPackageAssignmentApprovalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_packages(self) -> AccessPackagesRequestBuilder:
        """
        Provides operations to manage the accessPackages property of the microsoft.graph.entitlementManagement entity.
        """
        from .access_packages.access_packages_request_builder import AccessPackagesRequestBuilder

        return AccessPackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_policies(self) -> AssignmentPoliciesRequestBuilder:
        """
        Provides operations to manage the assignmentPolicies property of the microsoft.graph.entitlementManagement entity.
        """
        from .assignment_policies.assignment_policies_request_builder import AssignmentPoliciesRequestBuilder

        return AssignmentPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_requests(self) -> AssignmentRequestsRequestBuilder:
        """
        Provides operations to manage the assignmentRequests property of the microsoft.graph.entitlementManagement entity.
        """
        from .assignment_requests.assignment_requests_request_builder import AssignmentRequestsRequestBuilder

        return AssignmentRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.entitlementManagement entity.
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def catalogs(self) -> CatalogsRequestBuilder:
        """
        Provides operations to manage the catalogs property of the microsoft.graph.entitlementManagement entity.
        """
        from .catalogs.catalogs_request_builder import CatalogsRequestBuilder

        return CatalogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connected_organizations(self) -> ConnectedOrganizationsRequestBuilder:
        """
        Provides operations to manage the connectedOrganizations property of the microsoft.graph.entitlementManagement entity.
        """
        from .connected_organizations.connected_organizations_request_builder import ConnectedOrganizationsRequestBuilder

        return ConnectedOrganizationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_environments(self) -> ResourceEnvironmentsRequestBuilder:
        """
        Provides operations to manage the resourceEnvironments property of the microsoft.graph.entitlementManagement entity.
        """
        from .resource_environments.resource_environments_request_builder import ResourceEnvironmentsRequestBuilder

        return ResourceEnvironmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_requests(self) -> ResourceRequestsRequestBuilder:
        """
        Provides operations to manage the resourceRequests property of the microsoft.graph.entitlementManagement entity.
        """
        from .resource_requests.resource_requests_request_builder import ResourceRequestsRequestBuilder

        return ResourceRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_role_scopes(self) -> ResourceRoleScopesRequestBuilder:
        """
        Provides operations to manage the resourceRoleScopes property of the microsoft.graph.entitlementManagement entity.
        """
        from .resource_role_scopes.resource_role_scopes_request_builder import ResourceRoleScopesRequestBuilder

        return ResourceRoleScopesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resources(self) -> ResourcesRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.entitlementManagement entity.
        """
        from .resources.resources_request_builder import ResourcesRequestBuilder

        return ResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.entitlementManagement entity.
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EntitlementManagementRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EntitlementManagementRequestBuilderGetQueryParameters():
        """
        Get entitlementManagement from identityGovernance
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
    

