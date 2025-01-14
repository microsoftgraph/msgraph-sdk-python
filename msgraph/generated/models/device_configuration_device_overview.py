from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceConfigurationDeviceOverview(Entity, Parsable):
    # Version of the policy for that overview
    configuration_version: Optional[int] = None
    # Number of error devices
    error_count: Optional[int] = None
    # Number of failed devices
    failed_count: Optional[int] = None
    # Last update time
    last_update_date_time: Optional[datetime.datetime] = None
    # Number of not applicable devices
    not_applicable_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of pending devices
    pending_count: Optional[int] = None
    # Number of succeeded devices
    success_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceConfigurationDeviceOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfigurationDeviceOverview
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceConfigurationDeviceOverview()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "configurationVersion": lambda n : setattr(self, 'configuration_version', n.get_int_value()),
            "errorCount": lambda n : setattr(self, 'error_count', n.get_int_value()),
            "failedCount": lambda n : setattr(self, 'failed_count', n.get_int_value()),
            "lastUpdateDateTime": lambda n : setattr(self, 'last_update_date_time', n.get_datetime_value()),
            "notApplicableCount": lambda n : setattr(self, 'not_applicable_count', n.get_int_value()),
            "pendingCount": lambda n : setattr(self, 'pending_count', n.get_int_value()),
            "successCount": lambda n : setattr(self, 'success_count', n.get_int_value()),
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
        writer.write_int_value("configurationVersion", self.configuration_version)
        writer.write_int_value("errorCount", self.error_count)
        writer.write_int_value("failedCount", self.failed_count)
        writer.write_datetime_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_int_value("notApplicableCount", self.not_applicable_count)
        writer.write_int_value("pendingCount", self.pending_count)
        writer.write_int_value("successCount", self.success_count)
    

