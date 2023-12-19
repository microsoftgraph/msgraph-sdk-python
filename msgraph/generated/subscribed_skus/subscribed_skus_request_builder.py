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
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.subscribed_sku import SubscribedSku
    from ..models.subscribed_sku_collection_response import SubscribedSkuCollectionResponse
    from .item.subscribed_sku_item_request_builder import SubscribedSkuItemRequestBuilder

class SubscribedSkusRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of subscribedSku entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SubscribedSkusRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/subscribedSkus{?%24search,%24orderby,%24select}", path_parameters)
    
    def by_subscribed_sku_id(self,subscribed_sku_id: str) -> SubscribedSkuItemRequestBuilder:
        """
        Provides operations to manage the collection of subscribedSku entities.
        param subscribed_sku_id: The unique identifier of subscribedSku
        Returns: SubscribedSkuItemRequestBuilder
        """
        if not subscribed_sku_id:
            raise TypeError("subscribed_sku_id cannot be null.")
        from .item.subscribed_sku_item_request_builder import SubscribedSkuItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["subscribedSku%2Did"] = subscribed_sku_id
        return SubscribedSkuItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[SubscribedSkusRequestBuilderGetRequestConfiguration] = None) -> Optional[SubscribedSkuCollectionResponse]:
        """
        Get the list of commercial subscriptions that an organization has acquired. For the mapping of license names as displayed on the Microsoft Entra admin center or the Microsoft 365 admin center against their Microsoft Graph skuId and skuPartNumber properties, see Product names and service plan identifiers for licensing.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SubscribedSkuCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/subscribedsku-list?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.subscribed_sku_collection_response import SubscribedSkuCollectionResponse

        return await self.request_adapter.send_async(request_info, SubscribedSkuCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[SubscribedSku] = None, request_configuration: Optional[SubscribedSkusRequestBuilderPostRequestConfiguration] = None) -> Optional[SubscribedSku]:
        """
        Add new entity to subscribedSkus
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SubscribedSku]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.subscribed_sku import SubscribedSku

        return await self.request_adapter.send_async(request_info, SubscribedSku, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[SubscribedSkusRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the list of commercial subscriptions that an organization has acquired. For the mapping of license names as displayed on the Microsoft Entra admin center or the Microsoft 365 admin center against their Microsoft Graph skuId and skuPartNumber properties, see Product names and service plan identifiers for licensing.
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
    
    def to_post_request_information(self,body: Optional[SubscribedSku] = None, request_configuration: Optional[SubscribedSkusRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Add new entity to subscribedSkus
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
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> SubscribedSkusRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SubscribedSkusRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SubscribedSkusRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SubscribedSkusRequestBuilderGetQueryParameters():
        """
        Get the list of commercial subscriptions that an organization has acquired. For the mapping of license names as displayed on the Microsoft Entra admin center or the Microsoft 365 admin center against their Microsoft Graph skuId and skuPartNumber properties, see Product names and service plan identifiers for licensing.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SubscribedSkusRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[SubscribedSkusRequestBuilder.SubscribedSkusRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class SubscribedSkusRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

