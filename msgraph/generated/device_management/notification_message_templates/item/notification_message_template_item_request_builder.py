from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.notification_message_template import NotificationMessageTemplate
    from ....models.o_data_errors.o_data_error import ODataError
    from .localized_notification_messages.localized_notification_messages_request_builder import LocalizedNotificationMessagesRequestBuilder
    from .send_test_message.send_test_message_request_builder import SendTestMessageRequestBuilder

class NotificationMessageTemplateItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the notificationMessageTemplates property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new NotificationMessageTemplateItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/notificationMessageTemplates/{notificationMessageTemplate%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Deletes a notificationMessageTemplate.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/intune-notification-notificationmessagetemplate-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[NotificationMessageTemplateItemRequestBuilderGetQueryParameters]] = None) -> Optional[NotificationMessageTemplate]:
        """
        Read properties and relationships of the notificationMessageTemplate object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NotificationMessageTemplate]
        Find more info here: https://learn.microsoft.com/graph/api/intune-notification-notificationmessagetemplate-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.notification_message_template import NotificationMessageTemplate

        return await self.request_adapter.send_async(request_info, NotificationMessageTemplate, error_mapping)
    
    async def patch(self,body: NotificationMessageTemplate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NotificationMessageTemplate]:
        """
        Update the properties of a notificationMessageTemplate object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NotificationMessageTemplate]
        Find more info here: https://learn.microsoft.com/graph/api/intune-notification-notificationmessagetemplate-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.notification_message_template import NotificationMessageTemplate

        return await self.request_adapter.send_async(request_info, NotificationMessageTemplate, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a notificationMessageTemplate.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[NotificationMessageTemplateItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read properties and relationships of the notificationMessageTemplate object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: NotificationMessageTemplate, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of a notificationMessageTemplate object.
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
    
    def with_url(self,raw_url: str) -> NotificationMessageTemplateItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NotificationMessageTemplateItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NotificationMessageTemplateItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def localized_notification_messages(self) -> LocalizedNotificationMessagesRequestBuilder:
        """
        Provides operations to manage the localizedNotificationMessages property of the microsoft.graph.notificationMessageTemplate entity.
        """
        from .localized_notification_messages.localized_notification_messages_request_builder import LocalizedNotificationMessagesRequestBuilder

        return LocalizedNotificationMessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_test_message(self) -> SendTestMessageRequestBuilder:
        """
        Provides operations to call the sendTestMessage method.
        """
        from .send_test_message.send_test_message_request_builder import SendTestMessageRequestBuilder

        return SendTestMessageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class NotificationMessageTemplateItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class NotificationMessageTemplateItemRequestBuilderGetQueryParameters():
        """
        Read properties and relationships of the notificationMessageTemplate object.
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class NotificationMessageTemplateItemRequestBuilderGetRequestConfiguration(RequestConfiguration[NotificationMessageTemplateItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class NotificationMessageTemplateItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

