from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .print_document import PrintDocument
    from .print_job_configuration import PrintJobConfiguration
    from .print_job_status import PrintJobStatus
    from .print_task import PrintTask
    from .user_identity import UserIdentity

from .entity import Entity

@dataclass
class PrintJob(Entity, Parsable):
    # The dateTimeOffset when the job was acknowledged. Read-only.
    acknowledged_date_time: Optional[datetime.datetime] = None
    # The configuration property
    configuration: Optional[PrintJobConfiguration] = None
    # The createdBy property
    created_by: Optional[UserIdentity] = None
    # The DateTimeOffset when the job was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The documents property
    documents: Optional[list[PrintDocument]] = None
    # The error code of the print job. Read-only.
    error_code: Optional[int] = None
    # If true, document can be fetched by printer.
    is_fetchable: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains the source job URL, if the job has been redirected from another printer.
    redirected_from: Optional[str] = None
    # Contains the destination job URL, if the job has been redirected to another printer.
    redirected_to: Optional[str] = None
    # The status property
    status: Optional[PrintJobStatus] = None
    # A list of printTasks that were triggered by this print job.
    tasks: Optional[list[PrintTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrintJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrintJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .print_document import PrintDocument
        from .print_job_configuration import PrintJobConfiguration
        from .print_job_status import PrintJobStatus
        from .print_task import PrintTask
        from .user_identity import UserIdentity

        from .entity import Entity
        from .print_document import PrintDocument
        from .print_job_configuration import PrintJobConfiguration
        from .print_job_status import PrintJobStatus
        from .print_task import PrintTask
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "acknowledgedDateTime": lambda n : setattr(self, 'acknowledged_date_time', n.get_datetime_value()),
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(PrintJobConfiguration)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(UserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "documents": lambda n : setattr(self, 'documents', n.get_collection_of_object_values(PrintDocument)),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "isFetchable": lambda n : setattr(self, 'is_fetchable', n.get_bool_value()),
            "redirectedFrom": lambda n : setattr(self, 'redirected_from', n.get_str_value()),
            "redirectedTo": lambda n : setattr(self, 'redirected_to', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(PrintJobStatus)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(PrintTask)),
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
        writer.write_datetime_value("acknowledgedDateTime", self.acknowledged_date_time)
        writer.write_object_value("configuration", self.configuration)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("documents", self.documents)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_bool_value("isFetchable", self.is_fetchable)
        writer.write_str_value("redirectedFrom", self.redirected_from)
        writer.write_str_value("redirectedTo", self.redirected_to)
        writer.write_object_value("status", self.status)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

