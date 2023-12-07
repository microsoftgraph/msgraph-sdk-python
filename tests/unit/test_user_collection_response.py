import json
from os.path import join, dirname

from assertpy import assert_that
from kiota_abstractions.request_adapter import RequestAdapter
from mockito import mock, when, ANY

from generated.models.base_collection_pagination_response import BaseCollectionPaginationResponse
from msgraph.generated.models.user_collection_response import UserCollectionResponse
from tests.base import BaseTestCase


class UserCollectionResponseTestCase(BaseTestCase):
    @staticmethod
    def load_json(location: str):
        with open(join(dirname(__file__), location)) as file:
            return json.load(file)

    @classmethod
    def mock_users_collection(cls, resource) -> UserCollectionResponse:
        value = cls.load_json(resource)
        users = UserCollectionResponse()
        users.value = value.get("value")
        users.odata_next_link = value.get("@odata.nextLink")
        return users

    @classmethod
    async def mock_next_users(cls, resource):
        return cls.mock_users_collection(resource)

    @staticmethod
    async def next_users(users):
        return await users.__anext__()

    def test_iteration_when_odata_next_link_is_not_none(self):
        request_adapter = mock(spec=RequestAdapter)
        when(request_adapter).send_async(
            request_info=ANY,
            parsable_factory=ANY,
            error_map=ANY,
        ).thenReturn(self.mock_next_users("resources/next_users.json"))
        BaseCollectionPaginationResponse.request_adapter = request_adapter
        users = self.mock_users_collection("resources/users.json")

        assert_that(users).is_length(10)
        assert_that(users.value).does_not_contain({
            "@odata.id": "https://graph.microsoft.com/v2/c34aa217-8e78-4c5f-91a7-29e01e0d97d8/directoryObjects/6794f45f-949e-4e8b-b01c-03d777e1cbf8/Microsoft.DirectoryServices.User",
            "displayName": "David Blain",
            "mailNickname": "dabla",
        })

        self._loop.run_until_complete(self.next_users(users))

        assert_that(users).is_length(8)
        assert_that(users.value).contains({
            "@odata.id": "https://graph.microsoft.com/v2/c34aa217-8e78-4c5f-91a7-29e01e0d97d8/directoryObjects/6794f45f-949e-4e8b-b01c-03d777e1cbf8/Microsoft.DirectoryServices.User",
            "displayName": "David Blain",
            "mailNickname": "dabla",
        })

        self._loop.run_until_complete(self.next_users(users))

        assert_that(users.value).is_none()

        with self.assertRaises(StopAsyncIteration):
            self._loop.run_until_complete(self.next_users(users))
