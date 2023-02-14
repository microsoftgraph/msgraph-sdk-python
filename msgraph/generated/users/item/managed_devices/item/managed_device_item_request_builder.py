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

managed_device = lazy_import('msgraph.generated.models.managed_device')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
device_category_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.device_category.device_category_request_builder')
device_compliance_policy_states_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.device_compliance_policy_states.device_compliance_policy_states_request_builder')
device_compliance_policy_state_item_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.device_compliance_policy_states.item.device_compliance_policy_state_item_request_builder')
device_configuration_states_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.device_configuration_states.device_configuration_states_request_builder')
device_configuration_state_item_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.device_configuration_states.item.device_configuration_state_item_request_builder')
microsoft_graph_bypass_activation_lock_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_bypass_activation_lock.microsoft_graph_bypass_activation_lock_request_builder')
microsoft_graph_clean_windows_device_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_clean_windows_device.microsoft_graph_clean_windows_device_request_builder')
microsoft_graph_delete_user_from_shared_apple_device_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_delete_user_from_shared_apple_device.microsoft_graph_delete_user_from_shared_apple_device_request_builder')
microsoft_graph_disable_lost_mode_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_disable_lost_mode.microsoft_graph_disable_lost_mode_request_builder')
microsoft_graph_locate_device_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_locate_device.microsoft_graph_locate_device_request_builder')
microsoft_graph_logout_shared_apple_device_active_user_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_logout_shared_apple_device_active_user.microsoft_graph_logout_shared_apple_device_active_user_request_builder')
microsoft_graph_reboot_now_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_reboot_now.microsoft_graph_reboot_now_request_builder')
microsoft_graph_recover_passcode_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_recover_passcode.microsoft_graph_recover_passcode_request_builder')
microsoft_graph_remote_lock_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_remote_lock.microsoft_graph_remote_lock_request_builder')
microsoft_graph_request_remote_assistance_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_request_remote_assistance.microsoft_graph_request_remote_assistance_request_builder')
microsoft_graph_reset_passcode_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_reset_passcode.microsoft_graph_reset_passcode_request_builder')
microsoft_graph_retire_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_retire.microsoft_graph_retire_request_builder')
microsoft_graph_shut_down_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_shut_down.microsoft_graph_shut_down_request_builder')
microsoft_graph_sync_device_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_sync_device.microsoft_graph_sync_device_request_builder')
microsoft_graph_update_windows_device_account_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_update_windows_device_account.microsoft_graph_update_windows_device_account_request_builder')
microsoft_graph_windows_defender_scan_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_windows_defender_scan.microsoft_graph_windows_defender_scan_request_builder')
microsoft_graph_windows_defender_update_signatures_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_windows_defender_update_signatures.microsoft_graph_windows_defender_update_signatures_request_builder')
microsoft_graph_wipe_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.microsoft_graph_wipe.microsoft_graph_wipe_request_builder')
users_request_builder = lazy_import('msgraph.generated.users.item.managed_devices.item.users.users_request_builder')

