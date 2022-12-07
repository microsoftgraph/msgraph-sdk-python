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

hide_for_user_request_builder = lazy_import('msgraph.generated.chats.item.hide_for_user.hide_for_user_request_builder')
installed_apps_request_builder = lazy_import('msgraph.generated.chats.item.installed_apps.installed_apps_request_builder')
teams_app_installation_item_request_builder = lazy_import('msgraph.generated.chats.item.installed_apps.item.teams_app_installation_item_request_builder')
last_message_preview_request_builder = lazy_import('msgraph.generated.chats.item.last_message_preview.last_message_preview_request_builder')
mark_chat_read_for_user_request_builder = lazy_import('msgraph.generated.chats.item.mark_chat_read_for_user.mark_chat_read_for_user_request_builder')
mark_chat_unread_for_user_request_builder = lazy_import('msgraph.generated.chats.item.mark_chat_unread_for_user.mark_chat_unread_for_user_request_builder')
members_request_builder = lazy_import('msgraph.generated.chats.item.members.members_request_builder')
conversation_member_item_request_builder = lazy_import('msgraph.generated.chats.item.members.item.conversation_member_item_request_builder')
messages_request_builder = lazy_import('msgraph.generated.chats.item.messages.messages_request_builder')
chat_message_item_request_builder = lazy_import('msgraph.generated.chats.item.messages.item.chat_message_item_request_builder')
pinned_messages_request_builder = lazy_import('msgraph.generated.chats.item.pinned_messages.pinned_messages_request_builder')
pinned_chat_message_info_item_request_builder = lazy_import('msgraph.generated.chats.item.pinned_messages.item.pinned_chat_message_info_item_request_builder')
send_activity_notification_request_builder = lazy_import('msgraph.generated.chats.item.send_activity_notification.send_activity_notification_request_builder')
tabs_request_builder = lazy_import('msgraph.generated.chats.item.tabs.tabs_request_builder')
teams_tab_item_request_builder = lazy_import('msgraph.generated.chats.item.tabs.item.teams_tab_item_request_builder')
unhide_for_user_request_builder = lazy_import('msgraph.generated.chats.item.unhide_for_user.unhide_for_user_request_builder')
chat = lazy_import('msgraph.generated.models.chat')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ChatItemRequestBuilder():
    """
    Provides operations to manage the collection of chat entities.
    """
    def hide_for_user(self) -> hide_for_user_request_builder.HideForUserRequestBuilder:
        """
        Provides operations to call the hideForUser method.
        """
        return hide_for_user_request_builder.HideForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    def installed_apps(self) -> installed_apps_request_builder.InstalledAppsRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.chat entity.
        """
        return installed_apps_request_builder.InstalledAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def last_message_preview(self) -> last_message_preview_request_builder.LastMessagePreviewRequestBuilder:
        """
        Provides operations to manage the lastMessagePreview property of the microsoft.graph.chat entity.
        """
        return last_message_preview_request_builder.LastMessagePreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    def mark_chat_read_for_user(self) -> mark_chat_read_for_user_request_builder.MarkChatReadForUserRequestBuilder:
        """
        Provides operations to call the markChatReadForUser method.
        """
        return mark_chat_read_for_user_request_builder.MarkChatReadForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    def mark_chat_unread_for_user(self) -> mark_chat_unread_for_user_request_builder.MarkChatUnreadForUserRequestBuilder:
        """
        Provides operations to call the markChatUnreadForUser method.
        """
        return mark_chat_unread_for_user_request_builder.MarkChatUnreadForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.chat entity.
        """
        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def messages(self) -> messages_request_builder.MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.chat entity.
        """
        return messages_request_builder.MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def pinned_messages(self) -> pinned_messages_request_builder.PinnedMessagesRequestBuilder:
        """
        Provides operations to manage the pinnedMessages property of the microsoft.graph.chat entity.
        """
        return pinned_messages_request_builder.PinnedMessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def send_activity_notification(self) -> send_activity_notification_request_builder.SendActivityNotificationRequestBuilder:
        """
        Provides operations to call the sendActivityNotification method.
        """
        return send_activity_notification_request_builder.SendActivityNotificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    def tabs(self) -> tabs_request_builder.TabsRequestBuilder:
        """
        Provides operations to manage the tabs property of the microsoft.graph.chat entity.
        """
        return tabs_request_builder.TabsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def unhide_for_user(self) -> unhide_for_user_request_builder.UnhideForUserRequestBuilder:
        """
        Provides operations to call the unhideForUser method.
        """
        return unhide_for_user_request_builder.UnhideForUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ChatItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/chats/{chat%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ChatItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from chats
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
    
    def create_get_request_information(self,request_configuration: Optional[ChatItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a single chat (without its messages). This method supports federation. To access a chat, at least one chat member must belong to the tenant the request initiated from.
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
    
    def create_patch_request_information(self,body: Optional[chat.Chat] = None, request_configuration: Optional[ChatItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a chat object.
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
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[ChatItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete entity from chats
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[ChatItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[chat.Chat]:
        """
        Retrieve a single chat (without its messages). This method supports federation. To access a chat, at least one chat member must belong to the tenant the request initiated from.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[chat.Chat]
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
        return await self.request_adapter.send_async(request_info, chat.Chat, response_handler, error_mapping)
    
    def installed_apps_by_id(self,id: str) -> teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder:
        """
        Provides operations to manage the installedApps property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsAppInstallation%2Did"] = id
        return teams_app_installation_item_request_builder.TeamsAppInstallationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def members_by_id(self,id: str) -> conversation_member_item_request_builder.ConversationMemberItemRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: conversation_member_item_request_builder.ConversationMemberItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conversationMember%2Did"] = id
        return conversation_member_item_request_builder.ConversationMemberItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def messages_by_id(self,id: str) -> chat_message_item_request_builder.ChatMessageItemRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: chat_message_item_request_builder.ChatMessageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["chatMessage%2Did"] = id
        return chat_message_item_request_builder.ChatMessageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[chat.Chat] = None, request_configuration: Optional[ChatItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[chat.Chat]:
        """
        Update the properties of a chat object.
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[chat.Chat]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, chat.Chat, response_handler, error_mapping)
    
    def pinned_messages_by_id(self,id: str) -> pinned_chat_message_info_item_request_builder.PinnedChatMessageInfoItemRequestBuilder:
        """
        Provides operations to manage the pinnedMessages property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: pinned_chat_message_info_item_request_builder.PinnedChatMessageInfoItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["pinnedChatMessageInfo%2Did"] = id
        return pinned_chat_message_info_item_request_builder.PinnedChatMessageInfoItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tabs_by_id(self,id: str) -> teams_tab_item_request_builder.TeamsTabItemRequestBuilder:
        """
        Provides operations to manage the tabs property of the microsoft.graph.chat entity.
        Args:
            id: Unique identifier of the item
        Returns: teams_tab_item_request_builder.TeamsTabItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["teamsTab%2Did"] = id
        return teams_tab_item_request_builder.TeamsTabItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class ChatItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ChatItemRequestBuilderGetQueryParameters():
        """
        Retrieve a single chat (without its messages). This method supports federation. To access a chat, at least one chat member must belong to the tenant the request initiated from.
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
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class ChatItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ChatItemRequestBuilder.ChatItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ChatItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

