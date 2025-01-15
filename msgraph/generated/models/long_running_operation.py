from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attack_simulation_operation import AttackSimulationOperation
    from .engagement_async_operation import EngagementAsyncOperation
    from .entity import Entity
    from .long_running_operation_status import LongRunningOperationStatus
    from .rich_long_running_operation import RichLongRunningOperation

from .entity import Entity

@dataclass
class LongRunningOperation(Entity, Parsable):
    """
    The status of a long-running operation.
    """
    # The start time of the operation. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The time of the last action in the operation. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_action_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # URI of the resource that the operation is performed on.
    resource_location: Optional[str] = None
    # The status of the operation. The possible values are: notStarted, running, succeeded, failed, unknownFutureValue.
    status: Optional[LongRunningOperationStatus] = None
    # Details about the status of the operation.
    status_detail: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LongRunningOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LongRunningOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attackSimulationOperation".casefold():
            from .attack_simulation_operation import AttackSimulationOperation

            return AttackSimulationOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementAsyncOperation".casefold():
            from .engagement_async_operation import EngagementAsyncOperation

            return EngagementAsyncOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.richLongRunningOperation".casefold():
            from .rich_long_running_operation import RichLongRunningOperation

            return RichLongRunningOperation()
        return LongRunningOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attack_simulation_operation import AttackSimulationOperation
        from .engagement_async_operation import EngagementAsyncOperation
        from .entity import Entity
        from .long_running_operation_status import LongRunningOperationStatus
        from .rich_long_running_operation import RichLongRunningOperation

        from .attack_simulation_operation import AttackSimulationOperation
        from .engagement_async_operation import EngagementAsyncOperation
        from .entity import Entity
        from .long_running_operation_status import LongRunningOperationStatus
        from .rich_long_running_operation import RichLongRunningOperation

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastActionDateTime": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "resourceLocation": lambda n : setattr(self, 'resource_location', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(LongRunningOperationStatus)),
            "statusDetail": lambda n : setattr(self, 'status_detail', n.get_str_value()),
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
        writer.write_str_value("resourceLocation", self.resource_location)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusDetail", self.status_detail)
    

