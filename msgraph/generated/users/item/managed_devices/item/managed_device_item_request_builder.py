from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from .....models import managed_device
from .....models.o_data_errors import o_data_error
from .bypass_activation_lock import bypass_activation_lock_request_builder
from .clean_windows_device import clean_windows_device_request_builder
from .delete_user_from_shared_apple_device import delete_user_from_shared_apple_device_request_builder
from .device_category import device_category_request_builder
from .device_compliance_policy_states import device_compliance_policy_states_request_builder
from .device_compliance_policy_states.item import device_compliance_policy_state_item_request_builder
from .device_configuration_states import device_configuration_states_request_builder
from .device_configuration_states.item import device_configuration_state_item_request_builder
from .disable_lost_mode import disable_lost_mode_request_builder
from .locate_device import locate_device_request_builder
from .logout_shared_apple_device_active_user import logout_shared_apple_device_active_user_request_builder
from .reboot_now import reboot_now_request_builder
from .recover_passcode import recover_passcode_request_builder
from .remote_lock import remote_lock_request_builder
from .request_remote_assistance import request_remote_assistance_request_builder
from .reset_passcode import reset_passcode_request_builder
from .retire import retire_request_builder
from .shut_down import shut_down_request_builder
from .sync_device import sync_device_request_builder
from .update_windows_device_account import update_windows_device_account_request_builder
from .users import users_request_builder
from .windows_defender_scan import windows_defender_scan_request_builder
from .windows_defender_update_signatures import windows_defender_update_signatures_request_builder
from .wipe import wipe_request_builder

