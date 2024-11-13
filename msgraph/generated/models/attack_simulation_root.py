from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attack_simulation_operation import AttackSimulationOperation
    from .end_user_notification import EndUserNotification
    from .entity import Entity
    from .landing_page import LandingPage
    from .login_page import LoginPage
    from .payload import Payload
    from .simulation import Simulation
    from .simulation_automation import SimulationAutomation
    from .training import Training

from .entity import Entity

@dataclass
class AttackSimulationRoot(Entity, Parsable):
    # Represents an end user's notification for an attack simulation training.
    end_user_notifications: Optional[List[EndUserNotification]] = None
    # Represents an attack simulation training landing page.
    landing_pages: Optional[List[LandingPage]] = None
    # Represents an attack simulation training login page.
    login_pages: Optional[List[LoginPage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents an attack simulation training operation.
    operations: Optional[List[AttackSimulationOperation]] = None
    # Represents an attack simulation training campaign payload in a tenant.
    payloads: Optional[List[Payload]] = None
    # Represents simulation automation created to run on a tenant.
    simulation_automations: Optional[List[SimulationAutomation]] = None
    # Represents an attack simulation training campaign in a tenant.
    simulations: Optional[List[Simulation]] = None
    # Represents details about attack simulation trainings.
    trainings: Optional[List[Training]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttackSimulationRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttackSimulationRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attack_simulation_operation import AttackSimulationOperation
        from .end_user_notification import EndUserNotification
        from .entity import Entity
        from .landing_page import LandingPage
        from .login_page import LoginPage
        from .payload import Payload
        from .simulation import Simulation
        from .simulation_automation import SimulationAutomation
        from .training import Training

        from .attack_simulation_operation import AttackSimulationOperation
        from .end_user_notification import EndUserNotification
        from .entity import Entity
        from .landing_page import LandingPage
        from .login_page import LoginPage
        from .payload import Payload
        from .simulation import Simulation
        from .simulation_automation import SimulationAutomation
        from .training import Training

        fields: Dict[str, Callable[[Any], None]] = {
            "endUserNotifications": lambda n : setattr(self, 'end_user_notifications', n.get_collection_of_object_values(EndUserNotification)),
            "landingPages": lambda n : setattr(self, 'landing_pages', n.get_collection_of_object_values(LandingPage)),
            "loginPages": lambda n : setattr(self, 'login_pages', n.get_collection_of_object_values(LoginPage)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(AttackSimulationOperation)),
            "payloads": lambda n : setattr(self, 'payloads', n.get_collection_of_object_values(Payload)),
            "simulationAutomations": lambda n : setattr(self, 'simulation_automations', n.get_collection_of_object_values(SimulationAutomation)),
            "simulations": lambda n : setattr(self, 'simulations', n.get_collection_of_object_values(Simulation)),
            "trainings": lambda n : setattr(self, 'trainings', n.get_collection_of_object_values(Training)),
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
        from .attack_simulation_operation import AttackSimulationOperation
        from .end_user_notification import EndUserNotification
        from .entity import Entity
        from .landing_page import LandingPage
        from .login_page import LoginPage
        from .payload import Payload
        from .simulation import Simulation
        from .simulation_automation import SimulationAutomation
        from .training import Training

        writer.write_collection_of_object_values("endUserNotifications", self.end_user_notifications)
        writer.write_collection_of_object_values("landingPages", self.landing_pages)
        writer.write_collection_of_object_values("loginPages", self.login_pages)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("payloads", self.payloads)
        writer.write_collection_of_object_values("simulationAutomations", self.simulation_automations)
        writer.write_collection_of_object_values("simulations", self.simulations)
        writer.write_collection_of_object_values("trainings", self.trainings)
    

