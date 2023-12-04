from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, TYPE_CHECKING, Union, Any

from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.serialization import ParsableFactory

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.page import Page


class SitePageRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of site entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SiteItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/pages/{page%2Did}", path_parameters)
    
    async def get(self,request_configuration: Optional[SitePageRequestBuilderGetRequestConfiguration] = None) -> Optional[Page]:
        """
        Retrieve properties and relationships for a [site][] resource.A site resource represents a team site in SharePoint.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Site]
        Find more info here: https://learn.microsoft.com/graph/api/site-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.page import Page

        return await self.request_adapter.send_async(request_info, Page, error_mapping)

    def to_get_request_information(self,request_configuration: Optional[SitePageRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve properties and relationships for a [site][] resource.A site resource represents a team site in SharePoint.
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
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info


    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration


    @dataclass
    class SitePageRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        pass


