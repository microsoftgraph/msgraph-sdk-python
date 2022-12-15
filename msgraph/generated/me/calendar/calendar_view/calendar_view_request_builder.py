from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

count_request_builder = lazy_import('msgraph.generated.me.calendar.calendar_view.count.count_request_builder')
delta_request_builder = lazy_import('msgraph.generated.me.calendar.calendar_view.delta.delta_request_builder')
event_collection_response = lazy_import('msgraph.generated.models.event_collection_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class CalendarViewRequestBuilder():
    """
    Provides operations to manage the calendarView property of the microsoft.graph.calendar entity.
    """
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CalendarViewRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/calendar/calendarView{?startDateTime*,endDateTime*,%24top,%24skip,%24filter,%24count,%24orderby,%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[CalendarViewRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The calendar view for the calendar. Navigation property. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def delta(self,) -> delta_request_builder.DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        Returns: delta_request_builder.DeltaRequestBuilder
        """
        return delta_request_builder.DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    async def get(self,request_configuration: Optional[CalendarViewRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[event_collection_response.EventCollectionResponse]:
        """
        The calendar view for the calendar. Navigation property. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[event_collection_response.EventCollectionResponse]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, event_collection_response.EventCollectionResponse, response_handler, error_mapping)
    
    @dataclass
    class CalendarViewRequestBuilderGetQueryParameters():
        """
        The calendar view for the calendar. Navigation property. Read-only.
        """
        # Include count of items
        count: Optional[bool] = None

        # The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
        end_date_time: Optional[str] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
        start_date_time: Optional[str] = None

        # Show only the first n items
        top: Optional[int] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "count":
                return "%24count"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
    
    @dataclass
    class CalendarViewRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CalendarViewRequestBuilder.CalendarViewRequestBuilderGetQueryParameters] = None

    

