from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_hash import FileHash
    from .process_integrity_level import ProcessIntegrityLevel

@dataclass
class Process(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # User account identifier (user account context the process ran under) for example, AccountName, SID, and so on.
    account_name: Optional[str] = None
    # The full process invocation commandline including all parameters.
    command_line: Optional[str] = None
    # Time at which the process was started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Complex type containing file hashes (cryptographic and location-sensitive).
    file_hash: Optional[FileHash] = None
    # The integrity level of the process. Possible values are: unknown, untrusted, low, medium, high, system.
    integrity_level: Optional[ProcessIntegrityLevel] = None
    # True if the process is elevated.
    is_elevated: Optional[bool] = None
    # The name of the process' Image file.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # DateTime at which the parent process was started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    parent_process_created_date_time: Optional[datetime.datetime] = None
    # The Process ID (PID) of the parent process.
    parent_process_id: Optional[int] = None
    # The name of the image file of the parent process.
    parent_process_name: Optional[str] = None
    # Full path, including filename.
    path: Optional[str] = None
    # The Process ID (PID) of the process.
    process_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Process:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Process
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Process()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .file_hash import FileHash
        from .process_integrity_level import ProcessIntegrityLevel

        from .file_hash import FileHash
        from .process_integrity_level import ProcessIntegrityLevel

        fields: Dict[str, Callable[[Any], None]] = {
            "accountName": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "commandLine": lambda n : setattr(self, 'command_line', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "fileHash": lambda n : setattr(self, 'file_hash', n.get_object_value(FileHash)),
            "integrityLevel": lambda n : setattr(self, 'integrity_level', n.get_enum_value(ProcessIntegrityLevel)),
            "isElevated": lambda n : setattr(self, 'is_elevated', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parentProcessCreatedDateTime": lambda n : setattr(self, 'parent_process_created_date_time', n.get_datetime_value()),
            "parentProcessId": lambda n : setattr(self, 'parent_process_id', n.get_int_value()),
            "parentProcessName": lambda n : setattr(self, 'parent_process_name', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "processId": lambda n : setattr(self, 'process_id', n.get_int_value()),
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
        writer.write_str_value("accountName", self.account_name)
        writer.write_str_value("commandLine", self.command_line)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("fileHash", self.file_hash)
        writer.write_enum_value("integrityLevel", self.integrity_level)
        writer.write_bool_value("isElevated", self.is_elevated)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("parentProcessCreatedDateTime", self.parent_process_created_date_time)
        writer.write_int_value("parentProcessId", self.parent_process_id)
        writer.write_str_value("parentProcessName", self.parent_process_name)
        writer.write_str_value("path", self.path)
        writer.write_int_value("processId", self.process_id)
        writer.write_additional_data_value(self.additional_data)
    

