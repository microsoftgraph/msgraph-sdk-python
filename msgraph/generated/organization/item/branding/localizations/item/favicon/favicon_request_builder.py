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
    from .......models.o_data_errors.o_data_error import ODataError

class FaviconRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the media for the organization entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new FaviconRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}/branding/localizations/{organizationalBrandingLocalization%2Did}/favicon", path_parameters)
    
    async def get(self,request_configuration: Optional[FaviconRequestBuilderGetRequestConfiguration] = None) -> bytes:
        """
        A custom icon (favicon) to replace a default Microsoft product favicon on a Microsoft Entra tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        Find more info here: https://learn.microsoft.com/graph/api/organizationalbranding-list-localizations?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def put(self,body: bytes, content_type: Optional[str] = None, request_configuration: Optional[FaviconRequestBuilderPutRequestConfiguration] = None) -> bytes:
        """
        A custom icon (favicon) to replace a default Microsoft product favicon on a Microsoft Entra tenant.
        param body: Binary request body
        param content_type: The request body content type.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if not body:
            raise TypeError("body cannot be null.")
        if not content_type:
            raise TypeError("content_type cannot be null.")
        request_info = self.to_put_request_information(
            body, content_type, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[FaviconRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        A custom icon (favicon) to replace a default Microsoft product favicon on a Microsoft Entra tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "image/bmp, image/jpg, image/jpeg, image/gif, image/vnd.microsoft.icon, image/png, image/tiff, application/json")
        return request_info
    
    def to_put_request_information(self,body: bytes, content_type: Optional[str] = None, request_configuration: Optional[FaviconRequestBuilderPutRequestConfiguration] = None) -> RequestInformation:
        """
        A custom icon (favicon) to replace a default Microsoft product favicon on a Microsoft Entra tenant.
        param body: Binary request body
        param content_type: The request body content type.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        if not content_type:
            raise TypeError("content_type cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PUT
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_stream_content(body, content_type)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> FaviconRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FaviconRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return FaviconRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class FaviconRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class FaviconRequestBuilderPutRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

