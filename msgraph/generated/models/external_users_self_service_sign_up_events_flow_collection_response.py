from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
    from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse

@dataclass
class ExternalUsersSelfServiceSignUpEventsFlowCollectionResponse(BaseCollectionPaginationCountResponse, Parsable):
    # The value property
    value: Optional[List[ExternalUsersSelfServiceSignUpEventsFlow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalUsersSelfServiceSignUpEventsFlowCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalUsersSelfServiceSignUpEventsFlowCollectionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalUsersSelfServiceSignUpEventsFlowCollectionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

        from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(ExternalUsersSelfServiceSignUpEventsFlow)),
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
        from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

        writer.write_collection_of_object_values("value", self.value)
    

