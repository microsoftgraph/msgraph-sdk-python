from assertpy import assert_that

from msgraph.generated.models.page import Page
from msgraph.generated.models.site import Site
from msgraph.generated.models.site_pages_collection_response import SitePagesCollectionResponse
from tests.integration.base import BaseIntegrationTestCase

site_id = "0473718f-69cf-44a3-bfe8-8f280bc48c5e"


class SitePageRequestBuilderIntegrationTestCase(BaseIntegrationTestCase):

    def test_get_site_pages(self):
        actual = self._loop.run_until_complete(self.client.sites.by_site_id(site_id).pages.get())

        assert_that(actual).is_type_of(SitePagesCollectionResponse)
        assert_that(actual.value).is_length(6)

    def test_get_site_by_id(self):
        actual = self._loop.run_until_complete(self.client.sites.by_site_id(site_id).get())

        assert_that(actual).is_type_of(Site)
        assert_that(actual.odata_type).is_equal_to("#microsoft.graph.site")
        assert_that(actual.id).contains(site_id)
        assert_that(actual.display_name).is_equal_to("Give @ Contoso")
        assert_that(actual.name).is_equal_to("wgive")
        assert_that(actual.web_url).is_equal_to("https://850v1v.sharepoint.com/sites/wgive")

    def test_get_site_page_by_id(self):
        page_id = "b37ac897-12de-4c26-ae49-d5eed75abb16"

        actual = self._loop.run_until_complete(self.client.sites.by_site_id(site_id).by_page_id(page_id).get())

        assert_that(actual).is_type_of(Page)
        assert_that(actual.odata_type).is_equal_to("#microsoft.graph.sitePage")
        assert_that(actual.id).is_equal_to("b37ac897-12de-4c26-ae49-d5eed75abb16")
        assert_that(actual.title).is_equal_to("A Task Force for Change")
        assert_that(actual.name).is_equal_to("A-Task-Force-for-Change.aspx")
        assert_that(actual.web_url).is_equal_to("SitePages/A-Task-Force-for-Change.aspx")
