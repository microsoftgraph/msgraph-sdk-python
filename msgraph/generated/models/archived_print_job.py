from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .print_job_processing_state import PrintJobProcessingState
    from .user_identity import UserIdentity

@dataclass
class ArchivedPrintJob(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # True if the job was acquired by a printer; false otherwise. Read-only.
    acquired_by_printer: Optional[bool] = None
    # The dateTimeOffset when the job was acquired by the printer, if any. Read-only.
    acquired_date_time: Optional[datetime.datetime] = None
    # The dateTimeOffset when the job was completed, canceled or aborted. Read-only.
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ArchivedPrintJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ArchivedPrintJob
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ArchivedPrintJob()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .print_job_processing_state import PrintJobProcessingState
        from .user_identity import UserIdentity

        from .print_job_processing_state import PrintJobProcessingState
        from .user_identity import UserIdentity

        fields: Dict[str, Callable[[Any], None]] = {
            "acquired_by_printer": lambda n : setattr(self, 'acquired_by_printer', n.get_bool_value()),
            "acquired_date_time": lambda n : setattr(self, 'acquired_date_time', n.get_datetime_value()),
            "completion_date_time": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "copies_printed": lambda n : setattr(self, 'copies_printed', n.get_int_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(UserIdentity)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "printer_id": lambda n : setattr(self, 'printer_id', n.get_str_value()),
            "printer_name": lambda n : setattr(self, 'printer_name', n.get_str_value()),
            "processing_state": lambda n : setattr(self, 'processing_state', n.get_enum_value(PrintJobProcessingState)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("acquired_by_printer", self.acquired_by_printer)
        writer.write_datetime_value("acquired_date_time", self.acquired_date_time)
        writer.write_datetime_value("completion_date_time", self.completion_date_time)
        writer.write_int_value("copies_printed", self.copies_printed)
        writer.write_object_value("created_by", self.created_by)
        writer.write_datetime_value("created_date_time", self.created_date_time)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("printer_id", self.printer_id)
        writer.write_str_value("printer_name", self.printer_name)
        writer.write_enum_value("processing_state", self.processing_state)
        writer.write_additional_data_value(self.additional_data)
    

