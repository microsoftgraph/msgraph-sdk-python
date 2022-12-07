from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

file_hash = lazy_import('msgraph.generated.models.file_hash')
process_integrity_level = lazy_import('msgraph.generated.models.process_integrity_level')

class Process(AdditionalDataHolder, Parsable):
    @property
    def account_name(self,) -> Optional[str]:
        """
        Gets the accountName property value. User account identifier (user account context the process ran under) for example, AccountName, SID, and so on.
        Returns: Optional[str]
        """
        return self._account_name
    
    @account_name.setter
    def account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the accountName property value. User account identifier (user account context the process ran under) for example, AccountName, SID, and so on.
        Args:
            value: Value to set for the accountName property.
        """
        self._account_name = value
    
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
    def command_line(self,) -> Optional[str]:
        """
        Gets the commandLine property value. The full process invocation commandline including all parameters.
        Returns: Optional[str]
        """
        return self._command_line
    
    @command_line.setter
    def command_line(self,value: Optional[str] = None) -> None:
        """
        Sets the commandLine property value. The full process invocation commandline including all parameters.
        Args:
            value: Value to set for the commandLine property.
        """
        self._command_line = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new process and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # User account identifier (user account context the process ran under) for example, AccountName, SID, and so on.
        self._account_name: Optional[str] = None
        # The full process invocation commandline including all parameters.
        self._command_line: Optional[str] = None
        # Time at which the process was started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # Complex type containing file hashes (cryptographic and location-sensitive).
        self._file_hash: Optional[file_hash.FileHash] = None
        # The integrity level of the process. Possible values are: unknown, untrusted, low, medium, high, system.
        self._integrity_level: Optional[process_integrity_level.ProcessIntegrityLevel] = None
        # True if the process is elevated.
        self._is_elevated: Optional[bool] = None
        # The name of the process' Image file.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # DateTime at which the parent process was started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._parent_process_created_date_time: Optional[datetime] = None
        # The Process ID (PID) of the parent process.
        self._parent_process_id: Optional[int] = None
        # The name of the image file of the parent process.
        self._parent_process_name: Optional[str] = None
        # Full path, including filename.
        self._path: Optional[str] = None
        # The Process ID (PID) of the process.
        self._process_id: Optional[int] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Time at which the process was started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Time at which the process was started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Process:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Process
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Process()
    
    @property
    def file_hash(self,) -> Optional[file_hash.FileHash]:
        """
        Gets the fileHash property value. Complex type containing file hashes (cryptographic and location-sensitive).
        Returns: Optional[file_hash.FileHash]
        """
        return self._file_hash
    
    @file_hash.setter
    def file_hash(self,value: Optional[file_hash.FileHash] = None) -> None:
        """
        Sets the fileHash property value. Complex type containing file hashes (cryptographic and location-sensitive).
        Args:
            value: Value to set for the fileHash property.
        """
        self._file_hash = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "account_name": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "command_line": lambda n : setattr(self, 'command_line', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "file_hash": lambda n : setattr(self, 'file_hash', n.get_object_value(file_hash.FileHash)),
            "integrity_level": lambda n : setattr(self, 'integrity_level', n.get_enum_value(process_integrity_level.ProcessIntegrityLevel)),
            "is_elevated": lambda n : setattr(self, 'is_elevated', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parent_process_created_date_time": lambda n : setattr(self, 'parent_process_created_date_time', n.get_datetime_value()),
            "parent_process_id": lambda n : setattr(self, 'parent_process_id', n.get_int_value()),
            "parent_process_name": lambda n : setattr(self, 'parent_process_name', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "process_id": lambda n : setattr(self, 'process_id', n.get_int_value()),
        }
        return fields
    
    @property
    def integrity_level(self,) -> Optional[process_integrity_level.ProcessIntegrityLevel]:
        """
        Gets the integrityLevel property value. The integrity level of the process. Possible values are: unknown, untrusted, low, medium, high, system.
        Returns: Optional[process_integrity_level.ProcessIntegrityLevel]
        """
        return self._integrity_level
    
    @integrity_level.setter
    def integrity_level(self,value: Optional[process_integrity_level.ProcessIntegrityLevel] = None) -> None:
        """
        Sets the integrityLevel property value. The integrity level of the process. Possible values are: unknown, untrusted, low, medium, high, system.
        Args:
            value: Value to set for the integrityLevel property.
        """
        self._integrity_level = value
    
    @property
    def is_elevated(self,) -> Optional[bool]:
        """
        Gets the isElevated property value. True if the process is elevated.
        Returns: Optional[bool]
        """
        return self._is_elevated
    
    @is_elevated.setter
    def is_elevated(self,value: Optional[bool] = None) -> None:
        """
        Sets the isElevated property value. True if the process is elevated.
        Args:
            value: Value to set for the isElevated property.
        """
        self._is_elevated = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the process' Image file.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the process' Image file.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
    def parent_process_created_date_time(self,) -> Optional[datetime]:
        """
        Gets the parentProcessCreatedDateTime property value. DateTime at which the parent process was started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._parent_process_created_date_time
    
    @parent_process_created_date_time.setter
    def parent_process_created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the parentProcessCreatedDateTime property value. DateTime at which the parent process was started. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the parentProcessCreatedDateTime property.
        """
        self._parent_process_created_date_time = value
    
    @property
    def parent_process_id(self,) -> Optional[int]:
        """
        Gets the parentProcessId property value. The Process ID (PID) of the parent process.
        Returns: Optional[int]
        """
        return self._parent_process_id
    
    @parent_process_id.setter
    def parent_process_id(self,value: Optional[int] = None) -> None:
        """
        Sets the parentProcessId property value. The Process ID (PID) of the parent process.
        Args:
            value: Value to set for the parentProcessId property.
        """
        self._parent_process_id = value
    
    @property
    def parent_process_name(self,) -> Optional[str]:
        """
        Gets the parentProcessName property value. The name of the image file of the parent process.
        Returns: Optional[str]
        """
        return self._parent_process_name
    
    @parent_process_name.setter
    def parent_process_name(self,value: Optional[str] = None) -> None:
        """
        Sets the parentProcessName property value. The name of the image file of the parent process.
        Args:
            value: Value to set for the parentProcessName property.
        """
        self._parent_process_name = value
    
    @property
    def path(self,) -> Optional[str]:
        """
        Gets the path property value. Full path, including filename.
        Returns: Optional[str]
        """
        return self._path
    
    @path.setter
    def path(self,value: Optional[str] = None) -> None:
        """
        Sets the path property value. Full path, including filename.
        Args:
            value: Value to set for the path property.
        """
        self._path = value
    
    @property
    def process_id(self,) -> Optional[int]:
        """
        Gets the processId property value. The Process ID (PID) of the process.
        Returns: Optional[int]
        """
        return self._process_id
    
    @process_id.setter
    def process_id(self,value: Optional[int] = None) -> None:
        """
        Sets the processId property value. The Process ID (PID) of the process.
        Args:
            value: Value to set for the processId property.
        """
        self._process_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

