from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_info, media_stream, network_info

@dataclass
class Media(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Device information associated with the callee endpoint of this media.
    callee_device: Optional[device_info.DeviceInfo] = None
    # Network information associated with the callee endpoint of this media.
    callee_network: Optional[network_info.NetworkInfo] = None
    # Device information associated with the caller endpoint of this media.
    caller_device: Optional[device_info.DeviceInfo] = None
    # Network information associated with the caller endpoint of this media.
    caller_network: Optional[network_info.NetworkInfo] = None
    # How the media was identified during media negotiation stage.
    label: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Network streams associated with this media.
    streams: Optional[List[media_stream.MediaStream]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Media:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Media
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Media()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_info, media_stream, network_info

        fields: Dict[str, Callable[[Any], None]] = {
            "calleeDevice": lambda n : setattr(self, 'callee_device', n.get_object_value(device_info.DeviceInfo)),
            "calleeNetwork": lambda n : setattr(self, 'callee_network', n.get_object_value(network_info.NetworkInfo)),
            "callerDevice": lambda n : setattr(self, 'caller_device', n.get_object_value(device_info.DeviceInfo)),
            "callerNetwork": lambda n : setattr(self, 'caller_network', n.get_object_value(network_info.NetworkInfo)),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "streams": lambda n : setattr(self, 'streams', n.get_collection_of_object_values(media_stream.MediaStream)),
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
        writer.write_object_value("calleeDevice", self.callee_device)
        writer.write_object_value("calleeNetwork", self.callee_network)
        writer.write_object_value("callerDevice", self.caller_device)
        writer.write_object_value("callerNetwork", self.caller_network)
        writer.write_str_value("label", self.label)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("streams", self.streams)
        writer.write_additional_data_value(self.additional_data)
    

