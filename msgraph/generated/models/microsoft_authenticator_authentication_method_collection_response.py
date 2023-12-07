from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
from .microsoft_authenticator_authentication_method import (
    MicrosoftAuthenticatorAuthenticationMethod,
)


@dataclass
class MicrosoftAuthenticatorAuthenticationMethodCollectionResponse(
    BaseCollectionPaginationCountResponse[MicrosoftAuthenticatorAuthenticationMethod]
):
    value: Optional[List[MicrosoftAuthenticatorAuthenticationMethod]] = None

    def __init__(self):
        super().__init__(entity=MicrosoftAuthenticatorAuthenticationMethod)
