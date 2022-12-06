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

print = lazy_import('msgraph.generated.models.print')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
connectors_request_builder = lazy_import('msgraph.generated.print.connectors.connectors_request_builder')
print_connector_item_request_builder = lazy_import('msgraph.generated.print.connectors.item.print_connector_item_request_builder')
operations_request_builder = lazy_import('msgraph.generated.print.operations.operations_request_builder')
print_operation_item_request_builder = lazy_import('msgraph.generated.print.operations.item.print_operation_item_request_builder')
printers_request_builder = lazy_import('msgraph.generated.print.printers.printers_request_builder')
printer_item_request_builder = lazy_import('msgraph.generated.print.printers.item.printer_item_request_builder')
services_request_builder = lazy_import('msgraph.generated.print.services.services_request_builder')
print_service_item_request_builder = lazy_import('msgraph.generated.print.services.item.print_service_item_request_builder')
shares_request_builder = lazy_import('msgraph.generated.print.shares.shares_request_builder')
printer_share_item_request_builder = lazy_import('msgraph.generated.print.shares.item.printer_share_item_request_builder')
task_definitions_request_builder = lazy_import('msgraph.generated.print.task_definitions.task_definitions_request_builder')
print_task_definition_item_request_builder = lazy_import('msgraph.generated.print.task_definitions.item.print_task_definition_item_request_builder')

class PrintRequestBuilder():
    """
    Provides operations to manage the print singleton.
    """
    def connectors(self) -> connectors_request_builder.ConnectorsRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.print entity.
        """
        return connectors_request_builder.ConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.print entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def printers(self) -> printers_request_builder.PrintersRequestBuilder:
        """
        Provides operations to manage the printers property of the microsoft.graph.print entity.
        """
        return printers_request_builder.PrintersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def services(self) -> services_request_builder.ServicesRequestBuilder:
        """
        Provides operations to manage the services property of the microsoft.graph.print entity.
        """
        return services_request_builder.ServicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def shares(self) -> shares_request_builder.SharesRequestBuilder:
        """
        Provides operations to manage the shares property of the microsoft.graph.print entity.
        """
        return shares_request_builder.SharesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def task_definitions(self) -> task_definitions_request_builder.TaskDefinitionsRequestBuilder:
        """
        Provides operations to manage the taskDefinitions property of the microsoft.graph.print entity.
        """
        return task_definitions_request_builder.TaskDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def connectors_by_id(self,id: str) -> print_connector_item_request_builder.PrintConnectorItemRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.print entity.
        Args:
            id: Unique identifier of the item
        Returns: print_connector_item_request_builder.PrintConnectorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printConnector%2Did"] = id
        return print_connector_item_request_builder.PrintConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrintRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/print{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[PrintRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get print
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
    
    def create_patch_request_information(self,body: Optional[print.Print] = None, request_configuration: Optional[PrintRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update print
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
    
    async def get(self,request_configuration: Optional[PrintRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[print.Print]:
        """
        Get print
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[print.Print]
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
        return await self.request_adapter.send_async(request_info, print.Print, response_handler, error_mapping)
    
    def operations_by_id(self,id: str) -> print_operation_item_request_builder.PrintOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.print entity.
        Args:
            id: Unique identifier of the item
        Returns: print_operation_item_request_builder.PrintOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printOperation%2Did"] = id
        return print_operation_item_request_builder.PrintOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[print.Print] = None, request_configuration: Optional[PrintRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[print.Print]:
        """
        Update print
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[print.Print]
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
        return await self.request_adapter.send_async(request_info, print.Print, response_handler, error_mapping)
    
    def printers_by_id(self,id: str) -> printer_item_request_builder.PrinterItemRequestBuilder:
        """
        Provides operations to manage the printers property of the microsoft.graph.print entity.
        Args:
            id: Unique identifier of the item
        Returns: printer_item_request_builder.PrinterItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printer%2Did"] = id
        return printer_item_request_builder.PrinterItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def services_by_id(self,id: str) -> print_service_item_request_builder.PrintServiceItemRequestBuilder:
        """
        Provides operations to manage the services property of the microsoft.graph.print entity.
        Args:
            id: Unique identifier of the item
        Returns: print_service_item_request_builder.PrintServiceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printService%2Did"] = id
        return print_service_item_request_builder.PrintServiceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def shares_by_id(self,id: str) -> printer_share_item_request_builder.PrinterShareItemRequestBuilder:
        """
        Provides operations to manage the shares property of the microsoft.graph.print entity.
        Args:
            id: Unique identifier of the item
        Returns: printer_share_item_request_builder.PrinterShareItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printerShare%2Did"] = id
        return printer_share_item_request_builder.PrinterShareItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def task_definitions_by_id(self,id: str) -> print_task_definition_item_request_builder.PrintTaskDefinitionItemRequestBuilder:
        """
        Provides operations to manage the taskDefinitions property of the microsoft.graph.print entity.
        Args:
            id: Unique identifier of the item
        Returns: print_task_definition_item_request_builder.PrintTaskDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printTaskDefinition%2Did"] = id
        return print_task_definition_item_request_builder.PrintTaskDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class PrintRequestBuilderGetQueryParameters():
        """
        Get print
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
    class PrintRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PrintRequestBuilder.PrintRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PrintRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

