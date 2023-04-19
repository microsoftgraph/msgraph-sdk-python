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
    from ..........models import workbook_chart
    from ..........models.o_data_errors import o_data_error
    from .axes import axes_request_builder
    from .data_labels import data_labels_request_builder
    from .format import format_request_builder
    from .image import image_request_builder
    from .image_with_width import image_with_width_request_builder
    from .image_with_width_with_height import image_with_width_with_height_request_builder
    from .image_with_width_with_height_with_fitting_mode import image_with_width_with_height_with_fitting_mode_request_builder
    from .legend import legend_request_builder
    from .series import series_request_builder
    from .set_data import set_data_request_builder
    from .set_position import set_position_request_builder
    from .title import title_request_builder
    from .worksheet import worksheet_request_builder

class WorkbookChartItemRequestBuilder():
    """
    Provides operations to manage the charts property of the microsoft.graph.workbookWorksheet entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkbookChartItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[WorkbookChartItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property charts for drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ..........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WorkbookChartItemRequestBuilderGetRequestConfiguration] = None) -> Optional[workbook_chart.WorkbookChart]:
        """
        Returns collection of charts that are part of the worksheet. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_chart.WorkbookChart]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models import workbook_chart

        return await self.request_adapter.send_async(request_info, workbook_chart.WorkbookChart, error_mapping)
    
    def image_with_width(self,width: Optional[int] = None) -> image_with_width_request_builder.ImageWithWidthRequestBuilder:
        """
        Provides operations to call the image method.
        Args:
            width: Usage: width={width}
        Returns: image_with_width_request_builder.ImageWithWidthRequestBuilder
        """
        if width is None:
            raise Exception("width cannot be undefined")
        from .image_with_width import image_with_width_request_builder

        return image_with_width_request_builder.ImageWithWidthRequestBuilder(self.request_adapter, self.path_parameters, width)
    
    def image_with_width_with_height(self,height: Optional[int] = None, width: Optional[int] = None) -> image_with_width_with_height_request_builder.ImageWithWidthWithHeightRequestBuilder:
        """
        Provides operations to call the image method.
        Args:
            height: Usage: height={height}
            width: Usage: width={width}
        Returns: image_with_width_with_height_request_builder.ImageWithWidthWithHeightRequestBuilder
        """
        if height is None:
            raise Exception("height cannot be undefined")
        if width is None:
            raise Exception("width cannot be undefined")
        from .image_with_width_with_height import image_with_width_with_height_request_builder

        return image_with_width_with_height_request_builder.ImageWithWidthWithHeightRequestBuilder(self.request_adapter, self.path_parameters, height, width)
    
    def image_with_width_with_height_with_fitting_mode(self,fitting_mode: Optional[str] = None, height: Optional[int] = None, width: Optional[int] = None) -> image_with_width_with_height_with_fitting_mode_request_builder.ImageWithWidthWithHeightWithFittingModeRequestBuilder:
        """
        Provides operations to call the image method.
        Args:
            fittingMode: Usage: fittingMode='{fittingMode}'
            height: Usage: height={height}
            width: Usage: width={width}
        Returns: image_with_width_with_height_with_fitting_mode_request_builder.ImageWithWidthWithHeightWithFittingModeRequestBuilder
        """
        if fitting_mode is None:
            raise Exception("fitting_mode cannot be undefined")
        if height is None:
            raise Exception("height cannot be undefined")
        if width is None:
            raise Exception("width cannot be undefined")
        from .image_with_width_with_height_with_fitting_mode import image_with_width_with_height_with_fitting_mode_request_builder

        return image_with_width_with_height_with_fitting_mode_request_builder.ImageWithWidthWithHeightWithFittingModeRequestBuilder(self.request_adapter, self.path_parameters, fitting_mode, height, width)
    
    async def patch(self,body: Optional[workbook_chart.WorkbookChart] = None, request_configuration: Optional[WorkbookChartItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[workbook_chart.WorkbookChart]:
        """
        Update the navigation property charts in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_chart.WorkbookChart]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models import workbook_chart

        return await self.request_adapter.send_async(request_info, workbook_chart.WorkbookChart, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[WorkbookChartItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property charts for drives
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
    
    def to_get_request_information(self,request_configuration: Optional[WorkbookChartItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns collection of charts that are part of the worksheet. Read-only.
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
    
    def to_patch_request_information(self,body: Optional[workbook_chart.WorkbookChart] = None, request_configuration: Optional[WorkbookChartItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property charts in drives
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
    def axes(self) -> axes_request_builder.AxesRequestBuilder:
        """
        Provides operations to manage the axes property of the microsoft.graph.workbookChart entity.
        """
        from .axes import axes_request_builder

        return axes_request_builder.AxesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_labels(self) -> data_labels_request_builder.DataLabelsRequestBuilder:
        """
        Provides operations to manage the dataLabels property of the microsoft.graph.workbookChart entity.
        """
        from .data_labels import data_labels_request_builder

        return data_labels_request_builder.DataLabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def format(self) -> format_request_builder.FormatRequestBuilder:
        """
        Provides operations to manage the format property of the microsoft.graph.workbookChart entity.
        """
        from .format import format_request_builder

        return format_request_builder.FormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def image(self) -> image_request_builder.ImageRequestBuilder:
        """
        Provides operations to call the image method.
        """
        from .image import image_request_builder

        return image_request_builder.ImageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def legend(self) -> legend_request_builder.LegendRequestBuilder:
        """
        Provides operations to manage the legend property of the microsoft.graph.workbookChart entity.
        """
        from .legend import legend_request_builder

        return legend_request_builder.LegendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def series(self) -> series_request_builder.SeriesRequestBuilder:
        """
        Provides operations to manage the series property of the microsoft.graph.workbookChart entity.
        """
        from .series import series_request_builder

        return series_request_builder.SeriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_data(self) -> set_data_request_builder.SetDataRequestBuilder:
        """
        Provides operations to call the setData method.
        """
        from .set_data import set_data_request_builder

        return set_data_request_builder.SetDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_position(self) -> set_position_request_builder.SetPositionRequestBuilder:
        """
        Provides operations to call the setPosition method.
        """
        from .set_position import set_position_request_builder

        return set_position_request_builder.SetPositionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def title(self) -> title_request_builder.TitleRequestBuilder:
        """
        Provides operations to manage the title property of the microsoft.graph.workbookChart entity.
        """
        from .title import title_request_builder

        return title_request_builder.TitleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def worksheet(self) -> worksheet_request_builder.WorksheetRequestBuilder:
        """
        Provides operations to manage the worksheet property of the microsoft.graph.workbookChart entity.
        """
        from .worksheet import worksheet_request_builder

        return worksheet_request_builder.WorksheetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WorkbookChartItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WorkbookChartItemRequestBuilderGetQueryParameters():
        """
        Returns collection of charts that are part of the worksheet. Read-only.
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
    class WorkbookChartItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WorkbookChartItemRequestBuilder.WorkbookChartItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class WorkbookChartItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

