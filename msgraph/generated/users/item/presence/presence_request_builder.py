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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.presence import Presence
    from .clear_presence.clear_presence_request_builder import ClearPresenceRequestBuilder
    from .clear_user_preferred_presence.clear_user_preferred_presence_request_builder import ClearUserPreferredPresenceRequestBuilder
    from .set_presence.set_presence_request_builder import SetPresenceRequestBuilder
    from .set_status_message.set_status_message_request_builder import SetStatusMessageRequestBuilder
    from .set_user_preferred_presence.set_user_preferred_presence_request_builder import SetUserPreferredPresenceRequestBuilder

class PresenceRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the presence property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PresenceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/presence{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[PresenceRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property presence for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[PresenceRequestBuilderGetRequestConfiguration] = None) -> Optional[Presence]:
        """
        Get a user's presence information.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Presence]
        Find more info here: https://learn.microsoft.com/graph/api/presence-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.presence import Presence

        return await self.request_adapter.send_async(request_info, Presence, error_mapping)
    
    async def patch(self,body: Optional[Presence] = None, request_configuration: Optional[PresenceRequestBuilderPatchRequestConfiguration] = None) -> Optional[Presence]:
        """
        Update the navigation property presence in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Presence]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.presence import Presence

        return await self.request_adapter.send_async(request_info, Presence, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PresenceRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property presence for users
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
    
    def to_get_request_information(self,request_configuration: Optional[PresenceRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get a user's presence information.
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
    
    def to_patch_request_information(self,body: Optional[Presence] = None, request_configuration: Optional[PresenceRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property presence in users
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
    
    def with_url(self,raw_url: Optional[str] = None) -> PresenceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PresenceRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PresenceRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def clear_presence(self) -> ClearPresenceRequestBuilder:
        """
        Provides operations to call the clearPresence method.
        """
        from .clear_presence.clear_presence_request_builder import ClearPresenceRequestBuilder

        return ClearPresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clear_user_preferred_presence(self) -> ClearUserPreferredPresenceRequestBuilder:
        """
        Provides operations to call the clearUserPreferredPresence method.
        """
        from .clear_user_preferred_presence.clear_user_preferred_presence_request_builder import ClearUserPreferredPresenceRequestBuilder

        return ClearUserPreferredPresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_presence(self) -> SetPresenceRequestBuilder:
        """
        Provides operations to call the setPresence method.
        """
        from .set_presence.set_presence_request_builder import SetPresenceRequestBuilder

        return SetPresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_status_message(self) -> SetStatusMessageRequestBuilder:
        """
        Provides operations to call the setStatusMessage method.
        """
        from .set_status_message.set_status_message_request_builder import SetStatusMessageRequestBuilder

        return SetStatusMessageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set_user_preferred_presence(self) -> SetUserPreferredPresenceRequestBuilder:
        """
        Provides operations to call the setUserPreferredPresence method.
        """
        from .set_user_preferred_presence.set_user_preferred_presence_request_builder import SetUserPreferredPresenceRequestBuilder

        return SetUserPreferredPresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PresenceRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class PresenceRequestBuilderGetQueryParameters():
        """
        Get a user's presence information.
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
    class PresenceRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[PresenceRequestBuilder.PresenceRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PresenceRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

