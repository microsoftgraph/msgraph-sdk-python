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
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.place import Place
    from .count.count_request_builder import CountRequestBuilder
    from .graph_building.graph_building_request_builder import GraphBuildingRequestBuilder
    from .graph_desk.graph_desk_request_builder import GraphDeskRequestBuilder
    from .graph_floor.graph_floor_request_builder import GraphFloorRequestBuilder
    from .graph_room.graph_room_request_builder import GraphRoomRequestBuilder
    from .graph_room_list.graph_room_list_request_builder import GraphRoomListRequestBuilder
    from .graph_section.graph_section_request_builder import GraphSectionRequestBuilder
    from .graph_workspace.graph_workspace_request_builder import GraphWorkspaceRequestBuilder
    from .item.place_item_request_builder import PlaceItemRequestBuilder

class PlacesRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of place entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlacesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/places", path_parameters)
    
    def by_place_id(self,place_id: str) -> PlaceItemRequestBuilder:
        """
        Provides operations to manage the collection of place entities.
        param place_id: The unique identifier of place
        Returns: PlaceItemRequestBuilder
        """
        if place_id is None:
            raise TypeError("place_id cannot be null.")
        from .item.place_item_request_builder import PlaceItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["place%2Did"] = place_id
        return PlaceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: Place, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Place]:
        """
        Create a new place object. You can also use this method to create the following child object types: building, floor, section, room, workspace, or desk.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Place]
        Find more info here: https://learn.microsoft.com/graph/api/place-post?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.place import Place

        return await self.request_adapter.send_async(request_info, Place, error_mapping)
    
    def to_post_request_information(self,body: Place, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a new place object. You can also use this method to create the following child object types: building, floor, section, room, workspace, or desk.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> PlacesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlacesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlacesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_building(self) -> GraphBuildingRequestBuilder:
        """
        Casts the previous resource to building.
        """
        from .graph_building.graph_building_request_builder import GraphBuildingRequestBuilder

        return GraphBuildingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_desk(self) -> GraphDeskRequestBuilder:
        """
        Casts the previous resource to desk.
        """
        from .graph_desk.graph_desk_request_builder import GraphDeskRequestBuilder

        return GraphDeskRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_floor(self) -> GraphFloorRequestBuilder:
        """
        Casts the previous resource to floor.
        """
        from .graph_floor.graph_floor_request_builder import GraphFloorRequestBuilder

        return GraphFloorRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    
    @property
    def graph_section(self) -> GraphSectionRequestBuilder:
        """
        Casts the previous resource to section.
        """
        from .graph_section.graph_section_request_builder import GraphSectionRequestBuilder

        return GraphSectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_workspace(self) -> GraphWorkspaceRequestBuilder:
        """
        Casts the previous resource to workspace.
        """
        from .graph_workspace.graph_workspace_request_builder import GraphWorkspaceRequestBuilder

        return GraphWorkspaceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PlacesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

