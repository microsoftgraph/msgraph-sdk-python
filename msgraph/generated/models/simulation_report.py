from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

simulation_report_overview = lazy_import('msgraph.generated.models.simulation_report_overview')
user_simulation_details = lazy_import('msgraph.generated.models.user_simulation_details')

class SimulationReport(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new simulationReport and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Overview of an attack simulation and training campaign.
        self._overview: Optional[simulation_report_overview.SimulationReportOverview] = None
        # The tenant users and their online actions in an attack simulation and training campaign.
        self._simulation_users: Optional[List[user_simulation_details.UserSimulationDetails]] = None
    
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
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "overview": lambda n : setattr(self, 'overview', n.get_object_value(simulation_report_overview.SimulationReportOverview)),
            "simulation_users": lambda n : setattr(self, 'simulation_users', n.get_collection_of_object_values(user_simulation_details.UserSimulationDetails)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def overview(self,) -> Optional[simulation_report_overview.SimulationReportOverview]:
        """
        Gets the overview property value. Overview of an attack simulation and training campaign.
        Returns: Optional[simulation_report_overview.SimulationReportOverview]
        """
        return self._overview
    
    @overview.setter
    def overview(self,value: Optional[simulation_report_overview.SimulationReportOverview] = None) -> None:
        """
        Sets the overview property value. Overview of an attack simulation and training campaign.
        Args:
            value: Value to set for the overview property.
        """
        self._overview = value
    
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
    
    @property
    def simulation_users(self,) -> Optional[List[user_simulation_details.UserSimulationDetails]]:
        """
        Gets the simulationUsers property value. The tenant users and their online actions in an attack simulation and training campaign.
        Returns: Optional[List[user_simulation_details.UserSimulationDetails]]
        """
        return self._simulation_users
    
    @simulation_users.setter
    def simulation_users(self,value: Optional[List[user_simulation_details.UserSimulationDetails]] = None) -> None:
        """
        Sets the simulationUsers property value. The tenant users and their online actions in an attack simulation and training campaign.
        Args:
            value: Value to set for the simulationUsers property.
        """
        self._simulation_users = value
    

