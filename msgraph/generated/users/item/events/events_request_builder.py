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

event = lazy_import('msgraph.generated.models.event')
event_collection_response = lazy_import('msgraph.generated.models.event_collection_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
count_request_builder = lazy_import('msgraph.generated.users.item.events.count.count_request_builder')
delta_request_builder = lazy_import('msgraph.generated.users.item.events.delta.delta_request_builder')

class EventsRequestBuilder():
    """
    Provides operations to manage the events property of the microsoft.graph.user entity.
    """
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EventsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/events{?%24top,%24skip,%24filter,%24count,%24orderby,%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[EventsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get a list of event objects in the user's mailbox. The list contains single instance meetings and series masters. To get expanded event instances, you can get the calendar view, or get the instances of an event. Currently, this operation returns event bodies in only HTML format. There are two scenarios where an app can get events in another user's calendar:
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
    
    def create_post_request_information(self,body: Optional[event.Event] = None, request_configuration: Optional[EventsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create an event in the user's default calendar or specified calendar. By default, the **allowNewTimeProposals** property is set to true when an event is created, which means invitees can propose a different date/time for the event. See Propose new meeting times for more information on how to propose a time, and how to receive and accept a new time proposal. You can specify the time zone for each of the start and end times of the event as part of their values, because the **start** and **end** properties are of dateTimeTimeZone type. First find the supported time zones to make sure you set only time zones that have been configured for the user's mailbox server.  When an event is sent, the server sends invitations to all the attendees. **Setting the location in an event** An Exchange administrator can set up a mailbox and an email address for a resource such as a meeting room, or equipment like a projector. Users can then invite the resource as an attendee to a meeting. On behalf of the resource, the server accepts or rejects the meeting request based on the free/busy schedule of the resource. If the server accepts a meeting for the resource, it creates an event for the meeting in the resource's calendar. If the meeting is rescheduled, the server automatically updates the event in the resource's calendar. Another advantage of setting up a mailbox for a resource is to control scheduling of the resource, for example, only executivesor their delegates can book a private meeting room. If you're organizing an event that involves a meeting location: Additionally, if the meeting location has been set up as a resource, or if the event involves some equipment that has been set up as a resource:
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def delta(self,) -> delta_request_builder.DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        Returns: delta_request_builder.DeltaRequestBuilder
        """
        return delta_request_builder.DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    async def get(self,request_configuration: Optional[EventsRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[event_collection_response.EventCollectionResponse]:
        """
        Get a list of event objects in the user's mailbox. The list contains single instance meetings and series masters. To get expanded event instances, you can get the calendar view, or get the instances of an event. Currently, this operation returns event bodies in only HTML format. There are two scenarios where an app can get events in another user's calendar:
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
    
    async def post(self,body: Optional[event.Event] = None, request_configuration: Optional[EventsRequestBuilderPostRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[event.Event]:
        """
        Create an event in the user's default calendar or specified calendar. By default, the **allowNewTimeProposals** property is set to true when an event is created, which means invitees can propose a different date/time for the event. See Propose new meeting times for more information on how to propose a time, and how to receive and accept a new time proposal. You can specify the time zone for each of the start and end times of the event as part of their values, because the **start** and **end** properties are of dateTimeTimeZone type. First find the supported time zones to make sure you set only time zones that have been configured for the user's mailbox server.  When an event is sent, the server sends invitations to all the attendees. **Setting the location in an event** An Exchange administrator can set up a mailbox and an email address for a resource such as a meeting room, or equipment like a projector. Users can then invite the resource as an attendee to a meeting. On behalf of the resource, the server accepts or rejects the meeting request based on the free/busy schedule of the resource. If the server accepts a meeting for the resource, it creates an event for the meeting in the resource's calendar. If the meeting is rescheduled, the server automatically updates the event in the resource's calendar. Another advantage of setting up a mailbox for a resource is to control scheduling of the resource, for example, only executivesor their delegates can book a private meeting room. If you're organizing an event that involves a meeting location: Additionally, if the meeting location has been set up as a resource, or if the event involves some equipment that has been set up as a resource:
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[event.Event]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_post_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, event.Event, response_handler, error_mapping)
    
    @dataclass
    class EventsRequestBuilderGetQueryParameters():
        """
        Get a list of event objects in the user's mailbox. The list contains single instance meetings and series masters. To get expanded event instances, you can get the calendar view, or get the instances of an event. Currently, this operation returns event bodies in only HTML format. There are two scenarios where an app can get events in another user's calendar:
        """
        # Include count of items
        count: Optional[bool] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

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
    class EventsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EventsRequestBuilder.EventsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EventsRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

