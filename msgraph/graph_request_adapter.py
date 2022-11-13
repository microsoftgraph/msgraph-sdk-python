from kiota_abstractions.authentication import AuthenticationProvider
from msgraph.core import BaseGraphRequestAdapter


class GraphRequestAdapter(BaseGraphRequestAdapter):
    def __init__(self, auth_provider: AuthenticationProvider) -> None:
        super().__init__(auth_provider)

