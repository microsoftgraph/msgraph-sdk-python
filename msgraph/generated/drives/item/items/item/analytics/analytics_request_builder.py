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
    from ......models import item_analytics
    from ......models.o_data_errors import o_data_error
    from .all_time import all_time_request_builder
    from .item_activity_stats import item_activity_stats_request_builder
    from .last_seven_days import last_seven_days_request_builder

class AnalyticsRequestBuilder():
    """
    Provides operations to manage the analytics property of the microsoft.graph.driveItem entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AnalyticsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/analytics{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AnalyticsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property analytics for drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AnalyticsRequestBuilderGetRequestConfiguration] = None) -> Optional[item_analytics.ItemAnalytics]:
        """
        Analytics about the view activities that took place on this item.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[item_analytics.ItemAnalytics]
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
        from ......models import item_analytics

        return await self.request_adapter.send_async(request_info, item_analytics.ItemAnalytics, error_mapping)
    
    async def patch(self,body: Optional[item_analytics.ItemAnalytics] = None, request_configuration: Optional[AnalyticsRequestBuilderPatchRequestConfiguration] = None) -> Optional[item_analytics.ItemAnalytics]:
        """
        Update the navigation property analytics in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[item_analytics.ItemAnalytics]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import item_analytics

        return await self.request_adapter.send_async(request_info, item_analytics.ItemAnalytics, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AnalyticsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property analytics for drives
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
    
    def to_get_request_information(self,request_configuration: Optional[AnalyticsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Analytics about the view activities that took place on this item.
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
    
    def to_patch_request_information(self,body: Optional[item_analytics.ItemAnalytics] = None, request_configuration: Optional[AnalyticsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property analytics in drives
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
    def all_time(self) -> all_time_request_builder.AllTimeRequestBuilder:
        """
        Provides operations to manage the allTime property of the microsoft.graph.itemAnalytics entity.
        """
        from .all_time import all_time_request_builder

        return all_time_request_builder.AllTimeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def item_activity_stats(self) -> item_activity_stats_request_builder.ItemActivityStatsRequestBuilder:
        """
        Provides operations to manage the itemActivityStats property of the microsoft.graph.itemAnalytics entity.
        """
        from .item_activity_stats import item_activity_stats_request_builder

        return item_activity_stats_request_builder.ItemActivityStatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_seven_days(self) -> last_seven_days_request_builder.LastSevenDaysRequestBuilder:
        """
        Provides operations to manage the lastSevenDays property of the microsoft.graph.itemAnalytics entity.
        """
        from .last_seven_days import last_seven_days_request_builder

        return last_seven_days_request_builder.LastSevenDaysRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AnalyticsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AnalyticsRequestBuilderGetQueryParameters():
        """
        Analytics about the view activities that took place on this item.
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
    class AnalyticsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AnalyticsRequestBuilder.AnalyticsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AnalyticsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

