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
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.print import Print
    from .connectors.connectors_request_builder import ConnectorsRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .printers.printers_request_builder import PrintersRequestBuilder
    from .services.services_request_builder import ServicesRequestBuilder
    from .shares.shares_request_builder import SharesRequestBuilder
    from .task_definitions.task_definitions_request_builder import TaskDefinitionsRequestBuilder

class PrintRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the print singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PrintRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/print{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PrintRequestBuilderGetQueryParameters]] = None) -> Optional[Print]:
        """
        Get print
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Print]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.print import Print

        return await self.request_adapter.send_async(request_info, Print, error_mapping)
    
    async def patch(self,body: Print, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Print]:
        """
        Update print
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Print]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.print import Print

        return await self.request_adapter.send_async(request_info, Print, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PrintRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get print
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Print, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update print
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
    
    def with_url(self,raw_url: str) -> PrintRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PrintRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PrintRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def connectors(self) -> ConnectorsRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.print entity.
        """
        from .connectors.connectors_request_builder import ConnectorsRequestBuilder

        return ConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.print entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def printers(self) -> PrintersRequestBuilder:
        """
        Provides operations to manage the printers property of the microsoft.graph.print entity.
        """
        from .printers.printers_request_builder import PrintersRequestBuilder

        return PrintersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def services(self) -> ServicesRequestBuilder:
        """
        Provides operations to manage the services property of the microsoft.graph.print entity.
        """
        from .services.services_request_builder import ServicesRequestBuilder

        return ServicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shares(self) -> SharesRequestBuilder:
        """
        Provides operations to manage the shares property of the microsoft.graph.print entity.
        """
        from .shares.shares_request_builder import SharesRequestBuilder

        return SharesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_definitions(self) -> TaskDefinitionsRequestBuilder:
        """
        Provides operations to manage the taskDefinitions property of the microsoft.graph.print entity.
        """
        from .task_definitions.task_definitions_request_builder import TaskDefinitionsRequestBuilder

        return TaskDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PrintRequestBuilderGetQueryParameters():
        """
        Get print
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
    class PrintRequestBuilderGetRequestConfiguration(RequestConfiguration[PrintRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PrintRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

