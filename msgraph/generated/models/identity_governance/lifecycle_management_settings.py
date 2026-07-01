from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..email_settings import EmailSettings
    from ..entity import Entity
    from .quarantine_configuration import QuarantineConfiguration

from ..entity import Entity

@dataclass
class LifecycleManagementSettings(Entity, Parsable):
    # The emailSettings property
    email_settings: Optional[EmailSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The quarantineConfiguration property
    quarantine_configuration: Optional[QuarantineConfiguration] = None
    # The interval in hours at which all workflows running in the tenant should be scheduled for execution. This interval has a minimum value of 1 and a maximum value of 24. The default value is 3 hours.
    workflow_schedule_interval_in_hours: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecycleManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecycleManagementSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecycleManagementSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..email_settings import EmailSettings
        from ..entity import Entity
        from .quarantine_configuration import QuarantineConfiguration

        from ..email_settings import EmailSettings
        from ..entity import Entity
        from .quarantine_configuration import QuarantineConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "emailSettings": lambda n : setattr(self, 'email_settings', n.get_object_value(EmailSettings)),
            "quarantineConfiguration": lambda n : setattr(self, 'quarantine_configuration', n.get_object_value(QuarantineConfiguration)),
            "workflowScheduleIntervalInHours": lambda n : setattr(self, 'workflow_schedule_interval_in_hours', n.get_int_value()),
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
        writer.write_object_value("emailSettings", self.email_settings)
        writer.write_object_value("quarantineConfiguration", self.quarantine_configuration)
        writer.write_int_value("workflowScheduleIntervalInHours", self.workflow_schedule_interval_in_hours)
    

