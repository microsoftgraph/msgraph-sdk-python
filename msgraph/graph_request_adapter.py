from typing import Dict, Optional
import httpx
from kiota_abstractions.authentication import AuthenticationProvider
from msgraph_core import BaseGraphRequestAdapter, GraphClientFactory


class GraphRequestAdapter(BaseGraphRequestAdapter):
    def __init__(self, auth_provider: AuthenticationProvider, client: Optional[httpx.AsyncClient] = GraphClientFactory.create_with_default_middleware()) -> None:
        super().__init__(auth_provider, http_client=client)

