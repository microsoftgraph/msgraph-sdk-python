from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import simulation_report_overview, user_simulation_details

@dataclass
class SimulationReport(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Overview of an attack simulation and training campaign.
    overview: Optional[simulation_report_overview.SimulationReportOverview] = None
    # The tenant users and their online actions in an attack simulation and training campaign.
    simulation_users: Optional[List[user_simulation_details.UserSimulationDetails]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SimulationReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SimulationReport
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SimulationReport()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import simulation_report_overview, user_simulation_details

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "overview": lambda n : setattr(self, 'overview', n.get_object_value(simulation_report_overview.SimulationReportOverview)),
            "simulationUsers": lambda n : setattr(self, 'simulation_users', n.get_collection_of_object_values(user_simulation_details.UserSimulationDetails)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("overview", self.overview)
        writer.write_collection_of_object_values("simulationUsers", self.simulation_users)
        writer.write_additional_data_value(self.additional_data)
    

