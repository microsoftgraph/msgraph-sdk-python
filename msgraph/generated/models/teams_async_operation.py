from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, operation_error, teams_async_operation_status, teams_async_operation_type

from . import entity

@dataclass
class TeamsAsyncOperation(entity.Entity):
    # Number of times the operation was attempted before being marked successful or failed.
    attempts_count: Optional[int] = None
    # Time when the operation was created.
    created_date_time: Optional[datetime] = None
    # Any error that causes the async operation to fail.
    error: Optional[operation_error.OperationError] = None
    # Time when the async operation was last updated.
    last_action_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operationType property
    operation_type: Optional[teams_async_operation_type.TeamsAsyncOperationType] = None
    # The status property
    status: Optional[teams_async_operation_status.TeamsAsyncOperationStatus] = None
    # The ID of the object that's created or modified as result of this async operation, typically a team.
    target_resource_id: Optional[str] = None
    # The location of the object that's created or modified as result of this async operation. This URL should be treated as an opaque value and not parsed into its component paths.
    target_resource_location: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamsAsyncOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAsyncOperation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamsAsyncOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, operation_error, teams_async_operation_status, teams_async_operation_type

        from . import entity, operation_error, teams_async_operation_status, teams_async_operation_type

        fields: Dict[str, Callable[[Any], None]] = {
            "attemptsCount": lambda n : setattr(self, 'attempts_count', n.get_int_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(operation_error.OperationError)),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(teams_async_operation_type.TeamsAsyncOperationType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(teams_async_operation_status.TeamsAsyncOperationStatus)),
            "targetResourceId": lambda n : setattr(self, 'target_resource_id', n.get_str_value()),
            "targetResourceLocation": lambda n : setattr(self, 'target_resource_location', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("attemptsCount", self.attempts_count)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("targetResourceId", self.target_resource_id)
        writer.write_str_value("targetResourceLocation", self.target_resource_location)
    

