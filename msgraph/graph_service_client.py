from typing import List, Optional, TYPE_CHECKING, Union'
from azure.core.credentials import TokenCredential
from azure.core.credentials_async import AsyncTokenCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from httpx import AsyncClient

from .generated.base_graph_service_client import BaseGraphServiceClient
from .graph_request_adapter import GraphRequestAdapter

class GraphServiceClient(BaseGraphServiceClient):
    def __init__(
        self,
        credentials: Optional[Union[TokenCredential, AsyncTokenCredential]] = None,
        scopes: Optional[List[str]] = None,
        request_adapter: Optional[GraphRequestAdapter] = None
        
    ) -> None:
        """Constructs a client instance to use for making requests to the 
        Microsoft Graph v.1.0 API.

        Args:
            credentials (Union[TokenCredential, AsyncTokenCredential]): The
            tokenCredential to use for authentication. 
            scopes (Optional[List[str]]): The scopes to use for authentication.
            Defaults to ['https://graph.microsoft.com/.default'].
            request_adapter (Optional[GraphRequestAdapter], optional): The
            request adapter to use for requests. Defaults to None.
        """
        
        if not request_adapter:
            if not credentials:
                raise ValueError("Missing request adapter or valid credentials")
            
            if scopes:
                auth_provider = AzureIdentityAuthenticationProvider(credentials, scopes)
            else:
                auth_provider = AzureIdentityAuthenticationProvider(credentials)
    
            request_adapter = GraphRequestAdapter(auth_provider)
        
        super().__init__(request_adapter)