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
    from ........models.o_data_errors.o_data_error import ODataError
    from ........models.workbook_worksheet import WorkbookWorksheet
    from .cell_with_row_with_column.cell_with_row_with_column_request_builder import CellWithRowWithColumnRequestBuilder
    from .charts.charts_request_builder import ChartsRequestBuilder
    from .names.names_request_builder import NamesRequestBuilder
    from .pivot_tables.pivot_tables_request_builder import PivotTablesRequestBuilder
    from .protection.protection_request_builder import ProtectionRequestBuilder
    from .range.range_request_builder import RangeRequestBuilder
    from .range_with_address.range_with_address_request_builder import RangeWithAddressRequestBuilder
    from .tables.tables_request_builder import TablesRequestBuilder
    from .used_range.used_range_request_builder import UsedRangeRequestBuilder
    from .used_range_with_values_only.used_range_with_values_only_request_builder import UsedRangeWithValuesOnlyRequestBuilder

class WorkbookWorksheetItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the worksheets property of the microsoft.graph.workbook entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WorkbookWorksheetItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}{?%24expand,%24select}", path_parameters)
    
    def cell_with_row_with_column(self,column: int, row: int) -> CellWithRowWithColumnRequestBuilder:
        """
        Provides operations to call the cell method.
        param column: Usage: column={column}
        param row: Usage: row={row}
        Returns: CellWithRowWithColumnRequestBuilder
        """
        if column is None:
            raise TypeError("column cannot be null.")
        if row is None:
            raise TypeError("row cannot be null.")
        from .cell_with_row_with_column.cell_with_row_with_column_request_builder import CellWithRowWithColumnRequestBuilder

        return CellWithRowWithColumnRequestBuilder(self.request_adapter, self.path_parameters, column, row)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property worksheets for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WorkbookWorksheetItemRequestBuilderGetQueryParameters]] = None) -> Optional[WorkbookWorksheet]:
        """
        Represents a collection of worksheets associated with the workbook. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookWorksheet]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.workbook_worksheet import WorkbookWorksheet

        return await self.request_adapter.send_async(request_info, WorkbookWorksheet, error_mapping)
    
    async def patch(self,body: WorkbookWorksheet, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WorkbookWorksheet]:
        """
        Update the navigation property worksheets in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookWorksheet]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.workbook_worksheet import WorkbookWorksheet

        return await self.request_adapter.send_async(request_info, WorkbookWorksheet, error_mapping)
    
    def range_with_address(self,address: str) -> RangeWithAddressRequestBuilder:
        """
        Provides operations to call the range method.
        param address: Usage: address='{address}'
        Returns: RangeWithAddressRequestBuilder
        """
        if address is None:
            raise TypeError("address cannot be null.")
        from .range_with_address.range_with_address_request_builder import RangeWithAddressRequestBuilder

        return RangeWithAddressRequestBuilder(self.request_adapter, self.path_parameters, address)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property worksheets for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WorkbookWorksheetItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Represents a collection of worksheets associated with the workbook. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: WorkbookWorksheet, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property worksheets in drives
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
    
    def used_range_with_values_only(self,values_only: bool) -> UsedRangeWithValuesOnlyRequestBuilder:
        """
        Provides operations to call the usedRange method.
        param values_only: Usage: valuesOnly={valuesOnly}
        Returns: UsedRangeWithValuesOnlyRequestBuilder
        """
        if values_only is None:
            raise TypeError("values_only cannot be null.")
        from .used_range_with_values_only.used_range_with_values_only_request_builder import UsedRangeWithValuesOnlyRequestBuilder

        return UsedRangeWithValuesOnlyRequestBuilder(self.request_adapter, self.path_parameters, values_only)
    
    def with_url(self,raw_url: str) -> WorkbookWorksheetItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WorkbookWorksheetItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WorkbookWorksheetItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def charts(self) -> ChartsRequestBuilder:
        """
        Provides operations to manage the charts property of the microsoft.graph.workbookWorksheet entity.
        """
        from .charts.charts_request_builder import ChartsRequestBuilder

        return ChartsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def names(self) -> NamesRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.workbookWorksheet entity.
        """
        from .names.names_request_builder import NamesRequestBuilder

        return NamesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pivot_tables(self) -> PivotTablesRequestBuilder:
        """
        Provides operations to manage the pivotTables property of the microsoft.graph.workbookWorksheet entity.
        """
        from .pivot_tables.pivot_tables_request_builder import PivotTablesRequestBuilder

        return PivotTablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def protection(self) -> ProtectionRequestBuilder:
        """
        Provides operations to manage the protection property of the microsoft.graph.workbookWorksheet entity.
        """
        from .protection.protection_request_builder import ProtectionRequestBuilder

        return ProtectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def range(self) -> RangeRequestBuilder:
        """
        Provides operations to call the range method.
        """
        from .range.range_request_builder import RangeRequestBuilder

        return RangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tables(self) -> TablesRequestBuilder:
        """
        Provides operations to manage the tables property of the microsoft.graph.workbookWorksheet entity.
        """
        from .tables.tables_request_builder import TablesRequestBuilder

        return TablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def used_range(self) -> UsedRangeRequestBuilder:
        """
        Provides operations to call the usedRange method.
        """
        from .used_range.used_range_request_builder import UsedRangeRequestBuilder

        return UsedRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WorkbookWorksheetItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WorkbookWorksheetItemRequestBuilderGetQueryParameters():
        """
        Represents a collection of worksheets associated with the workbook. Read-only.
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
    class WorkbookWorksheetItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WorkbookWorksheetItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WorkbookWorksheetItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

