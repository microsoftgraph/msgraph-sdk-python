from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase
    from .resource_type_name import ResourceTypeName

from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase

@dataclass
class RecoveryJobEntityNamesFilter(RecoveryJobFilteringCriteriaBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.entraRecoveryServices.recoveryJobEntityNamesFilter"
    # The list of entity types to include in the recovery job.
    entity_types: Optional[list[ResourceTypeName]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecoveryJobEntityNamesFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecoveryJobEntityNamesFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecoveryJobEntityNamesFilter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase
        from .resource_type_name import ResourceTypeName

        from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase
        from .resource_type_name import ResourceTypeName

        fields: dict[str, Callable[[Any], None]] = {
            "entityTypes": lambda n : setattr(self, 'entity_types', n.get_collection_of_enum_values(ResourceTypeName)),
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
        writer.write_collection_of_enum_values("entityTypes", self.entity_types)
    

