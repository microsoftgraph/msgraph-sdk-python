from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from ....models import schedule
from ....models.o_data_errors import o_data_error
from .offer_shift_requests import offer_shift_requests_request_builder
from .offer_shift_requests.item import offer_shift_request_item_request_builder
from .open_shift_change_requests import open_shift_change_requests_request_builder
from .open_shift_change_requests.item import open_shift_change_request_item_request_builder
from .open_shifts import open_shifts_request_builder
from .open_shifts.item import open_shift_item_request_builder
from .scheduling_groups import scheduling_groups_request_builder
from .scheduling_groups.item import scheduling_group_item_request_builder
from .share import share_request_builder
from .shifts import shifts_request_builder
from .shifts.item import shift_item_request_builder
from .swap_shifts_change_requests import swap_shifts_change_requests_request_builder
from .swap_shifts_change_requests.item import swap_shifts_change_request_item_request_builder
from .time_off_reasons import time_off_reasons_request_builder
from .time_off_reasons.item import time_off_reason_item_request_builder
from .time_off_requests import time_off_requests_request_builder
from .time_off_requests.item import time_off_request_item_request_builder
from .times_off import times_off_request_builder
from .times_off.item import time_off_item_request_builder

class ScheduleRequestBuilder():
    """
    Provides operations to manage the schedule property of the microsoft.graph.team entity.
    """
    def offer_shift_requests(self) -> offer_shift_requests_request_builder.OfferShiftRequestsRequestBuilder:
        """
        Provides operations to manage the offerShiftRequests property of the microsoft.graph.schedule entity.
        """
        return offer_shift_requests_request_builder.OfferShiftRequestsRequestBuilder(self.request_adapter, self.path_parameters)

    def open_shift_change_requests(self) -> open_shift_change_requests_request_builder.OpenShiftChangeRequestsRequestBuilder:
        """
        Provides operations to manage the openShiftChangeRequests property of the microsoft.graph.schedule entity.
        """
        return open_shift_change_requests_request_builder.OpenShiftChangeRequestsRequestBuilder(self.request_adapter, self.path_parameters)

    def open_shifts(self) -> open_shifts_request_builder.OpenShiftsRequestBuilder:
        """
        Provides operations to manage the openShifts property of the microsoft.graph.schedule entity.
        """
        return open_shifts_request_builder.OpenShiftsRequestBuilder(self.request_adapter, self.path_parameters)

    def scheduling_groups(self) -> scheduling_groups_request_builder.SchedulingGroupsRequestBuilder:
        """
        Provides operations to manage the schedulingGroups property of the microsoft.graph.schedule entity.
        """
        return scheduling_groups_request_builder.SchedulingGroupsRequestBuilder(self.request_adapter, self.path_parameters)

    def share(self) -> share_request_builder.ShareRequestBuilder:
        """
        Provides operations to call the share method.
        """
        return share_request_builder.ShareRequestBuilder(self.request_adapter, self.path_parameters)

    def shifts(self) -> shifts_request_builder.ShiftsRequestBuilder:
        """
        Provides operations to manage the shifts property of the microsoft.graph.schedule entity.
        """
        return shifts_request_builder.ShiftsRequestBuilder(self.request_adapter, self.path_parameters)

    def swap_shifts_change_requests(self) -> swap_shifts_change_requests_request_builder.SwapShiftsChangeRequestsRequestBuilder:
        """
        Provides operations to manage the swapShiftsChangeRequests property of the microsoft.graph.schedule entity.
        """
        return swap_shifts_change_requests_request_builder.SwapShiftsChangeRequestsRequestBuilder(self.request_adapter, self.path_parameters)

    def time_off_reasons(self) -> time_off_reasons_request_builder.TimeOffReasonsRequestBuilder:
        """
        Provides operations to manage the timeOffReasons property of the microsoft.graph.schedule entity.
        """
        return time_off_reasons_request_builder.TimeOffReasonsRequestBuilder(self.request_adapter, self.path_parameters)

    def time_off_requests(self) -> time_off_requests_request_builder.TimeOffRequestsRequestBuilder:
        """
        Provides operations to manage the timeOffRequests property of the microsoft.graph.schedule entity.
        """
        return time_off_requests_request_builder.TimeOffRequestsRequestBuilder(self.request_adapter, self.path_parameters)

    def times_off(self) -> times_off_request_builder.TimesOffRequestBuilder:
        """
        Provides operations to manage the timesOff property of the microsoft.graph.schedule entity.
        """
        return times_off_request_builder.TimesOffRequestBuilder(self.request_adapter, self.path_parameters)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ScheduleRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise Exception("path_parameters cannot be undefined")
        if not request_adapter:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/teams/{team%2Did}/schedule{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def create_delete_request_information(self,request_configuration: Optional[ScheduleRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property schedule for teams
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

    def create_get_request_information(self,request_configuration: Optional[ScheduleRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a schedule object. The schedule creation process conforms to the One API guideline for resource based long running operations (RELO).When clients use the PUT method, if the schedule is provisioned, the operation updates the schedule; otherwise, the operation starts the schedule provisioning process in the background. During schedule provisioning, clients can use the GET method to get the schedule and look at the `provisionStatus` property for the current state of the provisioning. If the provisioning failed, clients can get additional information from the `provisionStatusCode` property. Clients can also inspect the configuration of the schedule.
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

    def create_put_request_information(self,body: Optional[schedule.Schedule] = None, request_configuration: Optional[ScheduleRequestBuilderPutRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property schedule in teams
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PUT
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info

    async def delete(self,request_configuration: Optional[ScheduleRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property schedule for teams
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)

    async def get(self,request_configuration: Optional[ScheduleRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[schedule.Schedule]:
        """
        Retrieve the properties and relationships of a schedule object. The schedule creation process conforms to the One API guideline for resource based long running operations (RELO).When clients use the PUT method, if the schedule is provisioned, the operation updates the schedule; otherwise, the operation starts the schedule provisioning process in the background. During schedule provisioning, clients can use the GET method to get the schedule and look at the `provisionStatus` property for the current state of the provisioning. If the provisioning failed, clients can get additional information from the `provisionStatusCode` property. Clients can also inspect the configuration of the schedule.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[schedule.Schedule]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, schedule.Schedule, response_handler, error_mapping)

    def offer_shift_requests_by_id(self,id: str) -> offer_shift_request_item_request_builder.OfferShiftRequestItemRequestBuilder:
        """
        Provides operations to manage the offerShiftRequests property of the microsoft.graph.schedule entity.
        Args:
            id: Unique identifier of the item
        Returns: offer_shift_request_item_request_builder.OfferShiftRequestItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["offerShiftRequest%2Did"] = id
        return offer_shift_request_item_request_builder.OfferShiftRequestItemRequestBuilder(self.request_adapter, url_tpl_params)

    def open_shift_change_requests_by_id(self,id: str) -> open_shift_change_request_item_request_builder.OpenShiftChangeRequestItemRequestBuilder:
        """
        Provides operations to manage the openShiftChangeRequests property of the microsoft.graph.schedule entity.
        Args:
            id: Unique identifier of the item
        Returns: open_shift_change_request_item_request_builder.OpenShiftChangeRequestItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["openShiftChangeRequest%2Did"] = id
        return open_shift_change_request_item_request_builder.OpenShiftChangeRequestItemRequestBuilder(self.request_adapter, url_tpl_params)

    def open_shifts_by_id(self,id: str) -> open_shift_item_request_builder.OpenShiftItemRequestBuilder:
        """
        Provides operations to manage the openShifts property of the microsoft.graph.schedule entity.
        Args:
            id: Unique identifier of the item
        Returns: open_shift_item_request_builder.OpenShiftItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["openShift%2Did"] = id
        return open_shift_item_request_builder.OpenShiftItemRequestBuilder(self.request_adapter, url_tpl_params)

    async def put(self,body: Optional[schedule.Schedule] = None, request_configuration: Optional[ScheduleRequestBuilderPutRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[schedule.Schedule]:
        """
        Update the navigation property schedule in teams
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[schedule.Schedule]
        """
        if not body:
            raise Exception("body cannot be undefined")
        request_info = self.create_put_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, schedule.Schedule, response_handler, error_mapping)

    def scheduling_groups_by_id(self,id: str) -> scheduling_group_item_request_builder.SchedulingGroupItemRequestBuilder:
        """
        Provides operations to manage the schedulingGroups property of the microsoft.graph.schedule entity.
        Args:
            id: Unique identifier of the item
        Returns: scheduling_group_item_request_builder.SchedulingGroupItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["schedulingGroup%2Did"] = id
        return scheduling_group_item_request_builder.SchedulingGroupItemRequestBuilder(self.request_adapter, url_tpl_params)

    def shifts_by_id(self,id: str) -> shift_item_request_builder.ShiftItemRequestBuilder:
        """
        Provides operations to manage the shifts property of the microsoft.graph.schedule entity.
        Args:
            id: Unique identifier of the item
        Returns: shift_item_request_builder.ShiftItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["shift%2Did"] = id
        return shift_item_request_builder.ShiftItemRequestBuilder(self.request_adapter, url_tpl_params)

    def swap_shifts_change_requests_by_id(self,id: str) -> swap_shifts_change_request_item_request_builder.SwapShiftsChangeRequestItemRequestBuilder:
        """
        Provides operations to manage the swapShiftsChangeRequests property of the microsoft.graph.schedule entity.
        Args:
            id: Unique identifier of the item
        Returns: swap_shifts_change_request_item_request_builder.SwapShiftsChangeRequestItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["swapShiftsChangeRequest%2Did"] = id
        return swap_shifts_change_request_item_request_builder.SwapShiftsChangeRequestItemRequestBuilder(self.request_adapter, url_tpl_params)

    def time_off_reasons_by_id(self,id: str) -> time_off_reason_item_request_builder.TimeOffReasonItemRequestBuilder:
        """
        Provides operations to manage the timeOffReasons property of the microsoft.graph.schedule entity.
        Args:
            id: Unique identifier of the item
        Returns: time_off_reason_item_request_builder.TimeOffReasonItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["timeOffReason%2Did"] = id
        return time_off_reason_item_request_builder.TimeOffReasonItemRequestBuilder(self.request_adapter, url_tpl_params)

    def time_off_requests_by_id(self,id: str) -> time_off_request_item_request_builder.TimeOffRequestItemRequestBuilder:
        """
        Provides operations to manage the timeOffRequests property of the microsoft.graph.schedule entity.
        Args:
            id: Unique identifier of the item
        Returns: time_off_request_item_request_builder.TimeOffRequestItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["timeOffRequest%2Did"] = id
        return time_off_request_item_request_builder.TimeOffRequestItemRequestBuilder(self.request_adapter, url_tpl_params)

    def times_off_by_id(self,id: str) -> time_off_item_request_builder.TimeOffItemRequestBuilder:
        """
        Provides operations to manage the timesOff property of the microsoft.graph.schedule entity.
        Args:
            id: Unique identifier of the item
        Returns: time_off_item_request_builder.TimeOffItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["timeOff%2Did"] = id
        return time_off_item_request_builder.TimeOffItemRequestBuilder(self.request_adapter, url_tpl_params)

    @dataclass
    class ScheduleRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ScheduleRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a schedule object. The schedule creation process conforms to the One API guideline for resource based long running operations (RELO).When clients use the PUT method, if the schedule is provisioned, the operation updates the schedule; otherwise, the operation starts the schedule provisioning process in the background. During schedule provisioning, clients can use the GET method to get the schedule and look at the `provisionStatus` property for the current state of the provisioning. If the provisioning failed, clients can get additional information from the `provisionStatusCode` property. Clients can also inspect the configuration of the schedule.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name

    
    @dataclass
    class ScheduleRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ScheduleRequestBuilder.ScheduleRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ScheduleRequestBuilderPutRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

