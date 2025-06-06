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
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.print_task import PrintTask
    from .definition.definition_request_builder import DefinitionRequestBuilder
    from .trigger.trigger_request_builder import TriggerRequestBuilder

class PrintTaskItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the tasks property of the microsoft.graph.printTaskDefinition entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PrintTaskItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/print/taskDefinitions/{printTaskDefinition%2Did}/tasks/{printTask%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property tasks for print
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PrintTaskItemRequestBuilderGetQueryParameters]] = None) -> Optional[PrintTask]:
        """
        Get details about a print task. For details about how to use this API to add pull printing support to Universal Print, see Extending Universal Print to support pull printing.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrintTask]
        Find more info here: https://learn.microsoft.com/graph/api/printtask-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.print_task import PrintTask

        return await self.request_adapter.send_async(request_info, PrintTask, error_mapping)
    
    async def patch(self,body: PrintTask, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PrintTask]:
        """
        Update a print task. For details about how to use this API to add pull printing support to Universal Print, see Extending Universal Print to support pull printing.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrintTask]
        Find more info here: https://learn.microsoft.com/graph/api/printtaskdefinition-update-task?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.print_task import PrintTask

        return await self.request_adapter.send_async(request_info, PrintTask, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property tasks for print
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PrintTaskItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get details about a print task. For details about how to use this API to add pull printing support to Universal Print, see Extending Universal Print to support pull printing.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: PrintTask, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update a print task. For details about how to use this API to add pull printing support to Universal Print, see Extending Universal Print to support pull printing.
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
    
    def with_url(self,raw_url: str) -> PrintTaskItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PrintTaskItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PrintTaskItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def definition(self) -> DefinitionRequestBuilder:
        """
        Provides operations to manage the definition property of the microsoft.graph.printTask entity.
        """
        from .definition.definition_request_builder import DefinitionRequestBuilder

        return DefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trigger(self) -> TriggerRequestBuilder:
        """
        Provides operations to manage the trigger property of the microsoft.graph.printTask entity.
        """
        from .trigger.trigger_request_builder import TriggerRequestBuilder

        return TriggerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PrintTaskItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PrintTaskItemRequestBuilderGetQueryParameters():
        """
        Get details about a print task. For details about how to use this API to add pull printing support to Universal Print, see Extending Universal Print to support pull printing.
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
    class PrintTaskItemRequestBuilderGetRequestConfiguration(RequestConfiguration[PrintTaskItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PrintTaskItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

