from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from ...long_running_operation_status import LongRunningOperationStatus
    from .export_success_operation import ExportSuccessOperation
    from .failed_operation import FailedOperation
    from .running_operation import RunningOperation

from ...entity import Entity

@dataclass
class Operation(Entity, Parsable):
    # The start time of the operation. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The time of the last action of the operation. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_action_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the operation. The possible values are: notStarted, running, completed, failed, unknownFutureValue.
    status: Optional[LongRunningOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Operation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Operation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.exportSuccessOperation".casefold():
            from .export_success_operation import ExportSuccessOperation

            return ExportSuccessOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.failedOperation".casefold():
            from .failed_operation import FailedOperation

            return FailedOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.runningOperation".casefold():
            from .running_operation import RunningOperation

            return RunningOperation()
        return Operation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from ...long_running_operation_status import LongRunningOperationStatus
        from .export_success_operation import ExportSuccessOperation
        from .failed_operation import FailedOperation
        from .running_operation import RunningOperation

        from ...entity import Entity
        from ...long_running_operation_status import LongRunningOperationStatus
        from .export_success_operation import ExportSuccessOperation
        from .failed_operation import FailedOperation
        from .running_operation import RunningOperation

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_enum_value("status", self.status)
    

