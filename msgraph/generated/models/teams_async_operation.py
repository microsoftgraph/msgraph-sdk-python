from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
operation_error = lazy_import('msgraph.generated.models.operation_error')
teams_async_operation_status = lazy_import('msgraph.generated.models.teams_async_operation_status')
teams_async_operation_type = lazy_import('msgraph.generated.models.teams_async_operation_type')

class TeamsAsyncOperation(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def attempts_count(self,) -> Optional[int]:
        """
        Gets the attemptsCount property value. Number of times the operation was attempted before being marked successful or failed.
        Returns: Optional[int]
        """
        return self._attempts_count
    
    @attempts_count.setter
    def attempts_count(self,value: Optional[int] = None) -> None:
        """
        Sets the attemptsCount property value. Number of times the operation was attempted before being marked successful or failed.
        Args:
            value: Value to set for the attemptsCount property.
        """
        self._attempts_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamsAsyncOperation and sets the default values.
        """
        super().__init__()
        # Number of times the operation was attempted before being marked successful or failed.
        self._attempts_count: Optional[int] = None
        # Time when the operation was created.
        self._created_date_time: Optional[datetime] = None
        # Any error that causes the async operation to fail.
        self._error: Optional[operation_error.OperationError] = None
        # Time when the async operation was last updated.
        self._last_action_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operationType property
        self._operation_type: Optional[teams_async_operation_type.TeamsAsyncOperationType] = None
        # The status property
        self._status: Optional[teams_async_operation_status.TeamsAsyncOperationStatus] = None
        # The ID of the object that's created or modified as result of this async operation, typically a team.
        self._target_resource_id: Optional[str] = None
        # The location of the object that's created or modified as result of this async operation. This URL should be treated as an opaque value and not parsed into its component paths.
        self._target_resource_location: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Time when the operation was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Time when the operation was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAsyncOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAsyncOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamsAsyncOperation()
    
    @property
    def error(self,) -> Optional[operation_error.OperationError]:
        """
        Gets the error property value. Any error that causes the async operation to fail.
        Returns: Optional[operation_error.OperationError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[operation_error.OperationError] = None) -> None:
        """
        Sets the error property value. Any error that causes the async operation to fail.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attempts_count": lambda n : setattr(self, 'attempts_count', n.get_int_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(operation_error.OperationError)),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "operation_type": lambda n : setattr(self, 'operation_type', n.get_enum_value(teams_async_operation_type.TeamsAsyncOperationType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(teams_async_operation_status.TeamsAsyncOperationStatus)),
            "target_resource_id": lambda n : setattr(self, 'target_resource_id', n.get_str_value()),
            "target_resource_location": lambda n : setattr(self, 'target_resource_location', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. Time when the async operation was last updated.
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. Time when the async operation was last updated.
        Args:
            value: Value to set for the lastActionDateTime property.
        """
        self._last_action_date_time = value
    
    @property
    def operation_type(self,) -> Optional[teams_async_operation_type.TeamsAsyncOperationType]:
        """
        Gets the operationType property value. The operationType property
        Returns: Optional[teams_async_operation_type.TeamsAsyncOperationType]
        """
        return self._operation_type
    
    @operation_type.setter
    def operation_type(self,value: Optional[teams_async_operation_type.TeamsAsyncOperationType] = None) -> None:
        """
        Sets the operationType property value. The operationType property
        Args:
            value: Value to set for the operationType property.
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
        writer.write_int_value("attemptsCount", self.attempts_count)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("targetResourceId", self.target_resource_id)
        writer.write_str_value("targetResourceLocation", self.target_resource_location)
    
    @property
    def status(self,) -> Optional[teams_async_operation_status.TeamsAsyncOperationStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[teams_async_operation_status.TeamsAsyncOperationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[teams_async_operation_status.TeamsAsyncOperationStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def target_resource_id(self,) -> Optional[str]:
        """
        Gets the targetResourceId property value. The ID of the object that's created or modified as result of this async operation, typically a team.
        Returns: Optional[str]
        """
        return self._target_resource_id
    
    @target_resource_id.setter
    def target_resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetResourceId property value. The ID of the object that's created or modified as result of this async operation, typically a team.
        Args:
            value: Value to set for the targetResourceId property.
        """
        self._target_resource_id = value
    
    @property
    def target_resource_location(self,) -> Optional[str]:
        """
        Gets the targetResourceLocation property value. The location of the object that's created or modified as result of this async operation. This URL should be treated as an opaque value and not parsed into its component paths.
        Returns: Optional[str]
        """
        return self._target_resource_location
    
    @target_resource_location.setter
    def target_resource_location(self,value: Optional[str] = None) -> None:
        """
        Sets the targetResourceLocation property value. The location of the object that's created or modified as result of this async operation. This URL should be treated as an opaque value and not parsed into its component paths.
        Args:
            value: Value to set for the targetResourceLocation property.
        """
        self._target_resource_location = value
    

