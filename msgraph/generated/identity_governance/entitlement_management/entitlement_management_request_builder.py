from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import entitlement_management
    from ...models.o_data_errors import o_data_error
    from .access_package_assignment_approvals import access_package_assignment_approvals_request_builder
    from .access_package_assignment_approvals.item import approval_item_request_builder
    from .access_packages import access_packages_request_builder
    from .access_packages.item import access_package_item_request_builder
    from .assignment_policies import assignment_policies_request_builder
    from .assignment_policies.item import access_package_assignment_policy_item_request_builder
    from .assignment_requests import assignment_requests_request_builder
    from .assignment_requests.item import access_package_assignment_request_item_request_builder
    from .assignments import assignments_request_builder
    from .assignments.item import access_package_assignment_item_request_builder
    from .catalogs import catalogs_request_builder
    from .catalogs.item import access_package_catalog_item_request_builder
    from .connected_organizations import connected_organizations_request_builder
    from .connected_organizations.item import connected_organization_item_request_builder
    from .settings import settings_request_builder

class EntitlementManagementRequestBuilder():
    """
    Provides operations to manage the entitlementManagement property of the microsoft.graph.identityGovernance entity.
    """
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
        self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def access_package_assignment_approvals_by_id(self,id: str) -> approval_item_request_builder.ApprovalItemRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentApprovals property of the microsoft.graph.entitlementManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: approval_item_request_builder.ApprovalItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .access_package_assignment_approvals.item import approval_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["approval%2Did"] = id
        return approval_item_request_builder.ApprovalItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def access_packages_by_id(self,id: str) -> access_package_item_request_builder.AccessPackageItemRequestBuilder:
        """
        Provides operations to manage the accessPackages property of the microsoft.graph.entitlementManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_item_request_builder.AccessPackageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .access_packages.item import access_package_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackage%2Did"] = id
        return access_package_item_request_builder.AccessPackageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignment_policies_by_id(self,id: str) -> access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder:
        """
        Provides operations to manage the assignmentPolicies property of the microsoft.graph.entitlementManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignment_policies.item import access_package_assignment_policy_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageAssignmentPolicy%2Did"] = id
        return access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignment_requests_by_id(self,id: str) -> access_package_assignment_request_item_request_builder.AccessPackageAssignmentRequestItemRequestBuilder:
        """
        Provides operations to manage the assignmentRequests property of the microsoft.graph.entitlementManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_assignment_request_item_request_builder.AccessPackageAssignmentRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignment_requests.item import access_package_assignment_request_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageAssignmentRequest%2Did"] = id
        return access_package_assignment_request_item_request_builder.AccessPackageAssignmentRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignments_by_id(self,id: str) -> access_package_assignment_item_request_builder.AccessPackageAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.entitlementManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_assignment_item_request_builder.AccessPackageAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignments.item import access_package_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageAssignment%2Did"] = id
        return access_package_assignment_item_request_builder.AccessPackageAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def catalogs_by_id(self,id: str) -> access_package_catalog_item_request_builder.AccessPackageCatalogItemRequestBuilder:
        """
        Provides operations to manage the catalogs property of the microsoft.graph.entitlementManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_catalog_item_request_builder.AccessPackageCatalogItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .catalogs.item import access_package_catalog_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageCatalog%2Did"] = id
        return access_package_catalog_item_request_builder.AccessPackageCatalogItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def connected_organizations_by_id(self,id: str) -> connected_organization_item_request_builder.ConnectedOrganizationItemRequestBuilder:
        """
        Provides operations to manage the connectedOrganizations property of the microsoft.graph.entitlementManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: connected_organization_item_request_builder.ConnectedOrganizationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .connected_organizations.item import connected_organization_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["connectedOrganization%2Did"] = id
        return connected_organization_item_request_builder.ConnectedOrganizationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[EntitlementManagementRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property entitlementManagement for identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[EntitlementManagementRequestBuilderGetRequestConfiguration] = None) -> Optional[entitlement_management.EntitlementManagement]:
        """
        Get entitlementManagement from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[entitlement_management.EntitlementManagement]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import entitlement_management

        return await self.request_adapter.send_async(request_info, entitlement_management.EntitlementManagement, error_mapping)
    
    async def patch(self,body: Optional[entitlement_management.EntitlementManagement] = None, request_configuration: Optional[EntitlementManagementRequestBuilderPatchRequestConfiguration] = None) -> Optional[entitlement_management.EntitlementManagement]:
        """
        Update the navigation property entitlementManagement in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[entitlement_management.EntitlementManagement]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import entitlement_management

        return await self.request_adapter.send_async(request_info, entitlement_management.EntitlementManagement, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EntitlementManagementRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property entitlementManagement for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[EntitlementManagementRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get entitlementManagement from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[entitlement_management.EntitlementManagement] = None, request_configuration: Optional[EntitlementManagementRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property entitlementManagement in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def access_package_assignment_approvals(self) -> access_package_assignment_approvals_request_builder.AccessPackageAssignmentApprovalsRequestBuilder:
        """
        Provides operations to manage the accessPackageAssignmentApprovals property of the microsoft.graph.entitlementManagement entity.
        """
        from .access_package_assignment_approvals import access_package_assignment_approvals_request_builder

        return access_package_assignment_approvals_request_builder.AccessPackageAssignmentApprovalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def access_packages(self) -> access_packages_request_builder.AccessPackagesRequestBuilder:
        """
        Provides operations to manage the accessPackages property of the microsoft.graph.entitlementManagement entity.
        """
        from .access_packages import access_packages_request_builder

        return access_packages_request_builder.AccessPackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_policies(self) -> assignment_policies_request_builder.AssignmentPoliciesRequestBuilder:
        """
        Provides operations to manage the assignmentPolicies property of the microsoft.graph.entitlementManagement entity.
        """
        from .assignment_policies import assignment_policies_request_builder

        return assignment_policies_request_builder.AssignmentPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_requests(self) -> assignment_requests_request_builder.AssignmentRequestsRequestBuilder:
        """
        Provides operations to manage the assignmentRequests property of the microsoft.graph.entitlementManagement entity.
        """
        from .assignment_requests import assignment_requests_request_builder

        return assignment_requests_request_builder.AssignmentRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.entitlementManagement entity.
        """
        from .assignments import assignments_request_builder

        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def catalogs(self) -> catalogs_request_builder.CatalogsRequestBuilder:
        """
        Provides operations to manage the catalogs property of the microsoft.graph.entitlementManagement entity.
        """
        from .catalogs import catalogs_request_builder

        return catalogs_request_builder.CatalogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def connected_organizations(self) -> connected_organizations_request_builder.ConnectedOrganizationsRequestBuilder:
        """
        Provides operations to manage the connectedOrganizations property of the microsoft.graph.entitlementManagement entity.
        """
        from .connected_organizations import connected_organizations_request_builder

        return connected_organizations_request_builder.ConnectedOrganizationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.entitlementManagement entity.
        """
        from .settings import settings_request_builder

        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EntitlementManagementRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EntitlementManagementRequestBuilderGetQueryParameters():
        """
        Get entitlementManagement from identityGovernance
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class EntitlementManagementRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

