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
    from ...........models.workbook_filter import WorkbookFilter
    from .apply.apply_request_builder import ApplyRequestBuilder
    from .apply_bottom_items_filter.apply_bottom_items_filter_request_builder import ApplyBottomItemsFilterRequestBuilder
    from .apply_bottom_percent_filter.apply_bottom_percent_filter_request_builder import ApplyBottomPercentFilterRequestBuilder
    from .apply_cell_color_filter.apply_cell_color_filter_request_builder import ApplyCellColorFilterRequestBuilder
    from .apply_custom_filter.apply_custom_filter_request_builder import ApplyCustomFilterRequestBuilder
    from .apply_dynamic_filter.apply_dynamic_filter_request_builder import ApplyDynamicFilterRequestBuilder
    from .apply_font_color_filter.apply_font_color_filter_request_builder import ApplyFontColorFilterRequestBuilder
    from .apply_icon_filter.apply_icon_filter_request_builder import ApplyIconFilterRequestBuilder
    from .apply_top_items_filter.apply_top_items_filter_request_builder import ApplyTopItemsFilterRequestBuilder
    from .apply_top_percent_filter.apply_top_percent_filter_request_builder import ApplyTopPercentFilterRequestBuilder
    from .apply_values_filter.apply_values_filter_request_builder import ApplyValuesFilterRequestBuilder
    from .clear.clear_request_builder import ClearRequestBuilder

class FilterRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the filter property of the microsoft.graph.workbookTableColumn entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FilterRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/tables/{workbookTable%2Did}/columns/{workbookTableColumn%2Did}/filter{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property filter for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[FilterRequestBuilderGetQueryParameters]] = None) -> Optional[WorkbookFilter]:
        """
        The filter applied to the column. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookFilter]
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
        from ...........models.workbook_filter import WorkbookFilter

        return await self.request_adapter.send_async(request_info, WorkbookFilter, error_mapping)
    
    async def patch(self,body: WorkbookFilter, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WorkbookFilter]:
        """
        Update the navigation property filter in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookFilter]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...........models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...........models.workbook_filter import WorkbookFilter

        return await self.request_adapter.send_async(request_info, WorkbookFilter, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property filter for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FilterRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The filter applied to the column. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: WorkbookFilter, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property filter in drives
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
    
    def with_url(self,raw_url: str) -> FilterRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FilterRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FilterRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def apply(self) -> ApplyRequestBuilder:
        """
        Provides operations to call the apply method.
        """
        from .apply.apply_request_builder import ApplyRequestBuilder

        return ApplyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_bottom_items_filter(self) -> ApplyBottomItemsFilterRequestBuilder:
        """
        Provides operations to call the applyBottomItemsFilter method.
        """
        from .apply_bottom_items_filter.apply_bottom_items_filter_request_builder import ApplyBottomItemsFilterRequestBuilder

        return ApplyBottomItemsFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_bottom_percent_filter(self) -> ApplyBottomPercentFilterRequestBuilder:
        """
        Provides operations to call the applyBottomPercentFilter method.
        """
        from .apply_bottom_percent_filter.apply_bottom_percent_filter_request_builder import ApplyBottomPercentFilterRequestBuilder

        return ApplyBottomPercentFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_cell_color_filter(self) -> ApplyCellColorFilterRequestBuilder:
        """
        Provides operations to call the applyCellColorFilter method.
        """
        from .apply_cell_color_filter.apply_cell_color_filter_request_builder import ApplyCellColorFilterRequestBuilder

        return ApplyCellColorFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_custom_filter(self) -> ApplyCustomFilterRequestBuilder:
        """
        Provides operations to call the applyCustomFilter method.
        """
        from .apply_custom_filter.apply_custom_filter_request_builder import ApplyCustomFilterRequestBuilder

        return ApplyCustomFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_dynamic_filter(self) -> ApplyDynamicFilterRequestBuilder:
        """
        Provides operations to call the applyDynamicFilter method.
        """
        from .apply_dynamic_filter.apply_dynamic_filter_request_builder import ApplyDynamicFilterRequestBuilder

        return ApplyDynamicFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_font_color_filter(self) -> ApplyFontColorFilterRequestBuilder:
        """
        Provides operations to call the applyFontColorFilter method.
        """
        from .apply_font_color_filter.apply_font_color_filter_request_builder import ApplyFontColorFilterRequestBuilder

        return ApplyFontColorFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_icon_filter(self) -> ApplyIconFilterRequestBuilder:
        """
        Provides operations to call the applyIconFilter method.
        """
        from .apply_icon_filter.apply_icon_filter_request_builder import ApplyIconFilterRequestBuilder

        return ApplyIconFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_top_items_filter(self) -> ApplyTopItemsFilterRequestBuilder:
        """
        Provides operations to call the applyTopItemsFilter method.
        """
        from .apply_top_items_filter.apply_top_items_filter_request_builder import ApplyTopItemsFilterRequestBuilder

        return ApplyTopItemsFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_top_percent_filter(self) -> ApplyTopPercentFilterRequestBuilder:
        """
        Provides operations to call the applyTopPercentFilter method.
        """
        from .apply_top_percent_filter.apply_top_percent_filter_request_builder import ApplyTopPercentFilterRequestBuilder

        return ApplyTopPercentFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_values_filter(self) -> ApplyValuesFilterRequestBuilder:
        """
        Provides operations to call the applyValuesFilter method.
        """
        from .apply_values_filter.apply_values_filter_request_builder import ApplyValuesFilterRequestBuilder

        return ApplyValuesFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clear(self) -> ClearRequestBuilder:
        """
        Provides operations to call the clear method.
        """
        from .clear.clear_request_builder import ClearRequestBuilder

        return ClearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FilterRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FilterRequestBuilderGetQueryParameters():
        """
        The filter applied to the column. Read-only.
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
    class FilterRequestBuilderGetRequestConfiguration(RequestConfiguration[FilterRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FilterRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

