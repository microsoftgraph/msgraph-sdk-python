from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

simulation_event = lazy_import('msgraph.generated.models.simulation_event')

class SimulationEventsContent(AdditionalDataHolder, Parsable):
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
    
    @property
    def compromised_rate(self,) -> Optional[float]:
        """
        Gets the compromisedRate property value. Actual percentage of users who fell for the simulated attack in an attack simulation and training campaign.
        Returns: Optional[float]
        """
        return self._compromised_rate
    
    @compromised_rate.setter
    def compromised_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the compromisedRate property value. Actual percentage of users who fell for the simulated attack in an attack simulation and training campaign.
        Args:
            value: Value to set for the compromisedRate property.
        """
        self._compromised_rate = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new simulationEventsContent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Actual percentage of users who fell for the simulated attack in an attack simulation and training campaign.
        self._compromised_rate: Optional[float] = None
        # List of simulation events in an attack simulation and training campaign.
        self._events: Optional[List[simulation_event.SimulationEvent]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SimulationEventsContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SimulationEventsContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SimulationEventsContent()
    
    @property
    def events(self,) -> Optional[List[simulation_event.SimulationEvent]]:
        """
        Gets the events property value. List of simulation events in an attack simulation and training campaign.
        Returns: Optional[List[simulation_event.SimulationEvent]]
        """
        return self._events
    
    @events.setter
    def events(self,value: Optional[List[simulation_event.SimulationEvent]] = None) -> None:
        """
        Sets the events property value. List of simulation events in an attack simulation and training campaign.
        Args:
            value: Value to set for the events property.
        """
        self._events = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compromised_rate": lambda n : setattr(self, 'compromised_rate', n.get_float_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(simulation_event.SimulationEvent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_float_value("compromisedRate", self.compromised_rate)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

