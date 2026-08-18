from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity_type_and_ids import EntityTypeAndIds
    from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase

from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase

@dataclass
class RecoveryJobEntityNameAndIdsFilter(RecoveryJobFilteringCriteriaBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.entraRecoveryServices.recoveryJobEntityNameAndIdsFilter"
    # The list of entity type and ID pairs to include in the recovery job. Duplicate entity types are not allowed and return a 400 Bad Request error.
    filter_values: Optional[list[EntityTypeAndIds]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecoveryJobEntityNameAndIdsFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecoveryJobEntityNameAndIdsFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecoveryJobEntityNameAndIdsFilter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity_type_and_ids import EntityTypeAndIds
        from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase

        from .entity_type_and_ids import EntityTypeAndIds
        from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase

        fields: dict[str, Callable[[Any], None]] = {
            "filterValues": lambda n : setattr(self, 'filter_values', n.get_collection_of_object_values(EntityTypeAndIds)),
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
        writer.write_collection_of_object_values("filterValues", self.filter_values)
    

