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
    from ..models.agreement import Agreement
    from ..models.agreement_collection_response import AgreementCollectionResponse
    from ..models.o_data_errors.o_data_error import ODataError
    from .item.agreement_item_request_builder import AgreementItemRequestBuilder

class AgreementsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AgreementsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/agreements{?%24search,%24select}", path_parameters)
    
    def by_agreement_id(self,agreement_id: str) -> AgreementItemRequestBuilder:
        """
        Provides operations to manage the collection of agreement entities.
        param agreement_id: The unique identifier of agreement
        Returns: AgreementItemRequestBuilder
        """
        if not agreement_id:
            raise TypeError("agreement_id cannot be null.")
        from .item.agreement_item_request_builder import AgreementItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreement%2Did"] = agreement_id
        return AgreementItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AgreementsRequestBuilderGetRequestConfiguration] = None) -> Optional[AgreementCollectionResponse]:
        """
        Get entities from agreements
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AgreementCollectionResponse]
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
        from ..models.agreement_collection_response import AgreementCollectionResponse

        return await self.request_adapter.send_async(request_info, AgreementCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[Agreement] = None, request_configuration: Optional[AgreementsRequestBuilderPostRequestConfiguration] = None) -> Optional[Agreement]:
        """
        Add new entity to agreements
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Agreement]
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
        from ..models.agreement import Agreement

        return await self.request_adapter.send_async(request_info, Agreement, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[AgreementsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get entities from agreements
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
    
    def to_post_request_information(self,body: Optional[Agreement] = None, request_configuration: Optional[AgreementsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Add new entity to agreements
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
    
    def with_url(self,raw_url: Optional[str] = None) -> AgreementsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AgreementsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AgreementsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AgreementsRequestBuilderGetQueryParameters():
        """
        Get entities from agreements
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AgreementsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AgreementsRequestBuilder.AgreementsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AgreementsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

