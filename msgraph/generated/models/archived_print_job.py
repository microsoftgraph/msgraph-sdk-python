from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .print_job_processing_state import PrintJobProcessingState
    from .user_identity import UserIdentity

@dataclass
class ArchivedPrintJob(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # True if the job was acquired by a printer; false otherwise. Read-only.
    acquired_by_printer: Optional[bool] = None
    # The dateTimeOffset when the job was acquired by the printer, if any. Read-only.
    acquired_date_time: Optional[datetime.datetime] = None
    # The dateTimeOffset when the job was completed, canceled, or aborted. Read-only.
    completion_date_time: Optional[datetime.datetime] = None
    # The number of copies that were printed. Read-only.
    copies_printed: Optional[int] = None
    # The user who created the print job. Read-only.
    created_by: Optional[UserIdentity] = None
    # The dateTimeOffset when the job was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The archived print job's GUID. Read-only.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The printer ID that the job was queued for. Read-only.
    printer_id: Optional[str] = None
    # The printer name that the job was queued for. Read-only.
    printer_name: Optional[str] = None
    # The processingState property
    processing_state: Optional[PrintJobProcessingState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ArchivedPrintJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ArchivedPrintJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ArchivedPrintJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .print_job_processing_state import PrintJobProcessingState
        from .user_identity import UserIdentity

        from .print_job_processing_state import PrintJobProcessingState
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "acquiredByPrinter": lambda n : setattr(self, 'acquired_by_printer', n.get_bool_value()),
            "acquiredDateTime": lambda n : setattr(self, 'acquired_date_time', n.get_datetime_value()),
            "completionDateTime": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "copiesPrinted": lambda n : setattr(self, 'copies_printed', n.get_int_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(UserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "printerId": lambda n : setattr(self, 'printer_id', n.get_str_value()),
            "printerName": lambda n : setattr(self, 'printer_name', n.get_str_value()),
            "processingState": lambda n : setattr(self, 'processing_state', n.get_enum_value(PrintJobProcessingState)),
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
        writer.write_bool_value("acquiredByPrinter", self.acquired_by_printer)
        writer.write_datetime_value("acquiredDateTime", self.acquired_date_time)
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_int_value("copiesPrinted", self.copies_printed)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("printerId", self.printer_id)
        writer.write_str_value("printerName", self.printer_name)
        writer.write_enum_value("processingState", self.processing_state)
        writer.write_additional_data_value(self.additional_data)
    

