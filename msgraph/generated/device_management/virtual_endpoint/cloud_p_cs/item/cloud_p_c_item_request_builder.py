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
    from .....models.cloud_p_c import CloudPC
    from .....models.o_data_errors.o_data_error import ODataError
    from .end_grace_period.end_grace_period_request_builder import EndGracePeriodRequestBuilder
    from .reboot.reboot_request_builder import RebootRequestBuilder
    from .rename.rename_request_builder import RenameRequestBuilder
    from .reprovision.reprovision_request_builder import ReprovisionRequestBuilder
    from .resize.resize_request_builder import ResizeRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .retrieve_cloud_pc_launch_detail.retrieve_cloud_pc_launch_detail_request_builder import RetrieveCloudPcLaunchDetailRequestBuilder
    from .troubleshoot.troubleshoot_request_builder import TroubleshootRequestBuilder

class CloudPCItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the cloudPCs property of the microsoft.graph.virtualEndpoint entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CloudPCItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/cloudPCs/{cloudPC%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property cloudPCs for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CloudPCItemRequestBuilderGetQueryParameters]] = None) -> Optional[CloudPC]:
        """
        Read the properties and relationships of a specific cloudPC object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPC]
        Find more info here: https://learn.microsoft.com/graph/api/cloudpc-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.cloud_p_c import CloudPC

        return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)
    
    async def patch(self,body: CloudPC, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CloudPC]:
        """
        Update the navigation property cloudPCs in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPC]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.cloud_p_c import CloudPC

        return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property cloudPCs for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CloudPCItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of a specific cloudPC object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CloudPC, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property cloudPCs in deviceManagement
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
    
    def with_url(self,raw_url: str) -> CloudPCItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CloudPCItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CloudPCItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def end_grace_period(self) -> EndGracePeriodRequestBuilder:
        """
        Provides operations to call the endGracePeriod method.
        """
        from .end_grace_period.end_grace_period_request_builder import EndGracePeriodRequestBuilder

        return EndGracePeriodRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot(self) -> RebootRequestBuilder:
        """
        Provides operations to call the reboot method.
        """
        from .reboot.reboot_request_builder import RebootRequestBuilder

        return RebootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rename(self) -> RenameRequestBuilder:
        """
        Provides operations to call the rename method.
        """
        from .rename.rename_request_builder import RenameRequestBuilder

        return RenameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprovision(self) -> ReprovisionRequestBuilder:
        """
        Provides operations to call the reprovision method.
        """
        from .reprovision.reprovision_request_builder import ReprovisionRequestBuilder

        return ReprovisionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resize(self) -> ResizeRequestBuilder:
        """
        Provides operations to call the resize method.
        """
        from .resize.resize_request_builder import ResizeRequestBuilder

        return ResizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retrieve_cloud_pc_launch_detail(self) -> RetrieveCloudPcLaunchDetailRequestBuilder:
        """
        Provides operations to call the retrieveCloudPcLaunchDetail method.
        """
        from .retrieve_cloud_pc_launch_detail.retrieve_cloud_pc_launch_detail_request_builder import RetrieveCloudPcLaunchDetailRequestBuilder

        return RetrieveCloudPcLaunchDetailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def troubleshoot(self) -> TroubleshootRequestBuilder:
        """
        Provides operations to call the troubleshoot method.
        """
        from .troubleshoot.troubleshoot_request_builder import TroubleshootRequestBuilder

        return TroubleshootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CloudPCItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CloudPCItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a specific cloudPC object.
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
    class CloudPCItemRequestBuilderGetRequestConfiguration(RequestConfiguration[CloudPCItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CloudPCItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

