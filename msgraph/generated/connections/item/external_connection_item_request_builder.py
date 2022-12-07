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

groups_request_builder = lazy_import('msgraph.generated.connections.item.groups.groups_request_builder')
external_group_item_request_builder = lazy_import('msgraph.generated.connections.item.groups.item.external_group_item_request_builder')
items_request_builder = lazy_import('msgraph.generated.connections.item.items.items_request_builder')
external_item_item_request_builder = lazy_import('msgraph.generated.connections.item.items.item.external_item_item_request_builder')
operations_request_builder = lazy_import('msgraph.generated.connections.item.operations.operations_request_builder')
connection_operation_item_request_builder = lazy_import('msgraph.generated.connections.item.operations.item.connection_operation_item_request_builder')
schema_request_builder = lazy_import('msgraph.generated.connections.item.schema.schema_request_builder')
external_connection = lazy_import('msgraph.generated.models.external_connectors.external_connection')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ExternalConnectionItemRequestBuilder():
    """
    Provides operations to manage the collection of externalConnection entities.
    """
    def groups(self) -> groups_request_builder.GroupsRequestBuilder:
        """
        Provides operations to manage the groups property of the microsoft.graph.externalConnectors.externalConnection entity.
        """
        return groups_request_builder.GroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.externalConnectors.externalConnection entity.
        """
        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.externalConnectors.externalConnection entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def schema(self) -> schema_request_builder.SchemaRequestBuilder:
        """
        Provides operations to manage the schema property of the microsoft.graph.externalConnectors.externalConnection entity.
        """
        return schema_request_builder.SchemaRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ExternalConnectionItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/connections/{externalConnection%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ExternalConnectionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from connections
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
    
    def create_get_request_information(self,request_configuration: Optional[ExternalConnectionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get entity from connections by key
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
    
    def create_patch_request_information(self,body: Optional[external_connection.ExternalConnection] = None, request_configuration: Optional[ExternalConnectionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in connections
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
    
    async def delete(self,request_configuration: Optional[ExternalConnectionItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete entity from connections
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[ExternalConnectionItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[external_connection.ExternalConnection]:
        """
        Get entity from connections by key
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[external_connection.ExternalConnection]
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
        return await self.request_adapter.send_async(request_info, external_connection.ExternalConnection, response_handler, error_mapping)
    
    def groups_by_id(self,id: str) -> external_group_item_request_builder.ExternalGroupItemRequestBuilder:
        """
        Provides operations to manage the groups property of the microsoft.graph.externalConnectors.externalConnection entity.
        Args:
            id: Unique identifier of the item
        Returns: external_group_item_request_builder.ExternalGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["externalGroup%2Did"] = id
        return external_group_item_request_builder.ExternalGroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def items_by_id(self,id: str) -> external_item_item_request_builder.ExternalItemItemRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.externalConnectors.externalConnection entity.
        Args:
            id: Unique identifier of the item
        Returns: external_item_item_request_builder.ExternalItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["externalItem%2Did"] = id
        return external_item_item_request_builder.ExternalItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> connection_operation_item_request_builder.ConnectionOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.externalConnectors.externalConnection entity.
        Args:
            id: Unique identifier of the item
        Returns: connection_operation_item_request_builder.ConnectionOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["connectionOperation%2Did"] = id
        return connection_operation_item_request_builder.ConnectionOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[external_connection.ExternalConnection] = None, request_configuration: Optional[ExternalConnectionItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[external_connection.ExternalConnection]:
        """
        Update entity in connections
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[external_connection.ExternalConnection]
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
        return await self.request_adapter.send_async(request_info, external_connection.ExternalConnection, response_handler, error_mapping)
    
    @dataclass
    class ExternalConnectionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ExternalConnectionItemRequestBuilderGetQueryParameters():
        """
        Get entity from connections by key
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
    class ExternalConnectionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ExternalConnectionItemRequestBuilder.ExternalConnectionItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ExternalConnectionItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

