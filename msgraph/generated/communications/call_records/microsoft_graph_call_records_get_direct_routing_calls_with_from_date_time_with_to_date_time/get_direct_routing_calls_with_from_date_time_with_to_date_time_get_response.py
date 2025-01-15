from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
    from ....models.call_records.direct_routing_log_row import DirectRoutingLogRow

from ....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse

@dataclass
class GetDirectRoutingCallsWithFromDateTimeWithToDateTimeGetResponse(BaseCollectionPaginationCountResponse, Parsable):
    # The value property
    value: Optional[list[DirectRoutingLogRow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GetDirectRoutingCallsWithFromDateTimeWithToDateTimeGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GetDirectRoutingCallsWithFromDateTimeWithToDateTimeGetResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GetDirectRoutingCallsWithFromDateTimeWithToDateTimeGetResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from ....models.call_records.direct_routing_log_row import DirectRoutingLogRow

        from ....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from ....models.call_records.direct_routing_log_row import DirectRoutingLogRow

        fields: dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(DirectRoutingLogRow)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("value", self.value)
    

