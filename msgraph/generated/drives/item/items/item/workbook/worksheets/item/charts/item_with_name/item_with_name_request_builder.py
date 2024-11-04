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

class ItemWithNameRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the item method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], name: Optional[str] = None) -> None:
        """
        Instantiates a new ItemWithNameRequestBuilder and sets the default values.
        param name: Usage: name='{name}'
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['name'] = name
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/item(name='{name}')", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WorkbookChart]:
        """
        Invoke function item
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookChart]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.workbook_chart import WorkbookChart

        return await self.request_adapter.send_async(request_info, WorkbookChart, error_mapping)
    
    def image_with_width(self,width: int) -> ImageWithWidthRequestBuilder:
        """
        Provides operations to call the image method.
        param width: Usage: width={width}
        Returns: ImageWithWidthRequestBuilder
        """
        if width is None:
            raise TypeError("width cannot be null.")
        from .image_with_width.image_with_width_request_builder import ImageWithWidthRequestBuilder

        return ImageWithWidthRequestBuilder(self.request_adapter, self.path_parameters, width)
    
    def image_with_width_with_height(self,height: int, width: int) -> ImageWithWidthWithHeightRequestBuilder:
        """
        Provides operations to call the image method.
        param height: Usage: height={height}
        param width: Usage: width={width}
        Returns: ImageWithWidthWithHeightRequestBuilder
        """
        if height is None:
            raise TypeError("height cannot be null.")
        if width is None:
            raise TypeError("width cannot be null.")
        from .image_with_width_with_height.image_with_width_with_height_request_builder import ImageWithWidthWithHeightRequestBuilder

        return ImageWithWidthWithHeightRequestBuilder(self.request_adapter, self.path_parameters, height, width)
    
    def image_with_width_with_height_with_fitting_mode(self,fitting_mode: str, height: int, width: int) -> ImageWithWidthWithHeightWithFittingModeRequestBuilder:
        """
        Provides operations to call the image method.
        param fitting_mode: Usage: fittingMode='{fittingMode}'
        param height: Usage: height={height}
        param width: Usage: width={width}
        Returns: ImageWithWidthWithHeightWithFittingModeRequestBuilder
        """
        if fitting_mode is None:
            raise TypeError("fitting_mode cannot be null.")
        if height is None:
            raise TypeError("height cannot be null.")
        if width is None:
            raise TypeError("width cannot be null.")
        from .image_with_width_with_height_with_fitting_mode.image_with_width_with_height_with_fitting_mode_request_builder import ImageWithWidthWithHeightWithFittingModeRequestBuilder

        return ImageWithWidthWithHeightWithFittingModeRequestBuilder(self.request_adapter, self.path_parameters, fitting_mode, height, width)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Invoke function item
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ItemWithNameRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ItemWithNameRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ItemWithNameRequestBuilder(self.request_adapter, raw_url)
    
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
    
    @dataclass
    class ItemWithNameRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

