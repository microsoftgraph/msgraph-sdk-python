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
    from .......models.o_data_errors.o_data_error import ODataError
    from .......models.time_card import TimeCard
    from .clock_out.clock_out_request_builder import ClockOutRequestBuilder
    from .confirm.confirm_request_builder import ConfirmRequestBuilder
    from .end_break.end_break_request_builder import EndBreakRequestBuilder
    from .start_break.start_break_request_builder import StartBreakRequestBuilder

class TimeCardItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the timeCards property of the microsoft.graph.schedule entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TimeCardItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/team/schedule/timeCards/{timeCard%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property timeCards for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[TimeCardItemRequestBuilderGetQueryParameters]] = None) -> Optional[TimeCard]:
        """
        The time cards in the schedule.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimeCard]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.time_card import TimeCard

        return await self.request_adapter.send_async(request_info, TimeCard, error_mapping)
    
    async def patch(self,body: TimeCard, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TimeCard]:
        """
        Update the navigation property timeCards in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TimeCard]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.time_card import TimeCard

        return await self.request_adapter.send_async(request_info, TimeCard, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property timeCards for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[TimeCardItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The time cards in the schedule.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: TimeCard, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property timeCards in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> TimeCardItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TimeCardItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TimeCardItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def clock_out(self) -> ClockOutRequestBuilder:
        """
        Provides operations to call the clockOut method.
        """
        from .clock_out.clock_out_request_builder import ClockOutRequestBuilder

        return ClockOutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def confirm(self) -> ConfirmRequestBuilder:
        """
        Provides operations to call the confirm method.
        """
        from .confirm.confirm_request_builder import ConfirmRequestBuilder

        return ConfirmRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def end_break(self) -> EndBreakRequestBuilder:
        """
        Provides operations to call the endBreak method.
        """
        from .end_break.end_break_request_builder import EndBreakRequestBuilder

        return EndBreakRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start_break(self) -> StartBreakRequestBuilder:
        """
        Provides operations to call the startBreak method.
        """
        from .start_break.start_break_request_builder import StartBreakRequestBuilder

        return StartBreakRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TimeCardItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TimeCardItemRequestBuilderGetQueryParameters():
        """
        The time cards in the schedule.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class TimeCardItemRequestBuilderGetRequestConfiguration(RequestConfiguration[TimeCardItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class TimeCardItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