class ManagedDeviceItemRequestBuilder():
    """
    Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
    """
    @property
    def device_category(self) -> device_category_request_builder.DeviceCategoryRequestBuilder:
        """
        Provides operations to manage the deviceCategory property of the microsoft.graph.managedDevice entity.
        """
        return device_category_request_builder.DeviceCategoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_states(self) -> device_compliance_policy_states_request_builder.DeviceCompliancePolicyStatesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyStates property of the microsoft.graph.managedDevice entity.
        """
        return device_compliance_policy_states_request_builder.DeviceCompliancePolicyStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_states(self) -> device_configuration_states_request_builder.DeviceConfigurationStatesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationStates property of the microsoft.graph.managedDevice entity.
        """
        return device_configuration_states_request_builder.DeviceConfigurationStatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_bypass_activation_lock(self) -> microsoft_graph_bypass_activation_lock_request_builder.MicrosoftGraphBypassActivationLockRequestBuilder:
        """
        Provides operations to call the bypassActivationLock method.
        """
        return microsoft_graph_bypass_activation_lock_request_builder.MicrosoftGraphBypassActivationLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_clean_windows_device(self) -> microsoft_graph_clean_windows_device_request_builder.MicrosoftGraphCleanWindowsDeviceRequestBuilder:
        """
        Provides operations to call the cleanWindowsDevice method.
        """
        return microsoft_graph_clean_windows_device_request_builder.MicrosoftGraphCleanWindowsDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_delete_user_from_shared_apple_device(self) -> microsoft_graph_delete_user_from_shared_apple_device_request_builder.MicrosoftGraphDeleteUserFromSharedAppleDeviceRequestBuilder:
        """
        Provides operations to call the deleteUserFromSharedAppleDevice method.
        """
        return microsoft_graph_delete_user_from_shared_apple_device_request_builder.MicrosoftGraphDeleteUserFromSharedAppleDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_disable_lost_mode(self) -> microsoft_graph_disable_lost_mode_request_builder.MicrosoftGraphDisableLostModeRequestBuilder:
        """
        Provides operations to call the disableLostMode method.
        """
        return microsoft_graph_disable_lost_mode_request_builder.MicrosoftGraphDisableLostModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_locate_device(self) -> microsoft_graph_locate_device_request_builder.MicrosoftGraphLocateDeviceRequestBuilder:
        """
        Provides operations to call the locateDevice method.
        """
        return microsoft_graph_locate_device_request_builder.MicrosoftGraphLocateDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_logout_shared_apple_device_active_user(self) -> microsoft_graph_logout_shared_apple_device_active_user_request_builder.MicrosoftGraphLogoutSharedAppleDeviceActiveUserRequestBuilder:
        """
        Provides operations to call the logoutSharedAppleDeviceActiveUser method.
        """
        return microsoft_graph_logout_shared_apple_device_active_user_request_builder.MicrosoftGraphLogoutSharedAppleDeviceActiveUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_reboot_now(self) -> microsoft_graph_reboot_now_request_builder.MicrosoftGraphRebootNowRequestBuilder:
        """
        Provides operations to call the rebootNow method.
        """
        return microsoft_graph_reboot_now_request_builder.MicrosoftGraphRebootNowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_recover_passcode(self) -> microsoft_graph_recover_passcode_request_builder.MicrosoftGraphRecoverPasscodeRequestBuilder:
        """
        Provides operations to call the recoverPasscode method.
        """
        return microsoft_graph_recover_passcode_request_builder.MicrosoftGraphRecoverPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_remote_lock(self) -> microsoft_graph_remote_lock_request_builder.MicrosoftGraphRemoteLockRequestBuilder:
        """
        Provides operations to call the remoteLock method.
        """
        return microsoft_graph_remote_lock_request_builder.MicrosoftGraphRemoteLockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_request_remote_assistance(self) -> microsoft_graph_request_remote_assistance_request_builder.MicrosoftGraphRequestRemoteAssistanceRequestBuilder:
        """
        Provides operations to call the requestRemoteAssistance method.
        """
        return microsoft_graph_request_remote_assistance_request_builder.MicrosoftGraphRequestRemoteAssistanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_reset_passcode(self) -> microsoft_graph_reset_passcode_request_builder.MicrosoftGraphResetPasscodeRequestBuilder:
        """
        Provides operations to call the resetPasscode method.
        """
        return microsoft_graph_reset_passcode_request_builder.MicrosoftGraphResetPasscodeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_retire(self) -> microsoft_graph_retire_request_builder.MicrosoftGraphRetireRequestBuilder:
        """
        Provides operations to call the retire method.
        """
        return microsoft_graph_retire_request_builder.MicrosoftGraphRetireRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_shut_down(self) -> microsoft_graph_shut_down_request_builder.MicrosoftGraphShutDownRequestBuilder:
        """
        Provides operations to call the shutDown method.
        """
        return microsoft_graph_shut_down_request_builder.MicrosoftGraphShutDownRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_sync_device(self) -> microsoft_graph_sync_device_request_builder.MicrosoftGraphSyncDeviceRequestBuilder:
        """
        Provides operations to call the syncDevice method.
        """
        return microsoft_graph_sync_device_request_builder.MicrosoftGraphSyncDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_update_windows_device_account(self) -> microsoft_graph_update_windows_device_account_request_builder.MicrosoftGraphUpdateWindowsDeviceAccountRequestBuilder:
        """
        Provides operations to call the updateWindowsDeviceAccount method.
        """
        return microsoft_graph_update_windows_device_account_request_builder.MicrosoftGraphUpdateWindowsDeviceAccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_windows_defender_scan(self) -> microsoft_graph_windows_defender_scan_request_builder.MicrosoftGraphWindowsDefenderScanRequestBuilder:
        """
        Provides operations to call the windowsDefenderScan method.
        """
        return microsoft_graph_windows_defender_scan_request_builder.MicrosoftGraphWindowsDefenderScanRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_windows_defender_update_signatures(self) -> microsoft_graph_windows_defender_update_signatures_request_builder.MicrosoftGraphWindowsDefenderUpdateSignaturesRequestBuilder:
        """
        Provides operations to call the windowsDefenderUpdateSignatures method.
        """
        return microsoft_graph_windows_defender_update_signatures_request_builder.MicrosoftGraphWindowsDefenderUpdateSignaturesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_wipe(self) -> microsoft_graph_wipe_request_builder.MicrosoftGraphWipeRequestBuilder:
        """
        Provides operations to call the wipe method.
        """
        return microsoft_graph_wipe_request_builder.MicrosoftGraphWipeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> users_request_builder.UsersRequestBuilder:
        """
        Provides operations to manage the users property of the microsoft.graph.managedDevice entity.
        """
        return users_request_builder.UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ManagedDeviceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/managedDevices/{managedDevice%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property managedDevices for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def device_compliance_policy_states_by_id(self,id: str) -> device_compliance_policy_state_item_request_builder.DeviceCompliancePolicyStateItemRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyStates property of the microsoft.graph.managedDevice entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_policy_state_item_request_builder.DeviceCompliancePolicyStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCompliancePolicyState%2Did"] = id
        return device_compliance_policy_state_item_request_builder.DeviceCompliancePolicyStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def device_configuration_states_by_id(self,id: str) -> device_configuration_state_item_request_builder.DeviceConfigurationStateItemRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationStates property of the microsoft.graph.managedDevice entity.
        Args:
            id: Unique identifier of the item
        Returns: device_configuration_state_item_request_builder.DeviceConfigurationStateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceConfigurationState%2Did"] = id
        return device_configuration_state_item_request_builder.DeviceConfigurationStateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[managed_device.ManagedDevice]:
        """
        The managed devices associated with the user.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_device.ManagedDevice]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, error_mapping)
    
    async def patch(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[managed_device.ManagedDevice]:
        """
        Update the navigation property managedDevices in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[managed_device.ManagedDevice]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property managedDevices for users
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
    
    def to_get_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The managed devices associated with the user.
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
    
    def to_patch_request_information(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property managedDevices in users
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
    
    @dataclass
    class ManagedDeviceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ManagedDeviceItemRequestBuilderGetQueryParameters():
        """
        The managed devices associated with the user.
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
    class ManagedDeviceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ManagedDeviceItemRequestBuilder.ManagedDeviceItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ManagedDeviceItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

