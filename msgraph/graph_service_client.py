from .generated.base_graph_service_client import BaseGraphServiceClient
from .graph_request_adapter import GraphRequestAdapter

class GraphServiceClient(BaseGraphServiceClient):
    def __init__(self, request_adapter: GraphRequestAdapter) -> None:
        super().__init__(request_adapter)