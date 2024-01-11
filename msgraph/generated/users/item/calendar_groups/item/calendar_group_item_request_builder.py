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
    from .....models.calendar_group import CalendarGroup
    from .....models.o_data_errors.o_data_error import ODataError
    from .calendars.calendars_request_builder import CalendarsRequestBuilder

class CalendarGroupItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the calendarGroups property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CalendarGroupItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/calendarGroups/{calendarGroup%2Did}{?%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[CalendarGroupItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a calendar group other than the default calendar group.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/calendargroup-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CalendarGroupItemRequestBuilderGetRequestConfiguration] = None) -> Optional[CalendarGroup]:
        """
        Retrieve the properties and relationships of a calendar group object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CalendarGroup]
        Find more info here: https://learn.microsoft.com/graph/api/calendargroup-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.calendar_group import CalendarGroup

        return await self.request_adapter.send_async(request_info, CalendarGroup, error_mapping)
    
    async def patch(self,body: Optional[CalendarGroup] = None, request_configuration: Optional[CalendarGroupItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[CalendarGroup]:
        """
        Update the properties of calendargroup object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CalendarGroup]
        Find more info here: https://learn.microsoft.com/graph/api/calendargroup-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.calendar_group import CalendarGroup

        return await self.request_adapter.send_async(request_info, CalendarGroup, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CalendarGroupItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a calendar group other than the default calendar group.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[CalendarGroupItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a calendar group object.
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
    
    def to_patch_request_information(self,body: Optional[CalendarGroup] = None, request_configuration: Optional[CalendarGroupItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of calendargroup object.
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
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CalendarGroupItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CalendarGroupItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CalendarGroupItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def calendars(self) -> CalendarsRequestBuilder:
        """
        Provides operations to manage the calendars property of the microsoft.graph.calendarGroup entity.
        """
        from .calendars.calendars_request_builder import CalendarsRequestBuilder

        return CalendarsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CalendarGroupItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class CalendarGroupItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a calendar group object.
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
    class CalendarGroupItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CalendarGroupItemRequestBuilder.CalendarGroupItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CalendarGroupItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

