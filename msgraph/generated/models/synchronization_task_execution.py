from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .synchronization_error import SynchronizationError
    from .synchronization_task_execution_result import SynchronizationTaskExecutionResult

@dataclass
class SynchronizationTaskExecution(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The activityIdentifier property
    activity_identifier: Optional[str] = None
    # The countEntitled property
    count_entitled: Optional[int] = None
    # The countEntitledForProvisioning property
    count_entitled_for_provisioning: Optional[int] = None
    # The countEscrowed property
    count_escrowed: Optional[int] = None
    # The countEscrowedRaw property
    count_escrowed_raw: Optional[int] = None
    # The countExported property
    count_exported: Optional[int] = None
    # The countExports property
    count_exports: Optional[int] = None
    # The countImported property
    count_imported: Optional[int] = None
    # The countImportedDeltas property
    count_imported_deltas: Optional[int] = None
    # The countImportedReferenceDeltas property
    count_imported_reference_deltas: Optional[int] = None
    # The error property
    error: Optional[SynchronizationError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[SynchronizationTaskExecutionResult] = None
    # The timeBegan property
    time_began: Optional[datetime.datetime] = None
    # The timeEnded property
    time_ended: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationTaskExecution:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationTaskExecution
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationTaskExecution()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .synchronization_error import SynchronizationError
        from .synchronization_task_execution_result import SynchronizationTaskExecutionResult

        from .synchronization_error import SynchronizationError
        from .synchronization_task_execution_result import SynchronizationTaskExecutionResult

        fields: Dict[str, Callable[[Any], None]] = {
            "activityIdentifier": lambda n : setattr(self, 'activity_identifier', n.get_str_value()),
            "countEntitled": lambda n : setattr(self, 'count_entitled', n.get_int_value()),
            "countEntitledForProvisioning": lambda n : setattr(self, 'count_entitled_for_provisioning', n.get_int_value()),
            "countEscrowed": lambda n : setattr(self, 'count_escrowed', n.get_int_value()),
            "countEscrowedRaw": lambda n : setattr(self, 'count_escrowed_raw', n.get_int_value()),
            "countExported": lambda n : setattr(self, 'count_exported', n.get_int_value()),
            "countExports": lambda n : setattr(self, 'count_exports', n.get_int_value()),
            "countImported": lambda n : setattr(self, 'count_imported', n.get_int_value()),
            "countImportedDeltas": lambda n : setattr(self, 'count_imported_deltas', n.get_int_value()),
            "countImportedReferenceDeltas": lambda n : setattr(self, 'count_imported_reference_deltas', n.get_int_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(SynchronizationError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(SynchronizationTaskExecutionResult)),
            "timeBegan": lambda n : setattr(self, 'time_began', n.get_datetime_value()),
            "timeEnded": lambda n : setattr(self, 'time_ended', n.get_datetime_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("activityIdentifier", self.activity_identifier)
        writer.write_int_value("countEntitled", self.count_entitled)
        writer.write_int_value("countEntitledForProvisioning", self.count_entitled_for_provisioning)
        writer.write_int_value("countEscrowed", self.count_escrowed)
        writer.write_int_value("countEscrowedRaw", self.count_escrowed_raw)
        writer.write_int_value("countExported", self.count_exported)
        writer.write_int_value("countExports", self.count_exports)
        writer.write_int_value("countImported", self.count_imported)
        writer.write_int_value("countImportedDeltas", self.count_imported_deltas)
        writer.write_int_value("countImportedReferenceDeltas", self.count_imported_reference_deltas)
        writer.write_object_value("error", self.error)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_datetime_value()("timeBegan", self.time_began)
        writer.write_datetime_value()("timeEnded", self.time_ended)
        writer.write_additional_data_value(self.additional_data)
    

