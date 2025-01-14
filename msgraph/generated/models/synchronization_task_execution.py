from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .synchronization_error import SynchronizationError
    from .synchronization_task_execution_result import SynchronizationTaskExecutionResult

@dataclass
class SynchronizationTaskExecution(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Identifier of the job run.
    activity_identifier: Optional[str] = None
    # Count of processed entries that were assigned for this application.
    count_entitled: Optional[int] = None
    # Count of processed entries that were assigned for provisioning.
    count_entitled_for_provisioning: Optional[int] = None
    # Count of entries that were escrowed (errors).
    count_escrowed: Optional[int] = None
    # Count of entries that were escrowed, including system-generated escrows.
    count_escrowed_raw: Optional[int] = None
    # Count of exported entries.
    count_exported: Optional[int] = None
    # Count of entries that were expected to be exported.
    count_exports: Optional[int] = None
    # Count of imported entries.
    count_imported: Optional[int] = None
    # Count of imported delta-changes.
    count_imported_deltas: Optional[int] = None
    # Count of imported delta-changes pertaining to reference changes.
    count_imported_reference_deltas: Optional[int] = None
    # If an error was encountered, contains a synchronizationError object with details.
    error: Optional[SynchronizationError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[SynchronizationTaskExecutionResult] = None
    # Time when this job run began. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    time_began: Optional[datetime.datetime] = None
    # Time when this job run ended. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    time_ended: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationTaskExecution:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationTaskExecution
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationTaskExecution()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .synchronization_error import SynchronizationError
        from .synchronization_task_execution_result import SynchronizationTaskExecutionResult

        from .synchronization_error import SynchronizationError
        from .synchronization_task_execution_result import SynchronizationTaskExecutionResult

        fields: dict[str, Callable[[Any], None]] = {
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
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
        writer.write_datetime_value("timeBegan", self.time_began)
        writer.write_datetime_value("timeEnded", self.time_ended)
        writer.write_additional_data_value(self.additional_data)
    

