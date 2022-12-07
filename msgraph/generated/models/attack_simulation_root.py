from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
simulation = lazy_import('msgraph.generated.models.simulation')
simulation_automation = lazy_import('msgraph.generated.models.simulation_automation')

class AttackSimulationRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new attackSimulationRoot and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents simulation automation created to run on a tenant.
        self._simulation_automations: Optional[List[simulation_automation.SimulationAutomation]] = None
        # Represents an attack simulation training campaign in a tenant.
        self._simulations: Optional[List[simulation.Simulation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttackSimulationRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "simulation_automations": lambda n : setattr(self, 'simulation_automations', n.get_collection_of_object_values(simulation_automation.SimulationAutomation)),
            "simulations": lambda n : setattr(self, 'simulations', n.get_collection_of_object_values(simulation.Simulation)),
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
        writer.write_collection_of_object_values("simulationAutomations", self.simulation_automations)
        writer.write_collection_of_object_values("simulations", self.simulations)
    
    @property
    def simulation_automations(self,) -> Optional[List[simulation_automation.SimulationAutomation]]:
        """
        Gets the simulationAutomations property value. Represents simulation automation created to run on a tenant.
        Returns: Optional[List[simulation_automation.SimulationAutomation]]
        """
        return self._simulation_automations
    
    @simulation_automations.setter
    def simulation_automations(self,value: Optional[List[simulation_automation.SimulationAutomation]] = None) -> None:
        """
        Sets the simulationAutomations property value. Represents simulation automation created to run on a tenant.
        Args:
            value: Value to set for the simulationAutomations property.
        """
        self._simulation_automations = value
    
    @property
    def simulations(self,) -> Optional[List[simulation.Simulation]]:
        """
        Gets the simulations property value. Represents an attack simulation training campaign in a tenant.
        Returns: Optional[List[simulation.Simulation]]
        """
        return self._simulations
    
    @simulations.setter
    def simulations(self,value: Optional[List[simulation.Simulation]] = None) -> None:
        """
        Sets the simulations property value. Represents an attack simulation training campaign in a tenant.
        Args:
            value: Value to set for the simulations property.
        """
        self._simulations = value
    

