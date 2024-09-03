from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .delegated_admin_relationship_operation_type import DelegatedAdminRelationshipOperationType
    from .entity import Entity
    from .long_running_operation_status import LongRunningOperationStatus

from .entity import Entity

@dataclass
class DelegatedAdminRelationshipOperation(Entity):
    # The time in ISO 8601 format and in UTC time when the long-running operation was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The data (payload) for the operation. Read-only.
    data: Optional[str] = None
    # The time in ISO 8601 format and in UTC time when the long-running operation was last modified. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operationType property
    operation_type: Optional[DelegatedAdminRelationshipOperationType] = None
    # The status property
    status: Optional[LongRunningOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegatedAdminRelationshipOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminRelationshipOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegatedAdminRelationshipOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .delegated_admin_relationship_operation_type import DelegatedAdminRelationshipOperationType
        from .entity import Entity
        from .long_running_operation_status import LongRunningOperationStatus

        from .delegated_admin_relationship_operation_type import DelegatedAdminRelationshipOperationType
        from .entity import Entity
        from .long_running_operation_status import LongRunningOperationStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "data": lambda n : setattr(self, 'data', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_enum_value(DelegatedAdminRelationshipOperationType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(LongRunningOperationStatus)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("data", self.data)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("operationType", self.operation_type)
        writer.write_enum_value("status", self.status)
    

