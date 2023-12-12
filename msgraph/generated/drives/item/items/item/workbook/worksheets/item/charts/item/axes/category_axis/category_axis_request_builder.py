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
    from ............models.o_data_errors.o_data_error import ODataError
    from ............models.workbook_chart_axis import WorkbookChartAxis
    from .format.format_request_builder import FormatRequestBuilder
    from .major_gridlines.major_gridlines_request_builder import MajorGridlinesRequestBuilder
    from .minor_gridlines.minor_gridlines_request_builder import MinorGridlinesRequestBuilder
    from .title.title_request_builder import TitleRequestBuilder

class CategoryAxisRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the categoryAxis property of the microsoft.graph.workbookChartAxes entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CategoryAxisRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}/axes/categoryAxis{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[CategoryAxisRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property categoryAxis for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ............models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CategoryAxisRequestBuilderGetRequestConfiguration] = None) -> Optional[WorkbookChartAxis]:
        """
        Represents the category axis in a chart. Read-only.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookChartAxis]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ............models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ............models.workbook_chart_axis import WorkbookChartAxis

        return await self.request_adapter.send_async(request_info, WorkbookChartAxis, error_mapping)
    
    async def patch(self,body: Optional[WorkbookChartAxis] = None, request_configuration: Optional[CategoryAxisRequestBuilderPatchRequestConfiguration] = None) -> Optional[WorkbookChartAxis]:
        """
        Update the navigation property categoryAxis in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookChartAxis]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ............models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ............models.workbook_chart_axis import WorkbookChartAxis

        return await self.request_adapter.send_async(request_info, WorkbookChartAxis, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CategoryAxisRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property categoryAxis for drives
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
    
    def to_get_request_information(self,request_configuration: Optional[CategoryAxisRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents the category axis in a chart. Read-only.
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
    
    def to_patch_request_information(self,body: Optional[WorkbookChartAxis] = None, request_configuration: Optional[CategoryAxisRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property categoryAxis in drives
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
    
    def with_url(self,raw_url: Optional[str] = None) -> CategoryAxisRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CategoryAxisRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CategoryAxisRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def format(self) -> FormatRequestBuilder:
        """
        Provides operations to manage the format property of the microsoft.graph.workbookChartAxis entity.
        """
        from .format.format_request_builder import FormatRequestBuilder

        return FormatRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def major_gridlines(self) -> MajorGridlinesRequestBuilder:
        """
        Provides operations to manage the majorGridlines property of the microsoft.graph.workbookChartAxis entity.
        """
        from .major_gridlines.major_gridlines_request_builder import MajorGridlinesRequestBuilder

        return MajorGridlinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def minor_gridlines(self) -> MinorGridlinesRequestBuilder:
        """
        Provides operations to manage the minorGridlines property of the microsoft.graph.workbookChartAxis entity.
        """
        from .minor_gridlines.minor_gridlines_request_builder import MinorGridlinesRequestBuilder

        return MinorGridlinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def title(self) -> TitleRequestBuilder:
        """
        Provides operations to manage the title property of the microsoft.graph.workbookChartAxis entity.
        """
        from .title.title_request_builder import TitleRequestBuilder

        return TitleRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CategoryAxisRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class CategoryAxisRequestBuilderGetQueryParameters():
        """
        Represents the category axis in a chart. Read-only.
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
    class CategoryAxisRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CategoryAxisRequestBuilder.CategoryAxisRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CategoryAxisRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

