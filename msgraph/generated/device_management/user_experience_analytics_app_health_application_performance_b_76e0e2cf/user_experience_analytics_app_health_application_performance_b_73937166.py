from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.user_experience_analytics_app_health_app_performance_by_app_vers_47d72806 import UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_47d72806
    from ...models.user_experience_analytics_app_health_app_performance_by_app_vers_ba5b7522 import UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522
    from .count.count_request_builder import CountRequestBuilder
    from .item.user_experience_analytics_app_health_app_performance_by_app_vers_e69cea9d import UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_e69cea9d

class UserExperienceAnalyticsAppHealthApplicationPerformanceB_73937166(BaseRequestBuilder):
    """
    Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails property of the microsoft.graph.deviceManagement entity. Original name: UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UserExperienceAnalyticsAppHealthApplicationPerformanceB_73937166 and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "", path_parameters)
    
    def by_user_experience_analytics_app_health_app_performance_by_app_version_details_id(self,user_experience_analytics_app_health_app_performance_by_app_version_details_id: str) -> UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_e69cea9d:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails property of the microsoft.graph.deviceManagement entity.
        param user_experience_analytics_app_health_app_performance_by_app_version_details_id: The unique identifier of userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
        Returns: UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_e69cea9d
        """
        if user_experience_analytics_app_health_app_performance_by_app_version_details_id is None:
            raise TypeError("user_experience_analytics_app_health_app_performance_by_app_version_details_id cannot be null.")
        from .item.user_experience_analytics_app_health_app_performance_by_app_vers_e69cea9d import UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_e69cea9d

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails%2Did"] = user_experience_analytics_app_health_app_performance_by_app_version_details_id
        return UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_e69cea9d(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilderGetQueryParameters]] = None) -> Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_47d72806]:
        """
        User experience analytics appHealth Application Performance by App Version details
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_47d72806]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.user_experience_analytics_app_health_app_performance_by_app_vers_47d72806 import UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_47d72806

        return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_47d72806, error_mapping)
    
    async def post(self,body: UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522]:
        """
        Create new navigation property to userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails for deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.user_experience_analytics_app_health_app_performance_by_app_vers_ba5b7522 import UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522

        return await self.request_adapter.send_async(request_info, UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        User experience analytics appHealth Application Performance by App Version details
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails for deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> UserExperienceAnalyticsAppHealthApplicationPerformanceB_73937166:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UserExperienceAnalyticsAppHealthApplicationPerformanceB_73937166
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return UserExperienceAnalyticsAppHealthApplicationPerformanceB_73937166(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilderGetQueryParameters():
        """
        User experience analytics appHealth Application Performance by App Version details
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[list[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[list[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilderGetRequestConfiguration(RequestConfiguration[UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

