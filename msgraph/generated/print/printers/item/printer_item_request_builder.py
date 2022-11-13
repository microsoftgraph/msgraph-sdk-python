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

from ....models import printer
from ....models.o_data_errors import o_data_error
from .connectors import connectors_request_builder
from .connectors.item import print_connector_item_request_builder
from .restore_factory_defaults import restore_factory_defaults_request_builder
from .shares import shares_request_builder
from .shares.item import printer_share_item_request_builder
from .task_triggers import task_triggers_request_builder
from .task_triggers.item import print_task_trigger_item_request_builder

class PrinterItemRequestBuilder():
    """
    Provides operations to manage the printers property of the microsoft.graph.print entity.
    """
    def connectors(self) -> connectors_request_builder.ConnectorsRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.printer entity.
        """
        return connectors_request_builder.ConnectorsRequestBuilder(self.request_adapter, self.path_parameters)

    def restore_factory_defaults(self) -> restore_factory_defaults_request_builder.RestoreFactoryDefaultsRequestBuilder:
        """
        Provides operations to call the restoreFactoryDefaults method.
        """
        return restore_factory_defaults_request_builder.RestoreFactoryDefaultsRequestBuilder(self.request_adapter, self.path_parameters)

    def shares(self) -> shares_request_builder.SharesRequestBuilder:
        """
        Provides operations to manage the shares property of the microsoft.graph.printer entity.
        """
        return shares_request_builder.SharesRequestBuilder(self.request_adapter, self.path_parameters)

    def task_triggers(self) -> task_triggers_request_builder.TaskTriggersRequestBuilder:
        """
        Provides operations to manage the taskTriggers property of the microsoft.graph.printer entity.
        """
        return task_triggers_request_builder.TaskTriggersRequestBuilder(self.request_adapter, self.path_parameters)

    def connectors_by_id(self,id: str) -> print_connector_item_request_builder.PrintConnectorItemRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.printer entity.
        Args:
            id: Unique identifier of the item
        Returns: print_connector_item_request_builder.PrintConnectorItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printConnector%2Did"] = id
        return print_connector_item_request_builder.PrintConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrinterItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise Exception("path_parameters cannot be undefined")
        if not request_adapter:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/print/printers/{printer%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def create_delete_request_information(self,request_configuration: Optional[PrinterItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property printers for print
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

    def create_get_request_information(self,request_configuration: Optional[PrinterItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The list of printers registered in the tenant.
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

    def create_patch_request_information(self,body: Optional[printer.Printer] = None, request_configuration: Optional[PrinterItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property printers in print
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
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

    async def delete(self,request_configuration: Optional[PrinterItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property printers for print
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)

    async def get(self,request_configuration: Optional[PrinterItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[printer.Printer]:
        """
        The list of printers registered in the tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[printer.Printer]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, printer.Printer, response_handler, error_mapping)

    async def patch(self,body: Optional[printer.Printer] = None, request_configuration: Optional[PrinterItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[printer.Printer]:
        """
        Update the navigation property printers in print
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[printer.Printer]
        """
        if not body:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, printer.Printer, response_handler, error_mapping)

    def shares_by_id(self,id: str) -> printer_share_item_request_builder.PrinterShareItemRequestBuilder:
        """
        Provides operations to manage the shares property of the microsoft.graph.printer entity.
        Args:
            id: Unique identifier of the item
        Returns: printer_share_item_request_builder.PrinterShareItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printerShare%2Did"] = id
        return printer_share_item_request_builder.PrinterShareItemRequestBuilder(self.request_adapter, url_tpl_params)

    def task_triggers_by_id(self,id: str) -> print_task_trigger_item_request_builder.PrintTaskTriggerItemRequestBuilder:
        """
        Provides operations to manage the taskTriggers property of the microsoft.graph.printer entity.
        Args:
            id: Unique identifier of the item
        Returns: print_task_trigger_item_request_builder.PrintTaskTriggerItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printTaskTrigger%2Did"] = id
        return print_task_trigger_item_request_builder.PrintTaskTriggerItemRequestBuilder(self.request_adapter, url_tpl_params)

    @dataclass
    class PrinterItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PrinterItemRequestBuilderGetQueryParameters():
        """
        The list of printers registered in the tenant.
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
            if not original_name:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name

    
    @dataclass
    class PrinterItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PrinterItemRequestBuilder.PrinterItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PrinterItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

