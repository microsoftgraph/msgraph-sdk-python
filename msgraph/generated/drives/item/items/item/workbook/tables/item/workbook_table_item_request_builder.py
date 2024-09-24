from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ........models.o_data_errors.o_data_error import ODataError
    from ........models.workbook_table import WorkbookTable
    from .clear_filters.clear_filters_request_builder import ClearFiltersRequestBuilder
    from .columns.columns_request_builder import ColumnsRequestBuilder
    from .convert_to_range.convert_to_range_request_builder import ConvertToRangeRequestBuilder
    from .data_body_range.data_body_range_request_builder import DataBodyRangeRequestBuilder
    from .header_row_range.header_row_range_request_builder import HeaderRowRangeRequestBuilder
    from .range.range_request_builder import RangeRequestBuilder
    from .reapply_filters.reapply_filters_request_builder import ReapplyFiltersRequestBuilder
    from .rows.rows_request_builder import RowsRequestBuilder
    from .sort.sort_request_builder import SortRequestBuilder
    from .total_row_range.total_row_range_request_builder import TotalRowRangeRequestBuilder
    from .worksheet.worksheet_request_builder import WorksheetRequestBuilder

class WorkbookTableItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the tables property of the microsoft.graph.workbook entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WorkbookTableItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/tables/{workbookTable%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property tables for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WorkbookTableItemRequestBuilderGetQueryParameters]] = None) -> Optional[WorkbookTable]:
        """
        Represents a collection of tables associated with the workbook. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookTable]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.workbook_table import WorkbookTable

        return await self.request_adapter.send_async(request_info, WorkbookTable, error_mapping)
    
    async def patch(self,body: WorkbookTable, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WorkbookTable]:
        """
        Update the navigation property tables in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookTable]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.workbook_table import WorkbookTable

        return await self.request_adapter.send_async(request_info, WorkbookTable, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property tables for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WorkbookTableItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Represents a collection of tables associated with the workbook. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: WorkbookTable, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property tables in drives
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
    
    def with_url(self,raw_url: str) -> WorkbookTableItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WorkbookTableItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WorkbookTableItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def clear_filters(self) -> ClearFiltersRequestBuilder:
        """
        Provides operations to call the clearFilters method.
        """
        from .clear_filters.clear_filters_request_builder import ClearFiltersRequestBuilder

        return ClearFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> ColumnsRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.workbookTable entity.
        """
        from .columns.columns_request_builder import ColumnsRequestBuilder

        return ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def convert_to_range(self) -> ConvertToRangeRequestBuilder:
        """
        Provides operations to call the convertToRange method.
        """
        from .convert_to_range.convert_to_range_request_builder import ConvertToRangeRequestBuilder

        return ConvertToRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_body_range(self) -> DataBodyRangeRequestBuilder:
        """
        Provides operations to call the dataBodyRange method.
        """
        from .data_body_range.data_body_range_request_builder import DataBodyRangeRequestBuilder

        return DataBodyRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def header_row_range(self) -> HeaderRowRangeRequestBuilder:
        """
        Provides operations to call the headerRowRange method.
        """
        from .header_row_range.header_row_range_request_builder import HeaderRowRangeRequestBuilder

        return HeaderRowRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def range(self) -> RangeRequestBuilder:
        """
        Provides operations to call the range method.
        """
        from .range.range_request_builder import RangeRequestBuilder

        return RangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reapply_filters(self) -> ReapplyFiltersRequestBuilder:
        """
        Provides operations to call the reapplyFilters method.
        """
        from .reapply_filters.reapply_filters_request_builder import ReapplyFiltersRequestBuilder

        return ReapplyFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rows(self) -> RowsRequestBuilder:
        """
        Provides operations to manage the rows property of the microsoft.graph.workbookTable entity.
        """
        from .rows.rows_request_builder import RowsRequestBuilder

        return RowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sort(self) -> SortRequestBuilder:
        """
        Provides operations to manage the sort property of the microsoft.graph.workbookTable entity.
        """
        from .sort.sort_request_builder import SortRequestBuilder

        return SortRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def total_row_range(self) -> TotalRowRangeRequestBuilder:
        """
        Provides operations to call the totalRowRange method.
        """
        from .total_row_range.total_row_range_request_builder import TotalRowRangeRequestBuilder

        return TotalRowRangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def worksheet(self) -> WorksheetRequestBuilder:
        """
        Provides operations to manage the worksheet property of the microsoft.graph.workbookTable entity.
        """
        from .worksheet.worksheet_request_builder import WorksheetRequestBuilder

        return WorksheetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WorkbookTableItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WorkbookTableItemRequestBuilderGetQueryParameters():
        """
        Represents a collection of tables associated with the workbook. Read-only.
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class WorkbookTableItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WorkbookTableItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WorkbookTableItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

