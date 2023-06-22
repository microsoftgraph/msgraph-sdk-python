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
    from ......models import synchronization_job
    from ......models.o_data_errors import o_data_error
    from .pause import pause_request_builder
    from .provision_on_demand import provision_on_demand_request_builder
    from .restart import restart_request_builder
    from .schema import schema_request_builder
    from .start import start_request_builder
    from .validate_credentials import validate_credentials_request_builder

class SynchronizationJobItemRequestBuilder():
    """
    Provides operations to manage the jobs property of the microsoft.graph.synchronization entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SynchronizationJobItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/applications/{application%2Did}/synchronization/jobs/{synchronizationJob%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[SynchronizationJobItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property jobs for applications
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[SynchronizationJobItemRequestBuilderGetRequestConfiguration] = None) -> Optional[synchronization_job.SynchronizationJob]:
        """
        Get jobs from applications
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[synchronization_job.SynchronizationJob]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import synchronization_job

        return await self.request_adapter.send_async(request_info, synchronization_job.SynchronizationJob, error_mapping)
    
    async def patch(self,body: Optional[synchronization_job.SynchronizationJob] = None, request_configuration: Optional[SynchronizationJobItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[synchronization_job.SynchronizationJob]:
        """
        Update the navigation property jobs in applications
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[synchronization_job.SynchronizationJob]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import synchronization_job

        return await self.request_adapter.send_async(request_info, synchronization_job.SynchronizationJob, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SynchronizationJobItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property jobs for applications
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
    
    def to_get_request_information(self,request_configuration: Optional[SynchronizationJobItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get jobs from applications
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
    
    def to_patch_request_information(self,body: Optional[synchronization_job.SynchronizationJob] = None, request_configuration: Optional[SynchronizationJobItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property jobs in applications
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    def pause(self) -> pause_request_builder.PauseRequestBuilder:
        """
        Provides operations to call the pause method.
        """
        from .pause import pause_request_builder

        return pause_request_builder.PauseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def provision_on_demand(self) -> provision_on_demand_request_builder.ProvisionOnDemandRequestBuilder:
        """
        Provides operations to call the provisionOnDemand method.
        """
        from .provision_on_demand import provision_on_demand_request_builder

        return provision_on_demand_request_builder.ProvisionOnDemandRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restart(self) -> restart_request_builder.RestartRequestBuilder:
        """
        Provides operations to call the restart method.
        """
        from .restart import restart_request_builder

        return restart_request_builder.RestartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schema(self) -> schema_request_builder.SchemaRequestBuilder:
        """
        Provides operations to manage the schema property of the microsoft.graph.synchronizationJob entity.
        """
        from .schema import schema_request_builder

        return schema_request_builder.SchemaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start(self) -> start_request_builder.StartRequestBuilder:
        """
        Provides operations to call the start method.
        """
        from .start import start_request_builder

        return start_request_builder.StartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_credentials(self) -> validate_credentials_request_builder.ValidateCredentialsRequestBuilder:
        """
        Provides operations to call the validateCredentials method.
        """
        from .validate_credentials import validate_credentials_request_builder

        return validate_credentials_request_builder.ValidateCredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SynchronizationJobItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SynchronizationJobItemRequestBuilderGetQueryParameters():
        """
        Get jobs from applications
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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
    class SynchronizationJobItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SynchronizationJobItemRequestBuilder.SynchronizationJobItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SynchronizationJobItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

