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
    from ....models.outlook_user import OutlookUser
    from ....models.o_data_errors.o_data_error import ODataError
    from .master_categories.master_categories_request_builder import MasterCategoriesRequestBuilder
    from .supported_languages.supported_languages_request_builder import SupportedLanguagesRequestBuilder
    from .supported_time_zones.supported_time_zones_request_builder import SupportedTimeZonesRequestBuilder
    from .supported_time_zones_with_time_zone_standard.supported_time_zones_with_time_zone_standard_request_builder import SupportedTimeZonesWithTimeZoneStandardRequestBuilder

class OutlookRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the outlook property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OutlookRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/outlook{?%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[OutlookRequestBuilderGetRequestConfiguration] = None) -> Optional[OutlookUser]:
        """
        Get outlook from users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OutlookUser]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.outlook_user import OutlookUser

        return await self.request_adapter.send_async(request_info, OutlookUser, error_mapping)
    
    def supported_time_zones_with_time_zone_standard(self,time_zone_standard: Optional[str] = None) -> SupportedTimeZonesWithTimeZoneStandardRequestBuilder:
        """
        Provides operations to call the supportedTimeZones method.
        param time_zone_standard: Usage: TimeZoneStandard='{TimeZoneStandard}'
        Returns: SupportedTimeZonesWithTimeZoneStandardRequestBuilder
        """
        if not time_zone_standard:
            raise TypeError("time_zone_standard cannot be null.")
        from .supported_time_zones_with_time_zone_standard.supported_time_zones_with_time_zone_standard_request_builder import SupportedTimeZonesWithTimeZoneStandardRequestBuilder

        return SupportedTimeZonesWithTimeZoneStandardRequestBuilder(self.request_adapter, self.path_parameters, time_zone_standard)
    
    def to_get_request_information(self,request_configuration: Optional[OutlookRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get outlook from users
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
    
    def with_url(self,raw_url: Optional[str] = None) -> OutlookRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OutlookRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return OutlookRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def master_categories(self) -> MasterCategoriesRequestBuilder:
        """
        Provides operations to manage the masterCategories property of the microsoft.graph.outlookUser entity.
        """
        from .master_categories.master_categories_request_builder import MasterCategoriesRequestBuilder

        return MasterCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def supported_languages(self) -> SupportedLanguagesRequestBuilder:
        """
        Provides operations to call the supportedLanguages method.
        """
        from .supported_languages.supported_languages_request_builder import SupportedLanguagesRequestBuilder

        return SupportedLanguagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def supported_time_zones(self) -> SupportedTimeZonesRequestBuilder:
        """
        Provides operations to call the supportedTimeZones method.
        """
        from .supported_time_zones.supported_time_zones_request_builder import SupportedTimeZonesRequestBuilder

        return SupportedTimeZonesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OutlookRequestBuilderGetQueryParameters():
        """
        Get outlook from users
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OutlookRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[OutlookRequestBuilder.OutlookRequestBuilderGetQueryParameters] = None

    

