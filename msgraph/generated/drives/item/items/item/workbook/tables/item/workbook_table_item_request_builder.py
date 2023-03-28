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

clear_filters_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.clear_filters.clear_filters_request_builder')
columns_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.columns.columns_request_builder')
workbook_table_column_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.columns.item.workbook_table_column_item_request_builder')
convert_to_range_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.convert_to_range.convert_to_range_request_builder')
data_body_range_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.data_body_range.data_body_range_request_builder')
header_row_range_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.header_row_range.header_row_range_request_builder')
range_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.range.range_request_builder')
reapply_filters_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.reapply_filters.reapply_filters_request_builder')
rows_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.rows.rows_request_builder')
workbook_table_row_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.rows.item.workbook_table_row_item_request_builder')
sort_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.sort.sort_request_builder')
total_row_range_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.total_row_range.total_row_range_request_builder')
worksheet_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.worksheet.worksheet_request_builder')
workbook_table = lazy_import('msgraph.generated.models.workbook_table')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class WorkbookTableItemRequestBuilder():
    """
    Provides operations to manage the tables property of the microsoft.graph.workbook entity.
    """
    @property
    def clear_filters(self) -> clear_filters_request_builder.ClearFiltersRequestBuilder:
        """
        Provides operations to call the clearFilters method.
        """
        return clear_filters_request_builder.ClearFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> columns_request_builder.ColumnsRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.workbookTable entity.
        """
        return columns_request_builder.ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def convert_to_range(self) -> convert_to_range_request_builder.ConvertToRangeRequestBuilder:
        """
        Provides operations to call the convertToRange method.
        """
        return convert_to_range_request_builder.ConvertToRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_body_range(self) -> data_body_range_request_builder.DataBodyRangeRequestBuilder:
        """
        Provides operations to call the dataBodyRange method.
        """
        return data_body_range_request_builder.DataBodyRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def header_row_range(self) -> header_row_range_request_builder.HeaderRowRangeRequestBuilder:
        """
        Provides operations to call the headerRowRange method.
        """
        return header_row_range_request_builder.HeaderRowRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def range(self) -> range_request_builder.RangeRequestBuilder:
        """
        Provides operations to call the range method.
        """
        return range_request_builder.RangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reapply_filters(self) -> reapply_filters_request_builder.ReapplyFiltersRequestBuilder:
        """
        Provides operations to call the reapplyFilters method.
        """
        return reapply_filters_request_builder.ReapplyFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rows(self) -> rows_request_builder.RowsRequestBuilder:
        """
        Provides operations to manage the rows property of the microsoft.graph.workbookTable entity.
        """
        return rows_request_builder.RowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sort(self) -> sort_request_builder.SortRequestBuilder:
        """
        Provides operations to manage the sort property of the microsoft.graph.workbookTable entity.
        """
        return sort_request_builder.SortRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def total_row_range(self) -> total_row_range_request_builder.TotalRowRangeRequestBuilder:
        """
        Provides operations to call the totalRowRange method.
        """
        return total_row_range_request_builder.TotalRowRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def worksheet(self) -> worksheet_request_builder.WorksheetRequestBuilder:
        """
        Provides operations to manage the worksheet property of the microsoft.graph.workbookTable entity.
        """
        return worksheet_request_builder.WorksheetRequestBuilder(self.request_adapter, self.path_parameters)
    
    def columns_by_id(self,id: str) -> workbook_table_column_item_request_builder.WorkbookTableColumnItemRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.workbookTable entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_table_column_item_request_builder.WorkbookTableColumnItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookTableColumn%2Did"] = id
        return workbook_table_column_item_request_builder.WorkbookTableColumnItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkbookTableItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/tables/{workbookTable%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[WorkbookTableItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property tables for drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WorkbookTableItemRequestBuilderGetRequestConfiguration] = None) -> Optional[workbook_table.WorkbookTable]:
        """
        Represents a collection of tables associated with the workbook. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_table.WorkbookTable]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, workbook_table.WorkbookTable, error_mapping)
    
    async def patch(self,body: Optional[workbook_table.WorkbookTable] = None, request_configuration: Optional[WorkbookTableItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[workbook_table.WorkbookTable]:
        """
        Update the navigation property tables in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_table.WorkbookTable]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, workbook_table.WorkbookTable, error_mapping)
    
    def rows_by_id(self,id: str) -> workbook_table_row_item_request_builder.WorkbookTableRowItemRequestBuilder:
        """
        Provides operations to manage the rows property of the microsoft.graph.workbookTable entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_table_row_item_request_builder.WorkbookTableRowItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookTableRow%2Did"] = id
        return workbook_table_row_item_request_builder.WorkbookTableRowItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[WorkbookTableItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property tables for drives
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
    
    def to_get_request_information(self,request_configuration: Optional[WorkbookTableItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents a collection of tables associated with the workbook. Read-only.
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
    
    def to_patch_request_information(self,body: Optional[workbook_table.WorkbookTable] = None, request_configuration: Optional[WorkbookTableItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property tables in drives
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
    
    @dataclass
    class WorkbookTableItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WorkbookTableItemRequestBuilderGetQueryParameters():
        """
        Represents a collection of tables associated with the workbook. Read-only.
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
    class WorkbookTableItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WorkbookTableItemRequestBuilder.WorkbookTableItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class WorkbookTableItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

