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

allowed_calendar_sharing_roles_with_user_request_builder = lazy_import('msgraph.generated.groups.item.calendar.allowed_calendar_sharing_roles_with_user.allowed_calendar_sharing_roles_with_user_request_builder')
calendar_permissions_request_builder = lazy_import('msgraph.generated.groups.item.calendar.calendar_permissions.calendar_permissions_request_builder')
calendar_permission_item_request_builder = lazy_import('msgraph.generated.groups.item.calendar.calendar_permissions.item.calendar_permission_item_request_builder')
calendar_view_request_builder = lazy_import('msgraph.generated.groups.item.calendar.calendar_view.calendar_view_request_builder')
event_item_request_builder = lazy_import('msgraph.generated.groups.item.calendar.calendar_view.item.event_item_request_builder')
events_request_builder = lazy_import('msgraph.generated.groups.item.calendar.events.events_request_builder')
event_item_request_builder = lazy_import('msgraph.generated.groups.item.calendar.events.item.event_item_request_builder')
get_schedule_request_builder = lazy_import('msgraph.generated.groups.item.calendar.get_schedule.get_schedule_request_builder')
multi_value_extended_properties_request_builder = lazy_import('msgraph.generated.groups.item.calendar.multi_value_extended_properties.multi_value_extended_properties_request_builder')
multi_value_legacy_extended_property_item_request_builder = lazy_import('msgraph.generated.groups.item.calendar.multi_value_extended_properties.item.multi_value_legacy_extended_property_item_request_builder')
single_value_extended_properties_request_builder = lazy_import('msgraph.generated.groups.item.calendar.single_value_extended_properties.single_value_extended_properties_request_builder')
single_value_legacy_extended_property_item_request_builder = lazy_import('msgraph.generated.groups.item.calendar.single_value_extended_properties.item.single_value_legacy_extended_property_item_request_builder')
calendar = lazy_import('msgraph.generated.models.calendar')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class CalendarRequestBuilder():
    """
    Provides operations to manage the calendar property of the microsoft.graph.group entity.
    """
    @property
    def calendar_permissions(self) -> calendar_permissions_request_builder.CalendarPermissionsRequestBuilder:
        """
        Provides operations to manage the calendarPermissions property of the microsoft.graph.calendar entity.
        """
        return calendar_permissions_request_builder.CalendarPermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_view(self) -> calendar_view_request_builder.CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.calendar entity.
        """
        return calendar_view_request_builder.CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> events_request_builder.EventsRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.calendar entity.
        """
        return events_request_builder.EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_schedule(self) -> get_schedule_request_builder.GetScheduleRequestBuilder:
        """
        Provides operations to call the getSchedule method.
        """
        return get_schedule_request_builder.GetScheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def multi_value_extended_properties(self) -> multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.calendar entity.
        """
        return multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def single_value_extended_properties(self) -> single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.calendar entity.
        """
        return single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def allowed_calendar_sharing_roles_with_user(self,user: Optional[str] = None) -> allowed_calendar_sharing_roles_with_user_request_builder.AllowedCalendarSharingRolesWithUserRequestBuilder:
        """
        Provides operations to call the allowedCalendarSharingRoles method.
        Args:
            User: Usage: User='{User}'
        Returns: allowed_calendar_sharing_roles_with_user_request_builder.AllowedCalendarSharingRolesWithUserRequestBuilder
        """
        if user is None:
            raise Exception("user cannot be undefined")
        return allowed_calendar_sharing_roles_with_user_request_builder.AllowedCalendarSharingRolesWithUserRequestBuilder(self.request_adapter, self.path_parameters, User)
    
    def calendar_permissions_by_id(self,id: str) -> calendar_permission_item_request_builder.CalendarPermissionItemRequestBuilder:
        """
        Provides operations to manage the calendarPermissions property of the microsoft.graph.calendar entity.
        Args:
            id: Unique identifier of the item
        Returns: calendar_permission_item_request_builder.CalendarPermissionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["calendarPermission%2Did"] = id
        return calendar_permission_item_request_builder.CalendarPermissionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def calendar_view_by_id(self,id: str) -> event_item_request_builder.EventItemRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.calendar entity.
        Args:
            id: Unique identifier of the item
        Returns: event_item_request_builder.EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did"] = id
        return event_item_request_builder.EventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CalendarRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/calendar{?%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[CalendarRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The group's calendar. Read-only.
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
    
    def events_by_id(self,id: str) -> event_item_request_builder.EventItemRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.calendar entity.
        Args:
            id: Unique identifier of the item
        Returns: event_item_request_builder.EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did"] = id
        return event_item_request_builder.EventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[CalendarRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[calendar.Calendar]:
        """
        The group's calendar. Read-only.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[calendar.Calendar]
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
        return await self.request_adapter.send_async(request_info, calendar.Calendar, response_handler, error_mapping)
    
    def multi_value_extended_properties_by_id(self,id: str) -> multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.calendar entity.
        Args:
            id: Unique identifier of the item
        Returns: multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["multiValueLegacyExtendedProperty%2Did"] = id
        return multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def single_value_extended_properties_by_id(self,id: str) -> single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.calendar entity.
        Args:
            id: Unique identifier of the item
        Returns: single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["singleValueLegacyExtendedProperty%2Did"] = id
        return single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class CalendarRequestBuilderGetQueryParameters():
        """
        The group's calendar. Read-only.
        """
        # Select properties to be returned
        select: Optional[List[str]] = None

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
            return original_name
        
    
    @dataclass
    class CalendarRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[CalendarRequestBuilder.CalendarRequestBuilderGetQueryParameters] = None

    

