from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
print_document = lazy_import('msgraph.generated.models.print_document')
print_job_configuration = lazy_import('msgraph.generated.models.print_job_configuration')
print_job_status = lazy_import('msgraph.generated.models.print_job_status')
print_task = lazy_import('msgraph.generated.models.print_task')
user_identity = lazy_import('msgraph.generated.models.user_identity')

class PrintJob(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def configuration(self,) -> Optional[print_job_configuration.PrintJobConfiguration]:
        """
        Gets the configuration property value. The configuration property
        Returns: Optional[print_job_configuration.PrintJobConfiguration]
        """
        return self._configuration
    
    @configuration.setter
    def configuration(self,value: Optional[print_job_configuration.PrintJobConfiguration] = None) -> None:
        """
        Sets the configuration property value. The configuration property
        Args:
            value: Value to set for the configuration property.
        """
        self._configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new printJob and sets the default values.
        """
        super().__init__()
        # The configuration property
        self._configuration: Optional[print_job_configuration.PrintJobConfiguration] = None
        # The createdBy property
        self._created_by: Optional[user_identity.UserIdentity] = None
        # The DateTimeOffset when the job was created. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The documents property
        self._documents: Optional[List[print_document.PrintDocument]] = None
        # If true, document can be fetched by printer.
        self._is_fetchable: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Contains the source job URL, if the job has been redirected from another printer.
        self._redirected_from: Optional[str] = None
        # Contains the destination job URL, if the job has been redirected to another printer.
        self._redirected_to: Optional[str] = None
        # The status property
        self._status: Optional[print_job_status.PrintJobStatus] = None
        # A list of printTasks that were triggered by this print job.
        self._tasks: Optional[List[print_task.PrintTask]] = None
    
    @property
    def created_by(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The DateTimeOffset when the job was created. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The DateTimeOffset when the job was created. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintJob
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintJob()
    
    @property
    def documents(self,) -> Optional[List[print_document.PrintDocument]]:
        """
        Gets the documents property value. The documents property
        Returns: Optional[List[print_document.PrintDocument]]
        """
        return self._documents
    
    @documents.setter
    def documents(self,value: Optional[List[print_document.PrintDocument]] = None) -> None:
        """
        Sets the documents property value. The documents property
        Args:
            value: Value to set for the documents property.
        """
        self._documents = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(print_job_configuration.PrintJobConfiguration)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(user_identity.UserIdentity)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "documents": lambda n : setattr(self, 'documents', n.get_collection_of_object_values(print_document.PrintDocument)),
            "is_fetchable": lambda n : setattr(self, 'is_fetchable', n.get_bool_value()),
            "redirected_from": lambda n : setattr(self, 'redirected_from', n.get_str_value()),
            "redirected_to": lambda n : setattr(self, 'redirected_to', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(print_job_status.PrintJobStatus)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(print_task.PrintTask)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_fetchable(self,) -> Optional[bool]:
        """
        Gets the isFetchable property value. If true, document can be fetched by printer.
        Returns: Optional[bool]
        """
        return self._is_fetchable
    
    @is_fetchable.setter
    def is_fetchable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFetchable property value. If true, document can be fetched by printer.
        Args:
            value: Value to set for the isFetchable property.
        """
        self._is_fetchable = value
    
    @property
    def redirected_from(self,) -> Optional[str]:
        """
        Gets the redirectedFrom property value. Contains the source job URL, if the job has been redirected from another printer.
        Returns: Optional[str]
        """
        return self._redirected_from
    
    @redirected_from.setter
    def redirected_from(self,value: Optional[str] = None) -> None:
        """
        Sets the redirectedFrom property value. Contains the source job URL, if the job has been redirected from another printer.
        Args:
            value: Value to set for the redirectedFrom property.
        """
        self._redirected_from = value
    
    @property
    def redirected_to(self,) -> Optional[str]:
        """
        Gets the redirectedTo property value. Contains the destination job URL, if the job has been redirected to another printer.
        Returns: Optional[str]
        """
        return self._redirected_to
    
    @redirected_to.setter
    def redirected_to(self,value: Optional[str] = None) -> None:
        """
        Sets the redirectedTo property value. Contains the destination job URL, if the job has been redirected to another printer.
        Args:
            value: Value to set for the redirectedTo property.
        """
        self._redirected_to = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("configuration", self.configuration)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("documents", self.documents)
        writer.write_bool_value("isFetchable", self.is_fetchable)
        writer.write_str_value("redirectedFrom", self.redirected_from)
        writer.write_str_value("redirectedTo", self.redirected_to)
        writer.write_object_value("status", self.status)
        writer.write_collection_of_object_values("tasks", self.tasks)
    
    @property
    def status(self,) -> Optional[print_job_status.PrintJobStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[print_job_status.PrintJobStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[print_job_status.PrintJobStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def tasks(self,) -> Optional[List[print_task.PrintTask]]:
        """
        Gets the tasks property value. A list of printTasks that were triggered by this print job.
        Returns: Optional[List[print_task.PrintTask]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[print_task.PrintTask]] = None) -> None:
        """
        Sets the tasks property value. A list of printTasks that were triggered by this print job.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    

