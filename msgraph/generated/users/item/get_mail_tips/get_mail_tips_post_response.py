from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from ....models.base_collection_pagination_count_response import (
    BaseCollectionPaginationCountResponse,
)
from ....models.mail_tips import MailTips


@dataclass
class GetMailTipsPostResponse(BaseCollectionPaginationCountResponse[MailTips]):
    value: Optional[List[MailTips]] = None

    def __init__(self):
        super().__init__(entity=MailTips)
