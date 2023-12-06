import asyncio
from os import getenv
from unittest import TestCase

from azure.identity.aio import ClientSecretCredential
from httpx import AsyncClient, Timeout
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph_core import GraphClientFactory

from msgraph import GraphServiceClient, GraphRequestAdapter

TENANT_ID = getenv("TENANT_ID")
CLIENT_ID = getenv("CLIENT_ID")
CLIENT_SECRET = getenv("CLIENT_SECRET")

credentials = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
)
scopes = ["https://graph.microsoft.com/.default"]


class BaseIntegrationTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        # TODO: If you're behind a proxy, you need to specify it twice for the client as well as the auth provider!
        http_client = GraphClientFactory.create_with_default_middleware(client=AsyncClient(proxies=None, timeout=Timeout(timeout=60.0)))
        auth_provider = AzureIdentityAuthenticationProvider(credentials=credentials, scopes=scopes,options={"proxies": None})
        request_adapter = GraphRequestAdapter(auth_provider=auth_provider, client=http_client)
        cls.client = GraphServiceClient(request_adapter=request_adapter)
        cls._loop = asyncio.get_event_loop()

    @classmethod
    def tearDownClass(cls):
        cls._loop.close()
