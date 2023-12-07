from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TypeVar

from generated.models.base_collection_pagination_response import BaseCollectionPaginationResponse
from generated.models.entity import Entity

T = TypeVar("T", bound=Entity)


@dataclass
class BaseDeltaFunctionResponse(BaseCollectionPaginationResponse[T]):
    odata_delta_link: Optional[str] = None
