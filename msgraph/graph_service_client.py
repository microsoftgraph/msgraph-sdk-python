# ------------------------------------
# Copyright (c) Microsoft Corporation. All Rights Reserved.
# Licensed under the MIT License.
# See License in the project root for license information.
# -----------------------------------

from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING, Union
from azure.core.credentials import TokenCredential
from azure.core.credentials_async import AsyncTokenCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider

from .generated.base_graph_service_client import BaseGraphServiceClient
from .graph_request_adapter import GraphRequestAdapter

if TYPE_CHECKING:
    from .generated.users.item.user_item_request_builder import UserItemRequestBuilder
    from msgraph_core.requests.batch_request_builder import BatchRequestBuilder


class GraphServiceClient(BaseGraphServiceClient):

    def __init__(
        self,
        credentials: Optional[Union[TokenCredential, AsyncTokenCredential]] = None,
        scopes: Optional[List[str]] = None,
        request_adapter: Optional[GraphRequestAdapter] = None,
    ) -> None:
        """Constructs a client instance to use for making requests to the 
        Microsoft Graph v.1.0 API.

        Args:
            credentials (Union[TokenCredential, AsyncTokenCredential]): The
            tokenCredential to use for authentication. 
            scopes (Optional[List[str]]): The scopes to use for authentication.
            Defaults to ['https://graph.microsoft.com/.default'].
            request_adapter (Optional[GraphRequestAdapter], optional): The request
            adapter to use for requests. Defaults to None.
        """

        if not request_adapter:
            if not credentials:
                raise ValueError("Missing request adapter or valid credentials")

            if scopes:
                auth_provider = AzureIdentityAuthenticationProvider(credentials, scopes=scopes)
            else:
                auth_provider = AzureIdentityAuthenticationProvider(credentials)

            request_adapter = GraphRequestAdapter(auth_provider)

        super().__init__(request_adapter)

    @property
    def me(self) -> UserItemRequestBuilder:
        """
        Maps requests to /me endpoint to /users/{{user-id}}
        """
        from .generated.users.item.user_item_request_builder import UserItemRequestBuilder

        url_tpl_parameters = self.path_parameters
        url_tpl_parameters["user%2Did"] = "me-token-to-replace"

        return UserItemRequestBuilder(self.request_adapter, url_tpl_parameters)

    @property
    def batch(self) -> BatchRequestBuilder:
        """
        Returns a BatchRequestBuilder to enable batch requests.
        """
        from msgraph_core.requests.batch_request_builder import BatchRequestBuilder

        return BatchRequestBuilder(self.request_adapter)
