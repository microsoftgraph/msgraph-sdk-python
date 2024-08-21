from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .count.count_request_builder import CountRequestBuilder
    from .graph_room.graph_room_request_builder import GraphRoomRequestBuilder
    from .graph_room_list.graph_room_list_request_builder import GraphRoomListRequestBuilder
    from .item.place_item_request_builder import PlaceItemRequestBuilder

class PlacesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /places
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
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
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    

