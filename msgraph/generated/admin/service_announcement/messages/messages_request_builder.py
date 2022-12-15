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

archive_request_builder = lazy_import('msgraph.generated.admin.service_announcement.messages.archive.archive_request_builder')
count_request_builder = lazy_import('msgraph.generated.admin.service_announcement.messages.count.count_request_builder')
favorite_request_builder = lazy_import('msgraph.generated.admin.service_announcement.messages.favorite.favorite_request_builder')
mark_read_request_builder = lazy_import('msgraph.generated.admin.service_announcement.messages.mark_read.mark_read_request_builder')
mark_unread_request_builder = lazy_import('msgraph.generated.admin.service_announcement.messages.mark_unread.mark_unread_request_builder')
unarchive_request_builder = lazy_import('msgraph.generated.admin.service_announcement.messages.unarchive.unarchive_request_builder')
unfavorite_request_builder = lazy_import('msgraph.generated.admin.service_announcement.messages.unfavorite.unfavorite_request_builder')
service_update_message = lazy_import('msgraph.generated.models.service_update_message')
service_update_message_collection_response = lazy_import('msgraph.generated.models.service_update_message_collection_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class MessagesRequestBuilder():
    """
    Provides operations to manage the messages property of the microsoft.graph.serviceAnnouncement entity.
    """
    @property
    def archive(self) -> archive_request_builder.ArchiveRequestBuilder:
        """
        Provides operations to call the archive method.
        """
        return archive_request_builder.ArchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def favorite(self) -> favorite_request_builder.FavoriteRequestBuilder:
        """
        Provides operations to call the favorite method.
        """
        return favorite_request_builder.FavoriteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mark_read(self) -> mark_read_request_builder.MarkReadRequestBuilder:
        """
        Provides operations to call the markRead method.
        """
        return mark_read_request_builder.MarkReadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mark_unread(self) -> mark_unread_request_builder.MarkUnreadRequestBuilder:
        """
        Provides operations to call the markUnread method.
        """
        return mark_unread_request_builder.MarkUnreadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unarchive(self) -> unarchive_request_builder.UnarchiveRequestBuilder:
        """
        Provides operations to call the unarchive method.
        """
        return unarchive_request_builder.UnarchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unfavorite(self) -> unfavorite_request_builder.UnfavoriteRequestBuilder:
        """
        Provides operations to call the unfavorite method.
        """
        return unfavorite_request_builder.UnfavoriteRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MessagesRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/admin/serviceAnnouncement/messages{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[MessagesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the serviceUpdateMessage resources from the **messages** navigation property. This operation retrieves all service update messages that exist for the tenant.
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
    
    def create_post_request_information(self,body: Optional[service_update_message.ServiceUpdateMessage] = None, request_configuration: Optional[MessagesRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to messages for admin
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
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def get(self,request_configuration: Optional[MessagesRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[service_update_message_collection_response.ServiceUpdateMessageCollectionResponse]:
        """
        Retrieve the serviceUpdateMessage resources from the **messages** navigation property. This operation retrieves all service update messages that exist for the tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[service_update_message_collection_response.ServiceUpdateMessageCollectionResponse]
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
        return await self.request_adapter.send_async(request_info, service_update_message_collection_response.ServiceUpdateMessageCollectionResponse, response_handler, error_mapping)
    
    async def post(self,body: Optional[service_update_message.ServiceUpdateMessage] = None, request_configuration: Optional[MessagesRequestBuilderPostRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[service_update_message.ServiceUpdateMessage]:
        """
        Create new navigation property to messages for admin
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[service_update_message.ServiceUpdateMessage]
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
        return await self.request_adapter.send_async(request_info, service_update_message.ServiceUpdateMessage, response_handler, error_mapping)
    
    @dataclass
    class MessagesRequestBuilderGetQueryParameters():
        """
        Retrieve the serviceUpdateMessage resources from the **messages** navigation property. This operation retrieves all service update messages that exist for the tenant.
        """
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

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
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
    
    @dataclass
    class MessagesRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class MessagesRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

