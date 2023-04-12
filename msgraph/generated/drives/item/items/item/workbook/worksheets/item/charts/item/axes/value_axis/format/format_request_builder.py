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
    from .............models import workbook_chart_axis_format
    from .............models.o_data_errors import o_data_error
    from .font import font_request_builder
    from .line import line_request_builder

class FormatRequestBuilder():
    """
    Provides operations to manage the format property of the microsoft.graph.workbookChartAxis entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new FormatRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/worksheets/{workbookWorksheet%2Did}/charts/{workbookChart%2Did}/axes/valueAxis/format{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[FormatRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property format for drives
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
    
    async def get(self,request_configuration: Optional[FormatRequestBuilderGetRequestConfiguration] = None) -> Optional[workbook_chart_axis_format.WorkbookChartAxisFormat]:
        """
        Represents the formatting of a chart object, which includes line and font formatting. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_chart_axis_format.WorkbookChartAxisFormat]
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
        from .............models import workbook_chart_axis_format

        return await self.request_adapter.send_async(request_info, workbook_chart_axis_format.WorkbookChartAxisFormat, error_mapping)
    
    async def patch(self,body: Optional[workbook_chart_axis_format.WorkbookChartAxisFormat] = None, request_configuration: Optional[FormatRequestBuilderPatchRequestConfiguration] = None) -> Optional[workbook_chart_axis_format.WorkbookChartAxisFormat]:
        """
        Update the navigation property format in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook_chart_axis_format.WorkbookChartAxisFormat]
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
        from .............models import workbook_chart_axis_format

        return await self.request_adapter.send_async(request_info, workbook_chart_axis_format.WorkbookChartAxisFormat, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[FormatRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property format for drives
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
    
    def to_get_request_information(self,request_configuration: Optional[FormatRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Represents the formatting of a chart object, which includes line and font formatting. Read-only.
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
    
    def to_patch_request_information(self,body: Optional[workbook_chart_axis_format.WorkbookChartAxisFormat] = None, request_configuration: Optional[FormatRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property format in drives
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
    def font(self) -> font_request_builder.FontRequestBuilder:
        """
        Provides operations to manage the font property of the microsoft.graph.workbookChartAxisFormat entity.
        """
        from .font import font_request_builder

        return font_request_builder.FontRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def line(self) -> line_request_builder.LineRequestBuilder:
        """
        Provides operations to manage the line property of the microsoft.graph.workbookChartAxisFormat entity.
        """
        from .line import line_request_builder

        return line_request_builder.LineRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FormatRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class FormatRequestBuilderGetQueryParameters():
        """
        Represents the formatting of a chart object, which includes line and font formatting. Read-only.
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
    class FormatRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[FormatRequestBuilder.FormatRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class FormatRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

