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

attachments_request_builder = lazy_import('msgraph.generated.me.events.item.attachments.attachments_request_builder')
attachment_item_request_builder = lazy_import('msgraph.generated.me.events.item.attachments.item.attachment_item_request_builder')
calendar_request_builder = lazy_import('msgraph.generated.me.events.item.calendar.calendar_request_builder')
extensions_request_builder = lazy_import('msgraph.generated.me.events.item.extensions.extensions_request_builder')
extension_item_request_builder = lazy_import('msgraph.generated.me.events.item.extensions.item.extension_item_request_builder')
instances_request_builder = lazy_import('msgraph.generated.me.events.item.instances.instances_request_builder')
event_item_request_builder = lazy_import('msgraph.generated.me.events.item.instances.item.event_item_request_builder')
microsoft_graph_accept_request_builder = lazy_import('msgraph.generated.me.events.item.microsoft_graph_accept.microsoft_graph_accept_request_builder')
microsoft_graph_cancel_request_builder = lazy_import('msgraph.generated.me.events.item.microsoft_graph_cancel.microsoft_graph_cancel_request_builder')
microsoft_graph_decline_request_builder = lazy_import('msgraph.generated.me.events.item.microsoft_graph_decline.microsoft_graph_decline_request_builder')
microsoft_graph_dismiss_reminder_request_builder = lazy_import('msgraph.generated.me.events.item.microsoft_graph_dismiss_reminder.microsoft_graph_dismiss_reminder_request_builder')
microsoft_graph_forward_request_builder = lazy_import('msgraph.generated.me.events.item.microsoft_graph_forward.microsoft_graph_forward_request_builder')
microsoft_graph_snooze_reminder_request_builder = lazy_import('msgraph.generated.me.events.item.microsoft_graph_snooze_reminder.microsoft_graph_snooze_reminder_request_builder')
microsoft_graph_tentatively_accept_request_builder = lazy_import('msgraph.generated.me.events.item.microsoft_graph_tentatively_accept.microsoft_graph_tentatively_accept_request_builder')
multi_value_extended_properties_request_builder = lazy_import('msgraph.generated.me.events.item.multi_value_extended_properties.multi_value_extended_properties_request_builder')
multi_value_legacy_extended_property_item_request_builder = lazy_import('msgraph.generated.me.events.item.multi_value_extended_properties.item.multi_value_legacy_extended_property_item_request_builder')
single_value_extended_properties_request_builder = lazy_import('msgraph.generated.me.events.item.single_value_extended_properties.single_value_extended_properties_request_builder')
single_value_legacy_extended_property_item_request_builder = lazy_import('msgraph.generated.me.events.item.single_value_extended_properties.item.single_value_legacy_extended_property_item_request_builder')
event = lazy_import('msgraph.generated.models.event')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class EventItemRequestBuilder():
    """
    Provides operations to manage the events property of the microsoft.graph.user entity.
    """
    @property
    def attachments(self) -> attachments_request_builder.AttachmentsRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.event entity.
        """
        return attachments_request_builder.AttachmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar(self) -> calendar_request_builder.CalendarRequestBuilder:
        """
        Provides operations to manage the calendar property of the microsoft.graph.event entity.
        """
        return calendar_request_builder.CalendarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.event entity.
        """
        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def instances(self) -> instances_request_builder.InstancesRequestBuilder:
        """
        Provides operations to manage the instances property of the microsoft.graph.event entity.
        """
        return instances_request_builder.InstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_accept(self) -> microsoft_graph_accept_request_builder.MicrosoftGraphAcceptRequestBuilder:
        """
        Provides operations to call the accept method.
        """
        return microsoft_graph_accept_request_builder.MicrosoftGraphAcceptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_cancel(self) -> microsoft_graph_cancel_request_builder.MicrosoftGraphCancelRequestBuilder:
        """
        Provides operations to call the cancel method.
        """
        return microsoft_graph_cancel_request_builder.MicrosoftGraphCancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_decline(self) -> microsoft_graph_decline_request_builder.MicrosoftGraphDeclineRequestBuilder:
        """
        Provides operations to call the decline method.
        """
        return microsoft_graph_decline_request_builder.MicrosoftGraphDeclineRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_dismiss_reminder(self) -> microsoft_graph_dismiss_reminder_request_builder.MicrosoftGraphDismissReminderRequestBuilder:
        """
        Provides operations to call the dismissReminder method.
        """
        return microsoft_graph_dismiss_reminder_request_builder.MicrosoftGraphDismissReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_forward(self) -> microsoft_graph_forward_request_builder.MicrosoftGraphForwardRequestBuilder:
        """
        Provides operations to call the forward method.
        """
        return microsoft_graph_forward_request_builder.MicrosoftGraphForwardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_snooze_reminder(self) -> microsoft_graph_snooze_reminder_request_builder.MicrosoftGraphSnoozeReminderRequestBuilder:
        """
        Provides operations to call the snoozeReminder method.
        """
        return microsoft_graph_snooze_reminder_request_builder.MicrosoftGraphSnoozeReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_tentatively_accept(self) -> microsoft_graph_tentatively_accept_request_builder.MicrosoftGraphTentativelyAcceptRequestBuilder:
        """
        Provides operations to call the tentativelyAccept method.
        """
        return microsoft_graph_tentatively_accept_request_builder.MicrosoftGraphTentativelyAcceptRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def multi_value_extended_properties(self) -> multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.event entity.
        """
        return multi_value_extended_properties_request_builder.MultiValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def single_value_extended_properties(self) -> single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.event entity.
        """
        return single_value_extended_properties_request_builder.SingleValueExtendedPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def attachments_by_id(self,id: str) -> attachment_item_request_builder.AttachmentItemRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: attachment_item_request_builder.AttachmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attachment%2Did"] = id
        return attachment_item_request_builder.AttachmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
        self.url_template: str = "{+baseurl}/me/events/{event%2Did}{?%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[EventItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property events for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def extensions_by_id(self,id: str) -> extension_item_request_builder.ExtensionItemRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: extension_item_request_builder.ExtensionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["extension%2Did"] = id
        return extension_item_request_builder.ExtensionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[EventItemRequestBuilderGetRequestConfiguration] = None) -> Optional[event.Event]:
        """
        The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[event.Event]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, event.Event, error_mapping)
    
    def instances_by_id(self,id: str) -> EventItemRequestBuilder:
        """
        Provides operations to manage the instances property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: EventItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did1"] = id
        return EventItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def multi_value_extended_properties_by_id(self,id: str) -> multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the multiValueExtendedProperties property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["multiValueLegacyExtendedProperty%2Did"] = id
        return multi_value_legacy_extended_property_item_request_builder.MultiValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[event.Event] = None, request_configuration: Optional[EventItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[event.Event]:
        """
        Update the navigation property events in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[event.Event]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, event.Event, error_mapping)
    
    def single_value_extended_properties_by_id(self,id: str) -> single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder:
        """
        Provides operations to manage the singleValueExtendedProperties property of the microsoft.graph.event entity.
        Args:
            id: Unique identifier of the item
        Returns: single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["singleValueLegacyExtendedProperty%2Did"] = id
        return single_value_legacy_extended_property_item_request_builder.SingleValueLegacyExtendedPropertyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[EventItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property events for me
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
    
    def to_get_request_information(self,request_configuration: Optional[EventItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[event.Event] = None, request_configuration: Optional[EventItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property events in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @dataclass
    class EventItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EventItemRequestBuilderGetQueryParameters():
        """
        The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.
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

    
    @dataclass
    class EventItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

