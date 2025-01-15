from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_identity import EmailIdentity
    from .entity import Entity
    from .simulation_automation_run import SimulationAutomationRun
    from .simulation_automation_status import SimulationAutomationStatus

from .entity import Entity

@dataclass
class SimulationAutomation(Entity, Parsable):
    # Identity of the user who created the attack simulation automation.
    created_by: Optional[EmailIdentity] = None
    # Date and time when the attack simulation automation was created.
    created_date_time: Optional[datetime.datetime] = None
    # Description of the attack simulation automation.
    description: Optional[str] = None
    # Display name of the attack simulation automation. Supports $filter and $orderby.
    display_name: Optional[str] = None
    # Identity of the user who most recently modified the attack simulation automation.
    last_modified_by: Optional[EmailIdentity] = None
    # Date and time when the attack simulation automation was most recently modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Date and time of the latest run of the attack simulation automation.
    last_run_date_time: Optional[datetime.datetime] = None
    # Date and time of the upcoming run of the attack simulation automation.
    next_run_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of simulation automation runs.
    runs: Optional[list[SimulationAutomationRun]] = None
    # Status of the attack simulation automation. Supports $filter and $orderby. The possible values are: unknown, draft, notRunning, running, completed, unknownFutureValue.
    status: Optional[SimulationAutomationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SimulationAutomation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SimulationAutomation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SimulationAutomation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_identity import EmailIdentity
        from .entity import Entity
        from .simulation_automation_run import SimulationAutomationRun
        from .simulation_automation_status import SimulationAutomationStatus

        from .email_identity import EmailIdentity
        from .entity import Entity
        from .simulation_automation_run import SimulationAutomationRun
        from .simulation_automation_status import SimulationAutomationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastRunDateTime": lambda n : setattr(self, 'last_run_date_time', n.get_datetime_value()),
            "nextRunDateTime": lambda n : setattr(self, 'next_run_date_time', n.get_datetime_value()),
            "runs": lambda n : setattr(self, 'runs', n.get_collection_of_object_values(SimulationAutomationRun)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SimulationAutomationStatus)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("lastRunDateTime", self.last_run_date_time)
        writer.write_datetime_value("nextRunDateTime", self.next_run_date_time)
        writer.write_collection_of_object_values("runs", self.runs)
        writer.write_enum_value("status", self.status)
    