class ManagedDeviceItemRequestBuilder():
    """
    Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
    """
    def bypass_activation_lock(self) -> bypass_activation_lock_request_builder.BypassActivationLockRequestBuilder:
        """
        Provides operations to call the bypassActivationLock method.
        """
        return bypass_activation_lock_request_builder.BypassActivationLockRequestBuilder(self.request_adapter, self.path_parameters)

    def clean_windows_device(self) -> clean_windows_device_request_builder.CleanWindowsDeviceRequestBuilder:
        """
        Provides operations to call the cleanWindowsDevice method.
        """
        return clean_windows_device_request_builder.CleanWindowsDeviceRequestBuilder(self.request_adapter, self.path_parameters)

    def delete_user_from_shared_apple_device(self) -> delete_user_from_shared_apple_device_request_builder.DeleteUserFromSharedAppleDeviceRequestBuilder:
        """
        Provides operations to call the deleteUserFromSharedAppleDevice method.
        """
        return delete_user_from_shared_apple_device_request_builder.DeleteUserFromSharedAppleDeviceRequestBuilder(self.request_adapter, self.path_parameters)

    def device_category(self) -> device_category_request_builder.DeviceCategoryRequestBuilder:
        """
        Provides operations to manage the deviceCategory property of the microsoft.graph.managedDevice entity.
        """
        return device_category_request_builder.DeviceCategoryRequestBuilder(self.request_adapter, self.path_parameters)

    def device_compliance_policy_states(self) -> device_compliance_policy_states_request_builder.DeviceCompliancePolicyStatesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyStates property of the microsoft.graph.managedDevice entity.
        """
        return device_compliance_policy_states_request_builder.DeviceCompliancePolicyStatesRequestBuilder(self.request_adapter, self.path_parameters)

    def device_configuration_states(self) -> device_configuration_states_request_builder.DeviceConfigurationStatesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationStates property of the microsoft.graph.managedDevice entity.
        """
        return device_configuration_states_request_builder.DeviceConfigurationStatesRequestBuilder(self.request_adapter, self.path_parameters)

    def disable_lost_mode(self) -> disable_lost_mode_request_builder.DisableLostModeRequestBuilder:
        """
        Provides operations to call the disableLostMode method.
        """
        return disable_lost_mode_request_builder.DisableLostModeRequestBuilder(self.request_adapter, self.path_parameters)

    def locate_device(self) -> locate_device_request_builder.LocateDeviceRequestBuilder:
        """
        Provides operations to call the locateDevice method.
        """
        return locate_device_request_builder.LocateDeviceRequestBuilder(self.request_adapter, self.path_parameters)

    def logout_shared_apple_device_active_user(self) -> logout_shared_apple_device_active_user_request_builder.LogoutSharedAppleDeviceActiveUserRequestBuilder:
        """
        Provides operations to call the logoutSharedAppleDeviceActiveUser method.
        """
        return logout_shared_apple_device_active_user_request_builder.LogoutSharedAppleDeviceActiveUserRequestBuilder(self.request_adapter, self.path_parameters)

    def reboot_now(self) -> reboot_now_request_builder.RebootNowRequestBuilder:
        """
        Provides operations to call the rebootNow method.
        """
        return reboot_now_request_builder.RebootNowRequestBuilder(self.request_adapter, self.path_parameters)

    def recover_passcode(self) -> recover_passcode_request_builder.RecoverPasscodeRequestBuilder:
        """
        Provides operations to call the recoverPasscode method.
        """
        return recover_passcode_request_builder.RecoverPasscodeRequestBuilder(self.request_adapter, self.path_parameters)

    def remote_lock(self) -> remote_lock_request_builder.RemoteLockRequestBuilder:
        """
        Provides operations to call the remoteLock method.
        """
        return remote_lock_request_builder.RemoteLockRequestBuilder(self.request_adapter, self.path_parameters)

    def request_remote_assistance(self) -> request_remote_assistance_request_builder.RequestRemoteAssistanceRequestBuilder:
        """
        Provides operations to call the requestRemoteAssistance method.
        """
        return request_remote_assistance_request_builder.RequestRemoteAssistanceRequestBuilder(self.request_adapter, self.path_parameters)

    def reset_passcode(self) -> reset_passcode_request_builder.ResetPasscodeRequestBuilder:
        """
        Provides operations to call the resetPasscode method.
        """
        return reset_passcode_request_builder.ResetPasscodeRequestBuilder(self.request_adapter, self.path_parameters)

    def retire(self) -> retire_request_builder.RetireRequestBuilder:
        """
        Provides operations to call the retire method.
        """
        return retire_request_builder.RetireRequestBuilder(self.request_adapter, self.path_parameters)

    def shut_down(self) -> shut_down_request_builder.ShutDownRequestBuilder:
        """
        Provides operations to call the shutDown method.
        """
        return shut_down_request_builder.ShutDownRequestBuilder(self.request_adapter, self.path_parameters)

    def sync_device(self) -> sync_device_request_builder.SyncDeviceRequestBuilder:
        """
        Provides operations to call the syncDevice method.
        """
        return sync_device_request_builder.SyncDeviceRequestBuilder(self.request_adapter, self.path_parameters)

    def update_windows_device_account(self) -> update_windows_device_account_request_builder.UpdateWindowsDeviceAccountRequestBuilder:
        """
        Provides operations to call the updateWindowsDeviceAccount method.
        """
        return update_windows_device_account_request_builder.UpdateWindowsDeviceAccountRequestBuilder(self.request_adapter, self.path_parameters)

    def users(self) -> users_request_builder.UsersRequestBuilder:
        """
        Provides operations to manage the users property of the microsoft.graph.managedDevice entity.
        """
        return users_request_builder.UsersRequestBuilder(self.request_adapter, self.path_parameters)

    def windows_defender_scan(self) -> windows_defender_scan_request_builder.WindowsDefenderScanRequestBuilder:
        """
        Provides operations to call the windowsDefenderScan method.
        """
        return windows_defender_scan_request_builder.WindowsDefenderScanRequestBuilder(self.request_adapter, self.path_parameters)

    def windows_defender_update_signatures(self) -> windows_defender_update_signatures_request_builder.WindowsDefenderUpdateSignaturesRequestBuilder:
        """
        Provides operations to call the windowsDefenderUpdateSignatures method.
        """
        return windows_defender_update_signatures_request_builder.WindowsDefenderUpdateSignaturesRequestBuilder(self.request_adapter, self.path_parameters)

    def wipe(self) -> wipe_request_builder.WipeRequestBuilder:
        """
        Provides operations to call the wipe method.
        """
        return wipe_request_builder.WipeRequestBuilder(self.request_adapter, self.path_parameters)

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

    def create_delete_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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

    def create_get_request_information(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info

    def create_patch_request_information(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property managedDevices in users
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

    async def delete(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property managedDevices for users
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

    async def get(self,request_configuration: Optional[ManagedDeviceItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[managed_device.ManagedDevice]:
        """
        The managed devices associated with the user.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[managed_device.ManagedDevice]
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
        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, response_handler, error_mapping)

    async def patch(self,body: Optional[managed_device.ManagedDevice] = None, request_configuration: Optional[ManagedDeviceItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[managed_device.ManagedDevice]:
        """
        Update the navigation property managedDevices in users
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[managed_device.ManagedDevice]
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
        return await self.request_adapter.send_async(request_info, managed_device.ManagedDevice, response_handler, error_mapping)

    @dataclass
    class ManagedDeviceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

