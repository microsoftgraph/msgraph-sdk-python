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

assign_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.assign.assign_request_builder')
assignments_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.assignments.assignments_request_builder')
device_configuration_assignment_item_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.assignments.item.device_configuration_assignment_item_request_builder')
device_setting_state_summaries_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.device_setting_state_summaries.device_setting_state_summaries_request_builder')
setting_state_device_summary_item_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.device_setting_state_summaries.item.setting_state_device_summary_item_request_builder')
device_statuses_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.device_statuses.device_statuses_request_builder')
device_configuration_device_status_item_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.device_statuses.item.device_configuration_device_status_item_request_builder')
device_status_overview_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.device_status_overview.device_status_overview_request_builder')
get_oma_setting_plain_text_value_with_secret_reference_value_id_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.get_oma_setting_plain_text_value_with_secret_reference_value_id.get_oma_setting_plain_text_value_with_secret_reference_value_id_request_builder')
user_statuses_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.user_statuses.user_statuses_request_builder')
device_configuration_user_status_item_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.user_statuses.item.device_configuration_user_status_item_request_builder')
user_status_overview_request_builder = lazy_import('msgraph.generated.device_management.device_configurations.item.user_status_overview.user_status_overview_request_builder')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DeviceConfigurationItemRequestBuilder():
    """
    Provides operations to manage the deviceConfigurations property of the microsoft.graph.deviceManagement entity.
    """
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceConfiguration entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def device_setting_state_summaries(self) -> device_setting_state_summaries_request_builder.DeviceSettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceSettingStateSummaries property of the microsoft.graph.deviceConfiguration entity.
        """
        return device_setting_state_summaries_request_builder.DeviceSettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def device_statuses(self) -> device_statuses_request_builder.DeviceStatusesRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.deviceConfiguration entity.
        """
        return device_statuses_request_builder.DeviceStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def device_status_overview(self) -> device_status_overview_request_builder.DeviceStatusOverviewRequestBuilder:
        """
        Provides operations to manage the deviceStatusOverview property of the microsoft.graph.deviceConfiguration entity.
        """
        return device_status_overview_request_builder.DeviceStatusOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    def user_statuses(self) -> user_statuses_request_builder.UserStatusesRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.deviceConfiguration entity.
        """
        return user_statuses_request_builder.UserStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def user_status_overview(self) -> user_status_overview_request_builder.UserStatusOverviewRequestBuilder:
        """
        Provides operations to manage the userStatusOverview property of the microsoft.graph.deviceConfiguration entity.
        """
        return user_status_overview_request_builder.UserStatusOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignments_by_id(self,id: str) -> device_configuration_assignment_item_request_builder.DeviceConfigurationAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.deviceConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: device_configuration_assignment_item_request_builder.DeviceConfigurationAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceConfigurationAssignment%2Did"] = id
        return device_configuration_assignment_item_request_builder.DeviceConfigurationAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceConfigurationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/deviceConfigurations/{deviceConfiguration%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[DeviceConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property deviceConfigurations for deviceManagement
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
    
    def create_get_request_information(self,request_configuration: Optional[DeviceConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The device configurations.
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
    
    def create_patch_request_information(self,body: Optional[device_configuration.DeviceConfiguration] = None, request_configuration: Optional[DeviceConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property deviceConfigurations in deviceManagement
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
    
    async def delete(self,request_configuration: Optional[DeviceConfigurationItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property deviceConfigurations for deviceManagement
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
        Provides operations to manage the deviceSettingStateSummaries property of the microsoft.graph.deviceConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: setting_state_device_summary_item_request_builder.SettingStateDeviceSummaryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["settingStateDeviceSummary%2Did"] = id
        return setting_state_device_summary_item_request_builder.SettingStateDeviceSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_statuses_by_id(self,id: str) -> device_configuration_device_status_item_request_builder.DeviceConfigurationDeviceStatusItemRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.deviceConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: device_configuration_device_status_item_request_builder.DeviceConfigurationDeviceStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceConfigurationDeviceStatus%2Did"] = id
        return device_configuration_device_status_item_request_builder.DeviceConfigurationDeviceStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DeviceConfigurationItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_configuration.DeviceConfiguration]:
        """
        The device configurations.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_configuration.DeviceConfiguration]
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
        return await self.request_adapter.send_async(request_info, device_configuration.DeviceConfiguration, response_handler, error_mapping)
    
    def get_oma_setting_plain_text_value_with_secret_reference_value_id(self,secret_reference_value_id: Optional[str] = None) -> get_oma_setting_plain_text_value_with_secret_reference_value_id_request_builder.GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequestBuilder:
        """
        Provides operations to call the getOmaSettingPlainTextValue method.
        Args:
            secretReferenceValueId: Usage: secretReferenceValueId='{secretReferenceValueId}'
        Returns: get_oma_setting_plain_text_value_with_secret_reference_value_id_request_builder.GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequestBuilder
        """
        if secret_reference_value_id is None:
            raise Exception("secret_reference_value_id cannot be undefined")
        return get_oma_setting_plain_text_value_with_secret_reference_value_id_request_builder.GetOmaSettingPlainTextValueWithSecretReferenceValueIdRequestBuilder(self.request_adapter, self.path_parameters, secretReferenceValueId)
    
    async def patch(self,body: Optional[device_configuration.DeviceConfiguration] = None, request_configuration: Optional[DeviceConfigurationItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_configuration.DeviceConfiguration]:
        """
        Update the navigation property deviceConfigurations in deviceManagement
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_configuration.DeviceConfiguration]
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
        return await self.request_adapter.send_async(request_info, device_configuration.DeviceConfiguration, response_handler, error_mapping)
    
    def user_statuses_by_id(self,id: str) -> device_configuration_user_status_item_request_builder.DeviceConfigurationUserStatusItemRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.deviceConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: device_configuration_user_status_item_request_builder.DeviceConfigurationUserStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceConfigurationUserStatus%2Did"] = id
        return device_configuration_user_status_item_request_builder.DeviceConfigurationUserStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class DeviceConfigurationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DeviceConfigurationItemRequestBuilderGetQueryParameters():
        """
        The device configurations.
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
    class DeviceConfigurationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceConfigurationItemRequestBuilder.DeviceConfigurationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceConfigurationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

