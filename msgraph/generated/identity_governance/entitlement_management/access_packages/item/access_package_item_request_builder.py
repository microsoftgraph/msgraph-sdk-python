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

access_packages_incompatible_with_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_packages.item.access_packages_incompatible_with.access_packages_incompatible_with_request_builder')
access_package_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_packages.item.access_packages_incompatible_with.item.access_package_item_request_builder')
assignment_policies_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_packages.item.assignment_policies.assignment_policies_request_builder')
access_package_assignment_policy_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_packages.item.assignment_policies.item.access_package_assignment_policy_item_request_builder')
catalog_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_packages.item.catalog.catalog_request_builder')
get_applicable_policy_requirements_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_packages.item.get_applicable_policy_requirements.get_applicable_policy_requirements_request_builder')
incompatible_access_packages_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_packages.item.incompatible_access_packages.incompatible_access_packages_request_builder')
access_package_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_packages.item.incompatible_access_packages.item.access_package_item_request_builder')
incompatible_groups_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_packages.item.incompatible_groups.incompatible_groups_request_builder')
group_item_request_builder = lazy_import('msgraph.generated.identity_governance.entitlement_management.access_packages.item.incompatible_groups.item.group_item_request_builder')
access_package = lazy_import('msgraph.generated.models.access_package')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class AccessPackageItemRequestBuilder():
    """
    Provides operations to manage the accessPackages property of the microsoft.graph.entitlementManagement entity.
    """
    def access_packages_incompatible_with(self) -> access_packages_incompatible_with_request_builder.AccessPackagesIncompatibleWithRequestBuilder:
        """
        Provides operations to manage the accessPackagesIncompatibleWith property of the microsoft.graph.accessPackage entity.
        """
        return access_packages_incompatible_with_request_builder.AccessPackagesIncompatibleWithRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignment_policies(self) -> assignment_policies_request_builder.AssignmentPoliciesRequestBuilder:
        """
        Provides operations to manage the assignmentPolicies property of the microsoft.graph.accessPackage entity.
        """
        return assignment_policies_request_builder.AssignmentPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def catalog(self) -> catalog_request_builder.CatalogRequestBuilder:
        """
        Provides operations to manage the catalog property of the microsoft.graph.accessPackage entity.
        """
        return catalog_request_builder.CatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_applicable_policy_requirements(self) -> get_applicable_policy_requirements_request_builder.GetApplicablePolicyRequirementsRequestBuilder:
        """
        Provides operations to call the getApplicablePolicyRequirements method.
        """
        return get_applicable_policy_requirements_request_builder.GetApplicablePolicyRequirementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def incompatible_access_packages(self) -> incompatible_access_packages_request_builder.IncompatibleAccessPackagesRequestBuilder:
        """
        Provides operations to manage the incompatibleAccessPackages property of the microsoft.graph.accessPackage entity.
        """
        return incompatible_access_packages_request_builder.IncompatibleAccessPackagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def incompatible_groups(self) -> incompatible_groups_request_builder.IncompatibleGroupsRequestBuilder:
        """
        Provides operations to manage the incompatibleGroups property of the microsoft.graph.accessPackage entity.
        """
        return incompatible_groups_request_builder.IncompatibleGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def access_packages_incompatible_with_by_id(self,id: str) -> AccessPackageItemRequestBuilder:
        """
        Provides operations to manage the accessPackagesIncompatibleWith property of the microsoft.graph.accessPackage entity.
        Args:
            id: Unique identifier of the item
        Returns: AccessPackageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackage%2Did1"] = id
        return AccessPackageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignment_policies_by_id(self,id: str) -> access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder:
        """
        Provides operations to manage the assignmentPolicies property of the microsoft.graph.accessPackage entity.
        Args:
            id: Unique identifier of the item
        Returns: access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackageAssignmentPolicy%2Did"] = id
        return access_package_assignment_policy_item_request_builder.AccessPackageAssignmentPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessPackageItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/entitlementManagement/accessPackages/{accessPackage%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[AccessPackageItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property accessPackages for identityGovernance
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
    
    def create_get_request_information(self,request_configuration: Optional[AccessPackageItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Access packages define the collection of resource roles and the policies for which subjects can request or be assigned access to those resources.
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
    
    def create_patch_request_information(self,body: Optional[access_package.AccessPackage] = None, request_configuration: Optional[AccessPackageItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property accessPackages in identityGovernance
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
    
    async def delete(self,request_configuration: Optional[AccessPackageItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property accessPackages for identityGovernance
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
    
    async def get(self,request_configuration: Optional[AccessPackageItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[access_package.AccessPackage]:
        """
        Access packages define the collection of resource roles and the policies for which subjects can request or be assigned access to those resources.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[access_package.AccessPackage]
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
        return await self.request_adapter.send_async(request_info, access_package.AccessPackage, response_handler, error_mapping)
    
    def incompatible_access_packages_by_id(self,id: str) -> AccessPackageItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.identityGovernance.entitlementManagement.accessPackages.item.incompatibleAccessPackages.item collection
        Args:
            id: Unique identifier of the item
        Returns: AccessPackageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessPackage%2Did1"] = id
        return AccessPackageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def incompatible_groups_by_id(self,id: str) -> group_item_request_builder.GroupItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.identityGovernance.entitlementManagement.accessPackages.item.incompatibleGroups.item collection
        Args:
            id: Unique identifier of the item
        Returns: group_item_request_builder.GroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["group%2Did"] = id
        return group_item_request_builder.GroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[access_package.AccessPackage] = None, request_configuration: Optional[AccessPackageItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[access_package.AccessPackage]:
        """
        Update the navigation property accessPackages in identityGovernance
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[access_package.AccessPackage]
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
        return await self.request_adapter.send_async(request_info, access_package.AccessPackage, response_handler, error_mapping)
    
    @dataclass
    class AccessPackageItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessPackageItemRequestBuilderGetQueryParameters():
        """
        Access packages define the collection of resource roles and the policies for which subjects can request or be assigned access to those resources.
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
    class AccessPackageItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessPackageItemRequestBuilder.AccessPackageItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessPackageItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

