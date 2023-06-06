from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import data_policy_operation_status, entity

from . import entity

@dataclass
class DataPolicyOperation(entity.Entity):
    # Represents when the request for this data policy operation was completed, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Null until the operation completes.
    completed_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the progress of an operation.
    progress: Optional[float] = None
    # Possible values are: notStarted, running, complete, failed, unknownFutureValue.
    status: Optional[data_policy_operation_status.DataPolicyOperationStatus] = None
    # The URL location to where data is being exported for export requests.
    storage_location: Optional[str] = None
    # Represents when the request for this data operation was submitted, in UTC time, using the ISO 8601 format. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    submitted_date_time: Optional[datetime] = None
    # The id for the user on whom the operation is performed.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataPolicyOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DataPolicyOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DataPolicyOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import data_policy_operation_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "progress": lambda n : setattr(self, 'progress', n.get_float_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(data_policy_operation_status.DataPolicyOperationStatus)),
            "storageLocation": lambda n : setattr(self, 'storage_location', n.get_str_value()),
            "submittedDateTime": lambda n : setattr(self, 'submitted_date_time', n.get_datetime_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_float_value("progress", self.progress)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("storageLocation", self.storage_location)
        writer.write_datetime_value("submittedDateTime", self.submitted_date_time)
        writer.write_str_value("userId", self.user_id)
    

