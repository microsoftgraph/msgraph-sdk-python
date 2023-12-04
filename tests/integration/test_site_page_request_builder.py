import asyncio
import unittest
from os import getenv

from assertpy import assert_that
from azure.identity.aio import ClientSecretCredential
from httpx import AsyncClient
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph_core import GraphClientFactory

from msgraph import GraphServiceClient, GraphRequestAdapter
from msgraph.generated.models.page import Page
from msgraph.generated.models.site import Site
from msgraph.generated.models.site_pages_collection_response import SitePagesCollectionResponse

TENANT_ID = getenv("TENANT_ID")
CLIENT_ID = getenv("CLIENT_ID")
CLIENT_SECRET = getenv("CLIENT_SECRET")

credentials = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
)
scopes = ["https://graph.microsoft.com/.default"]
# TODO: If you're behind a proxy, you need to specify it twice for the client as well as the auth provider!
http_client = GraphClientFactory.create_with_default_middleware(client=AsyncClient(proxies=None))
auth_provider = AzureIdentityAuthenticationProvider(credentials=credentials, scopes=scopes, options={"proxies": None})
request_adapter = GraphRequestAdapter(auth_provider=auth_provider, client=http_client)
client = GraphServiceClient(request_adapter=request_adapter)
site_id = "0473718f-69cf-44a3-bfe8-8f280bc48c5e"


class SitePageRequestBuilderIntegrationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._loop = asyncio.get_event_loop()

    @classmethod
    def tearDownClass(cls):
        cls._loop.close()

    def test_get_site_pages(self):
        actual = self._loop.run_until_complete(client.sites.by_site_id(site_id).pages.get())

        assert_that(actual).is_type_of(SitePagesCollectionResponse)
        assert_that(actual.value).is_length(6)

    def test_get_site_by_id(self):
        actual = self._loop.run_until_complete(client.sites.by_site_id(site_id).get())

        assert_that(actual).is_type_of(Site)
        assert_that(actual.odata_type).is_equal_to("#microsoft.graph.site")
        assert_that(actual.id).contains(site_id)
        assert_that(actual.display_name).is_equal_to("Give @ Contoso")
        assert_that(actual.name).is_equal_to("wgive")
        assert_that(actual.web_url).is_equal_to("https://850v1v.sharepoint.com/sites/wgive")

    def test_get_site_page_by_id(self):
        page_id = "b37ac897-12de-4c26-ae49-d5eed75abb16"

        actual = self._loop.run_until_complete(client.sites.by_site_id(site_id).by_page_id(page_id).get())

        assert_that(actual).is_type_of(Page)
        assert_that(actual.odata_type).is_equal_to("#microsoft.graph.sitePage")
        assert_that(actual.id).is_equal_to("b37ac897-12de-4c26-ae49-d5eed75abb16")
        assert_that(actual.title).is_equal_to("A Task Force for Change")
        assert_that(actual.name).is_equal_to("A-Task-Force-for-Change.aspx")
        assert_that(actual.web_url).is_equal_to("SitePages/A-Task-Force-for-Change.aspx")
