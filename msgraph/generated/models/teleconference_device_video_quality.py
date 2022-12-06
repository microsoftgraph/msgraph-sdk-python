from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teleconference_device_media_quality = lazy_import('msgraph.generated.models.teleconference_device_media_quality')

class TeleconferenceDeviceVideoQuality(teleconference_device_media_quality.TeleconferenceDeviceMediaQuality):
    @property
    def average_inbound_bit_rate(self,) -> Optional[float]:
        """
        Gets the averageInboundBitRate property value. The average inbound stream video bit rate per second.
        Returns: Optional[float]
        """
        return self._average_inbound_bit_rate
    
    @average_inbound_bit_rate.setter
    def average_inbound_bit_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the averageInboundBitRate property value. The average inbound stream video bit rate per second.
        Args:
            value: Value to set for the averageInboundBitRate property.
        """
        self._average_inbound_bit_rate = value
    
    @property
    def average_inbound_frame_rate(self,) -> Optional[float]:
        """
        Gets the averageInboundFrameRate property value. The average inbound stream video frame rate per second.
        Returns: Optional[float]
        """
        return self._average_inbound_frame_rate
    
    @average_inbound_frame_rate.setter
    def average_inbound_frame_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the averageInboundFrameRate property value. The average inbound stream video frame rate per second.
        Args:
            value: Value to set for the averageInboundFrameRate property.
        """
        self._average_inbound_frame_rate = value
    
    @property
    def average_outbound_bit_rate(self,) -> Optional[float]:
        """
        Gets the averageOutboundBitRate property value. The average outbound stream video bit rate per second.
        Returns: Optional[float]
        """
        return self._average_outbound_bit_rate
    
    @average_outbound_bit_rate.setter
    def average_outbound_bit_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the averageOutboundBitRate property value. The average outbound stream video bit rate per second.
        Args:
            value: Value to set for the averageOutboundBitRate property.
        """
        self._average_outbound_bit_rate = value
    
    @property
    def average_outbound_frame_rate(self,) -> Optional[float]:
        """
        Gets the averageOutboundFrameRate property value. The average outbound stream video frame rate per second.
        Returns: Optional[float]
        """
        return self._average_outbound_frame_rate
    
    @average_outbound_frame_rate.setter
    def average_outbound_frame_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the averageOutboundFrameRate property value. The average outbound stream video frame rate per second.
        Args:
            value: Value to set for the averageOutboundFrameRate property.
        """
        self._average_outbound_frame_rate = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new TeleconferenceDeviceVideoQuality and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.teleconferenceDeviceVideoQuality"
        # The average inbound stream video bit rate per second.
        self._average_inbound_bit_rate: Optional[float] = None
        # The average inbound stream video frame rate per second.
        self._average_inbound_frame_rate: Optional[float] = None
        # The average outbound stream video bit rate per second.
        self._average_outbound_bit_rate: Optional[float] = None
        # The average outbound stream video frame rate per second.
        self._average_outbound_frame_rate: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeleconferenceDeviceVideoQuality:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeleconferenceDeviceVideoQuality
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeleconferenceDeviceVideoQuality()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "average_inbound_bit_rate": lambda n : setattr(self, 'average_inbound_bit_rate', n.get_float_value()),
            "average_inbound_frame_rate": lambda n : setattr(self, 'average_inbound_frame_rate', n.get_float_value()),
            "average_outbound_bit_rate": lambda n : setattr(self, 'average_outbound_bit_rate', n.get_float_value()),
            "average_outbound_frame_rate": lambda n : setattr(self, 'average_outbound_frame_rate', n.get_float_value()),
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
        writer.write_float_value("averageInboundBitRate", self.average_inbound_bit_rate)
        writer.write_float_value("averageInboundFrameRate", self.average_inbound_frame_rate)
        writer.write_float_value("averageOutboundBitRate", self.average_outbound_bit_rate)
        writer.write_float_value("averageOutboundFrameRate", self.average_outbound_frame_rate)
    

