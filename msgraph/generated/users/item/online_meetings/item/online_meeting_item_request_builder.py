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
    from .....models.online_meeting import OnlineMeeting
    from .....models.o_data_errors.o_data_error import ODataError
    from .attendance_reports.attendance_reports_request_builder import AttendanceReportsRequestBuilder
    from .attendee_report.attendee_report_request_builder import AttendeeReportRequestBuilder
    from .get_virtual_appointment_join_web_url.get_virtual_appointment_join_web_url_request_builder import GetVirtualAppointmentJoinWebUrlRequestBuilder
    from .recordings.recordings_request_builder import RecordingsRequestBuilder
    from .transcripts.transcripts_request_builder import TranscriptsRequestBuilder

class OnlineMeetingItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the onlineMeetings property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OnlineMeetingItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/onlineMeetings/{onlineMeeting%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete an onlineMeeting object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/onlinemeeting-delete?view=graph-rest-1.0
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
    
    async def get(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderGetRequestConfiguration] = None) -> Optional[OnlineMeeting]:
        """
        Retrieve the properties and relationships of an onlineMeeting object. For example, you can: Teams live event attendee report (deprecated) is an online meeting artifact. For details, see Online meeting artifacts and permissions.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnlineMeeting]
        Find more info here: https://learn.microsoft.com/graph/api/onlinemeeting-get?view=graph-rest-1.0
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
        from .....models.online_meeting import OnlineMeeting

        return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)
    
    async def patch(self,body: Optional[OnlineMeeting] = None, request_configuration: Optional[OnlineMeetingItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[OnlineMeeting]:
        """
        Update the properties of the specified onlineMeeting object. Please see Request body section for the list of properties that support updating.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OnlineMeeting]
        Find more info here: https://learn.microsoft.com/graph/api/onlinemeeting-update?view=graph-rest-1.0
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
        from .....models.online_meeting import OnlineMeeting

        return await self.request_adapter.send_async(request_info, OnlineMeeting, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an onlineMeeting object.
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
    
    def to_get_request_information(self,request_configuration: Optional[OnlineMeetingItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of an onlineMeeting object. For example, you can: Teams live event attendee report (deprecated) is an online meeting artifact. For details, see Online meeting artifacts and permissions.
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
    
    def to_patch_request_information(self,body: Optional[OnlineMeeting] = None, request_configuration: Optional[OnlineMeetingItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of the specified onlineMeeting object. Please see Request body section for the list of properties that support updating.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> OnlineMeetingItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OnlineMeetingItemRequestBuilder
        """
        if not raw_url:
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
    def transcripts(self) -> TranscriptsRequestBuilder:
        """
        Provides operations to manage the transcripts property of the microsoft.graph.onlineMeeting entity.
        """
        from .transcripts.transcripts_request_builder import TranscriptsRequestBuilder

        return TranscriptsRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OnlineMeetingItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class OnlineMeetingItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of an onlineMeeting object. For example, you can: Teams live event attendee report (deprecated) is an online meeting artifact. For details, see Online meeting artifacts and permissions.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OnlineMeetingItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[OnlineMeetingItemRequestBuilder.OnlineMeetingItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OnlineMeetingItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

