from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .count.count_request_builder import CountRequestBuilder
    from .graph_room.graph_room_request_builder import GraphRoomRequestBuilder
    from .item.place_item_request_builder import PlaceItemRequestBuilder

class PlacesRequestBuilder():
    """
    Builds and executes requests for operations under /places
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PlacesRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/places"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def by_place_id(self,place_id: str) -> PlaceItemRequestBuilder:
        """
        Provides operations to manage the collection of place entities.
        Args:
            place_id: Unique identifier of the item
        Returns: PlaceItemRequestBuilder
        """
        if not place_id:
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
    

