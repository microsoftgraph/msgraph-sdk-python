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
    from ......models import site
    from ......models.o_data_errors import o_data_error

class GetByPathWithPathRequestBuilder():
    """
    Provides operations to call the getByPath method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, path: Optional[str] = None) -> None:
        """
        Instantiates a new GetByPathWithPathRequestBuilder and sets the default values.
        Args:
            path: Usage: path='{path}'
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/getByPath(path='{path}')"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params[""] = path
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[GetByPathWithPathRequestBuilderGetRequestConfiguration] = None) -> Optional[site.Site]:
        """
        Invoke function getByPath
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[site.Site]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import site

        return await self.request_adapter.send_async(request_info, site.Site, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[GetByPathWithPathRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function getByPath
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
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    @dataclass
    class GetByPathWithPathRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

