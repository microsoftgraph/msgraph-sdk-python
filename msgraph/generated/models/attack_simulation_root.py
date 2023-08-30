from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .simulation import Simulation
    from .simulation_automation import SimulationAutomation

from .entity import Entity

@dataclass
class AttackSimulationRoot(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents simulation automation created to run on a tenant.
    simulation_automations: Optional[List[SimulationAutomation]] = None
    # Represents an attack simulation training campaign in a tenant.
    simulations: Optional[List[Simulation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttackSimulationRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AttackSimulationRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .simulation import Simulation
        from .simulation_automation import SimulationAutomation

        from .entity import Entity
        from .simulation import Simulation
        from .simulation_automation import SimulationAutomation

        fields: Dict[str, Callable[[Any], None]] = {
            "simulationAutomations": lambda n : setattr(self, 'simulation_automations', n.get_collection_of_object_values(SimulationAutomation)),
            "simulations": lambda n : setattr(self, 'simulations', n.get_collection_of_object_values(Simulation)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("simulationAutomations", self.simulation_automations)
        writer.write_collection_of_object_values("simulations", self.simulations)
    

