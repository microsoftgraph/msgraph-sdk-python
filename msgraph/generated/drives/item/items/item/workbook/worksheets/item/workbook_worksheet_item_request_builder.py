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

charts_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.charts.charts_request_builder')
workbook_chart_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.charts.item.workbook_chart_item_request_builder')
cell_with_row_with_column_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.microsoft_graph_cell_with_row_with_column.cell_with_row_with_column_request_builder')
range_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.microsoft_graph_range.range_request_builder')
range_with_address_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.microsoft_graph_range_with_address.range_with_address_request_builder')
used_range_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.microsoft_graph_used_range.used_range_request_builder')
used_range_with_values_only_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.microsoft_graph_used_range_with_values_only.used_range_with_values_only_request_builder')
names_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.names.names_request_builder')
workbook_named_item_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.names.item.workbook_named_item_item_request_builder')
pivot_tables_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.pivot_tables.pivot_tables_request_builder')
workbook_pivot_table_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.pivot_tables.item.workbook_pivot_table_item_request_builder')
protection_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.protection.protection_request_builder')
tables_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.tables.tables_request_builder')
workbook_table_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.tables.item.workbook_table_item_request_builder')
workbook_worksheet = lazy_import('msgraph.generated.models.workbook_worksheet')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class WorkbookWorksheetItemRequestBuilder():
    """
    Provides operations to manage the worksheets property of the microsoft.graph.workbook entity.
    """
    @property
    def charts(self) -> charts_request_builder.ChartsRequestBuilder:
        """
        Provides operations to manage the charts property of the microsoft.graph.workbookWorksheet entity.
        """
        return charts_request_builder.ChartsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_range(self) -> range_request_builder.RangeRequestBuilder:
        """
        Provides operations to call the range method.
        """
        return range_request_builder.RangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_used_range(self) -> used_range_request_builder.UsedRangeRequestBuilder:
        """
        Provides operations to call the usedRange method.
        """
        return used_range_request_builder.UsedRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def names(self) -> names_request_builder.NamesRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.workbookWorksheet entity.
        """
        return names_request_builder.NamesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pivot_tables(self) -> pivot_tables_request_builder.PivotTablesRequestBuilder:
        """
        Provides operations to manage the pivotTables property of the microsoft.graph.workbookWorksheet entity.
        """
        return pivot_tables_request_builder.PivotTablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def protection(self) -> protection_request_builder.ProtectionRequestBuilder:
        """
        Provides operations to manage the protection property of the microsoft.graph.workbookWorksheet entity.
        """
        return protection_request_builder.ProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tables(self) -> tables_request_builder.TablesRequestBuilder:
        """
        Provides operations to manage the tables property of the microsoft.graph.workbookWorksheet entity.
        """
        return tables_request_builder.TablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def charts_by_id(self,id: str) -> workbook_chart_item_request_builder.WorkbookChartItemRequestBuilder:
        """
        Provides operations to manage the charts property of the microsoft.graph.workbookWorksheet entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_chart_item_request_builder.WorkbookChartItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookChart%2Did"] = id
        return workbook_chart_item_request_builder.WorkbookChartItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, workbook_worksheet_id: Optional[str] = None) -> None:
        """
        Instantiates a new WorkbookWorksheetItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
            workbookWorksheetId: key: id of workbookWorksheet
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params["workbookWorksheet%2Did"] = workbookWorksheetId
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[WorkbookWorksheetItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property worksheets for drives
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
    
    async def get(self,request_configuration: Optional[WorkbookWorksheetItemRequestBuilderGetRequestConfiguration] = None) -> Optional[workbook_worksheet.WorkbookWorksheet]:
        """
        Represents a collection of worksheets associated with the workbook. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_worksheet.WorkbookWorksheet]
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
        return await self.request_adapter.send_async(request_info, workbook_worksheet.WorkbookWorksheet, error_mapping)
    
    def microsoft_graph_cell_with_row_with_column(self,column: Optional[int] = None, row: Optional[int] = None) -> cell_with_row_with_column_request_builder.CellWithRowWithColumnRequestBuilder:
        """
        Provides operations to call the cell method.
        Args:
            column: Usage: column={column}
            row: Usage: row={row}
        Returns: cell_with_row_with_column_request_builder.CellWithRowWithColumnRequestBuilder
        """
        if column is None:
            raise Exception("column cannot be undefined")
        if row is None:
            raise Exception("row cannot be undefined")
        return cell_with_row_with_column_request_builder.CellWithRowWithColumnRequestBuilder(self.request_adapter, self.path_parameters, column, row)
    
    def microsoft_graph_range_with_address(self,address: Optional[str] = None) -> range_with_address_request_builder.RangeWithAddressRequestBuilder:
        """
        Provides operations to call the range method.
        Args:
            address: Usage: address='{address}'
        Returns: range_with_address_request_builder.RangeWithAddressRequestBuilder
        """
        if address is None:
            raise Exception("address cannot be undefined")
        return range_with_address_request_builder.RangeWithAddressRequestBuilder(self.request_adapter, self.path_parameters, address)
    
    def microsoft_graph_used_range_with_values_only(self,values_only: Optional[bool] = None) -> used_range_with_values_only_request_builder.UsedRangeWithValuesOnlyRequestBuilder:
        """
        Provides operations to call the usedRange method.
        Args:
            valuesOnly: Usage: valuesOnly={valuesOnly}
        Returns: used_range_with_values_only_request_builder.UsedRangeWithValuesOnlyRequestBuilder
        """
        if values_only is None:
            raise Exception("values_only cannot be undefined")
        return used_range_with_values_only_request_builder.UsedRangeWithValuesOnlyRequestBuilder(self.request_adapter, self.path_parameters, valuesOnly)
    
    def names_by_id(self,id: str) -> workbook_named_item_item_request_builder.WorkbookNamedItemItemRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.workbookWorksheet entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_named_item_item_request_builder.WorkbookNamedItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookNamedItem%2Did"] = id
        return workbook_named_item_item_request_builder.WorkbookNamedItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[workbook_worksheet.WorkbookWorksheet] = None, request_configuration: Optional[WorkbookWorksheetItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[workbook_worksheet.WorkbookWorksheet]:
        """
        Update the navigation property worksheets in drives
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_worksheet.WorkbookWorksheet]
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
        return await self.request_adapter.send_async(request_info, workbook_worksheet.WorkbookWorksheet, error_mapping)
    
    def pivot_tables_by_id(self,id: str) -> workbook_pivot_table_item_request_builder.WorkbookPivotTableItemRequestBuilder:
        """
        Provides operations to manage the pivotTables property of the microsoft.graph.workbookWorksheet entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_pivot_table_item_request_builder.WorkbookPivotTableItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookPivotTable%2Did"] = id
        return workbook_pivot_table_item_request_builder.WorkbookPivotTableItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tables_by_id(self,id: str) -> workbook_table_item_request_builder.WorkbookTableItemRequestBuilder:
        """
        Provides operations to manage the tables property of the microsoft.graph.workbookWorksheet entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_table_item_request_builder.WorkbookTableItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookTable%2Did"] = id
        return workbook_table_item_request_builder.WorkbookTableItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[WorkbookWorksheetItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property worksheets for drives
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
    
    def to_get_request_information(self,request_configuration: Optional[WorkbookWorksheetItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents a collection of worksheets associated with the workbook. Read-only.
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
    
    def to_patch_request_information(self,body: Optional[workbook_worksheet.WorkbookWorksheet] = None, request_configuration: Optional[WorkbookWorksheetItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property worksheets in drives
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
    
    @dataclass
    class WorkbookWorksheetItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WorkbookWorksheetItemRequestBuilderGetQueryParameters():
        """
        Represents a collection of worksheets associated with the workbook. Read-only.
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
    class WorkbookWorksheetItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WorkbookWorksheetItemRequestBuilder.WorkbookWorksheetItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class WorkbookWorksheetItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

