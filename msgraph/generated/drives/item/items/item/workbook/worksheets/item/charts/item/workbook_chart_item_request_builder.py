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
    from ..........models.o_data_errors.o_data_error import ODataError
    from ..........models.workbook_chart import WorkbookChart
    from .axes.axes_request_builder import AxesRequestBuilder
    from .data_labels.data_labels_request_builder import DataLabelsRequestBuilder
    from .format.format_request_builder import FormatRequestBuilder
    from .image.image_request_builder import ImageRequestBuilder
    from .image_with_width.image_with_width_request_builder import ImageWithWidthRequestBuilder
    from .image_with_width_with_height.image_with_width_with_height_request_builder import ImageWithWidthWithHeightRequestBuilder
    from .image_with_width_with_height_with_fitting_mode.image_with_width_with_height_with_fitting_mode_request_builder import ImageWithWidthWithHeightWithFittingModeRequestBuilder
    from .legend.legend_request_builder import LegendRequestBuilder
    from .series.series_request_builder import SeriesRequestBuilder
    from .set_data.set_data_request_builder import SetDataRequestBuilder
    from .set_position.set_position_request_builder import SetPositionRequestBuilder
    from .title.title_request_builder import TitleRequestBuilder
    from .worksheet.worksheet_request_builder import WorksheetRequestBuilder

class WorkbookChartItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the charts property of the microsoft.graph.workbookWorksheet entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkbookChartItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[WorkbookChartItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes the chart object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/chart-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WorkbookChartItemRequestBuilderGetRequestConfiguration] = None) -> Optional[WorkbookChart]:
        """
        Retrieve the properties and relationships of chart object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookChart]
        Find more info here: https://learn.microsoft.com/graph/api/chart-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.workbook_chart import WorkbookChart

        return await self.request_adapter.send_async(request_info, WorkbookChart, error_mapping)
    
    def image_with_width(self,width: Optional[int] = None) -> ImageWithWidthRequestBuilder:
        """
        Provides operations to call the image method.
        param width: Usage: width={width}
        Returns: ImageWithWidthRequestBuilder
        """
        if not width:
            raise TypeError("width cannot be null.")
        from .image_with_width.image_with_width_request_builder import ImageWithWidthRequestBuilder

        return ImageWithWidthRequestBuilder(self.request_adapter, self.path_parameters, width)
    
    def image_with_width_with_height(self,height: Optional[int] = None, width: Optional[int] = None) -> ImageWithWidthWithHeightRequestBuilder:
        """
        Provides operations to call the image method.
        param height: Usage: height={height}
        param width: Usage: width={width}
        Returns: ImageWithWidthWithHeightRequestBuilder
        """
        if not height:
            raise TypeError("height cannot be null.")
        if not width:
            raise TypeError("width cannot be null.")
        from .image_with_width_with_height.image_with_width_with_height_request_builder import ImageWithWidthWithHeightRequestBuilder

        return ImageWithWidthWithHeightRequestBuilder(self.request_adapter, self.path_parameters, height, width)
    
    def image_with_width_with_height_with_fitting_mode(self,fitting_mode: Optional[str] = None, height: Optional[int] = None, width: Optional[int] = None) -> ImageWithWidthWithHeightWithFittingModeRequestBuilder:
        """
        Provides operations to call the image method.
        param fitting_mode: Usage: fittingMode='{fittingMode}'
        param height: Usage: height={height}
        param width: Usage: width={width}
        Returns: ImageWithWidthWithHeightWithFittingModeRequestBuilder
        """
        if not fitting_mode:
            raise TypeError("fitting_mode cannot be null.")
        if not height:
            raise TypeError("height cannot be null.")
        if not width:
            raise TypeError("width cannot be null.")
        from .image_with_width_with_height_with_fitting_mode.image_with_width_with_height_with_fitting_mode_request_builder import ImageWithWidthWithHeightWithFittingModeRequestBuilder

        return ImageWithWidthWithHeightWithFittingModeRequestBuilder(self.request_adapter, self.path_parameters, fitting_mode, height, width)
    
    async def patch(self,body: Optional[WorkbookChart] = None, request_configuration: Optional[WorkbookChartItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[WorkbookChart]:
        """
        Update the properties of chart object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookChart]
        Find more info here: https://learn.microsoft.com/graph/api/chart-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.workbook_chart import WorkbookChart

        return await self.request_adapter.send_async(request_info, WorkbookChart, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[WorkbookChartItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes the chart object.
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
    
    def to_get_request_information(self,request_configuration: Optional[WorkbookChartItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of chart object.
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
    
    def to_patch_request_information(self,body: Optional[WorkbookChart] = None, request_configuration: Optional[WorkbookChartItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of chart object.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> WorkbookChartItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WorkbookChartItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return WorkbookChartItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def axes(self) -> AxesRequestBuilder:
        """
        Provides operations to manage the axes property of the microsoft.graph.workbookChart entity.
        """
        from .axes.axes_request_builder import AxesRequestBuilder

        return AxesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_labels(self) -> DataLabelsRequestBuilder:
        """
        Provides operations to manage the dataLabels property of the microsoft.graph.workbookChart entity.
        """
        from .data_labels.data_labels_request_builder import DataLabelsRequestBuilder

        return DataLabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def format(self) -> FormatRequestBuilder:
        """
        Provides operations to manage the format property of the microsoft.graph.workbookChart entity.
        """
        from .format.format_request_builder import FormatRequestBuilder

        return FormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def image(self) -> ImageRequestBuilder:
        """
        Provides operations to call the image method.
        """
        from .image.image_request_builder import ImageRequestBuilder

        return ImageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def legend(self) -> LegendRequestBuilder:
        """
        Provides operations to manage the legend property of the microsoft.graph.workbookChart entity.
        """
        from .legend.legend_request_builder import LegendRequestBuilder

        return LegendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def series(self) -> SeriesRequestBuilder:
        """
        Provides operations to manage the series property of the microsoft.graph.workbookChart entity.
        """
        from .series.series_request_builder import SeriesRequestBuilder

        return SeriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_data(self) -> SetDataRequestBuilder:
        """
        Provides operations to call the setData method.
        """
        from .set_data.set_data_request_builder import SetDataRequestBuilder

        return SetDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_position(self) -> SetPositionRequestBuilder:
        """
        Provides operations to call the setPosition method.
        """
        from .set_position.set_position_request_builder import SetPositionRequestBuilder

        return SetPositionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def title(self) -> TitleRequestBuilder:
        """
        Provides operations to manage the title property of the microsoft.graph.workbookChart entity.
        """
        from .title.title_request_builder import TitleRequestBuilder

        return TitleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def worksheet(self) -> WorksheetRequestBuilder:
        """
        Provides operations to manage the worksheet property of the microsoft.graph.workbookChart entity.
        """
        from .worksheet.worksheet_request_builder import WorksheetRequestBuilder

        return WorksheetRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WorkbookChartItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class WorkbookChartItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of chart object.
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
    class WorkbookChartItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[WorkbookChartItemRequestBuilder.WorkbookChartItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class WorkbookChartItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

