from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .error_detail import ErrorDetail
    from .monitor_run_status import MonitorRunStatus

from .entity import Entity

@dataclass
class ConfigurationMonitoringResult(Entity, Parsable):
    # Number of drifts observed during a monitor run. Supports $filter (eq, ne, ge, le) and $orderby.
    drifts_count: Optional[int] = None
    # All the error details that prevent the monitor from running successfully. The error details are a contained entity. Returned only on $select.
    error_details: Optional[list[ErrorDetail]] = None
    # Globally unique identifier (GUID) of the monitor. System-generated. Supports $filter (eq, ne).
    monitor_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Date and time at which the monitor run completed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, ge, le) and $orderby.
    run_completion_date_time: Optional[datetime.datetime] = None
    # Date and time at which the monitor run initiated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, ge, le) and $orderby.
    run_initiation_date_time: Optional[datetime.datetime] = None
    # The runStatus property
    run_status: Optional[MonitorRunStatus] = None
    # Globally unique identifier (GUID) of the tenant for which the monitor runs. Fetched automatically by the system. Supports $filter (eq, ne).
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationMonitoringResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationMonitoringResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationMonitoringResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .error_detail import ErrorDetail
        from .monitor_run_status import MonitorRunStatus

        from .entity import Entity
        from .error_detail import ErrorDetail
        from .monitor_run_status import MonitorRunStatus

        fields: dict[str, Callable[[Any], None]] = {
            "driftsCount": lambda n : setattr(self, 'drifts_count', n.get_int_value()),
            "errorDetails": lambda n : setattr(self, 'error_details', n.get_collection_of_object_values(ErrorDetail)),
            "monitorId": lambda n : setattr(self, 'monitor_id', n.get_str_value()),
            "runCompletionDateTime": lambda n : setattr(self, 'run_completion_date_time', n.get_datetime_value()),
            "runInitiationDateTime": lambda n : setattr(self, 'run_initiation_date_time', n.get_datetime_value()),
            "runStatus": lambda n : setattr(self, 'run_status', n.get_enum_value(MonitorRunStatus)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_enum_value("runStatus", self.run_status)
    

