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
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.schedule import Schedule
    from .day_notes.day_notes_request_builder import DayNotesRequestBuilder
    from .offer_shift_requests.offer_shift_requests_request_builder import OfferShiftRequestsRequestBuilder
    from .open_shifts.open_shifts_request_builder import OpenShiftsRequestBuilder
    from .open_shift_change_requests.open_shift_change_requests_request_builder import OpenShiftChangeRequestsRequestBuilder
    from .scheduling_groups.scheduling_groups_request_builder import SchedulingGroupsRequestBuilder
    from .share.share_request_builder import ShareRequestBuilder
    from .shifts.shifts_request_builder import ShiftsRequestBuilder
    from .swap_shifts_change_requests.swap_shifts_change_requests_request_builder import SwapShiftsChangeRequestsRequestBuilder
    from .times_off.times_off_request_builder import TimesOffRequestBuilder
    from .time_cards.time_cards_request_builder import TimeCardsRequestBuilder
    from .time_off_reasons.time_off_reasons_request_builder import TimeOffReasonsRequestBuilder
    from .time_off_requests.time_off_requests_request_builder import TimeOffRequestsRequestBuilder

class ScheduleRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the schedule property of the microsoft.graph.team entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ScheduleRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/team/schedule{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property schedule for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ScheduleRequestBuilderGetQueryParameters]] = None) -> Optional[Schedule]:
        """
        The schedule of shifts for this team.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Schedule]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.schedule import Schedule

        return await self.request_adapter.send_async(request_info, Schedule, error_mapping)
    
    async def put(self,body: Schedule, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Schedule]:
        """
        Update the navigation property schedule in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Schedule]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.schedule import Schedule

        return await self.request_adapter.send_async(request_info, Schedule, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property schedule for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ScheduleRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The schedule of shifts for this team.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: Schedule, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property schedule in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ScheduleRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ScheduleRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ScheduleRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def day_notes(self) -> DayNotesRequestBuilder:
        """
        Provides operations to manage the dayNotes property of the microsoft.graph.schedule entity.
        """
        from .day_notes.day_notes_request_builder import DayNotesRequestBuilder

        return DayNotesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def offer_shift_requests(self) -> OfferShiftRequestsRequestBuilder:
        """
        Provides operations to manage the offerShiftRequests property of the microsoft.graph.schedule entity.
        """
        from .offer_shift_requests.offer_shift_requests_request_builder import OfferShiftRequestsRequestBuilder

        return OfferShiftRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def open_shift_change_requests(self) -> OpenShiftChangeRequestsRequestBuilder:
        """
        Provides operations to manage the openShiftChangeRequests property of the microsoft.graph.schedule entity.
        """
        from .open_shift_change_requests.open_shift_change_requests_request_builder import OpenShiftChangeRequestsRequestBuilder

        return OpenShiftChangeRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def open_shifts(self) -> OpenShiftsRequestBuilder:
        """
        Provides operations to manage the openShifts property of the microsoft.graph.schedule entity.
        """
        from .open_shifts.open_shifts_request_builder import OpenShiftsRequestBuilder

        return OpenShiftsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scheduling_groups(self) -> SchedulingGroupsRequestBuilder:
        """
        Provides operations to manage the schedulingGroups property of the microsoft.graph.schedule entity.
        """
        from .scheduling_groups.scheduling_groups_request_builder import SchedulingGroupsRequestBuilder

        return SchedulingGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def share(self) -> ShareRequestBuilder:
        """
        Provides operations to call the share method.
        """
        from .share.share_request_builder import ShareRequestBuilder

        return ShareRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shifts(self) -> ShiftsRequestBuilder:
        """
        Provides operations to manage the shifts property of the microsoft.graph.schedule entity.
        """
        from .shifts.shifts_request_builder import ShiftsRequestBuilder

        return ShiftsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def swap_shifts_change_requests(self) -> SwapShiftsChangeRequestsRequestBuilder:
        """
        Provides operations to manage the swapShiftsChangeRequests property of the microsoft.graph.schedule entity.
        """
        from .swap_shifts_change_requests.swap_shifts_change_requests_request_builder import SwapShiftsChangeRequestsRequestBuilder

        return SwapShiftsChangeRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def time_cards(self) -> TimeCardsRequestBuilder:
        """
        Provides operations to manage the timeCards property of the microsoft.graph.schedule entity.
        """
        from .time_cards.time_cards_request_builder import TimeCardsRequestBuilder

        return TimeCardsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def time_off_reasons(self) -> TimeOffReasonsRequestBuilder:
        """
        Provides operations to manage the timeOffReasons property of the microsoft.graph.schedule entity.
        """
        from .time_off_reasons.time_off_reasons_request_builder import TimeOffReasonsRequestBuilder

        return TimeOffReasonsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def time_off_requests(self) -> TimeOffRequestsRequestBuilder:
        """
        Provides operations to manage the timeOffRequests property of the microsoft.graph.schedule entity.
        """
        from .time_off_requests.time_off_requests_request_builder import TimeOffRequestsRequestBuilder

        return TimeOffRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def times_off(self) -> TimesOffRequestBuilder:
        """
        Provides operations to manage the timesOff property of the microsoft.graph.schedule entity.
        """
        from .times_off.times_off_request_builder import TimesOffRequestBuilder

        return TimesOffRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ScheduleRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ScheduleRequestBuilderGetQueryParameters():
        """
        The schedule of shifts for this team.
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
    class ScheduleRequestBuilderGetRequestConfiguration(RequestConfiguration[ScheduleRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ScheduleRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

