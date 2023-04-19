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
    from ........models import workbook_worksheet
    from ........models.o_data_errors import o_data_error
    from .cell_with_row_with_column import cell_with_row_with_column_request_builder
    from .charts import charts_request_builder
    from .names import names_request_builder
    from .pivot_tables import pivot_tables_request_builder
    from .protection import protection_request_builder
    from .range import range_request_builder
    from .range_with_address import range_with_address_request_builder
    from .tables import tables_request_builder
    from .used_range import used_range_request_builder
    from .used_range_with_values_only import used_range_with_values_only_request_builder

class WorkbookWorksheetItemRequestBuilder():
    """
    Provides operations to manage the worksheets property of the microsoft.graph.workbook entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkbookWorksheetItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def cell_with_row_with_column(self,column: Optional[int] = None, row: Optional[int] = None) -> cell_with_row_with_column_request_builder.CellWithRowWithColumnRequestBuilder:
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
        from .cell_with_row_with_column import cell_with_row_with_column_request_builder

        return cell_with_row_with_column_request_builder.CellWithRowWithColumnRequestBuilder(self.request_adapter, self.path_parameters, column, row)
    
    async def delete(self,request_configuration: Optional[WorkbookWorksheetItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property worksheets for drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.o_data_errors import o_data_error

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
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models import workbook_worksheet

        return await self.request_adapter.send_async(request_info, workbook_worksheet.WorkbookWorksheet, error_mapping)
    
    async def patch(self,body: Optional[workbook_worksheet.WorkbookWorksheet] = None, request_configuration: Optional[WorkbookWorksheetItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[workbook_worksheet.WorkbookWorksheet]:
        """
        Update the navigation property worksheets in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_worksheet.WorkbookWorksheet]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models import workbook_worksheet

        return await self.request_adapter.send_async(request_info, workbook_worksheet.WorkbookWorksheet, error_mapping)
    
    def range_with_address(self,address: Optional[str] = None) -> range_with_address_request_builder.RangeWithAddressRequestBuilder:
        """
        Provides operations to call the range method.
        Args:
            address: Usage: address='{address}'
        Returns: range_with_address_request_builder.RangeWithAddressRequestBuilder
        """
        if address is None:
            raise Exception("address cannot be undefined")
        from .range_with_address import range_with_address_request_builder

        return range_with_address_request_builder.RangeWithAddressRequestBuilder(self.request_adapter, self.path_parameters, address)
    
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[workbook_worksheet.WorkbookWorksheet] = None, request_configuration: Optional[WorkbookWorksheetItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property worksheets in drives
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
    
    def used_range_with_values_only(self,values_only: Optional[bool] = None) -> used_range_with_values_only_request_builder.UsedRangeWithValuesOnlyRequestBuilder:
        """
        Provides operations to call the usedRange method.
        Args:
            valuesOnly: Usage: valuesOnly={valuesOnly}
        Returns: used_range_with_values_only_request_builder.UsedRangeWithValuesOnlyRequestBuilder
        """
        if values_only is None:
            raise Exception("values_only cannot be undefined")
        from .used_range_with_values_only import used_range_with_values_only_request_builder

        return used_range_with_values_only_request_builder.UsedRangeWithValuesOnlyRequestBuilder(self.request_adapter, self.path_parameters, values_only)
    
    @property
    def charts(self) -> charts_request_builder.ChartsRequestBuilder:
        """
        Provides operations to manage the charts property of the microsoft.graph.workbookWorksheet entity.
        """
        from .charts import charts_request_builder

        return charts_request_builder.ChartsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def names(self) -> names_request_builder.NamesRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.workbookWorksheet entity.
        """
        from .names import names_request_builder

        return names_request_builder.NamesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pivot_tables(self) -> pivot_tables_request_builder.PivotTablesRequestBuilder:
        """
        Provides operations to manage the pivotTables property of the microsoft.graph.workbookWorksheet entity.
        """
        from .pivot_tables import pivot_tables_request_builder

        return pivot_tables_request_builder.PivotTablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def protection(self) -> protection_request_builder.ProtectionRequestBuilder:
        """
        Provides operations to manage the protection property of the microsoft.graph.workbookWorksheet entity.
        """
        from .protection import protection_request_builder

        return protection_request_builder.ProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def range(self) -> range_request_builder.RangeRequestBuilder:
        """
        Provides operations to call the range method.
        """
        from .range import range_request_builder

        return range_request_builder.RangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tables(self) -> tables_request_builder.TablesRequestBuilder:
        """
        Provides operations to manage the tables property of the microsoft.graph.workbookWorksheet entity.
        """
        from .tables import tables_request_builder

        return tables_request_builder.TablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def used_range(self) -> used_range_request_builder.UsedRangeRequestBuilder:
        """
        Provides operations to call the usedRange method.
        """
        from .used_range import used_range_request_builder

        return used_range_request_builder.UsedRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WorkbookWorksheetItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WorkbookWorksheetItemRequestBuilderGetQueryParameters():
        """
        Represents a collection of worksheets associated with the workbook. Read-only.
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
    class WorkbookWorksheetItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

