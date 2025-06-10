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
    from .....models.online_meeting import OnlineMeeting
    from .....models.o_data_errors.o_data_error import ODataError
    from .attendance_reports.attendance_reports_request_builder import AttendanceReportsRequestBuilder
    from .attendee_report.attendee_report_request_builder import AttendeeReportRequestBuilder
    from .get_virtual_appointment_join_web_url.get_virtual_appointment_join_web_url_request_builder import GetVirtualAppointmentJoinWebUrlRequestBuilder
    from .recordings.recordings_request_builder import RecordingsRequestBuilder
    from .send_virtual_appointment_reminder_sms.send_virtual_appointment_reminder_sms_request_builder import SendVirtualAppointmentReminderSmsRequestBuilder
    from .send_virtual_appointment_sms.send_virtual_appointment_sms_request_builder import SendVirtualAppointmentSmsRequestBuilder
    from .transcripts.transcripts_request_builder import TranscriptsRequestBuilder

class OnlineMeetingItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the onlineMeetings property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OnlineMeetingItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/onlineMeetings/{onlineMeeting%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property onlineMeetings for users
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[OnlineMeetingItemRequestBuilderGetQueryParameters]] = None) -> Optional[OnlineMeeting]:
        """
        Information about a meeting, including the URL used to join a meeting, the attendees list, and the description.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnlineMeeting]
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
        from .....models.online_meeting import OnlineMeeting

        return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)
    
    async def patch(self,body: OnlineMeeting, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OnlineMeeting]:
        """
        Update the navigation property onlineMeetings in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnlineMeeting]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.online_meeting import OnlineMeeting

        return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property onlineMeetings for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[OnlineMeetingItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Information about a meeting, including the URL used to join a meeting, the attendees list, and the description.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: OnlineMeeting, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property onlineMeetings in users
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
    
    def with_url(self,raw_url: str) -> OnlineMeetingItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OnlineMeetingItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OnlineMeetingItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def attendance_reports(self) -> AttendanceReportsRequestBuilder:
        """
        Provides operations to manage the attendanceReports property of the microsoft.graph.onlineMeetingBase entity.
        """
        from .attendance_reports.attendance_reports_request_builder import AttendanceReportsRequestBuilder

        return AttendanceReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attendee_report(self) -> AttendeeReportRequestBuilder:
        """
        Provides operations to manage the media for the user entity.
        """
        from .attendee_report.attendee_report_request_builder import AttendeeReportRequestBuilder

        return AttendeeReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_virtual_appointment_join_web_url(self) -> GetVirtualAppointmentJoinWebUrlRequestBuilder:
        """
        Provides operations to call the getVirtualAppointmentJoinWebUrl method.
        """
        from .get_virtual_appointment_join_web_url.get_virtual_appointment_join_web_url_request_builder import GetVirtualAppointmentJoinWebUrlRequestBuilder

        return GetVirtualAppointmentJoinWebUrlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recordings(self) -> RecordingsRequestBuilder:
        """
        Provides operations to manage the recordings property of the microsoft.graph.onlineMeeting entity.
        """
        from .recordings.recordings_request_builder import RecordingsRequestBuilder

        return RecordingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_virtual_appointment_reminder_sms(self) -> SendVirtualAppointmentReminderSmsRequestBuilder:
        """
        Provides operations to call the sendVirtualAppointmentReminderSms method.
        """
        from .send_virtual_appointment_reminder_sms.send_virtual_appointment_reminder_sms_request_builder import SendVirtualAppointmentReminderSmsRequestBuilder

        return SendVirtualAppointmentReminderSmsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_virtual_appointment_sms(self) -> SendVirtualAppointmentSmsRequestBuilder:
        """
        Provides operations to call the sendVirtualAppointmentSms method.
        """
        from .send_virtual_appointment_sms.send_virtual_appointment_sms_request_builder import SendVirtualAppointmentSmsRequestBuilder

        return SendVirtualAppointmentSmsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transcripts(self) -> TranscriptsRequestBuilder:
        """
        Provides operations to manage the transcripts property of the microsoft.graph.onlineMeeting entity.
        """
        from .transcripts.transcripts_request_builder import TranscriptsRequestBuilder

        return TranscriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OnlineMeetingItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OnlineMeetingItemRequestBuilderGetQueryParameters():
        """
        Information about a meeting, including the URL used to join a meeting, the attendees list, and the description.
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
    class OnlineMeetingItemRequestBuilderGetRequestConfiguration(RequestConfiguration[OnlineMeetingItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OnlineMeetingItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

