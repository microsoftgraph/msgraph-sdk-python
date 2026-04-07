from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drifted_property import DriftedProperty
    from .drift_status import DriftStatus
    from .entity import Entity
    from .open_complex_dictionary_type import OpenComplexDictionaryType

from .entity import Entity

@dataclass
class ConfigurationDrift(Entity, Parsable):
    # Resource instance for which the drift is detected. Supports $filter (eq, ne, startsWith) and $orderby.
    baseline_resource_display_name: Optional[str] = None
    # Properties within one or more resource instances in which drift is detected. Returned only on $select.
    drifted_properties: Optional[list[DriftedProperty]] = None
    # The date and time at which drift is first detected. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, ge, le) and $orderby.
    first_reported_date_time: Optional[datetime.datetime] = None
    # Globally unique identifier (GUID) of the monitor. System-generated. Supports $filter (eq, ne).
    monitor_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceInstanceIdentifier property
    resource_instance_identifier: Optional[OpenComplexDictionaryType] = None
    # Resource for which the drift is detected. Supports $filter (eq, ne, startsWith).
    resource_type: Optional[str] = None
    # The status property
    status: Optional[DriftStatus] = None
    # Globally unique identifier (GUID) of the tenant for which the monitor runs. Fetched automatically by the system. Supports $filter (eq, ne).
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationDrift:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationDrift
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationDrift()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .drifted_property import DriftedProperty
        from .drift_status import DriftStatus
        from .entity import Entity
        from .open_complex_dictionary_type import OpenComplexDictionaryType

        from .drifted_property import DriftedProperty
        from .drift_status import DriftStatus
        from .entity import Entity
        from .open_complex_dictionary_type import OpenComplexDictionaryType

        fields: dict[str, Callable[[Any], None]] = {
            "baselineResourceDisplayName": lambda n : setattr(self, 'baseline_resource_display_name', n.get_str_value()),
            "driftedProperties": lambda n : setattr(self, 'drifted_properties', n.get_collection_of_object_values(DriftedProperty)),
            "firstReportedDateTime": lambda n : setattr(self, 'first_reported_date_time', n.get_datetime_value()),
            "monitorId": lambda n : setattr(self, 'monitor_id', n.get_str_value()),
            "resourceInstanceIdentifier": lambda n : setattr(self, 'resource_instance_identifier', n.get_object_value(OpenComplexDictionaryType)),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(DriftStatus)),
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
        writer.write_object_value("resourceInstanceIdentifier", self.resource_instance_identifier)
        writer.write_enum_value("status", self.status)
    

