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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.place import Place
    from .graph_room.graph_room_request_builder import GraphRoomRequestBuilder
    from .graph_room_list.graph_room_list_request_builder import GraphRoomListRequestBuilder

class PlaceItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of place entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PlaceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/places/{place%2Did}", path_parameters)
    
    async def delete(self,request_configuration: Optional[PlaceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete entity from places
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def patch(self,body: Optional[Place] = None, request_configuration: Optional[PlaceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[Place]:
        """
        Update the properties of place object, which can be a room or roomList. You can identify the room or roomList by specifying the id or emailAddress property.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Place]
        Find more info here: https://learn.microsoft.com/graph/api/place-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.place import Place

        return await self.request_adapter.send_async(request_info, Place, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PlaceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from places
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
    
    def to_patch_request_information(self,body: Optional[Place] = None, request_configuration: Optional[PlaceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of place object, which can be a room or roomList. You can identify the room or roomList by specifying the id or emailAddress property.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> PlaceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlaceItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PlaceItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def graph_room(self) -> GraphRoomRequestBuilder:
        """
        Casts the previous resource to room.
        """
        from .graph_room.graph_room_request_builder import GraphRoomRequestBuilder

        return GraphRoomRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_room_list(self) -> GraphRoomListRequestBuilder:
        """
        Casts the previous resource to roomList.
        """
        from .graph_room_list.graph_room_list_request_builder import GraphRoomListRequestBuilder

        return GraphRoomListRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PlaceItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PlaceItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

