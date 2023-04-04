from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.external_connectors import external_connection
    from ....models.o_data_errors import o_data_error
    from .groups import groups_request_builder
    from .groups.item import external_group_item_request_builder
    from .items import items_request_builder
    from .items.item import external_item_item_request_builder
    from .operations import operations_request_builder
    from .operations.item import connection_operation_item_request_builder
    from .schema import schema_request_builder

class ExternalConnectionItemRequestBuilder():
    """
    Provides operations to manage the connections property of the microsoft.graph.externalConnectors.external entity.
    """
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
        self.url_template: str = "{+baseurl}/external/connections/{externalConnection%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ExternalConnectionItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property connections for external
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
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
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def get(self,request_configuration: Optional[ExternalConnectionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[external_connection.ExternalConnection]:
        """
        Get connections from external
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[external_connection.ExternalConnection]
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
        from ....models.external_connectors import external_connection

        return await self.request_adapter.send_async(request_info, external_connection.ExternalConnection, error_mapping)
    
    def groups_by_id(self,id: str) -> external_group_item_request_builder.ExternalGroupItemRequestBuilder:
        """
        Provides operations to manage the groups property of the microsoft.graph.externalConnectors.externalConnection entity.
        Args:
            id: Unique identifier of the item
        Returns: external_group_item_request_builder.ExternalGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .groups.item import external_group_item_request_builder

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
        from .items.item import external_item_item_request_builder

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
        from .operations.item import connection_operation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["connectionOperation%2Did"] = id
        return connection_operation_item_request_builder.ConnectionOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[external_connection.ExternalConnection] = None, request_configuration: Optional[ExternalConnectionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[external_connection.ExternalConnection]:
        """
        Update the navigation property connections in external
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[external_connection.ExternalConnection]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.external_connectors import external_connection

        return await self.request_adapter.send_async(request_info, external_connection.ExternalConnection, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ExternalConnectionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property connections for external
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
    
    def to_get_request_information(self,request_configuration: Optional[ExternalConnectionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get connections from external
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
    
    def to_patch_request_information(self,body: Optional[external_connection.ExternalConnection] = None, request_configuration: Optional[ExternalConnectionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property connections in external
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
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
    def groups(self) -> groups_request_builder.GroupsRequestBuilder:
        """
        Provides operations to manage the groups property of the microsoft.graph.externalConnectors.externalConnection entity.
        """
        from .groups import groups_request_builder

        return groups_request_builder.GroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.externalConnectors.externalConnection entity.
        """
        from .items import items_request_builder

        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.externalConnectors.externalConnection entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schema(self) -> schema_request_builder.SchemaRequestBuilder:
        """
        Provides operations to manage the schema property of the microsoft.graph.externalConnectors.externalConnection entity.
        """
        from .schema import schema_request_builder

        return schema_request_builder.SchemaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ExternalConnectionItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ExternalConnectionItemRequestBuilderGetQueryParameters():
        """
        Get connections from external
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class ExternalConnectionItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

