from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
simulation_automation_run_status = lazy_import('msgraph.generated.models.simulation_automation_run_status')

class SimulationAutomationRun(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new simulationAutomationRun and sets the default values.
        """
        super().__init__()
        # Date and time when the run ends in an attack simulation automation.
        self._end_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Unique identifier for the attack simulation campaign initiated in the attack simulation automation run.
        self._simulation_id: Optional[str] = None
        # Date and time when the run starts in an attack simulation automation.
        self._start_date_time: Optional[datetime] = None
        # Status of the attack simulation automation run. The possible values are: unknown, running, succeeded, failed, skipped, unknownFutureValue.
        self._status: Optional[simulation_automation_run_status.SimulationAutomationRunStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SimulationAutomationRun:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SimulationAutomationRun
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SimulationAutomationRun()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. Date and time when the run ends in an attack simulation automation.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. Date and time when the run ends in an attack simulation automation.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "simulation_id": lambda n : setattr(self, 'simulation_id', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(simulation_automation_run_status.SimulationAutomationRunStatus)),
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
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("simulationId", self.simulation_id)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
    
    @property
    def simulation_id(self,) -> Optional[str]:
        """
        Gets the simulationId property value. Unique identifier for the attack simulation campaign initiated in the attack simulation automation run.
        Returns: Optional[str]
        """
        return self._simulation_id
    
    @simulation_id.setter
    def simulation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the simulationId property value. Unique identifier for the attack simulation campaign initiated in the attack simulation automation run.
        Args:
            value: Value to set for the simulationId property.
        """
        self._simulation_id = value
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. Date and time when the run starts in an attack simulation automation.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. Date and time when the run starts in an attack simulation automation.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[simulation_automation_run_status.SimulationAutomationRunStatus]:
        """
        Gets the status property value. Status of the attack simulation automation run. The possible values are: unknown, running, succeeded, failed, skipped, unknownFutureValue.
        Returns: Optional[simulation_automation_run_status.SimulationAutomationRunStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[simulation_automation_run_status.SimulationAutomationRunStatus] = None) -> None:
        """
        Sets the status property value. Status of the attack simulation automation run. The possible values are: unknown, running, succeeded, failed, skipped, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

