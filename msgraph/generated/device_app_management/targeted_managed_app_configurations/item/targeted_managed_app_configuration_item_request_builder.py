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

apps_request_builder = lazy_import('msgraph.generated.device_app_management.targeted_managed_app_configurations.item.apps.apps_request_builder')
managed_mobile_app_item_request_builder = lazy_import('msgraph.generated.device_app_management.targeted_managed_app_configurations.item.apps.item.managed_mobile_app_item_request_builder')
assign_request_builder = lazy_import('msgraph.generated.device_app_management.targeted_managed_app_configurations.item.assign.assign_request_builder')
assignments_request_builder = lazy_import('msgraph.generated.device_app_management.targeted_managed_app_configurations.item.assignments.assignments_request_builder')
targeted_managed_app_policy_assignment_item_request_builder = lazy_import('msgraph.generated.device_app_management.targeted_managed_app_configurations.item.assignments.item.targeted_managed_app_policy_assignment_item_request_builder')
deployment_summary_request_builder = lazy_import('msgraph.generated.device_app_management.targeted_managed_app_configurations.item.deployment_summary.deployment_summary_request_builder')
target_apps_request_builder = lazy_import('msgraph.generated.device_app_management.targeted_managed_app_configurations.item.target_apps.target_apps_request_builder')
targeted_managed_app_configuration = lazy_import('msgraph.generated.models.targeted_managed_app_configuration')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class TargetedManagedAppConfigurationItemRequestBuilder():
    """
    Provides operations to manage the targetedManagedAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
    """
    @property
    def apps(self) -> apps_request_builder.AppsRequestBuilder:
        """
        Provides operations to manage the apps property of the microsoft.graph.targetedManagedAppConfiguration entity.
        """
        return apps_request_builder.AppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.targetedManagedAppConfiguration entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deployment_summary(self) -> deployment_summary_request_builder.DeploymentSummaryRequestBuilder:
        """
        Provides operations to manage the deploymentSummary property of the microsoft.graph.targetedManagedAppConfiguration entity.
        """
        return deployment_summary_request_builder.DeploymentSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def target_apps(self) -> target_apps_request_builder.TargetAppsRequestBuilder:
        """
        Provides operations to call the targetApps method.
        """
        return target_apps_request_builder.TargetAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def apps_by_id(self,id: str) -> managed_mobile_app_item_request_builder.ManagedMobileAppItemRequestBuilder:
        """
        Provides operations to manage the apps property of the microsoft.graph.targetedManagedAppConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_mobile_app_item_request_builder.ManagedMobileAppItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedMobileApp%2Did"] = id
        return managed_mobile_app_item_request_builder.ManagedMobileAppItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignments_by_id(self,id: str) -> targeted_managed_app_policy_assignment_item_request_builder.TargetedManagedAppPolicyAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.targetedManagedAppConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: targeted_managed_app_policy_assignment_item_request_builder.TargetedManagedAppPolicyAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["targetedManagedAppPolicyAssignment%2Did"] = id
        return targeted_managed_app_policy_assignment_item_request_builder.TargetedManagedAppPolicyAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TargetedManagedAppConfigurationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceAppManagement/targetedManagedAppConfigurations/{targetedManagedAppConfiguration%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property targetedManagedAppConfigurations for deviceAppManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Targeted managed app configurations.
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
    
    def create_patch_request_information(self,body: Optional[targeted_managed_app_configuration.TargetedManagedAppConfiguration] = None, request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property targetedManagedAppConfigurations in deviceAppManagement
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property targetedManagedAppConfigurations for deviceAppManagement
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
    
    async def get(self,request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[targeted_managed_app_configuration.TargetedManagedAppConfiguration]:
        """
        Targeted managed app configurations.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[targeted_managed_app_configuration.TargetedManagedAppConfiguration]
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
        return await self.request_adapter.send_async(request_info, targeted_managed_app_configuration.TargetedManagedAppConfiguration, response_handler, error_mapping)
    
    async def patch(self,body: Optional[targeted_managed_app_configuration.TargetedManagedAppConfiguration] = None, request_configuration: Optional[TargetedManagedAppConfigurationItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[targeted_managed_app_configuration.TargetedManagedAppConfiguration]:
        """
        Update the navigation property targetedManagedAppConfigurations in deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[targeted_managed_app_configuration.TargetedManagedAppConfiguration]
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
        return await self.request_adapter.send_async(request_info, targeted_managed_app_configuration.TargetedManagedAppConfiguration, response_handler, error_mapping)
    
    @dataclass
    class TargetedManagedAppConfigurationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TargetedManagedAppConfigurationItemRequestBuilderGetQueryParameters():
        """
        Targeted managed app configurations.
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
    class TargetedManagedAppConfigurationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TargetedManagedAppConfigurationItemRequestBuilder.TargetedManagedAppConfigurationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TargetedManagedAppConfigurationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

