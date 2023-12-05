from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkbookWorksheetItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}{?%24select,%24expand}", path_parameters)
    
    def cell_with_row_with_column(self,column: Optional[int] = None, row: Optional[int] = None) -> CellWithRowWithColumnRequestBuilder:
        """
        Provides operations to call the cell method.
        param column: Usage: column={column}
        param row: Usage: row={row}
        Returns: CellWithRowWithColumnRequestBuilder
        """
        if not column:
            raise TypeError("column cannot be null.")
        if not row:
            raise TypeError("row cannot be null.")
        from .cell_with_row_with_column.cell_with_row_with_column_request_builder import CellWithRowWithColumnRequestBuilder

        return CellWithRowWithColumnRequestBuilder(self.request_adapter, self.path_parameters, column, row)
    
    async def delete(self,request_configuration: Optional[WorkbookWorksheetItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes the worksheet from the workbook.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/worksheet-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WorkbookWorksheetItemRequestBuilderGetRequestConfiguration] = None) -> Optional[WorkbookWorksheet]:
        """
        Retrieve the properties and relationships of worksheet object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookWorksheet]
        Find more info here: https://learn.microsoft.com/graph/api/worksheet-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.workbook_worksheet import WorkbookWorksheet

        return await self.request_adapter.send_async(request_info, WorkbookWorksheet, error_mapping)
    
    async def patch(self,body: Optional[WorkbookWorksheet] = None, request_configuration: Optional[WorkbookWorksheetItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[WorkbookWorksheet]:
        """
        Update the properties of worksheet object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookWorksheet]
        Find more info here: https://learn.microsoft.com/graph/api/worksheet-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.workbook_worksheet import WorkbookWorksheet

        return await self.request_adapter.send_async(request_info, WorkbookWorksheet, error_mapping)
    
    def range_with_address(self,address: Optional[str] = None) -> RangeWithAddressRequestBuilder:
        """
        Provides operations to call the range method.
        param address: Usage: address='{address}'
        Returns: RangeWithAddressRequestBuilder
        """
        if not address:
            raise TypeError("address cannot be null.")
        from .range_with_address.range_with_address_request_builder import RangeWithAddressRequestBuilder

        return RangeWithAddressRequestBuilder(self.request_adapter, self.path_parameters, address)
    
    def to_delete_request_information(self,request_configuration: Optional[WorkbookWorksheetItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes the worksheet from the workbook.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[WorkbookWorksheetItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of worksheet object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[WorkbookWorksheet] = None, request_configuration: Optional[WorkbookWorksheetItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of worksheet object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def used_range_with_values_only(self,values_only: Optional[bool] = None) -> UsedRangeWithValuesOnlyRequestBuilder:
        """
        Provides operations to call the usedRange method.
        param values_only: Usage: valuesOnly={valuesOnly}
        Returns: UsedRangeWithValuesOnlyRequestBuilder
        """
        if not values_only:
            raise TypeError("values_only cannot be null.")
        from .used_range_with_values_only.used_range_with_values_only_request_builder import UsedRangeWithValuesOnlyRequestBuilder

        return UsedRangeWithValuesOnlyRequestBuilder(self.request_adapter, self.path_parameters, values_only)
    
    def with_url(self,raw_url: Optional[str] = None) -> WorkbookWorksheetItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WorkbookWorksheetItemRequestBuilder
        """
        if not raw_url:
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
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WorkbookWorksheetItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class WorkbookWorksheetItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of worksheet object.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WorkbookWorksheetItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[WorkbookWorksheetItemRequestBuilder.WorkbookWorksheetItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WorkbookWorksheetItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

