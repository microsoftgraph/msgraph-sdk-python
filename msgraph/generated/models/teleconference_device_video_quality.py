from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality
    from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality

from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality

@dataclass
class TeleconferenceDeviceVideoQuality(TeleconferenceDeviceMediaQuality):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.teleconferenceDeviceVideoQuality"
    # The average inbound stream video bit rate per second.
    average_inbound_bit_rate: Optional[float] = None
    # The average inbound stream video frame rate per second.
    average_inbound_frame_rate: Optional[float] = None
    # The average outbound stream video bit rate per second.
    average_outbound_bit_rate: Optional[float] = None
    # The average outbound stream video frame rate per second.
    average_outbound_frame_rate: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeleconferenceDeviceVideoQuality:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeleconferenceDeviceVideoQuality
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teleconferenceDeviceScreenSharingQuality".casefold():
            from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality

            return TeleconferenceDeviceScreenSharingQuality()
        return TeleconferenceDeviceVideoQuality()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality
        from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality

        from .teleconference_device_media_quality import TeleconferenceDeviceMediaQuality
        from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality

        fields: Dict[str, Callable[[Any], None]] = {
            "averageInboundBitRate": lambda n : setattr(self, 'average_inbound_bit_rate', n.get_float_value()),
            "averageInboundFrameRate": lambda n : setattr(self, 'average_inbound_frame_rate', n.get_float_value()),
            "averageOutboundBitRate": lambda n : setattr(self, 'average_outbound_bit_rate', n.get_float_value()),
            "averageOutboundFrameRate": lambda n : setattr(self, 'average_outbound_frame_rate', n.get_float_value()),
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
        writer.write_float_value("averageInboundBitRate", self.average_inbound_bit_rate)
        writer.write_float_value("averageInboundFrameRate", self.average_inbound_frame_rate)
        writer.write_float_value("averageOutboundBitRate", self.average_outbound_bit_rate)
        writer.write_float_value("averageOutboundFrameRate", self.average_outbound_frame_rate)
    

