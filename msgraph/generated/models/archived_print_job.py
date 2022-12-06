from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

print_job_processing_state = lazy_import('msgraph.generated.models.print_job_processing_state')
user_identity = lazy_import('msgraph.generated.models.user_identity')

class ArchivedPrintJob(AdditionalDataHolder, Parsable):
    @property
    def acquired_by_printer(self,) -> Optional[bool]:
        """
        Gets the acquiredByPrinter property value. True if the job was acquired by a printer; false otherwise. Read-only.
        Returns: Optional[bool]
        """
        return self._acquired_by_printer
    
    @acquired_by_printer.setter
    def acquired_by_printer(self,value: Optional[bool] = None) -> None:
        """
        Sets the acquiredByPrinter property value. True if the job was acquired by a printer; false otherwise. Read-only.
        Args:
            value: Value to set for the acquiredByPrinter property.
        """
        self._acquired_by_printer = value
    
    @property
    def acquired_date_time(self,) -> Optional[datetime]:
        """
        Gets the acquiredDateTime property value. The dateTimeOffset when the job was acquired by the printer, if any. Read-only.
        Returns: Optional[datetime]
        """
        return self._acquired_date_time
    
    @acquired_date_time.setter
    def acquired_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the acquiredDateTime property value. The dateTimeOffset when the job was acquired by the printer, if any. Read-only.
        Args:
            value: Value to set for the acquiredDateTime property.
        """
        self._acquired_date_time = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def completion_date_time(self,) -> Optional[datetime]:
        """
        Gets the completionDateTime property value. The dateTimeOffset when the job was completed, canceled or aborted. Read-only.
        Returns: Optional[datetime]
        """
        return self._completion_date_time
    
    @completion_date_time.setter
    def completion_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completionDateTime property value. The dateTimeOffset when the job was completed, canceled or aborted. Read-only.
        Args:
            value: Value to set for the completionDateTime property.
        """
        self._completion_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new archivedPrintJob and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # True if the job was acquired by a printer; false otherwise. Read-only.
        self._acquired_by_printer: Optional[bool] = None
        # The dateTimeOffset when the job was acquired by the printer, if any. Read-only.
        self._acquired_date_time: Optional[datetime] = None
        # The dateTimeOffset when the job was completed, canceled or aborted. Read-only.
        self._completion_date_time: Optional[datetime] = None
        # The number of copies that were printed. Read-only.
        self._copies_printed: Optional[int] = None
        # The user who created the print job. Read-only.
        self._created_by: Optional[user_identity.UserIdentity] = None
        # The dateTimeOffset when the job was created. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The archived print job's GUID. Read-only.
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The printer ID that the job was queued for. Read-only.
        self._printer_id: Optional[str] = None
        # The processingState property
        self._processing_state: Optional[print_job_processing_state.PrintJobProcessingState] = None
    
    @property
    def copies_printed(self,) -> Optional[int]:
        """
        Gets the copiesPrinted property value. The number of copies that were printed. Read-only.
        Returns: Optional[int]
        """
        return self._copies_printed
    
    @copies_printed.setter
    def copies_printed(self,value: Optional[int] = None) -> None:
        """
        Sets the copiesPrinted property value. The number of copies that were printed. Read-only.
        Args:
            value: Value to set for the copiesPrinted property.
        """
        self._copies_printed = value
    
    @property
    def created_by(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the createdBy property value. The user who created the print job. Read-only.
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the createdBy property value. The user who created the print job. Read-only.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The dateTimeOffset when the job was created. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The dateTimeOffset when the job was created. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ArchivedPrintJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ArchivedPrintJob
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ArchivedPrintJob()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "acquired_by_printer": lambda n : setattr(self, 'acquired_by_printer', n.get_bool_value()),
            "acquired_date_time": lambda n : setattr(self, 'acquired_date_time', n.get_datetime_value()),
            "completion_date_time": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "copies_printed": lambda n : setattr(self, 'copies_printed', n.get_int_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(user_identity.UserIdentity)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "printer_id": lambda n : setattr(self, 'printer_id', n.get_str_value()),
            "processing_state": lambda n : setattr(self, 'processing_state', n.get_enum_value(print_job_processing_state.PrintJobProcessingState)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The archived print job's GUID. Read-only.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The archived print job's GUID. Read-only.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def printer_id(self,) -> Optional[str]:
        """
        Gets the printerId property value. The printer ID that the job was queued for. Read-only.
        Returns: Optional[str]
        """
        return self._printer_id
    
    @printer_id.setter
    def printer_id(self,value: Optional[str] = None) -> None:
        """
        Sets the printerId property value. The printer ID that the job was queued for. Read-only.
        Args:
            value: Value to set for the printerId property.
        """
        self._printer_id = value
    
    @property
    def processing_state(self,) -> Optional[print_job_processing_state.PrintJobProcessingState]:
        """
        Gets the processingState property value. The processingState property
        Returns: Optional[print_job_processing_state.PrintJobProcessingState]
        """
        return self._processing_state
    
    @processing_state.setter
    def processing_state(self,value: Optional[print_job_processing_state.PrintJobProcessingState] = None) -> None:
        """
        Sets the processingState property value. The processingState property
        Args:
            value: Value to set for the processingState property.
        """
        self._processing_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("acquiredByPrinter", self.acquired_by_printer)
        writer.write_datetime_value("acquiredDateTime", self.acquired_date_time)
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_int_value("copiesPrinted", self.copies_printed)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("printerId", self.printer_id)
        writer.write_enum_value("processingState", self.processing_state)
        writer.write_additional_data_value(self.additional_data)
    

