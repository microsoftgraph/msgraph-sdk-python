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
    from .........models.canvas_layout import CanvasLayout
    from .........models.o_data_errors.o_data_error import ODataError
    from .horizontal_sections.horizontal_sections_request_builder import HorizontalSectionsRequestBuilder
    from .vertical_section.vertical_section_request_builder import VerticalSectionRequestBuilder

class CanvasLayoutRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the canvasLayout property of the microsoft.graph.sitePage entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CanvasLayoutRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/pages/{baseSitePage%2Did}/graph.sitePage/canvasLayout{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property canvasLayout for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CanvasLayoutRequestBuilderGetQueryParameters]] = None) -> Optional[CanvasLayout]:
        """
        Indicates the layout of the content in a given SharePoint page, including horizontal sections and vertical sections.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CanvasLayout]
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
        from .........models.canvas_layout import CanvasLayout

        return await self.request_adapter.send_async(request_info, CanvasLayout, error_mapping)
    
    async def patch(self,body: CanvasLayout, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CanvasLayout]:
        """
        Update the navigation property canvasLayout in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CanvasLayout]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .........models.canvas_layout import CanvasLayout

        return await self.request_adapter.send_async(request_info, CanvasLayout, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property canvasLayout for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CanvasLayoutRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Indicates the layout of the content in a given SharePoint page, including horizontal sections and vertical sections.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: CanvasLayout, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property canvasLayout in groups
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
    
    def with_url(self,raw_url: str) -> CanvasLayoutRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CanvasLayoutRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CanvasLayoutRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def horizontal_sections(self) -> HorizontalSectionsRequestBuilder:
        """
        Provides operations to manage the horizontalSections property of the microsoft.graph.canvasLayout entity.
        """
        from .horizontal_sections.horizontal_sections_request_builder import HorizontalSectionsRequestBuilder

        return HorizontalSectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vertical_section(self) -> VerticalSectionRequestBuilder:
        """
        Provides operations to manage the verticalSection property of the microsoft.graph.canvasLayout entity.
        """
        from .vertical_section.vertical_section_request_builder import VerticalSectionRequestBuilder

        return VerticalSectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CanvasLayoutRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CanvasLayoutRequestBuilderGetQueryParameters():
        """
        Indicates the layout of the content in a given SharePoint page, including horizontal sections and vertical sections.
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
    class CanvasLayoutRequestBuilderGetRequestConfiguration(RequestConfiguration[CanvasLayoutRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CanvasLayoutRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

