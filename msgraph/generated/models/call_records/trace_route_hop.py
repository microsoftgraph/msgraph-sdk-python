from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TraceRouteHop(AdditionalDataHolder, Parsable):
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
        Instantiates a new traceRouteHop and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The network path count of this hop that was used to compute the RTT.
        self._hop_count: Optional[int] = None
        # IP address used for this hop in the network trace.
        self._ip_address: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The time from when the trace route packet was sent from the client to this hop and back to the client, denoted in [ISO 8601][] format. For example, 1 second is denoted as PT1S, where P is the duration designator, T is the time designator, and S is the second designator.
        self._round_trip_time: Optional[Timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TraceRouteHop:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TraceRouteHop
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TraceRouteHop()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "hop_count": lambda n : setattr(self, 'hop_count', n.get_int_value()),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "round_trip_time": lambda n : setattr(self, 'round_trip_time', n.get_object_value(Timedelta)),
        }
        return fields
    
    @property
    def hop_count(self,) -> Optional[int]:
        """
        Gets the hopCount property value. The network path count of this hop that was used to compute the RTT.
        Returns: Optional[int]
        """
        return self._hop_count
    
    @hop_count.setter
    def hop_count(self,value: Optional[int] = None) -> None:
        """
        Sets the hopCount property value. The network path count of this hop that was used to compute the RTT.
        Args:
            value: Value to set for the hopCount property.
        """
        self._hop_count = value
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. IP address used for this hop in the network trace.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. IP address used for this hop in the network trace.
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
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
    def round_trip_time(self,) -> Optional[Timedelta]:
        """
        Gets the roundTripTime property value. The time from when the trace route packet was sent from the client to this hop and back to the client, denoted in [ISO 8601][] format. For example, 1 second is denoted as PT1S, where P is the duration designator, T is the time designator, and S is the second designator.
        Returns: Optional[Timedelta]
        """
        return self._round_trip_time
    
    @round_trip_time.setter
    def round_trip_time(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the roundTripTime property value. The time from when the trace route packet was sent from the client to this hop and back to the client, denoted in [ISO 8601][] format. For example, 1 second is denoted as PT1S, where P is the duration designator, T is the time designator, and S is the second designator.
        Args:
            value: Value to set for the roundTripTime property.
        """
        self._round_trip_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("hopCount", self.hop_count)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("roundTripTime", self.round_trip_time)
        writer.write_additional_data_value(self.additional_data)
    

