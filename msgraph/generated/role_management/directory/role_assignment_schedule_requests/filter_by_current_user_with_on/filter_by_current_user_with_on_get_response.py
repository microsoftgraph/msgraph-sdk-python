from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
    from .....models.unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest

from .....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse

@dataclass
class FilterByCurrentUserWithOnGetResponse(BaseCollectionPaginationCountResponse, Parsable):
    # The value property
    value: Optional[List[UnifiedRoleAssignmentScheduleRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilterByCurrentUserWithOnGetResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterByCurrentUserWithOnGetResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilterByCurrentUserWithOnGetResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .....models.unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest

        from .....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .....models.unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(UnifiedRoleAssignmentScheduleRequest)),
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
        from .....models.base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .....models.unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest

        writer.write_collection_of_object_values("value", self.value)
    

