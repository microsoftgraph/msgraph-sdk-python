from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import BaseRequestConfiguration
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation

from ...models.o_data_errors.o_data_error import ODataError
from ...models.page import Page
from ...models.site_pages_collection_response import SitePagesCollectionResponse

T = TypeVar("T", bound=Parsable)


class BaseSiteRequestBuilder(BaseRequestBuilder, Generic[T]):
    def __init__(
        self,
        parsable_factory: T,
        request_adapter: RequestAdapter,
        url_template: str,
        path_parameters: Optional[Union[(Dict[(str, Any)], str)]] = None,
    ) -> None:
        "\n        Instantiates a new SiteItemRequestBuilder and sets the default values.\n        param path_parameters: The raw url or the Url template parameters for the request.\n        param url_template: The url template.\n        param request_adapter: The request adapter to use to execute the requests.\n        Returns: None\n"
        super().__init__(request_adapter, url_template, path_parameters)
        self._parsable_factory = parsable_factory

    def to_get_request_information(
        self,
        request_configuration: Optional[
            SitePageRequestBuilderGetRequestConfiguration
        ] = None,
    ) -> RequestInformation:
        "\n        Retrieve properties and relationships for a [site][] resource.\n        A site resource represents a team site in SharePoint.\n        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.\n        Returns: RequestInformation\n"
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(
                request_configuration.query_parameters
            )
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info

    async def get(
        self,
        request_configuration: Optional[
            SitePageRequestBuilderGetRequestConfiguration
        ] = None,
    ) -> Optional[T]:
        "\n        Retrieve properties and relationships for a [site][] resource.\n        A site resource represents a team site in SharePoint.\n        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.\n        Returns: Optional[Site]\n        Find more info here: https://learn.microsoft.com/graph/api/site-get?view=graph-rest-1.0\n"
        request_info = self.to_get_request_information(request_configuration)
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[(str, ParsableFactory)] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null")
        return await self.request_adapter.send_async(
            request_info, self._parsable_factory, error_mapping
        )


class SitePagesRequestBuilder(BaseSiteRequestBuilder[SitePagesCollectionResponse]):
    "\n    Provides operations to manage the collection of site entities.\n"

    def __init__(
        self,
        request_adapter: RequestAdapter,
        path_parameters: Optional[Union[(Dict[(str, Any)], str)]] = None,
    ) -> None:
        "\n        Instantiates a new SiteItemRequestBuilder and sets the default values.\n        param path_parameters: The raw url or the Url template parameters for the request.\n        param request_adapter: The request adapter to use to execute the requests.\n        Returns: None\n"
        super().__init__(
            SitePagesCollectionResponse,
            request_adapter,
            "{+baseurl}/sites/{site%2Did}/pages",
            path_parameters,
        )


class SitePageRequestBuilder(BaseSiteRequestBuilder[Page]):
    "\n    Provides operations to manage the collection of site entities.\n"

    def __init__(
        self,
        request_adapter: RequestAdapter,
        path_parameters: Optional[Union[(Dict[(str, Any)], str)]] = None,
    ) -> None:
        "\n        Instantiates a new SiteItemRequestBuilder and sets the default values.\n        param path_parameters: The raw url or the Url template parameters for the request.\n        param request_adapter: The request adapter to use to execute the requests.\n        Returns: None\n"
        super().__init__(
            Page,
            request_adapter,
            "{+baseurl}/sites/{site%2Did}/pages/{page%2Did}",
            path_parameters,
        )


@dataclass
class SitePagesRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
    pass


@dataclass
class SitePageRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
    pass
