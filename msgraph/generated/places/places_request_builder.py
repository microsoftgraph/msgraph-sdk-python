from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .count import count_request_builder
    from .graph_room import graph_room_request_builder
    from .item import place_item_request_builder

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
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/places"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def by_place_id(self,place_id: str) -> place_item_request_builder.PlaceItemRequestBuilder:
        """
        Provides operations to manage the collection of place entities.
        Args:
            place_id: Unique identifier of the item
        Returns: place_item_request_builder.PlaceItemRequestBuilder
        """
        if place_id is None:
            raise Exception("place_id cannot be undefined")
        from .item import place_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["place%2Did"] = place_id
        return place_item_request_builder.PlaceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count import count_request_builder

        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_room(self) -> graph_room_request_builder.GraphRoomRequestBuilder:
        """
        Casts the previous resource to room.
        """
        from .graph_room import graph_room_request_builder

        return graph_room_request_builder.GraphRoomRequestBuilder(self.request_adapter, self.path_parameters)
    

