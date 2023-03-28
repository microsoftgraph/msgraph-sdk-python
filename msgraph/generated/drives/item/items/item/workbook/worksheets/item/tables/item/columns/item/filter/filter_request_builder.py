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
    from .............models import workbook_filter
    from .............models.o_data_errors import o_data_error
    from .apply import apply_request_builder
    from .apply_bottom_items_filter import apply_bottom_items_filter_request_builder
    from .apply_bottom_percent_filter import apply_bottom_percent_filter_request_builder
    from .apply_cell_color_filter import apply_cell_color_filter_request_builder
    from .apply_custom_filter import apply_custom_filter_request_builder
    from .apply_dynamic_filter import apply_dynamic_filter_request_builder
    from .apply_font_color_filter import apply_font_color_filter_request_builder
    from .apply_icon_filter import apply_icon_filter_request_builder
    from .apply_top_items_filter import apply_top_items_filter_request_builder
    from .apply_top_percent_filter import apply_top_percent_filter_request_builder
    from .apply_values_filter import apply_values_filter_request_builder
    from .clear import clear_request_builder

class FilterRequestBuilder():
    """
    Provides operations to manage the filter property of the microsoft.graph.workbookTableColumn entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new FilterRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/tables/{workbookTable%2Did}/columns/{workbookTableColumn%2Did}/filter{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[FilterRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property filter for drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .............models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[FilterRequestBuilderGetRequestConfiguration] = None) -> Optional[workbook_filter.WorkbookFilter]:
        """
        Retrieve the filter applied to the column. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_filter.WorkbookFilter]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .............models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .............models import workbook_filter

        return await self.request_adapter.send_async(request_info, workbook_filter.WorkbookFilter, error_mapping)
    
    async def patch(self,body: Optional[workbook_filter.WorkbookFilter] = None, request_configuration: Optional[FilterRequestBuilderPatchRequestConfiguration] = None) -> Optional[workbook_filter.WorkbookFilter]:
        """
        Update the navigation property filter in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_filter.WorkbookFilter]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .............models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .............models import workbook_filter

        return await self.request_adapter.send_async(request_info, workbook_filter.WorkbookFilter, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[FilterRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property filter for drives
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
    
    def to_get_request_information(self,request_configuration: Optional[FilterRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the filter applied to the column. Read-only.
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
    
    def to_patch_request_information(self,body: Optional[workbook_filter.WorkbookFilter] = None, request_configuration: Optional[FilterRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property filter in drives
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
    def apply(self) -> apply_request_builder.ApplyRequestBuilder:
        """
        Provides operations to call the apply method.
        """
        from .apply import apply_request_builder

        return apply_request_builder.ApplyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_bottom_items_filter(self) -> apply_bottom_items_filter_request_builder.ApplyBottomItemsFilterRequestBuilder:
        """
        Provides operations to call the applyBottomItemsFilter method.
        """
        from .apply_bottom_items_filter import apply_bottom_items_filter_request_builder

        return apply_bottom_items_filter_request_builder.ApplyBottomItemsFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_bottom_percent_filter(self) -> apply_bottom_percent_filter_request_builder.ApplyBottomPercentFilterRequestBuilder:
        """
        Provides operations to call the applyBottomPercentFilter method.
        """
        from .apply_bottom_percent_filter import apply_bottom_percent_filter_request_builder

        return apply_bottom_percent_filter_request_builder.ApplyBottomPercentFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_cell_color_filter(self) -> apply_cell_color_filter_request_builder.ApplyCellColorFilterRequestBuilder:
        """
        Provides operations to call the applyCellColorFilter method.
        """
        from .apply_cell_color_filter import apply_cell_color_filter_request_builder

        return apply_cell_color_filter_request_builder.ApplyCellColorFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_custom_filter(self) -> apply_custom_filter_request_builder.ApplyCustomFilterRequestBuilder:
        """
        Provides operations to call the applyCustomFilter method.
        """
        from .apply_custom_filter import apply_custom_filter_request_builder

        return apply_custom_filter_request_builder.ApplyCustomFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_dynamic_filter(self) -> apply_dynamic_filter_request_builder.ApplyDynamicFilterRequestBuilder:
        """
        Provides operations to call the applyDynamicFilter method.
        """
        from .apply_dynamic_filter import apply_dynamic_filter_request_builder

        return apply_dynamic_filter_request_builder.ApplyDynamicFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_font_color_filter(self) -> apply_font_color_filter_request_builder.ApplyFontColorFilterRequestBuilder:
        """
        Provides operations to call the applyFontColorFilter method.
        """
        from .apply_font_color_filter import apply_font_color_filter_request_builder

        return apply_font_color_filter_request_builder.ApplyFontColorFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_icon_filter(self) -> apply_icon_filter_request_builder.ApplyIconFilterRequestBuilder:
        """
        Provides operations to call the applyIconFilter method.
        """
        from .apply_icon_filter import apply_icon_filter_request_builder

        return apply_icon_filter_request_builder.ApplyIconFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_top_items_filter(self) -> apply_top_items_filter_request_builder.ApplyTopItemsFilterRequestBuilder:
        """
        Provides operations to call the applyTopItemsFilter method.
        """
        from .apply_top_items_filter import apply_top_items_filter_request_builder

        return apply_top_items_filter_request_builder.ApplyTopItemsFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_top_percent_filter(self) -> apply_top_percent_filter_request_builder.ApplyTopPercentFilterRequestBuilder:
        """
        Provides operations to call the applyTopPercentFilter method.
        """
        from .apply_top_percent_filter import apply_top_percent_filter_request_builder

        return apply_top_percent_filter_request_builder.ApplyTopPercentFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_values_filter(self) -> apply_values_filter_request_builder.ApplyValuesFilterRequestBuilder:
        """
        Provides operations to call the applyValuesFilter method.
        """
        from .apply_values_filter import apply_values_filter_request_builder

        return apply_values_filter_request_builder.ApplyValuesFilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clear(self) -> clear_request_builder.ClearRequestBuilder:
        """
        Provides operations to call the clear method.
        """
        from .clear import clear_request_builder

        return clear_request_builder.ClearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FilterRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class FilterRequestBuilderGetQueryParameters():
        """
        Retrieve the filter applied to the column. Read-only.
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
    class FilterRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[FilterRequestBuilder.FilterRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class FilterRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

