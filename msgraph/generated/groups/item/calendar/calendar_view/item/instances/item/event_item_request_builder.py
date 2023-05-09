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
    from ........models import event
    from ........models.o_data_errors import o_data_error
    from .accept import accept_request_builder
    from .attachments import attachments_request_builder
    from .calendar import calendar_request_builder
    from .cancel import cancel_request_builder
    from .decline import decline_request_builder
    from .dismiss_reminder import dismiss_reminder_request_builder
    from .extensions import extensions_request_builder
    from .forward import forward_request_builder
    from .snooze_reminder import snooze_reminder_request_builder
    from .tentatively_accept import tentatively_accept_request_builder

class EventItemRequestBuilder():
    """
    Provides operations to manage the instances property of the microsoft.graph.event entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EventItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/calendar/calendarView/{event%2Did}/instances/{event%2Did1}{?startDateTime*,endDateTime*,%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[EventItemRequestBuilderGetRequestConfiguration] = None) -> Optional[event.Event]:
        """
        The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[event.Event]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models import event

        return await self.request_adapter.send_async(request_info, event.Event, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[EventItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
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
    
    @property
    def accept(self) -> accept_request_builder.AcceptRequestBuilder:
        """
        Provides operations to call the accept method.
        """
        from .accept import accept_request_builder

        return accept_request_builder.AcceptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def attachments(self) -> attachments_request_builder.AttachmentsRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.event entity.
        """
        from .attachments import attachments_request_builder

        return attachments_request_builder.AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar(self) -> calendar_request_builder.CalendarRequestBuilder:
        """
        Provides operations to manage the calendar property of the microsoft.graph.event entity.
        """
        from .calendar import calendar_request_builder

        return calendar_request_builder.CalendarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cancel(self) -> cancel_request_builder.CancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        from .cancel import cancel_request_builder

        return cancel_request_builder.CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def decline(self) -> decline_request_builder.DeclineRequestBuilder:
        """
        Provides operations to call the decline method.
        """
        from .decline import decline_request_builder

        return decline_request_builder.DeclineRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dismiss_reminder(self) -> dismiss_reminder_request_builder.DismissReminderRequestBuilder:
        """
        Provides operations to call the dismissReminder method.
        """
        from .dismiss_reminder import dismiss_reminder_request_builder

        return dismiss_reminder_request_builder.DismissReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.event entity.
        """
        from .extensions import extensions_request_builder

        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forward(self) -> forward_request_builder.ForwardRequestBuilder:
        """
        Provides operations to call the forward method.
        """
        from .forward import forward_request_builder

        return forward_request_builder.ForwardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def snooze_reminder(self) -> snooze_reminder_request_builder.SnoozeReminderRequestBuilder:
        """
        Provides operations to call the snoozeReminder method.
        """
        from .snooze_reminder import snooze_reminder_request_builder

        return snooze_reminder_request_builder.SnoozeReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tentatively_accept(self) -> tentatively_accept_request_builder.TentativelyAcceptRequestBuilder:
        """
        Provides operations to call the tentativelyAccept method.
        """
        from .tentatively_accept import tentatively_accept_request_builder

        return tentatively_accept_request_builder.TentativelyAcceptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EventItemRequestBuilderGetQueryParameters():
        """
        The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions that have been modified, but does not include occurrences that have been cancelled from the series. Navigation property. Read-only. Nullable.
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
            if original_name == "select":
                return "%24select"
            if original_name == "end_date_time":
                return "endDateTime"
            if original_name == "start_date_time":
                return "startDateTime"
            return original_name
        
        # The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
        end_date_time: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
        start_date_time: Optional[str] = None

    
    @dataclass
    class EventItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EventItemRequestBuilder.EventItemRequestBuilderGetQueryParameters] = None

    

