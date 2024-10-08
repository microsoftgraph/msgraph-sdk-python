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
    from .........models.o_data_errors.o_data_error import ODataError
    from .........models.workbook_range import WorkbookRange
    from .bounding_rect_with_another_range.bounding_rect_with_another_range_request_builder import BoundingRectWithAnotherRangeRequestBuilder
    from .cell_with_row_with_column.cell_with_row_with_column_request_builder import CellWithRowWithColumnRequestBuilder
    from .clear.clear_request_builder import ClearRequestBuilder
    from .columns_after.columns_after_request_builder import ColumnsAfterRequestBuilder
    from .columns_after_with_count.columns_after_with_count_request_builder import ColumnsAfterWithCountRequestBuilder
    from .columns_before.columns_before_request_builder import ColumnsBeforeRequestBuilder
    from .columns_before_with_count.columns_before_with_count_request_builder import ColumnsBeforeWithCountRequestBuilder
    from .column_with_column.column_with_column_request_builder import ColumnWithColumnRequestBuilder
    from .delete.delete_request_builder import DeleteRequestBuilder
    from .entire_column.entire_column_request_builder import EntireColumnRequestBuilder
    from .entire_row.entire_row_request_builder import EntireRowRequestBuilder
    from .format.format_request_builder import FormatRequestBuilder
    from .insert.insert_request_builder import InsertRequestBuilder
    from .intersection_with_another_range.intersection_with_another_range_request_builder import IntersectionWithAnotherRangeRequestBuilder
    from .last_cell.last_cell_request_builder import LastCellRequestBuilder
    from .last_column.last_column_request_builder import LastColumnRequestBuilder
    from .last_row.last_row_request_builder import LastRowRequestBuilder
    from .merge.merge_request_builder import MergeRequestBuilder
    from .offset_range_with_row_offset_with_column_offset.offset_range_with_row_offset_with_column_offset_request_builder import OffsetRangeWithRowOffsetWithColumnOffsetRequestBuilder
    from .resized_range_with_delta_rows_with_delta_columns.resized_range_with_delta_rows_with_delta_columns_request_builder import ResizedRangeWithDeltaRowsWithDeltaColumnsRequestBuilder
    from .rows_above.rows_above_request_builder import RowsAboveRequestBuilder
    from .rows_above_with_count.rows_above_with_count_request_builder import RowsAboveWithCountRequestBuilder
    from .rows_below.rows_below_request_builder import RowsBelowRequestBuilder
    from .rows_below_with_count.rows_below_with_count_request_builder import RowsBelowWithCountRequestBuilder
    from .row_with_row.row_with_row_request_builder import RowWithRowRequestBuilder
    from .sort.sort_request_builder import SortRequestBuilder
    from .unmerge.unmerge_request_builder import UnmergeRequestBuilder
    from .visible_view.visible_view_request_builder import VisibleViewRequestBuilder
    from .worksheet.worksheet_request_builder import WorksheetRequestBuilder

class UsedRangeRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the usedRange method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new UsedRangeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/usedRange()", path_parameters)
    
    def bounding_rect_with_another_range(self,another_range: str) -> BoundingRectWithAnotherRangeRequestBuilder:
        """
        Provides operations to call the boundingRect method.
        param another_range: Usage: anotherRange='{anotherRange}'
        Returns: BoundingRectWithAnotherRangeRequestBuilder
        """
        if another_range is None:
            raise TypeError("another_range cannot be null.")
        from .bounding_rect_with_another_range.bounding_rect_with_another_range_request_builder import BoundingRectWithAnotherRangeRequestBuilder

        return BoundingRectWithAnotherRangeRequestBuilder(self.request_adapter, self.path_parameters, another_range)
    
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
    
    def column_with_column(self,column: int) -> ColumnWithColumnRequestBuilder:
        """
        Provides operations to call the column method.
        param column: Usage: column={column}
        Returns: ColumnWithColumnRequestBuilder
        """
        if column is None:
            raise TypeError("column cannot be null.")
        from .column_with_column.column_with_column_request_builder import ColumnWithColumnRequestBuilder

        return ColumnWithColumnRequestBuilder(self.request_adapter, self.path_parameters, column)
    
    def columns_after_with_count(self,count: int) -> ColumnsAfterWithCountRequestBuilder:
        """
        Provides operations to call the columnsAfter method.
        param count: Usage: count={count}
        Returns: ColumnsAfterWithCountRequestBuilder
        """
        if count is None:
            raise TypeError("count cannot be null.")
        from .columns_after_with_count.columns_after_with_count_request_builder import ColumnsAfterWithCountRequestBuilder

        return ColumnsAfterWithCountRequestBuilder(self.request_adapter, self.path_parameters, count)
    
    def columns_before_with_count(self,count: int) -> ColumnsBeforeWithCountRequestBuilder:
        """
        Provides operations to call the columnsBefore method.
        param count: Usage: count={count}
        Returns: ColumnsBeforeWithCountRequestBuilder
        """
        if count is None:
            raise TypeError("count cannot be null.")
        from .columns_before_with_count.columns_before_with_count_request_builder import ColumnsBeforeWithCountRequestBuilder

        return ColumnsBeforeWithCountRequestBuilder(self.request_adapter, self.path_parameters, count)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WorkbookRange]:
        """
        Invoke function usedRange
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookRange]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.workbook_range import WorkbookRange

        return await self.request_adapter.send_async(request_info, WorkbookRange, error_mapping)
    
    def intersection_with_another_range(self,another_range: str) -> IntersectionWithAnotherRangeRequestBuilder:
        """
        Provides operations to call the intersection method.
        param another_range: Usage: anotherRange='{anotherRange}'
        Returns: IntersectionWithAnotherRangeRequestBuilder
        """
        if another_range is None:
            raise TypeError("another_range cannot be null.")
        from .intersection_with_another_range.intersection_with_another_range_request_builder import IntersectionWithAnotherRangeRequestBuilder

        return IntersectionWithAnotherRangeRequestBuilder(self.request_adapter, self.path_parameters, another_range)
    
    def offset_range_with_row_offset_with_column_offset(self,column_offset: int, row_offset: int) -> OffsetRangeWithRowOffsetWithColumnOffsetRequestBuilder:
        """
        Provides operations to call the offsetRange method.
        param column_offset: Usage: columnOffset={columnOffset}
        param row_offset: Usage: rowOffset={rowOffset}
        Returns: OffsetRangeWithRowOffsetWithColumnOffsetRequestBuilder
        """
        if column_offset is None:
            raise TypeError("column_offset cannot be null.")
        if row_offset is None:
            raise TypeError("row_offset cannot be null.")
        from .offset_range_with_row_offset_with_column_offset.offset_range_with_row_offset_with_column_offset_request_builder import OffsetRangeWithRowOffsetWithColumnOffsetRequestBuilder

        return OffsetRangeWithRowOffsetWithColumnOffsetRequestBuilder(self.request_adapter, self.path_parameters, column_offset, row_offset)
    
    def resized_range_with_delta_rows_with_delta_columns(self,delta_columns: int, delta_rows: int) -> ResizedRangeWithDeltaRowsWithDeltaColumnsRequestBuilder:
        """
        Provides operations to call the resizedRange method.
        param delta_columns: Usage: deltaColumns={deltaColumns}
        param delta_rows: Usage: deltaRows={deltaRows}
        Returns: ResizedRangeWithDeltaRowsWithDeltaColumnsRequestBuilder
        """
        if delta_columns is None:
            raise TypeError("delta_columns cannot be null.")
        if delta_rows is None:
            raise TypeError("delta_rows cannot be null.")
        from .resized_range_with_delta_rows_with_delta_columns.resized_range_with_delta_rows_with_delta_columns_request_builder import ResizedRangeWithDeltaRowsWithDeltaColumnsRequestBuilder

        return ResizedRangeWithDeltaRowsWithDeltaColumnsRequestBuilder(self.request_adapter, self.path_parameters, delta_columns, delta_rows)
    
    def row_with_row(self,row: int) -> RowWithRowRequestBuilder:
        """
        Provides operations to call the row method.
        param row: Usage: row={row}
        Returns: RowWithRowRequestBuilder
        """
        if row is None:
            raise TypeError("row cannot be null.")
        from .row_with_row.row_with_row_request_builder import RowWithRowRequestBuilder

        return RowWithRowRequestBuilder(self.request_adapter, self.path_parameters, row)
    
    def rows_above_with_count(self,count: int) -> RowsAboveWithCountRequestBuilder:
        """
        Provides operations to call the rowsAbove method.
        param count: Usage: count={count}
        Returns: RowsAboveWithCountRequestBuilder
        """
        if count is None:
            raise TypeError("count cannot be null.")
        from .rows_above_with_count.rows_above_with_count_request_builder import RowsAboveWithCountRequestBuilder

        return RowsAboveWithCountRequestBuilder(self.request_adapter, self.path_parameters, count)
    
    def rows_below_with_count(self,count: int) -> RowsBelowWithCountRequestBuilder:
        """
        Provides operations to call the rowsBelow method.
        param count: Usage: count={count}
        Returns: RowsBelowWithCountRequestBuilder
        """
        if count is None:
            raise TypeError("count cannot be null.")
        from .rows_below_with_count.rows_below_with_count_request_builder import RowsBelowWithCountRequestBuilder

        return RowsBelowWithCountRequestBuilder(self.request_adapter, self.path_parameters, count)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Invoke function usedRange
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> UsedRangeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UsedRangeRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return UsedRangeRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def clear(self) -> ClearRequestBuilder:
        """
        Provides operations to call the clear method.
        """
        from .clear.clear_request_builder import ClearRequestBuilder

        return ClearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns_after(self) -> ColumnsAfterRequestBuilder:
        """
        Provides operations to call the columnsAfter method.
        """
        from .columns_after.columns_after_request_builder import ColumnsAfterRequestBuilder

        return ColumnsAfterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns_before(self) -> ColumnsBeforeRequestBuilder:
        """
        Provides operations to call the columnsBefore method.
        """
        from .columns_before.columns_before_request_builder import ColumnsBeforeRequestBuilder

        return ColumnsBeforeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_path(self) -> DeleteRequestBuilder:
        """
        Provides operations to call the delete method.
        """
        from .delete.delete_request_builder import DeleteRequestBuilder

        return DeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def entire_column(self) -> EntireColumnRequestBuilder:
        """
        Provides operations to call the entireColumn method.
        """
        from .entire_column.entire_column_request_builder import EntireColumnRequestBuilder

        return EntireColumnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def entire_row(self) -> EntireRowRequestBuilder:
        """
        Provides operations to call the entireRow method.
        """
        from .entire_row.entire_row_request_builder import EntireRowRequestBuilder

        return EntireRowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def format(self) -> FormatRequestBuilder:
        """
        Provides operations to manage the format property of the microsoft.graph.workbookRange entity.
        """
        from .format.format_request_builder import FormatRequestBuilder

        return FormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def insert(self) -> InsertRequestBuilder:
        """
        Provides operations to call the insert method.
        """
        from .insert.insert_request_builder import InsertRequestBuilder

        return InsertRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_cell(self) -> LastCellRequestBuilder:
        """
        Provides operations to call the lastCell method.
        """
        from .last_cell.last_cell_request_builder import LastCellRequestBuilder

        return LastCellRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_column(self) -> LastColumnRequestBuilder:
        """
        Provides operations to call the lastColumn method.
        """
        from .last_column.last_column_request_builder import LastColumnRequestBuilder

        return LastColumnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_row(self) -> LastRowRequestBuilder:
        """
        Provides operations to call the lastRow method.
        """
        from .last_row.last_row_request_builder import LastRowRequestBuilder

        return LastRowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def merge(self) -> MergeRequestBuilder:
        """
        Provides operations to call the merge method.
        """
        from .merge.merge_request_builder import MergeRequestBuilder

        return MergeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rows_above(self) -> RowsAboveRequestBuilder:
        """
        Provides operations to call the rowsAbove method.
        """
        from .rows_above.rows_above_request_builder import RowsAboveRequestBuilder

        return RowsAboveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rows_below(self) -> RowsBelowRequestBuilder:
        """
        Provides operations to call the rowsBelow method.
        """
        from .rows_below.rows_below_request_builder import RowsBelowRequestBuilder

        return RowsBelowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sort(self) -> SortRequestBuilder:
        """
        Provides operations to manage the sort property of the microsoft.graph.workbookRange entity.
        """
        from .sort.sort_request_builder import SortRequestBuilder

        return SortRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unmerge(self) -> UnmergeRequestBuilder:
        """
        Provides operations to call the unmerge method.
        """
        from .unmerge.unmerge_request_builder import UnmergeRequestBuilder

        return UnmergeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def visible_view(self) -> VisibleViewRequestBuilder:
        """
        Provides operations to call the visibleView method.
        """
        from .visible_view.visible_view_request_builder import VisibleViewRequestBuilder

        return VisibleViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def worksheet(self) -> WorksheetRequestBuilder:
        """
        Provides operations to manage the worksheet property of the microsoft.graph.workbookRange entity.
        """
        from .worksheet.worksheet_request_builder import WorksheetRequestBuilder

        return WorksheetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UsedRangeRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

