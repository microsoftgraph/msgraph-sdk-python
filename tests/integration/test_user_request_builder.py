from assertpy import assert_that

from tests.integration.base import BaseIntegrationTestCase


class UserRequestBuilderIntegrationTestCase(BaseIntegrationTestCase):

    def test_get_users_delta(self):
        actual = self._loop.run_until_complete(self.get_users_delta())

        assert_that(actual).is_not_none()

    async def get_users_delta(self):
        result = []
        users = await self.client.users.delta.get()
        async for u in users:
            result.extend(u)

        return result