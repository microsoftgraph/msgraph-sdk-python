from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

count_request_builder = lazy_import('msgraph.generated.places.count.count_request_builder')
graph_room_request_builder = lazy_import('msgraph.generated.places.graph_room.graph_room_request_builder')

class PlacesRequestBuilder():
    """
    Builds and executes requests for operations under /places
    """
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_room(self) -> graph_room_request_builder.GraphRoomRequestBuilder:
        """
        Casts the previous resource to room.
        """
        return graph_room_request_builder.GraphRoomRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    

