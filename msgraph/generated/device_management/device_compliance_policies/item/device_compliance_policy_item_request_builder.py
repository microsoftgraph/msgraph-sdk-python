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

assign_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.assign.assign_request_builder')
assignments_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.assignments.assignments_request_builder')
device_compliance_policy_assignment_item_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.assignments.item.device_compliance_policy_assignment_item_request_builder')
device_setting_state_summaries_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.device_setting_state_summaries.device_setting_state_summaries_request_builder')
setting_state_device_summary_item_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.device_setting_state_summaries.item.setting_state_device_summary_item_request_builder')
device_statuses_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.device_statuses.device_statuses_request_builder')
device_compliance_device_status_item_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.device_statuses.item.device_compliance_device_status_item_request_builder')
device_status_overview_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.device_status_overview.device_status_overview_request_builder')
schedule_actions_for_rules_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.schedule_actions_for_rules.schedule_actions_for_rules_request_builder')
scheduled_actions_for_rule_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.scheduled_actions_for_rule.scheduled_actions_for_rule_request_builder')
device_compliance_scheduled_action_for_rule_item_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.scheduled_actions_for_rule.item.device_compliance_scheduled_action_for_rule_item_request_builder')
user_statuses_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.user_statuses.user_statuses_request_builder')
device_compliance_user_status_item_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.user_statuses.item.device_compliance_user_status_item_request_builder')
user_status_overview_request_builder = lazy_import('msgraph.generated.device_management.device_compliance_policies.item.user_status_overview.user_status_overview_request_builder')
device_compliance_policy = lazy_import('msgraph.generated.models.device_compliance_policy')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DeviceCompliancePolicyItemRequestBuilder():
    """
    Provides operations to manage the deviceCompliancePolicies property of the microsoft.graph.deviceManagement entity.
    """
    @property
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_setting_state_summaries(self) -> device_setting_state_summaries_request_builder.DeviceSettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceSettingStateSummaries property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        return device_setting_state_summaries_request_builder.DeviceSettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_statuses(self) -> device_statuses_request_builder.DeviceStatusesRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        return device_statuses_request_builder.DeviceStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_status_overview(self) -> device_status_overview_request_builder.DeviceStatusOverviewRequestBuilder:
        """
        Provides operations to manage the deviceStatusOverview property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        return device_status_overview_request_builder.DeviceStatusOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schedule_actions_for_rules(self) -> schedule_actions_for_rules_request_builder.ScheduleActionsForRulesRequestBuilder:
        """
        Provides operations to call the scheduleActionsForRules method.
        """
        return schedule_actions_for_rules_request_builder.ScheduleActionsForRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scheduled_actions_for_rule(self) -> scheduled_actions_for_rule_request_builder.ScheduledActionsForRuleRequestBuilder:
        """
        Provides operations to manage the scheduledActionsForRule property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        return scheduled_actions_for_rule_request_builder.ScheduledActionsForRuleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_statuses(self) -> user_statuses_request_builder.UserStatusesRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        return user_statuses_request_builder.UserStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_status_overview(self) -> user_status_overview_request_builder.UserStatusOverviewRequestBuilder:
        """
        Provides operations to manage the userStatusOverview property of the microsoft.graph.deviceCompliancePolicy entity.
        """
        return user_status_overview_request_builder.UserStatusOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignments_by_id(self,id: str) -> device_compliance_policy_assignment_item_request_builder.DeviceCompliancePolicyAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceCompliancePolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_policy_assignment_item_request_builder.DeviceCompliancePolicyAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCompliancePolicyAssignment%2Did"] = id
        return device_compliance_policy_assignment_item_request_builder.DeviceCompliancePolicyAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceCompliancePolicyItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/deviceCompliancePolicies/{deviceCompliancePolicy%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property deviceCompliancePolicies for deviceManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The device compliance policies.
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
    
    def create_patch_request_information(self,body: Optional[device_compliance_policy.DeviceCompliancePolicy] = None, request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property deviceCompliancePolicies in deviceManagement
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
    
    async def delete(self,request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property deviceCompliancePolicies for deviceManagement
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
    
    def device_setting_state_summaries_by_id(self,id: str) -> setting_state_device_summary_item_request_builder.SettingStateDeviceSummaryItemRequestBuilder:
        """
        Provides operations to manage the deviceSettingStateSummaries property of the microsoft.graph.deviceCompliancePolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: setting_state_device_summary_item_request_builder.SettingStateDeviceSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["settingStateDeviceSummary%2Did"] = id
        return setting_state_device_summary_item_request_builder.SettingStateDeviceSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_statuses_by_id(self,id: str) -> device_compliance_device_status_item_request_builder.DeviceComplianceDeviceStatusItemRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.deviceCompliancePolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_device_status_item_request_builder.DeviceComplianceDeviceStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceComplianceDeviceStatus%2Did"] = id
        return device_compliance_device_status_item_request_builder.DeviceComplianceDeviceStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_compliance_policy.DeviceCompliancePolicy]:
        """
        The device compliance policies.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_compliance_policy.DeviceCompliancePolicy]
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
        return await self.request_adapter.send_async(request_info, device_compliance_policy.DeviceCompliancePolicy, response_handler, error_mapping)
    
    async def patch(self,body: Optional[device_compliance_policy.DeviceCompliancePolicy] = None, request_configuration: Optional[DeviceCompliancePolicyItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_compliance_policy.DeviceCompliancePolicy]:
        """
        Update the navigation property deviceCompliancePolicies in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_compliance_policy.DeviceCompliancePolicy]
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
        return await self.request_adapter.send_async(request_info, device_compliance_policy.DeviceCompliancePolicy, response_handler, error_mapping)
    
    def scheduled_actions_for_rule_by_id(self,id: str) -> device_compliance_scheduled_action_for_rule_item_request_builder.DeviceComplianceScheduledActionForRuleItemRequestBuilder:
        """
        Provides operations to manage the scheduledActionsForRule property of the microsoft.graph.deviceCompliancePolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_scheduled_action_for_rule_item_request_builder.DeviceComplianceScheduledActionForRuleItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceComplianceScheduledActionForRule%2Did"] = id
        return device_compliance_scheduled_action_for_rule_item_request_builder.DeviceComplianceScheduledActionForRuleItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def user_statuses_by_id(self,id: str) -> device_compliance_user_status_item_request_builder.DeviceComplianceUserStatusItemRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.deviceCompliancePolicy entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_user_status_item_request_builder.DeviceComplianceUserStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceComplianceUserStatus%2Did"] = id
        return device_compliance_user_status_item_request_builder.DeviceComplianceUserStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class DeviceCompliancePolicyItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceCompliancePolicyItemRequestBuilderGetQueryParameters():
        """
        The device compliance policies.
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
    class DeviceCompliancePolicyItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceCompliancePolicyItemRequestBuilder.DeviceCompliancePolicyItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceCompliancePolicyItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

