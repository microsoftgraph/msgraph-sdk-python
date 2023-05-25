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
        credentials: Union[TokenCredential, AsyncTokenCredential],
        scopes: Optional[List[str]],
        base_url: Optional[str] = None,
        client: Optional[AsyncClient] = None
    ) -> None:
        """Constructs a client instance to use for making requests to the 
        Microsoft Graph v.1.0 API.

        Args:
            credentials (Union[TokenCredential, AsyncTokenCredential]): The
            tokenCredential to use for authentication. 
            scopes (Optional[List[str]]): The scopes to use for authentication.
            Defaults to ['https://graph.microsoft.com/.default'].
            base_url (Optional[str], optional): The base url to use for
            requests. Defaults to https://graph.microsoft.com/v1.0.
            client (Optional[AsyncClient], optional): A custom httpx.AsyncClient
            to use for http requests. Defaults to None.
        """
        
        if scopes:
            auth_provider = AzureIdentityAuthenticationProvider(credentials, scopes)
        else:
            auth_provider = AzureIdentityAuthenticationProvider(credentials)
        
        if client:
            request_adapter = GraphRequestAdapter(auth_provider, client)
        else:
            request_adapter = GraphRequestAdapter(auth_provider)
        
        if base_url:
            request_adapter.base_url = base_url
        
        
        super().__init__(request_adapter)