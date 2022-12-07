from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SimulationEvent(AdditionalDataHolder, Parsable):
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
        Instantiates a new simulationEvent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Count of the simulation event occurrence in an attack simulation and training campaign.
        self._count: Optional[int] = None
        # Name of the simulation event in an attack simulation and training campaign.
        self._event_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def count(self,) -> Optional[int]:
        """
        Gets the count property value. Count of the simulation event occurrence in an attack simulation and training campaign.
        Returns: Optional[int]
        """
        return self._count
    
    @count.setter
    def count(self,value: Optional[int] = None) -> None:
        """
        Sets the count property value. Count of the simulation event occurrence in an attack simulation and training campaign.
        Args:
            value: Value to set for the count property.
        """
        self._count = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SimulationEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SimulationEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SimulationEvent()
    
    @property
    def event_name(self,) -> Optional[str]:
        """
        Gets the eventName property value. Name of the simulation event in an attack simulation and training campaign.
        Returns: Optional[str]
        """
        return self._event_name
    
    @event_name.setter
    def event_name(self,value: Optional[str] = None) -> None:
        """
        Sets the eventName property value. Name of the simulation event in an attack simulation and training campaign.
        Args:
            value: Value to set for the eventName property.
        """
        self._event_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "event_name": lambda n : setattr(self, 'event_name', n.get_str_value()),
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
        writer.write_int_value("count", self.count)
        writer.write_str_value("eventName", self.event_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

