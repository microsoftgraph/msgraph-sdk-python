from .generated import BaseGraphClient
from .graph_request_adapter import BaseGraphRequestAdapter

class GraphServiceClient(BaseGraphClient):
    def __init__(self, request_adapter: BaseGraphRequestAdapter) -> None:
        super().init(request_adapter)