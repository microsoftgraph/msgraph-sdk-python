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
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.synchronization_job import SynchronizationJob
    from .bulk_upload.bulk_upload_request_builder import BulkUploadRequestBuilder
    from .pause.pause_request_builder import PauseRequestBuilder
    from .provision_on_demand.provision_on_demand_request_builder import ProvisionOnDemandRequestBuilder
    from .restart.restart_request_builder import RestartRequestBuilder
    from .schema.schema_request_builder import SchemaRequestBuilder
    from .start.start_request_builder import StartRequestBuilder
    from .validate_credentials.validate_credentials_request_builder import ValidateCredentialsRequestBuilder

class SynchronizationJobItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the jobs property of the microsoft.graph.synchronization entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SynchronizationJobItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/applications/{application%2Did}/synchronization/jobs/{synchronizationJob%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property jobs for applications
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SynchronizationJobItemRequestBuilderGetQueryParameters]] = None) -> Optional[SynchronizationJob]:
        """
        Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SynchronizationJob]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.synchronization_job import SynchronizationJob

        return await self.request_adapter.send_async(request_info, SynchronizationJob, error_mapping)
    
    async def patch(self,body: SynchronizationJob, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SynchronizationJob]:
        """
        Update the navigation property jobs in applications
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SynchronizationJob]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.synchronization_job import SynchronizationJob

        return await self.request_adapter.send_async(request_info, SynchronizationJob, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property jobs for applications
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SynchronizationJobItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: SynchronizationJob, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property jobs in applications
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
    
    def with_url(self,raw_url: str) -> SynchronizationJobItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SynchronizationJobItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SynchronizationJobItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk_upload(self) -> BulkUploadRequestBuilder:
        """
        Provides operations to manage the bulkUpload property of the microsoft.graph.synchronizationJob entity.
        """
        from .bulk_upload.bulk_upload_request_builder import BulkUploadRequestBuilder

        return BulkUploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pause(self) -> PauseRequestBuilder:
        """
        Provides operations to call the pause method.
        """
        from .pause.pause_request_builder import PauseRequestBuilder

        return PauseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def provision_on_demand(self) -> ProvisionOnDemandRequestBuilder:
        """
        Provides operations to call the provisionOnDemand method.
        """
        from .provision_on_demand.provision_on_demand_request_builder import ProvisionOnDemandRequestBuilder

        return ProvisionOnDemandRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restart(self) -> RestartRequestBuilder:
        """
        Provides operations to call the restart method.
        """
        from .restart.restart_request_builder import RestartRequestBuilder

        return RestartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schema(self) -> SchemaRequestBuilder:
        """
        Provides operations to manage the schema property of the microsoft.graph.synchronizationJob entity.
        """
        from .schema.schema_request_builder import SchemaRequestBuilder

        return SchemaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start(self) -> StartRequestBuilder:
        """
        Provides operations to call the start method.
        """
        from .start.start_request_builder import StartRequestBuilder

        return StartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_credentials(self) -> ValidateCredentialsRequestBuilder:
        """
        Provides operations to call the validateCredentials method.
        """
        from .validate_credentials.validate_credentials_request_builder import ValidateCredentialsRequestBuilder

        return ValidateCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SynchronizationJobItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SynchronizationJobItemRequestBuilderGetQueryParameters():
        """
        Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class SynchronizationJobItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SynchronizationJobItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SynchronizationJobItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

