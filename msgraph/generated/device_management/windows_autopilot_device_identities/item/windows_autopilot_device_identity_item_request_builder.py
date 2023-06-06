from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import windows_autopilot_device_identity
    from ....models.o_data_errors import o_data_error
    from .assign_user_to_device import assign_user_to_device_request_builder
    from .unassign_user_from_device import unassign_user_from_device_request_builder
    from .update_device_properties import update_device_properties_request_builder

class WindowsAutopilotDeviceIdentityItemRequestBuilder():
    """
    Provides operations to manage the windowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WindowsAutopilotDeviceIdentityItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/windowsAutopilotDeviceIdentities/{windowsAutopilotDeviceIdentity%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property windowsAutopilotDeviceIdentities for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderGetRequestConfiguration] = None) -> Optional[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]:
        """
        The Windows autopilot device identities contained collection.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import windows_autopilot_device_identity

        return await self.request_adapter.send_async(request_info, windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity, error_mapping)
    
    async def patch(self,body: Optional[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity] = None, request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]:
        """
        Update the navigation property windowsAutopilotDeviceIdentities in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import windows_autopilot_device_identity

        return await self.request_adapter.send_async(request_info, windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property windowsAutopilotDeviceIdentities for deviceManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The Windows autopilot device identities contained collection.
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
    
    def to_patch_request_information(self,body: Optional[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity] = None, request_configuration: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property windowsAutopilotDeviceIdentities in deviceManagement
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
    def assign_user_to_device(self) -> assign_user_to_device_request_builder.AssignUserToDeviceRequestBuilder:
        """
        Provides operations to call the assignUserToDevice method.
        """
        from .assign_user_to_device import assign_user_to_device_request_builder

        return assign_user_to_device_request_builder.AssignUserToDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unassign_user_from_device(self) -> unassign_user_from_device_request_builder.UnassignUserFromDeviceRequestBuilder:
        """
        Provides operations to call the unassignUserFromDevice method.
        """
        from .unassign_user_from_device import unassign_user_from_device_request_builder

        return unassign_user_from_device_request_builder.UnassignUserFromDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_device_properties(self) -> update_device_properties_request_builder.UpdateDevicePropertiesRequestBuilder:
        """
        Provides operations to call the updateDeviceProperties method.
        """
        from .update_device_properties import update_device_properties_request_builder

        return update_device_properties_request_builder.UpdateDevicePropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WindowsAutopilotDeviceIdentityItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WindowsAutopilotDeviceIdentityItemRequestBuilderGetQueryParameters():
        """
        The Windows autopilot device identities contained collection.
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
    class WindowsAutopilotDeviceIdentityItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WindowsAutopilotDeviceIdentityItemRequestBuilder.WindowsAutopilotDeviceIdentityItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class WindowsAutopilotDeviceIdentityItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

