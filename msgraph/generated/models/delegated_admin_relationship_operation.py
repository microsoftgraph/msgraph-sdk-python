from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delegated_admin_relationship_operation_type, entity, long_running_operation_status

from . import entity

class DelegatedAdminRelationshipOperation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new delegatedAdminRelationshipOperation and sets the default values.
        """
        super().__init__()
        # The time in ISO 8601 format and in UTC time when the long-running operation was created. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The data (payload) for the operation. Read-only.
        self._data: Optional[str] = None
        # The time in ISO 8601 format and in UTC time when the long-running operation was last modified. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operationType property
        self._operation_type: Optional[delegated_admin_relationship_operation_type.DelegatedAdminRelationshipOperationType] = None
        # The status property
        self._status: Optional[long_running_operation_status.LongRunningOperationStatus] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The time in ISO 8601 format and in UTC time when the long-running operation was created. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The time in ISO 8601 format and in UTC time when the long-running operation was created. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedAdminRelationshipOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminRelationshipOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DelegatedAdminRelationshipOperation()
    
    @property
    def data(self,) -> Optional[str]:
        """
        Gets the data property value. The data (payload) for the operation. Read-only.
        Returns: Optional[str]
        """
        return self._data
    
    @data.setter
    def data(self,value: Optional[str] = None) -> None:
        """
        Sets the data property value. The data (payload) for the operation. Read-only.
        Args:
            value: Value to set for the data property.
        """
        self._data = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delegated_admin_relationship_operation_type, entity, long_running_operation_status

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "data": lambda n : setattr(self, 'data', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(delegated_admin_relationship_operation_type.DelegatedAdminRelationshipOperationType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(long_running_operation_status.LongRunningOperationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The time in ISO 8601 format and in UTC time when the long-running operation was last modified. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The time in ISO 8601 format and in UTC time when the long-running operation was last modified. Read-only.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def operation_type(self,) -> Optional[delegated_admin_relationship_operation_type.DelegatedAdminRelationshipOperationType]:
        """
        Gets the operationType property value. The operationType property
        Returns: Optional[delegated_admin_relationship_operation_type.DelegatedAdminRelationshipOperationType]
        """
        return self._operation_type
    
    @operation_type.setter
    def operation_type(self,value: Optional[delegated_admin_relationship_operation_type.DelegatedAdminRelationshipOperationType] = None) -> None:
        """
        Sets the operationType property value. The operationType property
        Args:
            value: Value to set for the operation_type property.
        """
        self._operation_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("data", self.data)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[long_running_operation_status.LongRunningOperationStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[long_running_operation_status.LongRunningOperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[long_running_operation_status.LongRunningOperationStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

