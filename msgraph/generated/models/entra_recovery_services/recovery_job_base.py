from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .recovery_job import RecoveryJob
    from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase
    from .recovery_preview_job import RecoveryPreviewJob
    from .recovery_status import RecoveryStatus

from ..entity import Entity

@dataclass
class RecoveryJobBase(Entity, Parsable):
    # Optional filtering criteria used to scope the job to specific entity types or entity IDs.
    filtering_criteria: Optional[RecoveryJobFilteringCriteriaBase] = None
    # The date and time when the job completed. Null if the job is still running.
    job_completion_date_time: Optional[datetime.datetime] = None
    # The date and time when the job started.
    job_start_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[RecoveryStatus] = None
    # The target snapshot timestamp to which the tenant is being restored. Supports $filter (eq, ne).
    target_state_date_time: Optional[datetime.datetime] = None
    # The total count of changed directory object links (relationships) calculated by the job. null until the job completes calculation. Not all calculated link changes may be successfully applied; see totalLinksModified on derived types for the count of links that were actually modified.
    total_changed_links_calculated: Optional[int] = None
    # The total count of changed directory objects calculated by the job. null until the job completes calculation. Not all calculated object changes may be successfully applied; see totalObjectsModified on derived types for the count of objects that were actually modified.
    total_changed_objects_calculated: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecoveryJobBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecoveryJobBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.entraRecoveryServices.recoveryJob".casefold():
            from .recovery_job import RecoveryJob

            return RecoveryJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.entraRecoveryServices.recoveryPreviewJob".casefold():
            from .recovery_preview_job import RecoveryPreviewJob

            return RecoveryPreviewJob()
        return RecoveryJobBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .recovery_job import RecoveryJob
        from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase
        from .recovery_preview_job import RecoveryPreviewJob
        from .recovery_status import RecoveryStatus

        from ..entity import Entity
        from .recovery_job import RecoveryJob
        from .recovery_job_filtering_criteria_base import RecoveryJobFilteringCriteriaBase
        from .recovery_preview_job import RecoveryPreviewJob
        from .recovery_status import RecoveryStatus

        fields: dict[str, Callable[[Any], None]] = {
            "filteringCriteria": lambda n : setattr(self, 'filtering_criteria', n.get_object_value(RecoveryJobFilteringCriteriaBase)),
            "jobCompletionDateTime": lambda n : setattr(self, 'job_completion_date_time', n.get_datetime_value()),
            "jobStartDateTime": lambda n : setattr(self, 'job_start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(RecoveryStatus)),
            "targetStateDateTime": lambda n : setattr(self, 'target_state_date_time', n.get_datetime_value()),
            "totalChangedLinksCalculated": lambda n : setattr(self, 'total_changed_links_calculated', n.get_int_value()),
            "totalChangedObjectsCalculated": lambda n : setattr(self, 'total_changed_objects_calculated', n.get_int_value()),
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
        writer.write_object_value("filteringCriteria", self.filtering_criteria)
        writer.write_datetime_value("jobCompletionDateTime", self.job_completion_date_time)
        writer.write_datetime_value("jobStartDateTime", self.job_start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("targetStateDateTime", self.target_state_date_time)
        writer.write_int_value("totalChangedLinksCalculated", self.total_changed_links_calculated)
        writer.write_int_value("totalChangedObjectsCalculated", self.total_changed_objects_calculated)
    

