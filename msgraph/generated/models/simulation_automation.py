from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

email_identity = lazy_import('msgraph.generated.models.email_identity')
entity = lazy_import('msgraph.generated.models.entity')
simulation_automation_run = lazy_import('msgraph.generated.models.simulation_automation_run')
simulation_automation_status = lazy_import('msgraph.generated.models.simulation_automation_status')

class SimulationAutomation(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new simulationAutomation and sets the default values.
        """
        super().__init__()
        # Identity of the user who created the attack simulation automation.
        self._created_by: Optional[email_identity.EmailIdentity] = None
        # Date and time when the attack simulation automation was created.
        self._created_date_time: Optional[datetime] = None
        # Description of the attack simulation automation.
        self._description: Optional[str] = None
        # Display name of the attack simulation automation. Supports $filter and $orderby.
        self._display_name: Optional[str] = None
        # Identity of the user who most recently modified the attack simulation automation.
        self._last_modified_by: Optional[email_identity.EmailIdentity] = None
        # Date and time when the attack simulation automation was most recently modified.
        self._last_modified_date_time: Optional[datetime] = None
        # Date and time of the latest run of the attack simulation automation.
        self._last_run_date_time: Optional[datetime] = None
        # Date and time of the upcoming run of the attack simulation automation.
        self._next_run_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of simulation automation runs.
        self._runs: Optional[List[simulation_automation_run.SimulationAutomationRun]] = None
        # Status of the attack simulation automation. Supports $filter and $orderby. The possible values are: unknown, draft, notRunning, running, completed, unknownFutureValue.
        self._status: Optional[simulation_automation_status.SimulationAutomationStatus] = None
    
    @property
    def created_by(self,) -> Optional[email_identity.EmailIdentity]:
        """
        Gets the createdBy property value. Identity of the user who created the attack simulation automation.
        Returns: Optional[email_identity.EmailIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[email_identity.EmailIdentity] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user who created the attack simulation automation.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time when the attack simulation automation was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time when the attack simulation automation was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SimulationAutomation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SimulationAutomation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SimulationAutomation()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the attack simulation automation.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the attack simulation automation.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the attack simulation automation. Supports $filter and $orderby.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the attack simulation automation. Supports $filter and $orderby.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(email_identity.EmailIdentity)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(email_identity.EmailIdentity)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "last_run_date_time": lambda n : setattr(self, 'last_run_date_time', n.get_datetime_value()),
            "next_run_date_time": lambda n : setattr(self, 'next_run_date_time', n.get_datetime_value()),
            "runs": lambda n : setattr(self, 'runs', n.get_collection_of_object_values(simulation_automation_run.SimulationAutomationRun)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(simulation_automation_status.SimulationAutomationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_by(self,) -> Optional[email_identity.EmailIdentity]:
        """
        Gets the lastModifiedBy property value. Identity of the user who most recently modified the attack simulation automation.
        Returns: Optional[email_identity.EmailIdentity]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[email_identity.EmailIdentity] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user who most recently modified the attack simulation automation.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Date and time when the attack simulation automation was most recently modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Date and time when the attack simulation automation was most recently modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def last_run_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRunDateTime property value. Date and time of the latest run of the attack simulation automation.
        Returns: Optional[datetime]
        """
        return self._last_run_date_time
    
    @last_run_date_time.setter
    def last_run_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRunDateTime property value. Date and time of the latest run of the attack simulation automation.
        Args:
            value: Value to set for the lastRunDateTime property.
        """
        self._last_run_date_time = value
    
    @property
    def next_run_date_time(self,) -> Optional[datetime]:
        """
        Gets the nextRunDateTime property value. Date and time of the upcoming run of the attack simulation automation.
        Returns: Optional[datetime]
        """
        return self._next_run_date_time
    
    @next_run_date_time.setter
    def next_run_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the nextRunDateTime property value. Date and time of the upcoming run of the attack simulation automation.
        Args:
            value: Value to set for the nextRunDateTime property.
        """
        self._next_run_date_time = value
    
    @property
    def runs(self,) -> Optional[List[simulation_automation_run.SimulationAutomationRun]]:
        """
        Gets the runs property value. A collection of simulation automation runs.
        Returns: Optional[List[simulation_automation_run.SimulationAutomationRun]]
        """
        return self._runs
    
    @runs.setter
    def runs(self,value: Optional[List[simulation_automation_run.SimulationAutomationRun]] = None) -> None:
        """
        Sets the runs property value. A collection of simulation automation runs.
        Args:
            value: Value to set for the runs property.
        """
        self._runs = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def status(self,) -> Optional[simulation_automation_status.SimulationAutomationStatus]:
        """
        Gets the status property value. Status of the attack simulation automation. Supports $filter and $orderby. The possible values are: unknown, draft, notRunning, running, completed, unknownFutureValue.
        Returns: Optional[simulation_automation_status.SimulationAutomationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[simulation_automation_status.SimulationAutomationStatus] = None) -> None:
        """
        Sets the status property value. Status of the attack simulation automation. Supports $filter and $orderby. The possible values are: unknown, draft, notRunning, running, completed, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

