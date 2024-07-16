from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
    from ....models.o_data_errors.o_data_error import ODataError
    from .assign.assign_request_builder import AssignRequestBuilder
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .device_statuses.device_statuses_request_builder import DeviceStatusesRequestBuilder
    from .device_status_summary.device_status_summary_request_builder import DeviceStatusSummaryRequestBuilder
    from .user_statuses.user_statuses_request_builder import UserStatusesRequestBuilder
    from .user_status_summary.user_status_summary_request_builder import UserStatusSummaryRequestBuilder

class ManagedDeviceMobileAppConfigurationItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the mobileAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ManagedDeviceMobileAppConfigurationItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mobileAppConfigurations/{managedDeviceMobileAppConfiguration%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes a iosMobileAppConfiguration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/intune-apps-iosmobileappconfiguration-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ManagedDeviceMobileAppConfigurationItemRequestBuilderGetQueryParameters]] = None) -> Optional[ManagedDeviceMobileAppConfiguration]:
        """
        Read properties and relationships of the managedDeviceMobileAppConfiguration object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedDeviceMobileAppConfiguration]
        Find more info here: https://learn.microsoft.com/graph/api/intune-apps-manageddevicemobileappconfiguration-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

        return await self.request_adapter.send_async(request_info, ManagedDeviceMobileAppConfiguration, error_mapping)
    
    async def patch(self,body: ManagedDeviceMobileAppConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ManagedDeviceMobileAppConfiguration]:
        """
        Update the properties of a iosMobileAppConfiguration object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ManagedDeviceMobileAppConfiguration]
        Find more info here: https://learn.microsoft.com/graph/api/intune-apps-iosmobileappconfiguration-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

        return await self.request_adapter.send_async(request_info, ManagedDeviceMobileAppConfiguration, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a iosMobileAppConfiguration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ManagedDeviceMobileAppConfigurationItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read properties and relationships of the managedDeviceMobileAppConfiguration object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ManagedDeviceMobileAppConfiguration, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of a iosMobileAppConfiguration object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ManagedDeviceMobileAppConfigurationItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ManagedDeviceMobileAppConfigurationItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ManagedDeviceMobileAppConfigurationItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assign(self) -> AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        from .assign.assign_request_builder import AssignRequestBuilder

        return AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_status_summary(self) -> DeviceStatusSummaryRequestBuilder:
        """
        Provides operations to manage the deviceStatusSummary property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        """
        from .device_status_summary.device_status_summary_request_builder import DeviceStatusSummaryRequestBuilder

        return DeviceStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_statuses(self) -> DeviceStatusesRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        """
        from .device_statuses.device_statuses_request_builder import DeviceStatusesRequestBuilder

        return DeviceStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_status_summary(self) -> UserStatusSummaryRequestBuilder:
        """
        Provides operations to manage the userStatusSummary property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        """
        from .user_status_summary.user_status_summary_request_builder import UserStatusSummaryRequestBuilder

        return UserStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_statuses(self) -> UserStatusesRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.managedDeviceMobileAppConfiguration entity.
        """
        from .user_statuses.user_statuses_request_builder import UserStatusesRequestBuilder

        return UserStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ManagedDeviceMobileAppConfigurationItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManagedDeviceMobileAppConfigurationItemRequestBuilderGetQueryParameters():
        """
        Read properties and relationships of the managedDeviceMobileAppConfiguration object.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
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
    class ManagedDeviceMobileAppConfigurationItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ManagedDeviceMobileAppConfigurationItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ManagedDeviceMobileAppConfigurationItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

