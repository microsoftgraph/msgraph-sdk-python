from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .configuration_baseline import ConfigurationBaseline
    from .entity import Entity
    from .identity_set import IdentitySet
    from .monitor_mode import MonitorMode
    from .monitor_status import MonitorStatus
    from .open_complex_dictionary_type import OpenComplexDictionaryType

from .entity import Entity

@dataclass
class ConfigurationMonitor(Entity, Parsable):
    # The baseline property
    baseline: Optional[ConfigurationBaseline] = None
    # The createdBy property
    created_by: Optional[IdentitySet] = None
    # The date and time when the monitor was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, ge, le) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # User-friendly description of the monitor given by the user. Supports $filter (eq, ne, startsWith) and $orderby.
    description: Optional[str] = None
    # User-friendly name given by the user to the monitor. Supports $filter (eq, ne, startsWith) and $orderby.
    display_name: Optional[str] = None
    # The reason for the monitor's inactivation. Returned only on $select.
    inactivation_reason: Optional[str] = None
    # The lastModifiedBy property
    last_modified_by: Optional[IdentitySet] = None
    # The date and time when the monitor was last modified. If no modifications are made to the monitor, it's the same as createdDateTime. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, ge, le) and $orderby.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The mode property
    mode: Optional[MonitorMode] = None
    # Frequency at which the monitor runs. The default frequency is six hours. Regardless of when you create or update a monitor, it gets triggered within the next 6 hours. Currently, monitors are picked up at fixed times: 6 AM, 12 PM, 6 PM, and 12 AM (all in GMT). For example, if you create a monitor at 9 AM, it gets triggered around 12 PM. If you update a monitor at 4 PM, it gets triggered around 6 PM.
    monitor_run_frequency_in_hours: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Key-value pairs that contain parameter values which might be used in the baseline. Returned only on $select.
    parameters: Optional[OpenComplexDictionaryType] = None
    # The status property
    status: Optional[MonitorStatus] = None
    # Globally unique identifier (GUID) of the tenant for which the monitor runs. Fetched automatically by the system. Supports $filter (eq, ne).
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationMonitor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationMonitor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationMonitor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .configuration_baseline import ConfigurationBaseline
        from .entity import Entity
        from .identity_set import IdentitySet
        from .monitor_mode import MonitorMode
        from .monitor_status import MonitorStatus
        from .open_complex_dictionary_type import OpenComplexDictionaryType

        from .configuration_baseline import ConfigurationBaseline
        from .entity import Entity
        from .identity_set import IdentitySet
        from .monitor_mode import MonitorMode
        from .monitor_status import MonitorStatus
        from .open_complex_dictionary_type import OpenComplexDictionaryType

        fields: dict[str, Callable[[Any], None]] = {
            "baseline": lambda n : setattr(self, 'baseline', n.get_object_value(ConfigurationBaseline)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "inactivationReason": lambda n : setattr(self, 'inactivation_reason', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(MonitorMode)),
            "monitorRunFrequencyInHours": lambda n : setattr(self, 'monitor_run_frequency_in_hours', n.get_int_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_object_value(OpenComplexDictionaryType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(MonitorStatus)),
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
        writer.write_object_value("baseline", self.baseline)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_enum_value("mode", self.mode)
        writer.write_object_value("parameters", self.parameters)
        writer.write_enum_value("status", self.status)
    

