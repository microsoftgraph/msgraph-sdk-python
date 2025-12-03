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
    from .....models.chat import Chat
    from .....models.o_data_errors.o_data_error import ODataError
    from .hide_for_user.hide_for_user_request_builder import HideForUserRequestBuilder
    from .installed_apps.installed_apps_request_builder import InstalledAppsRequestBuilder
    from .last_message_preview.last_message_preview_request_builder import LastMessagePreviewRequestBuilder
    from .mark_chat_read_for_user.mark_chat_read_for_user_request_builder import MarkChatReadForUserRequestBuilder
    from .mark_chat_unread_for_user.mark_chat_unread_for_user_request_builder import MarkChatUnreadForUserRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .messages.messages_request_builder import MessagesRequestBuilder
    from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder
    from .pinned_messages.pinned_messages_request_builder import PinnedMessagesRequestBuilder
    from .remove_all_access_for_user.remove_all_access_for_user_request_builder import RemoveAllAccessForUserRequestBuilder
    from .send_activity_notification.send_activity_notification_request_builder import SendActivityNotificationRequestBuilder
    from .tabs.tabs_request_builder import TabsRequestBuilder
    from .unhide_for_user.unhide_for_user_request_builder import UnhideForUserRequestBuilder

class ChatItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the chats property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ChatItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/chats/{chat%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property chats for users
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ChatItemRequestBuilderGetQueryParameters]] = None) -> Optional[Chat]:
        """
        Retrieve a single chat (without its messages). This method supports federation. To access a chat, at least one chat member must belong to the tenant the request initiated from.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Chat]
        Find more info here: https://learn.microsoft.com/graph/api/chat-get?view=graph-rest-1.0
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
        from .....models.chat import Chat

        return await self.request_adapter.send_async(request_info, Chat, error_mapping)
    
    async def patch(self,body: Chat, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Chat]:
        """
        Update the navigation property chats in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Chat]
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
        from .....models.chat import Chat

        return await self.request_adapter.send_async(request_info, Chat, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property chats for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ChatItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve a single chat (without its messages). This method supports federation. To access a chat, at least one chat member must belong to the tenant the request initiated from.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Chat, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property chats in users
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
    
    def with_url(self,raw_url: str) -> ChatItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ChatItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ChatItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def hide_for_user(self) -> HideForUserRequestBuilder:
        """
        Provides operations to call the hideForUser method.
        """
        from .hide_for_user.hide_for_user_request_builder import HideForUserRequestBuilder

        return HideForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def installed_apps(self) -> InstalledAppsRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.chat entity.
        """
        from .installed_apps.installed_apps_request_builder import InstalledAppsRequestBuilder

        return InstalledAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_message_preview(self) -> LastMessagePreviewRequestBuilder:
        """
        Provides operations to manage the lastMessagePreview property of the microsoft.graph.chat entity.
        """
        from .last_message_preview.last_message_preview_request_builder import LastMessagePreviewRequestBuilder

        return LastMessagePreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mark_chat_read_for_user(self) -> MarkChatReadForUserRequestBuilder:
        """
        Provides operations to call the markChatReadForUser method.
        """
        from .mark_chat_read_for_user.mark_chat_read_for_user_request_builder import MarkChatReadForUserRequestBuilder

        return MarkChatReadForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mark_chat_unread_for_user(self) -> MarkChatUnreadForUserRequestBuilder:
        """
        Provides operations to call the markChatUnreadForUser method.
        """
        from .mark_chat_unread_for_user.mark_chat_unread_for_user_request_builder import MarkChatUnreadForUserRequestBuilder

        return MarkChatUnreadForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.chat entity.
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.chat entity.
        """
        from .messages.messages_request_builder import MessagesRequestBuilder

        return MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.chat entity.
        """
        from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder

        return PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pinned_messages(self) -> PinnedMessagesRequestBuilder:
        """
        Provides operations to manage the pinnedMessages property of the microsoft.graph.chat entity.
        """
        from .pinned_messages.pinned_messages_request_builder import PinnedMessagesRequestBuilder

        return PinnedMessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_all_access_for_user(self) -> RemoveAllAccessForUserRequestBuilder:
        """
        Provides operations to call the removeAllAccessForUser method.
        """
        from .remove_all_access_for_user.remove_all_access_for_user_request_builder import RemoveAllAccessForUserRequestBuilder

        return RemoveAllAccessForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_activity_notification(self) -> SendActivityNotificationRequestBuilder:
        """
        Provides operations to call the sendActivityNotification method.
        """
        from .send_activity_notification.send_activity_notification_request_builder import SendActivityNotificationRequestBuilder

        return SendActivityNotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tabs(self) -> TabsRequestBuilder:
        """
        Provides operations to manage the tabs property of the microsoft.graph.chat entity.
        """
        from .tabs.tabs_request_builder import TabsRequestBuilder

        return TabsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unhide_for_user(self) -> UnhideForUserRequestBuilder:
        """
        Provides operations to call the unhideForUser method.
        """
        from .unhide_for_user.unhide_for_user_request_builder import UnhideForUserRequestBuilder

        return UnhideForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ChatItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ChatItemRequestBuilderGetQueryParameters():
        """
        Retrieve a single chat (without its messages). This method supports federation. To access a chat, at least one chat member must belong to the tenant the request initiated from.
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
    class ChatItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ChatItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ChatItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

