from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_info, media_stream, network_info

class Media(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new media and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Device information associated with the callee endpoint of this media.
        self._callee_device: Optional[device_info.DeviceInfo] = None
        # Network information associated with the callee endpoint of this media.
        self._callee_network: Optional[network_info.NetworkInfo] = None
        # Device information associated with the caller endpoint of this media.
        self._caller_device: Optional[device_info.DeviceInfo] = None
        # Network information associated with the caller endpoint of this media.
        self._caller_network: Optional[network_info.NetworkInfo] = None
        # How the media was identified during media negotiation stage.
        self._label: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Network streams associated with this media.
        self._streams: Optional[List[media_stream.MediaStream]] = None
    
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
    def callee_device(self,) -> Optional[device_info.DeviceInfo]:
        """
        Gets the calleeDevice property value. Device information associated with the callee endpoint of this media.
        Returns: Optional[device_info.DeviceInfo]
        """
        return self._callee_device
    
    @callee_device.setter
    def callee_device(self,value: Optional[device_info.DeviceInfo] = None) -> None:
        """
        Sets the calleeDevice property value. Device information associated with the callee endpoint of this media.
        Args:
            value: Value to set for the callee_device property.
        """
        self._callee_device = value
    
    @property
    def callee_network(self,) -> Optional[network_info.NetworkInfo]:
        """
        Gets the calleeNetwork property value. Network information associated with the callee endpoint of this media.
        Returns: Optional[network_info.NetworkInfo]
        """
        return self._callee_network
    
    @callee_network.setter
    def callee_network(self,value: Optional[network_info.NetworkInfo] = None) -> None:
        """
        Sets the calleeNetwork property value. Network information associated with the callee endpoint of this media.
        Args:
            value: Value to set for the callee_network property.
        """
        self._callee_network = value
    
    @property
    def caller_device(self,) -> Optional[device_info.DeviceInfo]:
        """
        Gets the callerDevice property value. Device information associated with the caller endpoint of this media.
        Returns: Optional[device_info.DeviceInfo]
        """
        return self._caller_device
    
    @caller_device.setter
    def caller_device(self,value: Optional[device_info.DeviceInfo] = None) -> None:
        """
        Sets the callerDevice property value. Device information associated with the caller endpoint of this media.
        Args:
            value: Value to set for the caller_device property.
        """
        self._caller_device = value
    
    @property
    def caller_network(self,) -> Optional[network_info.NetworkInfo]:
        """
        Gets the callerNetwork property value. Network information associated with the caller endpoint of this media.
        Returns: Optional[network_info.NetworkInfo]
        """
        return self._caller_network
    
    @caller_network.setter
    def caller_network(self,value: Optional[network_info.NetworkInfo] = None) -> None:
        """
        Sets the callerNetwork property value. Network information associated with the caller endpoint of this media.
        Args:
            value: Value to set for the caller_network property.
        """
        self._caller_network = value
    
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
    
    @property
    def label(self,) -> Optional[str]:
        """
        Gets the label property value. How the media was identified during media negotiation stage.
        Returns: Optional[str]
        """
        return self._label
    
    @label.setter
    def label(self,value: Optional[str] = None) -> None:
        """
        Sets the label property value. How the media was identified during media negotiation stage.
        Args:
            value: Value to set for the label property.
        """
        self._label = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_object_value("calleeDevice", self.callee_device)
        writer.write_object_value("calleeNetwork", self.callee_network)
        writer.write_object_value("callerDevice", self.caller_device)
        writer.write_object_value("callerNetwork", self.caller_network)
        writer.write_str_value("label", self.label)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("streams", self.streams)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def streams(self,) -> Optional[List[media_stream.MediaStream]]:
        """
        Gets the streams property value. Network streams associated with this media.
        Returns: Optional[List[media_stream.MediaStream]]
        """
        return self._streams
    
    @streams.setter
    def streams(self,value: Optional[List[media_stream.MediaStream]] = None) -> None:
        """
        Sets the streams property value. Network streams associated with this media.
        Args:
            value: Value to set for the streams property.
        """
        self._streams = value
    

