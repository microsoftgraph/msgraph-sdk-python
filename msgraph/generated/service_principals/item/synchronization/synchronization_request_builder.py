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
    from ....models import synchronization
    from ....models.o_data_errors import o_data_error
    from .acquire_access_token import acquire_access_token_request_builder
    from .jobs import jobs_request_builder
    from .secrets import secrets_request_builder
    from .templates import templates_request_builder

class SynchronizationRequestBuilder():
    """
    Provides operations to manage the synchronization property of the microsoft.graph.servicePrincipal entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SynchronizationRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/synchronization{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[SynchronizationRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property synchronization for servicePrincipals
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
    
    async def get(self,request_configuration: Optional[SynchronizationRequestBuilderGetRequestConfiguration] = None) -> Optional[synchronization.Synchronization]:
        """
        Get synchronization from servicePrincipals
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[synchronization.Synchronization]
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
        from ....models import synchronization

        return await self.request_adapter.send_async(request_info, synchronization.Synchronization, error_mapping)
    
    async def put(self,body: Optional[synchronization.Synchronization] = None, request_configuration: Optional[SynchronizationRequestBuilderPutRequestConfiguration] = None) -> Optional[synchronization.Synchronization]:
        """
        Update the navigation property synchronization in servicePrincipals
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[synchronization.Synchronization]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import synchronization

        return await self.request_adapter.send_async(request_info, synchronization.Synchronization, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[SynchronizationRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property synchronization for servicePrincipals
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
    
    def to_get_request_information(self,request_configuration: Optional[SynchronizationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get synchronization from servicePrincipals
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
    
    def to_put_request_information(self,body: Optional[synchronization.Synchronization] = None, request_configuration: Optional[SynchronizationRequestBuilderPutRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property synchronization in servicePrincipals
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
        request_info.http_method = Method.PUT
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def acquire_access_token(self) -> acquire_access_token_request_builder.AcquireAccessTokenRequestBuilder:
        """
        Provides operations to call the acquireAccessToken method.
        """
        from .acquire_access_token import acquire_access_token_request_builder

        return acquire_access_token_request_builder.AcquireAccessTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> jobs_request_builder.JobsRequestBuilder:
        """
        Provides operations to manage the jobs property of the microsoft.graph.synchronization entity.
        """
        from .jobs import jobs_request_builder

        return jobs_request_builder.JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def secrets(self) -> secrets_request_builder.SecretsRequestBuilder:
        """
        The secrets property
        """
        from .secrets import secrets_request_builder

        return secrets_request_builder.SecretsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def templates(self) -> templates_request_builder.TemplatesRequestBuilder:
        """
        Provides operations to manage the templates property of the microsoft.graph.synchronization entity.
        """
        from .templates import templates_request_builder

        return templates_request_builder.TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SynchronizationRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class SynchronizationRequestBuilderGetQueryParameters():
        """
        Get synchronization from servicePrincipals
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
    class SynchronizationRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SynchronizationRequestBuilder.SynchronizationRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SynchronizationRequestBuilderPutRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

