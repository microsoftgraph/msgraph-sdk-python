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
    from ...........models.o_data_errors.o_data_error import ODataError
    from ...........models.workbook_table_column import WorkbookTableColumn
    from ...........models.workbook_table_column_collection_response import WorkbookTableColumnCollectionResponse
    from .add.add_request_builder import AddRequestBuilder
    from .count.count_request_builder import CountRequestBuilder
    from .item.workbook_table_column_item_request_builder import WorkbookTableColumnItemRequestBuilder
    from .item_at_with_index.item_at_with_index_request_builder import ItemAtWithIndexRequestBuilder

class ColumnsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the columns property of the microsoft.graph.workbookTable entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ColumnsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/tables/{workbookTable%2Did}/columns{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_workbook_table_column_id(self,workbook_table_column_id: str) -> WorkbookTableColumnItemRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.workbookTable entity.
        param workbook_table_column_id: The unique identifier of workbookTableColumn
        Returns: WorkbookTableColumnItemRequestBuilder
        """
        if workbook_table_column_id is None:
            raise TypeError("workbook_table_column_id cannot be null.")
        from .item.workbook_table_column_item_request_builder import WorkbookTableColumnItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookTableColumn%2Did"] = workbook_table_column_id
        return WorkbookTableColumnItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ColumnsRequestBuilderGetQueryParameters]] = None) -> Optional[WorkbookTableColumnCollectionResponse]:
        """
        The list of all the columns in the table. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookTableColumnCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...........models.workbook_table_column_collection_response import WorkbookTableColumnCollectionResponse

        return await self.request_adapter.send_async(request_info, WorkbookTableColumnCollectionResponse, error_mapping)
    
    def item_at_with_index(self,index: int) -> ItemAtWithIndexRequestBuilder:
        """
        Provides operations to call the itemAt method.
        param index: Usage: index={index}
        Returns: ItemAtWithIndexRequestBuilder
        """
        if index is None:
            raise TypeError("index cannot be null.")
        from .item_at_with_index.item_at_with_index_request_builder import ItemAtWithIndexRequestBuilder

        return ItemAtWithIndexRequestBuilder(self.request_adapter, self.path_parameters, index)
    
    async def post(self,body: WorkbookTableColumn, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WorkbookTableColumn]:
        """
        Create new navigation property to columns for drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookTableColumn]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...........models.workbook_table_column import WorkbookTableColumn

        return await self.request_adapter.send_async(request_info, WorkbookTableColumn, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ColumnsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The list of all the columns in the table. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: WorkbookTableColumn, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to columns for drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ColumnsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ColumnsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ColumnsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def add(self) -> AddRequestBuilder:
        """
        Provides operations to call the add method.
        """
        from .add.add_request_builder import AddRequestBuilder

        return AddRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to call the count method.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ColumnsRequestBuilderGetQueryParameters():
        """
        The list of all the columns in the table. Read-only.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[list[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[list[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class ColumnsRequestBuilderGetRequestConfiguration(RequestConfiguration[ColumnsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ColumnsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

